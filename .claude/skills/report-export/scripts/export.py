"""Convert a Markdown report to .docx (and optionally .pdf).

Usage:
  python export.py <input.md> <output.docx> [--pdf]

Supports headings, bullet/numbered lists, tables, and **bold**.
"""
import argparse
import re
import sys
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt

FONT = "Malgun Gothic"
SEPARATOR = re.compile(r"^:?-+:?$")


def set_font(doc):
    for name in ("Normal", "Heading 1", "Heading 2", "Heading 3", "Heading 4", "Title"):
        style = doc.styles[name]
        style.font.name = FONT
        style.element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), FONT)
    doc.styles["Normal"].font.size = Pt(10.5)


def add_inline(par, text, bold=False):
    for part in re.split(r"(\*\*[^*]+\*\*)", text):
        if len(part) > 4 and part.startswith("**") and part.endswith("**"):
            par.add_run(part[2:-2]).bold = True
        elif part:
            par.add_run(part).bold = bold or None


def add_table(doc, lines):
    rows = [[c.strip() for c in line.strip().strip("|").split("|")] for line in lines]
    rows = [r for r in rows if not all(SEPARATOR.match(c) for c in r if c)]
    if not rows:
        return
    width = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=width)
    table.style = "Table Grid"
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            cell = table.cell(i, j)
            cell.text = ""
            add_inline(cell.paragraphs[0], value, bold=(i == 0))


def convert(md_path: Path, out_path: Path):
    doc = Document()
    set_font(doc)
    table = []
    for raw in md_path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.lstrip().startswith("|"):
            table.append(line)
            continue
        if table:
            add_table(doc, table)
            table = []
        if not line.strip() or re.fullmatch(r"-{3,}|\*{3,}", line.strip()):
            continue
        if m := re.match(r"^(#{1,6})\s+(.*)", line):
            doc.add_heading(m.group(2).strip(), level=min(len(m.group(1)), 4))
        elif m := re.match(r"^\s*[-*]\s+(.*)", line):
            add_inline(doc.add_paragraph(style="List Bullet"), m.group(1))
        elif m := re.match(r"^\s*\d+[.)]\s+(.*)", line):
            add_inline(doc.add_paragraph(style="List Number"), m.group(1))
        else:
            add_inline(doc.add_paragraph(), line.strip())
    if table:
        add_table(doc, table)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out_path)


def main():
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--pdf", action="store_true")
    args = ap.parse_args()

    src, out = Path(args.input), Path(args.output)
    if out.exists():
        raise SystemExit(f"Output already exists, use a new version: {out}")
    convert(src, out)
    print(f"Saved: {out}")

    if args.pdf:
        try:
            from docx2pdf import convert as to_pdf
        except ImportError:
            sys.exit("PDF skipped: run `pip install docx2pdf` (Microsoft Word required).")
        pdf = out.with_suffix(".pdf")
        to_pdf(str(out), str(pdf))
        print(f"Saved: {pdf}")


if __name__ == "__main__":
    main()
