# Writing plan

*Companion to [00-syllabus.md](00-syllabus.md). The syllabus fixes what each session establishes and which earlier sessions it builds on. This file fixes how a session is written.*

## A session

1. **Heading.** "Session NN. Title", then the kind (definition, theorem, construction, calculation, example, experiment, survey or problems) and "Builds on:" with the session numbers from the syllabus.
2. **The claim.** The syllabus's *Establishes* line, as the first paragraph. The rest of the session earns it.
3. **Recall.** For cited results that are not on the Part's toolkit page: a short list at the start of the session, as its first section ("## 5.1 Recall") or as a paragraph before it, one item per earlier session, each result restated with its session and section number. Names of recalled results are in italics: bold marks only the place where a term is defined.
4. **Definitions.** Each new term is printed in bold where it is defined, and is not used before.
5. **Statement and proof.** Every step either is an elementary manipulation written out on the page or cites a session by number. Never write "clearly", "obviously", "it is easy to see" or "it can be shown". A computation is written out, not summarised.
6. **Worked example.** The result computed on the smallest case that shows it (usually a qubit, two qubits or a qutrit), with every line of the arithmetic.
7. **Boundary.** Where it is natural, what fails when a hypothesis is dropped, with a counterexample.
8. **Gap.** If the syllabus lists a gap for the session, a box reading "Gap. Omitted: ... Why: ... Where: ...", in the same words as the syllabus.
9. **Exercises,** in three tiers:
   - *Check*: compute.
   - *Prove*: rerun the argument on a variant.
   - *Extend*: optional.

   Every exercise is solvable from the session and earlier ones. The solutions are in a separate volume, keyed by session number. No step of the text is left to an exercise, and nothing later depends on one. A survey session may have a few exercises on its one checkable idea.

## A Part

- **An opening page.** It states the Part's goal, then its toolkit: every result from an earlier Part that the Part's sessions use, each with its session number and its statement. The toolkit page is generated from the sessions' *Builds on* lists.
- **The sessions,** in order.
- **A problem set,** in every Part except 26. It combines the Part's results in new ways. Nothing later cites it.

## Rules of writing

- **Voice.** The voice of *MPPI from the Beginning*: calm, exact and plain. Short declarative sentences, British spelling. No hype, no metaphors, no exclamation marks.
- **Concise means no wasted words.** It never means a skipped step.
- **One unit of understanding per session.** If a draft needs two, split it, and change the syllabus first.
- **Change the syllabus first.** If a draft needs a result that no earlier session establishes, add a session for it in its proper place before writing; never prove it in passing.
- **Use the literature's name** for every result, and give the original reference where the result first appears.
- **Label claims.** Mark every statement of consequence as a definition, theorem, postulate, experimental result or interpretation.
- **History appears only as content:** who proved what, what an experiment measured, which loophole it closed.
- **Check the primary source** for every number, attribution, date and experimental value before the session is written.
- **Excursions.** A session that leaves finite dimensions is titled *Excursion*, says what it assumes, and labels every gap.

## Notation

- **Scalars and inner products.** Scalars are F = R or C. The inner product <u, v> is conjugate-linear in its first slot.
- **Dirac notation** is used from Session [[dirac-notation]].
- **Dual space.** V* = L(V, F).
- **Pauli matrices.** Written X, Y, Z. The forms σ_x, σ_y, σ_z are noted once, as the literature's alternative.
- **ħ.** Explicit from the dynamics postulate (Session [[dynamics-postulate]]) on. The mathematics Parts write exp(-itH). Session [[no-canonical-pair-finite]] writes the canonical pair as [Q, P], so X keeps its meaning as the Pauli matrix and the shift.
- **Measurement parameters.** Unsharpness and measurement strength are s. Detection efficiency is η. Ozawa's error and disturbance are ε(A) and η(B).
- **Entropy.** The natural logarithm (nats). log₂ and the binary entropy h(q) are defined in Session [[shannon-entropy]].
- **Order of parties.** Two-party states list Alice first. Two-qubit columns are in the order 00, 01, 10, 11.

## Files and Markdown

**Files.** Session n is the file `sessions/NNN-slug.md`, and its solutions are in `solutions/NNN-slug.md`. NNN is n padded to three digits; the slug is the one in the syllabus. A session's number appears in its heading and in references to it.

**Layout of a session file.**

```text
# 1.5. Limits of real sequences

*Theorem. Builds on Sessions 3 and 4.*

**Claim.** The session's one claim, in one to three sentences.

## 5.1 First section
...
## 5.4 Worked example
...

> **Gap.** Omitted: ... Why: ... Where: ...      (only where the syllabus lists a gap)

## Exercises

*Check*

1. ...

*Prove*

4. ...

*Extend*

6. ...

Solutions: [solutions/005-limits-of-sequences.md](../solutions/005-limits-of-sequences.md).
```

