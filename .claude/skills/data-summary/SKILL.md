---
name: data-summary
description: Summarizes an Excel/CSV file in inputs/data/ into Markdown tables (sum, mean, min, max, and period-over-period change with outlier flags). Use whenever report numbers come from a spreadsheet.
---
# Data Summary

## Prerequisites
`pip install pandas openpyxl`

## Usage
```
python .claude/skills/data-summary/scripts/summarize.py <file> [--sheet NAME] [--date-col COL] [--period PERIOD] [--out PATH]
```
- `--date-col` and `--period` together compare the period with the previous one.
- `--period` accepts `2026-10` (month) or `2026-W45` (ISO week).
- Without `--out`, the result prints to stdout.

## Steps
1. Open the file once to find the date column and the numeric columns.
2. Run the script with `--out workspace/<report-id>/raw_<file-stem>.md`.
3. Review the output. Changes of 30% or more are marked `이상치`.
4. Merge the needed tables into `workspace/<report-id>/analysis.md`, keeping the source file name. Rename English column names to Korean (e.g., `revenue` → `매출`).

## Output Language
The script writes its headings and table headers in Korean, so its output can go into report working files as is.

## Notes
- CSV files are read as UTF-8, falling back to CP949.
- If the script fails, report the error message as is. Do not compute the numbers by hand instead.
