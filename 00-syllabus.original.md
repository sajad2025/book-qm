# Session 00 — Syllabus

**Quantum mechanics from zero to the foundations literature, in 100 sessions of ~10 minutes.**

---

## What this is

A standard-track development of quantum mechanics in finite-dimensional Hilbert spaces, following the conventions and notation used in the usual graduate references, with more explanation per step than those references give. No invented analogies, no "quantum is like a spinning coin." When a result has a name in the literature, we use that name, so that what you learn here matches what you will read in a paper.

The destination is set by the questions you already asked: whether observation and action can be simultaneous, whether measurement can be done from outside a system, whether local realism could be true but unverifiable. Those are real questions in the field with real names — Breuer's theorem, relational quantum mechanics, superdeterminism, contextuality. The path below is the shortest honest route from zero to being able to read the papers that address them.

## What this is not

Seventeen hours is enough to make you literate in this material and able to follow a quant-ph paper on foundations. It is not enough to make you a physicist. There is no chemistry here, no atomic spectra, no scattering theory, no field theory. We stay in finite dimensions almost throughout, which cuts out most of the analysis and none of the conceptual content.

## Assumed background

Linear algebra over the complex numbers: vector spaces, bases, matrices, eigenvalues, inner products, SVD. If you know those, most of Part I is a change of notation rather than new mathematics. Physics background assumed: none.

## Standard references

You do not need to buy anything, but these are the anchors, and each part below names the one it tracks.

- Nielsen & Chuang, *Quantum Computation and Quantum Information*, Ch. 2 — the formalism
- Peres, *Quantum Theory: Concepts and Methods* — measurement, Bell, Kochen–Specker
- Bell, *Speakable and Unspeakable in Quantum Mechanics* — the original papers
- Preskill, Caltech Ph219 lecture notes, Ch. 2–4 — freely available online
- Zurek, *Rev. Mod. Phys.* 75, 715 (2003) — decoherence
- Landsman, *Foundations of Quantum Theory* — the careful modern treatment

---

## Part 0 — Orientation (Sessions 01–03)

| # | Session |
|---|---|
| 01 | What the theory is a theory *of*; the three questions this course chases |
| 02 | Dirac notation as a relabeling of column and row vectors |
| 03 | Complex numbers, minimum working set: modulus, phase, `e^{iθ}` |

## Part I — State space and operators (04–18)
*Tracks Nielsen & Chuang §2.1.*

| # | Session |
|---|---|
| 04 | Hilbert space: definition, and why finite dimensions suffice for us |
| 05 | Inner product, norm, orthonormal bases |
| 06 | The qubit: `C²` and the computational basis |
| 07 | Superposition and the normalization condition |
| 08 | Global phase, and why it carries no physical content |
| 09 | Relative phase, and why it does |
| 10 | The Bloch sphere I: construction from a general qubit state |
| 11 | The Bloch sphere II: reading states and bases off the picture |
| 12 | Linear operators and their matrix representations |
| 13 | Adjoints; Hermitian operators |
| 14 | The spectral theorem for Hermitian operators |
| 15 | The Pauli matrices `X, Y, Z` |
| 16 | Unitary operators; preservation of the inner product |
| 17 | Projectors and resolutions of the identity |
| 18 | Commutators; what `[X, Z] ≠ 0` actually means |

## Part II — The postulates (19–30)
*Tracks Nielsen & Chuang §2.2, Peres Ch. 2–3.*

| # | Session |
|---|---|
| 19 | Postulate 1: states are unit vectors in a Hilbert space |
| 20 | Postulate 2: closed-system evolution is unitary |
| 21 | The Schrödinger equation as the generator of that unitary |
| 22 | Postulate 3: observables are Hermitian operators |
| 23 | The Born rule |
| 24 | Postulate 4: projective measurement and the state-update rule |
| 25 | Expectation values |
| 26 | Variance; derivation of the uncertainty relation |
| 27 | Why uncertainty is a statement about ensembles, not about disturbance |
| 28 | Postulate 5: composite systems and the tensor product |
| 29 | Worked example: one qubit measured in two different bases |
| 30 | Part II review and self-check |

## Part III — Mixed states and general measurement (31–42)
*Tracks Nielsen & Chuang §2.4, §8.2.*

| # | Session |
|---|---|
| 31 | Why pure states are not enough: ignorance versus superposition |
| 32 | The density operator: definition and defining properties |
| 33 | Pure versus mixed; the purity criterion `tr(ρ²)` |
| 34 | The Bloch ball: where the mixed states live |
| 35 | Evolution and measurement in density-operator language |
| 36 | Ensemble ambiguity: one `ρ`, many preparations |
| 37 | The partial trace |
| 38 | Reduced density operators |
| 39 | POVMs: measurement in its general form |
| 40 | Naimark dilation: every POVM is a projective measurement on a larger space |
| 41 | Kraus operators and quantum channels |
| 42 | Part III review |

