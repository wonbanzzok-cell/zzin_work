"""Summarize an Excel/CSV file into Markdown tables.

Usage:
  python summarize.py <file> [--sheet NAME] [--date-col COL] [--period PERIOD] [--out PATH]

PERIOD: YYYY-MM (month) or YYYY-Www (ISO week). With --date-col, the period is
compared with the previous period of the same length.
"""
import argparse
import datetime as dt
import sys
from pathlib import Path

import pandas as pd

OUTLIER_PCT = 30.0


def load(path: Path, sheet):
    suffix = path.suffix.lower()
    if suffix in (".xlsx", ".xlsm", ".xls"):
        return pd.read_excel(path, sheet_name=sheet or 0)
    if suffix == ".csv":
        for enc in ("utf-8-sig", "cp949"):
            try:
                return pd.read_csv(path, encoding=enc)
            except UnicodeDecodeError:
                continue
    raise SystemExit(f"Unsupported or unreadable file: {path}")


def period_bounds(period: str):
    """Return (prev_start, start, end) timestamps for the period."""
    if "-W" in period:
        year, week = period.split("-W")
        start = pd.Timestamp(dt.date.fromisocalendar(int(year), int(week), 1))
        return start - pd.Timedelta(days=7), start, start + pd.Timedelta(days=7)
    start = pd.Timestamp(f"{period}-01")
    return start - pd.offsets.MonthBegin(1), start, start + pd.offsets.MonthBegin(1)


def fmt(v):
    if pd.isna(v):
        return "-"
    v = float(v)
    return f"{v:,.0f}" if v.is_integer() else f"{v:,.1f}"


def signed(v):
    if pd.isna(v):
        return "-"
    return ("+" if v > 0 else "") + fmt(v)


def stats_table(df):
    rows = ["| 항목 | 합계 | 평균 | 최소 | 최대 |", "|---|---:|---:|---:|---:|"]
    for col in df.select_dtypes("number").columns:
        s = df[col]
        rows.append(f"| {col} | {fmt(s.sum())} | {fmt(s.mean())} | {fmt(s.min())} | {fmt(s.max())} |")
    return "\n".join(rows)


def change_table(prev, cur):
    rows = [
        "| 항목 | 직전 기간 | 해당 기간 | 증감 | 증감률 | 비고 |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for col in cur.select_dtypes("number").columns:
        a, b = prev[col].sum(), cur[col].sum()
        diff = b - a
        pct = diff / a * 100 if a else float("nan")
        flag = "이상치" if not pd.isna(pct) and abs(pct) >= OUTLIER_PCT else ""
        pct_s = "-" if pd.isna(pct) else f"{pct:+.1f}%"
        rows.append(f"| {col} | {fmt(a)} | {fmt(b)} | {signed(diff)} | {pct_s} | {flag} |")
    return "\n".join(rows)


def main():
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--sheet")
    ap.add_argument("--date-col")
    ap.add_argument("--period")
    ap.add_argument("--out")
    args = ap.parse_args()

    path = Path(args.file)
    df = load(path, args.sheet)
    lines = [f"# 데이터 요약: {path.name}", "", f"출처: `{path.as_posix()}`", f"행 수: {len(df):,}", ""]

    if args.date_col and args.period:
        if args.date_col not in df.columns:
            raise SystemExit(f"Column not found: {args.date_col}. Columns: {list(df.columns)}")
        dates = pd.to_datetime(df[args.date_col], errors="coerce")
        prev_start, start, end = period_bounds(args.period)
        cur = df[(dates >= start) & (dates < end)]
        prev = df[(dates >= prev_start) & (dates < start)]
        last_day = (end - pd.Timedelta(days=1)).date()
        lines += [
            f"## 해당 기간 {args.period} ({start.date()} ~ {last_day}, {len(cur):,}행)",
            "", stats_table(cur), "",
            f"## 직전 기간 대비 증감 (직전 기간 {len(prev):,}행)",
            "", change_table(prev, cur), "",
            f"이상치: 증감률 절대값 {OUTLIER_PCT:.0f}% 이상",
        ]
    else:
        lines += ["## 전체 데이터", "", stats_table(df)]

    text = "\n".join(lines) + "\n"
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(f"Saved: {out}")
    else:
        print(text)


if __name__ == "__main__":
    main()