- **Headings.** A session's heading gives its Part and its number in the book, then its title: "# 1.5. Limits of real sequences" is Session 5, in Part 1. Session numbers run through the whole book, so prose refers to a session by its number alone ("Session 5"), and sections are numbered 5.1, 5.2 and so on. Parts are numbered 1 to 26.
- **The kind line.** It repeats the kind from the syllabus, and its "Builds on" list repeats the syllabus's list for the session.
- **The solutions file** opens with "# Solutions to 1.5. Limits of real sequences", then has the sections "## Check", "## Prove" and "## Extend". Each solution starts with the exercise's number in bold ("**4.**"), and parts are labelled (a), (b), (c). Every exercise is solved in full; a solution cites results as the text does and does not prove an earlier result again.
- **References.** Refer to other sessions as "Session 7". The reader turns these into links, and `plan/check_sessions.py` checks that none points forward or outside the session's prerequisites.
- **Statements and proofs.** Label statements inside a session in bold ("**Lemma.**", "**Theorem.**", "**Definition.**"). A proof opens with "*Proof.*" and ends with ∎.

**Mathematics in Markdown.** The reader renders mathematics with KaTeX, and GitHub renders it too.
- **Delimiters.** Inline mathematics is `$...$` on a single line. Displayed mathematics is `$$` on a line of its own, then the formula, then `$$` on a line of its own.
- **Order signs.** Inside mathematics write `\lt`, `\gt`, `\le` and `\ge`, never a bare `<` or `>`.
- **Tables.** Never put `|` inside a table. Write `\lvert x \rvert` and `\lVert x \rVert` there, or avoid tables that need them.
- **Dollar signs.** Never put a literal dollar sign in text.
- **Brackets.** Write inner products and kets with `\langle`, `\rangle` and `\lvert`, `\rangle`.

**Notation of Part 1.**
- **Numbers.** $\mathbb{N} = \{1, 2, 3, \dots\}$. Write "n ≥ 0" explicitly when 0 is wanted. $\mathbb{Z}$, $\mathbb{Q}$ and $\mathbb{R}$ are the integers, rationals and reals.
- **Intervals** are written $[a,b]$, $(a,b)$ and $[a,b)$.
- **Sets.** Set-builder $\{x \in S : P(x)\}$. Subset $\subseteq$. The empty set $\emptyset$. Complement $A \setminus B$.
- **Functions.** $f : A \to B$ with $x \mapsto f(x)$. The image is $f(A)$ and the preimage $f^{-1}(B)$. Composition is $g \circ f$.
- **Sequences.** $(a_n)$, with $a_n \to a$ or $\lim_{n \to \infty} a_n = a$. Subsequences are $(a_{n_k})$.
- **Small quantities.** $\varepsilon$ and $\delta$ are positive reals, and the text says so each time: "let $\varepsilon \gt 0$".
- **Index letters.** When $j$, $k$, $m$, $n$ and $n_0$ index sums, products, powers or sequences, they stand for natural numbers or zero (Session [[induction-finite-sums]], Section 3.3). Other letters, such as $K$, $M$, $s$ and $t$, are used for real bounds.
- **Decimals** are defined in Session [[continuous-functions]], Section 7.9. Before it, numbers are written as fractions.
- **Countable choice.** The book assumes the axiom of countable choice, stated in Session [[continuous-functions]], Section 7.3. A proof that picks one element from each of infinitely many nonempty sets, by no rule, cites it there. A proof that can pick by a rule, such as the least natural number with a property, does so and needs no axiom.
- **Bounds.** $\sup S$ and $\inf S$.
- **Words in prose.** Write "if and only if", never "iff". Write "for every" and "there exists" in prose; keep $\forall$ and $\exists$ for displayed formulas that state negations.

## Proof routes for the hardest results

These routes were chosen when the syllabus was designed and checked against the sources.

**Mathematics.**
- The spectral theorem (Session [[spectral-theorem-normal]]): an eigenvalue exists by the fundamental theorem of algebra, which is proved by the minimum-modulus argument; then triangular form, then Schur, then "a normal triangular matrix is diagonal". No determinants.
- Continuous unitary groups have a generator (Session [[one-parameter-unitary-groups]]): the Neumann series and V = (1/ε)∫U, so finite-dimensional Stone needs no differentiability assumption.
- The SVD (Session [[svd]]) from the eigenbasis of T†T, and the polar decomposition from the SVD. One equal-Gram lemma serves unitary freedom, purification and Kraus freedom.

