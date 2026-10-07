# Quantum Mechanics from the Beginning

A graduate course in quantum mechanics in finite-dimensional Hilbert spaces, from school mathematics to the foundations literature on measurement, nonlocality, contextuality and observers. It runs to 452 sessions in 26 Parts, builds every piece of mathematics it uses, and proves every result it can. It is aimed at three questions: whether observation and action can be simultaneous, whether measurement can be done from outside a system, and whether local realism could be true but unverifiable.

The book is being written. [The syllabus](00-syllabus.md) fixes every session; the sessions appear in `sessions/` as they are written.

## Read it

- **Online:** <https://sajad2025.github.io/book-qm/>.
- **In the reader.** `index.html` is a single-page reader with a contents drawer grouped by Part, three page colours and adjustable text size. It loads the sessions from `sessions/` and their solutions from `solutions/`, renders the mathematics with KaTeX, and turns references such as "Session 7" into links. Each Part has a page with its goal and its toolkit: the results from earlier Parts that its sessions cite. "Save for offline" at the foot of the contents drawer downloads the syllabus and every written session, with solutions and fonts, so it reads without a connection.
- **In Farsi.** The book is bilingual. The button on the home page, or «فا» in the top bar, switches the reader to the Farsi translation, right to left in the Vazirmatn font, with the formulas unchanged; «EN» switches back. The Farsi files are in `fa/`.
- **On GitHub.** Every session is a plain Markdown file and renders directly on github.com, formulas included. Start with [the syllabus](00-syllabus.md), then [Session 1](sessions/001-orientation.md).

## Contents

| Part | Sessions | |
|---|---|---|
| 1 | 1–11 | Sets, real numbers and limits |
| 2 | 12–26 | Complex numbers, polynomials and groups |
| 3 | 27–45 | Vector spaces and linear maps |
| 4 | 46–62 | Inner-product spaces |
| 5 | 63–76 | Spectral theory |
| 6 | 77–88 | Finite probability |
| 7 | 89–105 | The postulates for a single system |
| 8 | 106–124 | Integrals, Taylor's theorem and the analysis of operators |
| 9 | 125–136 | Dynamics of a closed system |
| 10 | 137–148 | Positivity, singular values and the trace norm |
| 11 | 149–161 | Compactness and convexity in finite dimensions |
| 12 | 162–177 | Direct sums and tensor products |
| 13 | 178–190 | Composite systems and density operators |
| 14 | 191–199 | Reduced states, purification and entanglement |
| 15 | 200–208 | Entropy |
| 16 | 209–220 | Probability 2: concentration, Markov processes and densities |
| 17 | 221–243 | General measurements and channels |
| 18 | 244–261 | Entanglement and information |
| 19 | 262–294 | Measurement, disturbance and feedback (Q1) |
| 20 | 295–328 | Hidden variables and Bell's theorem (Q3) |
| 21 | 329–342 | Bell experiments, loopholes and measurement dependence (Q3) |
| 22 | 343–384 | Contextuality and the reality of the quantum state (Q3) |
| 23 | 385–400 | The measurement problem and decoherence (Q2) |
| 24 | 401–423 | Observers inside the system (Q2) |
| 25 | 424–447 | Interpretations |
| 26 | 448–452 | The reader's own question |

## Preview locally

The reader fetches the sessions over HTTP, so open it through a local server, not from disk:

```text
python -m http.server
```

then visit `http://localhost:8000`.

## Publish with GitHub Pages

1. In the repository, open Settings, then Pages.
2. Under "Build and deployment", choose "Deploy from a branch", then the branch `main` and the folder `/ (root)`, and save.
3. The reader appears at <https://sajad2025.github.io/book-qm/> a minute or two later, and updates on every push.

The empty file `.nojekyll` tells GitHub Pages to serve the Markdown files as they are. Keep it.

## The plan tools

`plan/sessions.jsonl` is the source of truth for the session list; [plan/README.md](plan/README.md) describes it. Run the tools from this folder.

```text
python3 plan/check_sessions.py [N ...]     # check written sessions against the syllabus and the writing plan
python3 plan/build_book_json.py            # regenerate book.json after adding a session or solutions file
```

After editing the session list, validate it and regenerate the syllabus (English and Farsi), the writing plan and `book.json`:

```text
python3 plan/validate.py plan/sessions.jsonl
python3 plan/build_syllabus.py plan/sessions.jsonl plan/front-matter.md 00-syllabus.md
python3 plan/build_syllabus.py plan/sessions.jsonl plan/fa/front-matter.md fa/00-syllabus.md --fa plan/fa.json
python3 plan/build_plan.py plan/sessions.jsonl plan/writing-plan.tmpl.md 01-writing-plan.md
python3 plan/build_book_json.py
```

The Farsi translation follows [plan/fa/STYLE.md](plan/fa/STYLE.md), its conventions and glossary. Session n in Farsi is `fa/sessions/NNN-slug.md`, with its solutions in `fa/solutions/`; the Farsi titles, claims, Part goals and gap notes are in `plan/fa.json`. `python3 plan/check_fa.py [N ...]` checks each translation against its English source: the same formulas, sections, exercises and references.

The reader shows a session as written only once `book.json` lists its file, so run `build_book_json.py` whenever a session or solutions file is added.

## Layout

```text
index.html              the reader
sw.js                   service worker for offline reading
book.json               Parts and sessions used by the reader (generated)
00-syllabus.md          Session 0: every session's claim and prerequisites (generated)
01-writing-plan.md      how a session is written (generated)
sessions/NNN-slug.md    one Markdown file per session
solutions/NNN-slug.md   the solutions to its exercises
fa/                     the Farsi translation: 00-syllabus.md, sessions/, solutions/
plan/                   the session list and the scripts that check it and build the files above
```