## Part IV — Composite systems, entanglement, EPR (43–55)
*Tracks Nielsen & Chuang §2.2.8, §12.5; EPR (1935).*

| # | Session |
|---|---|
| 43 | Tensor products concretely: two qubits in `C⁴` |
| 44 | Product states versus entangled states |
| 45 | The Bell basis |
| 46 | The Schmidt decomposition (this is the SVD) |
| 47 | Entanglement entropy |
| 48 | The no-signalling theorem |
| 49 | Why each half of a Bell pair is maximally mixed |
| 50 | The no-cloning theorem |
| 51 | Monogamy of entanglement |
| 52 | EPR 1935: what Einstein, Podolsky and Rosen actually argued |
| 53 | The EPR criterion of reality, stated precisely |
| 54 | Bohr's reply, and why it is hard to read |
| 55 | Part IV review |

## Part V — Bell's theorem and the experiments (56–72)
*Tracks Bell (1964), CHSH (1969), Peres Ch. 6.*

| # | Session |
|---|---|
| 56 | What a hidden-variable model is, formally |
| 57 | Local causality, written as an equation |
| 58 | Measurement independence (the freedom-of-choice assumption) |
| 59 | Bell's 1964 inequality: the derivation |
| 60 | The CHSH inequality I: setup |
| 61 | The CHSH inequality II: the classical bound of 2 |
| 62 | The quantum prediction: `2√2` |
| 63 | Tsirelson's bound: why quantum mechanics stops there |
| 64 | What Bell's theorem does **not** assume — disturbance, determinism |
| 65 | The PR box: no-signalling alone does not give you quantum theory |
| 66 | Experiments I: Freedman–Clauser, Aspect |
| 67 | Experiments II: the detection loophole |
| 68 | Experiments III: the locality loophole |
| 69 | The loophole-free tests of 2015: Hensen, Giustina, Shalm |
| 70 | Cosmic Bell tests and the freedom-of-choice loophole |
| 71 | Superdeterminism: the surviving option and what it costs |
| 72 | Part V review |

## Part VI — Contextuality (73–82)
*Tracks Kochen–Specker (1967), Mermin, Peres.*

| # | Session |
|---|---|
| 73 | Noncontextual hidden variables: the assumption stated |
| 74 | Gleason's theorem |
| 75 | The Kochen–Specker theorem: statement |
| 76 | Kochen–Specker: proof idea via a finite vector set |
| 77 | The Peres–Mermin square: the whole theorem on one page |
| 78 | Contextuality versus nonlocality: how the two relate |
| 79 | State-independent versus state-dependent contextuality |
| 80 | Spekkens' operational reformulation |
| 81 | Contextuality as a computational resource |
| 82 | Part VI review |

## Part VII — Measurement, observers, and the self-reference results (83–96)
*Tracks Zurek RMP (2003), Everett (1957), Rovelli (1996), Frauchiger–Renner (2018).*

| # | Session |
|---|---|
| 83 | The measurement problem, stated without hand-waving |
| 84 | Von Neumann's chain and the Heisenberg cut |
| 85 | Decoherence I: entanglement with the environment |
| 86 | Decoherence II: einselection and pointer states |
| 87 | What decoherence solves, and what it leaves untouched |
| 88 | Everett's relative-state formulation (1957) |
| 89 | Branching, and why other branches are dynamically inaccessible |
| 90 | Rovelli's relational quantum mechanics (1996) |
| 91 | Breuer's theorem: the impossibility of accurate self-measurement |
| 92 | Wigner's friend |
| 93 | Frauchiger–Renner (2018) |
| 94 | Quantum reference frames |
| 95 | The interpretation map: Copenhagen, Bohmian, GRW, QBism, Everett |
| 96 | Part VII review |

## Part VIII — Your own question (97–100)

| # | Session |
|---|---|
| 97 | Restating your original intuition inside the formalism |
| 98 | Theorem, postulate, or interpretation: what would count as new |
| 99 | How to read a quant-ph paper; how to write to an author |
| 100 | Where to go from here |

---

## How to run this

Ten minutes is enough to read one session, not to read it twice. Read once at pace, and if a session leaves you unable to state its one claim in a sentence, re-read it the next night rather than moving on. Sessions marked *review* exist so that slippage has somewhere to be absorbed.

The parts are cumulative: Part V is unreadable without Part IV, and Part VII is unreadable without Part III. Skipping ahead to the parts you care about is possible but will cost you more time than it saves.