**Channels and distinguishability.**
- Channels: the Choi cycle, CP ⇒ positive Choi operator ⇒ Kraus ⇒ CP (Sessions [[choi-cp-positive]] and [[kraus-representation]]); Stinespring from Kraus. Naimark both by an isometry and by direct sum.
- Fidelity: Uhlmann's theorem first. Then Fuchs-van de Graaf: the upper bound by purifications, the lower bound by the Powers-Størmer inequality (Session [[powers-stormer]]).
- The Helstrom bound by the Jordan decomposition: the maximum of tr(PA) over 0 ≤ P ≤ I is tr A₊.

**Q1: measurement and disturbance.**
- Englert's relation: purify the detector, then use the contractivity of the trace distance.
- The Zeno effect: an exact bound from 1 - cos x ≤ x²/2. The trapped-ion experiment tested (1 - cosⁿ(π/n))/2 (Session [[zeno-experiment]]).
- The Wigner-Araki-Yanase theorem in full for precise, repeatable measurements, from the conservation of L_S ⊗ I + I ⊗ L_P.
- Ozawa: the identity [N,D] + [N,B] + [A,D] = -[A,B] (Session [[ozawa-identity]]), then Cauchy-Schwarz.
- Repeated weak measurement: E[√(p(1-p))] contracts exactly at every step, so no martingale convergence theorem is needed.

**Q3: Bell.**
- Fine's theorem follows Fine (1982), not a correlator-first route. First, local models are equivalent to joint distributions. Second, triples of ±1 variables. Third, gluing two triples along (B0, B1), so that the eight CHSH inequalities remain (Sessions [[fine-joint-distribution]]-[[fine-gluing]]).
- Tsirelson's bound from C² = 4I - [A0,A1] ⊗ [B0,B1], then a sum-of-squares proof with its equality conditions.
- The Werner state's CHSH value is max(2, 2√2 p).
- The detection loophole: Larsson's bound 4/η - 2, with η the minimum conditional detection probability. An explicit local model attains it.
- Bell tests as hypothesis tests: Azuma-Hoeffding, with no independence assumed between trials.

**Q3: contextuality and the reality of the state.**
- Kochen-Specker has three independent proofs:
  - the Peres-Mermin square;
  - the 18 vectors of Cabello, Estebaranz and García-Alcaine in dimension four;
  - Peres' 33 rays in dimension three: 3 + 6 + 12 + 12 rays from (0,0,1), (0,1,1), (0,1,√2) and (1,1,√2), with 16 orthogonal triples and 72 orthogonal pairs.

  The lift to every dimension d ≥ 3 is by restriction to three-dimensional subspaces.
- Gleason's theorem.
  - Busch's version for effects, in three steps: additivity, linear extension, the Born rule.
  - The projective version by the Cooke-Keane-Moran staircase, from frame functions on S² to the complex lift. Follow the corrected version in the Chalmers thesis noted under the sessions below. Its compactness step is a labelled gap.
- KCBS: the noncontextual bound 2 from the independent sets of the five-cycle; the quantum value √5 from the pentagram; and the quantum maximum √5 by Bessel's inequality.
- PBR, in four steps:
  - the case of |0> and |+>;
  - the two-copy threshold;
  - the n-copy circuit H^⊗n R_α Z_β^⊗n, with condition 2^(1/n) - 1 ≤ tan(θ/2);
  - the general theorem.

**Q2: observers inside the system.**
- Breuer's theorem follows Breuer (1995), sections 3-5:
  - inference maps;
  - proper inclusion and the meshing condition;
  - Propositions 1 and 2 with the Lemma;
  - the strengthening for states that differ only in their EPR phases;
  - the conclusion about relative validity (Sessions [[breuer-inference-maps]]-[[breuer-what-remains]]).
- Frauchiger-Renner: the coin √(1/3)|h> + √(2/3)|t>, the event (ok̄, ok) with probability 1/12, and the inference chain under assumptions Q, C and S.
- Local friendliness:
  - the LF polytope defined through marginals;
  - LF equals local for two settings per side;
  - for three settings, the inequality of Bong et al. (2020), with local-friendly bound 6 and quantum maximum about 7.345;
  - the simplest analytic violation, a CHSH-type sub-inequality at 2√2.

**Interpretations.**
- Pilot-wave theory on a finite configuration space, the Bell-Vink process: the finite probability current, positive-part jump rates, then equivariance by Grönwall's uniqueness (Session [[bell-vink-equivariance]]). It is restricted to intervals on which no amplitude vanishes.

## Before writing a Part

1. Check every citation in the Part against its primary source, and attach the sources to the sessions.
2. Generate the Part's toolkit page from the sessions' *Builds on* lists.
3. Write the sessions in order. After each one, check that it uses nothing outside its *Builds on* list and the sessions those depend on.
4. Write the exercises and their solutions with the session, not afterwards.

## Session notes

Writing guidance attached to particular sessions: which source a proof should follow, a subtle point, or a check to make first.

<<NOTES>>
