# Report Defaults

Default values for the template header fields. `report-draft` reads this file at the start of every run and copies the values into the report info block of `todo.md`.

| Field | Value |
|---|---|
| author | |
| department | |

- Write the values in Korean, e.g., `홍길동`, `경영기획팀`.
- If a value is empty, `report-draft` asks the user at the start of the run, then offers to save the answer here.
- Do not put personal contact details (phone, email) here.
