# 0. Syllabus

**Quantum Mechanics from the Beginning: finite-dimensional quantum theory, from school mathematics to the foundations literature**

This is a graduate course in quantum mechanics in finite-dimensional Hilbert spaces, in <<N_SESSIONS>> sessions in <<N_PARTS>> Parts. It builds every piece of mathematics it uses and proves every result it can. Its aim is that the reader understands the mathematics fully: why each postulate takes its form, what each theorem assumes and shows, and where each proof could fail. The destination is the foundations literature on measurement, nonlocality, contextuality and observers. When a result has a name there, the book uses that name, so what is learned here matches what a paper says. The route is long, and every step on it is small.

## Assumed background

School mathematics up to single-variable calculus: limits, derivatives, the exponential and trigonometric functions, and simple integrals. Beyond that, only the willingness to follow a proof line by line.

Everything else is built inside the book, each piece in sessions of its own that later sessions cite:
- the axioms of the real numbers, countable sets, limits, continuity, the mean value theorem, Taylor's theorem and the integral;
- complex numbers, complex series and the exponential;
- linear algebra over R and C, through the spectral theorem, the singular value decomposition, the trace norm and tensor products;
- the matrix exponential and one-parameter groups;
- compactness and convexity in R^n;
- finite probability, through martingales, Hoeffding's and Azuma's inequalities, Markov chains, densities on an interval and the uniform distribution on the sphere;
- Shannon and von Neumann entropy.

A reader who already knows a topic can skip its Part. A reader who does not will find every step there.

## Method

- **One unit of understanding per session.** A session holds a definition with its first consequences, a theorem with its proof, a construction, or a complete worked analysis. Its one claim is stated at the top.
- **Small steps of even height.** A long proof becomes a sequence of sessions: lemma, lemma, theorem. A small fact joins the session it belongs to. Sessions differ in length, not in difficulty of step.
- **Full proofs.** Every result is proved, except where a proof needs tools outside the book or is too long for its use here. Each such place is a labelled gap stating what is omitted, why, and where a full proof can be found. There are <<N_GAPS>> gaps, listed at the end of this syllabus.
- **Everything cited, nothing forward.** Each session lists the earlier sessions whose results it uses, and nothing is used before it is established. Each Part opens with a toolkit page that restates the results from earlier Parts that its sessions use. A session gives its own short *Recall* only for a result that is not on its Part's page.
- **Labels.** Each statement is marked as a definition, theorem, postulate, experimental result or interpretation, so the reader always knows which kind of claim is being made.
- **Worked examples.** Every general result is computed on a small case, usually a qubit, two qubits or a qutrit. The examples in the mathematics Parts are the objects the physics later uses.
- **Exercises.** Each session ends with exercises in three tiers: check, prove, extend. All are solvable from that session and earlier ones. Full solutions are in a separate volume, by Part. Each Part except 26 ends with a problem set that nothing later depends on.

## The three questions

The course is aimed at three questions, stated here in ordinary words:

1. whether observation and action can be simultaneous (Q1);
2. whether measurement can be done from outside a system (Q2);
3. whether local realism could be true but unverifiable (Q3).

None of them can be stated precisely until the formalism is built. Part 19 restates Q1 as statements about instruments, joint measurability, error-disturbance relations and conservation laws. Parts 20-22 restate Q3 as statements about ontological models, Bell inequalities, measurement dependence and fine-tuning, contextuality and the reality of the quantum state. Parts 23-24 restate Q2 as statements about the Heisenberg cut, self-measurement and observers modelled as quantum systems. Part 26 returns to the questions in these words.

## Scope

All Hilbert spaces are finite-dimensional. This removes most of the analysis and none of the conceptual content that the three questions need.

Five topics need infinite dimensions or continuous time. Each appears as a session titled *Excursion*, with its gaps labelled:
- wavefunctions on the line, with position and momentum;
- Heisenberg's position-momentum relation;
- the continuous-time limit of monitoring;
- continuous Bohmian mechanics;
- continuum collapse models and their experimental bounds.

Left out:
- atomic spectra, scattering, identical particles beyond the swap operator, and field theory, because none is needed for the destination;
- the asymptotic theory of quantum information, beyond the statements where it is labelled;
- the stabilizer formalism.

## Standard references

These are anchors, not requirements.

- S. Axler, *Linear Algebra Done Right*, 4th ed.: the route to the spectral theorem
- W. Rudin, *Principles of Mathematical Analysis*, 3rd ed.: the analysis
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information*, Ch. 2, 8-9: the formalism and channels
- A. Peres, *Quantum Theory: Concepts and Methods*: measurement, Bell and Kochen-Specker
- J. S. Bell, *Speakable and Unspeakable in Quantum Mechanics*: the original papers
- J. Preskill, Caltech Ph219 lecture notes, Ch. 2-4: freely available
- T. Heinosaari and M. Ziman, *The Mathematical Language of Quantum Theory*: POVMs, instruments and joint measurability
- H. M. Wiseman and G. J. Milburn, *Quantum Measurement and Control*: filtering and feedback
- W. H. Zurek, *Rev. Mod. Phys.* 75, 715 (2003): decoherence
- K. Landsman, *Foundations of Quantum Theory*: the careful modern treatment
