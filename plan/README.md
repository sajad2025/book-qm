# plan/

The session list behind `00-syllabus.md` and `01-writing-plan.md`.

- `sessions.jsonl` is the source of truth: one line per Part or session, with each session's one claim, the earlier sessions it uses, and any labelled gap.
- `front-matter.md` is the opening of the syllabus; `writing-plan.tmpl.md` is the writing plan, with session references written as `[[slug]]`.
- `sl.py` makes safe edits to the list (insert, merge, move, add uses); it refuses to save a list in which a session uses a later one.

After editing, validate and regenerate both documents from the `book-qm` folder:

```text
python3 plan/validate.py plan/sessions.jsonl
python3 plan/build_syllabus.py plan/sessions.jsonl plan/front-matter.md 00-syllabus.md
python3 plan/build_plan.py plan/sessions.jsonl plan/writing-plan.tmpl.md 01-writing-plan.md
```
