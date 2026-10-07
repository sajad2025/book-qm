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
- **A problem set,** in every Part except XXVI. It combines the Part's results in new ways. Nothing later cites it.

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
- **Dirac notation** is used from Session 55.
- **Dual space.** V* = L(V, F).
- **Pauli matrices.** Written X, Y, Z. The forms σ_x, σ_y, σ_z are noted once, as the literature's alternative.
- **ħ.** Explicit from the dynamics postulate (Session 125) on. The mathematics Parts write exp(-itH). Session 102 writes the canonical pair as [Q, P], so X keeps its meaning as the Pauli matrix and the shift.
- **Measurement parameters.** Unsharpness and measurement strength are s. Detection efficiency is η. Ozawa's error and disturbance are ε(A) and η(B).
- **Entropy.** The natural logarithm (nats). log₂ and the binary entropy h(q) are defined in Session 200.
- **Order of parties.** Two-party states list Alice first. Two-qubit columns are in the order 00, 01, 10, 11.

## Files and Markdown

**Files.** Session n is the file `sessions/NNN-slug.md`, and its solutions are in `solutions/NNN-slug.md`. NNN is n padded to three digits; the slug is the one in the syllabus. A session's number appears in its heading and in references to it.

**Layout of a session file.**

```text
# Session 5. Limits of real sequences

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

- **Headings.** Sessions are numbered without padding in headings and prose ("Session 5"), and sections as 5.1, 5.2 and so on.
- **The kind line.** It repeats the kind from the syllabus, and its "Builds on" list repeats the syllabus's list for the session.
- **The solutions file** opens with "# Solutions to Session 5. Limits of real sequences", then has the sections "## Check", "## Prove" and "## Extend". Each solution starts with the exercise's number in bold ("**4.**"), and parts are labelled (a), (b), (c). Every exercise is solved in full; a solution cites results as the text does and does not prove an earlier result again.
- **References.** Refer to other sessions as "Session 7". The reader turns these into links, and `plan/check_sessions.py` checks that none points forward or outside the session's prerequisites.
- **Statements and proofs.** Label statements inside a session in bold ("**Lemma.**", "**Theorem.**", "**Definition.**"). A proof opens with "*Proof.*" and ends with ∎.

**Mathematics in Markdown.** The reader renders mathematics with KaTeX, and GitHub renders it too.
- **Delimiters.** Inline mathematics is `$...$` on a single line. Displayed mathematics is `$$` on a line of its own, then the formula, then `$$` on a line of its own.
- **Order signs.** Inside mathematics write `\lt`, `\gt`, `\le` and `\ge`, never a bare `<` or `>`.
- **Tables.** Never put `|` inside a table. Write `\lvert x \rvert` and `\lVert x \rVert` there, or avoid tables that need them.
- **Dollar signs.** Never put a literal dollar sign in text.
- **Brackets.** Write inner products and kets with `\langle`, `\rangle` and `\lvert`, `\rangle`.

**Notation of Part I.**
- **Numbers.** $\mathbb{N} = \{1, 2, 3, \dots\}$. Write "n ≥ 0" explicitly when 0 is wanted. $\mathbb{Z}$, $\mathbb{Q}$ and $\mathbb{R}$ are the integers, rationals and reals.
- **Intervals** are written $[a,b]$, $(a,b)$ and $[a,b)$.
- **Sets.** Set-builder $\{x \in S : P(x)\}$. Subset $\subseteq$. The empty set $\emptyset$. Complement $A \setminus B$.
- **Functions.** $f : A \to B$ with $x \mapsto f(x)$. The image is $f(A)$ and the preimage $f^{-1}(B)$. Composition is $g \circ f$.
- **Sequences.** $(a_n)$, with $a_n \to a$ or $\lim_{n \to \infty} a_n = a$. Subsequences are $(a_{n_k})$.
- **Small quantities.** $\varepsilon$ and $\delta$ are positive reals, and the text says so each time: "let $\varepsilon \gt 0$".
- **Index letters.** When $j$, $k$, $m$, $n$ and $n_0$ index sums, products, powers or sequences, they stand for natural numbers or zero (Session 3, Section 3.3). Other letters, such as $K$, $M$, $s$ and $t$, are used for real bounds.
- **Decimals** are defined in Session 7, Section 7.9. Before it, numbers are written as fractions.
- **Countable choice.** The book assumes the axiom of countable choice, stated in Session 7, Section 7.3. A proof that picks one element from each of infinitely many nonempty sets, by no rule, cites it there. A proof that can pick by a rule, such as the least natural number with a property, does so and needs no axiom.
- **Bounds.** $\sup S$ and $\inf S$.
- **Words in prose.** Write "if and only if", never "iff". Write "for every" and "there exists" in prose; keep $\forall$ and $\exists$ for displayed formulas that state negations.

## Proof routes for the hardest results

These routes were chosen when the syllabus was designed and checked against the sources.

**Mathematics.**
- The spectral theorem (Session 68): an eigenvalue exists by the fundamental theorem of algebra, which is proved by the minimum-modulus argument; then triangular form, then Schur, then "a normal triangular matrix is diagonal". No determinants.
- Continuous unitary groups have a generator (Session 122): the Neumann series and V = (1/ε)∫U, so finite-dimensional Stone needs no differentiability assumption.
- The SVD (Session 140) from the eigenbasis of T†T, and the polar decomposition from the SVD. One equal-Gram lemma serves unitary freedom, purification and Kraus freedom.

**Channels and distinguishability.**
- Channels: the Choi cycle, CP ⇒ positive Choi operator ⇒ Kraus ⇒ CP (Sessions 230 and 231); Stinespring from Kraus. Naimark both by an isometry and by direct sum.
- Fidelity: Uhlmann's theorem first. Then Fuchs-van de Graaf: the upper bound by purifications, the lower bound by the Powers-Størmer inequality (Session 147).
- The Helstrom bound by the Jordan decomposition: the maximum of tr(PA) over 0 ≤ P ≤ I is tr A₊.

**Q1: measurement and disturbance.**
- Englert's relation: purify the detector, then use the contractivity of the trace distance.
- The Zeno effect: an exact bound from 1 - cos x ≤ x²/2. The trapped-ion experiment tested (1 - cosⁿ(π/n))/2 (Session 268).
- The Wigner-Araki-Yanase theorem in full for precise, repeatable measurements, from the conservation of L_S ⊗ I + I ⊗ L_P.
- Ozawa: the identity [N,D] + [N,B] + [A,D] = -[A,B] (Session 279), then Cauchy-Schwarz.
- Repeated weak measurement: E[√(p(1-p))] contracts exactly at every step, so no martingale convergence theorem is needed.

**Q3: Bell.**
- Fine's theorem follows Fine (1982), not a correlator-first route. First, local models are equivalent to joint distributions. Second, triples of ±1 variables. Third, gluing two triples along (B0, B1), so that the eight CHSH inequalities remain (Sessions 309-311).
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
  - the conclusion about relative validity (Sessions 403-407).
- Frauchiger-Renner: the coin √(1/3)|h> + √(2/3)|t>, the event (ok̄, ok) with probability 1/12, and the inference chain under assumptions Q, C and S.
- Local friendliness:
  - the LF polytope defined through marginals;
  - LF equals local for two settings per side;
  - for three settings, the inequality of Bong et al. (2020), with local-friendly bound 6 and quantum maximum about 7.345;
  - the simplest analytic violation, a CHSH-type sub-inequality at 2√2.

**Interpretations.**
- Pilot-wave theory on a finite configuration space, the Bell-Vink process: the finite probability current, positive-part jump rates, then equivariance by Grönwall's uniqueness (Session 439). It is restricted to intervals on which no amplitude vanishes.

## Before writing a Part

1. Check every citation in the Part against its primary source, and attach the sources to the sessions.
2. Generate the Part's toolkit page from the sessions' *Builds on* lists.
3. Write the sessions in order. After each one, check that it uses nothing outside its *Builds on* list and the sessions those depend on.
4. Write the exercises and their solutions with the session, not afterwards.

## Session notes

Writing guidance attached to particular sessions: which source a proof should follow, a subtle point, or a check to make first.

- **Session 23. Every nonconstant complex polynomial has a root.** Follow Axler, Linear Algebra Done Right, 4th ed., Ch. 4, result 4.12 (p. 125), or Rudin PMA Thm 8.8. a_k is the lowest nonzero coefficient of the expansion at z0, not the leading coefficient of p.
- **Session 155. Interior and boundary points of convex sets.** Interior point: if S is not in a hyperplane it contains n+1 affinely independent points, and the open simplex they span contains a ball. Segment: the intersection with the line is closed, bounded and convex, hence an interval; points beyond its ends lie outside S.
- **Session 159. Bounded solution sets of linear inequalities are polytopes.** If the tight constraints at x leave a nonzero direction d, x +- eps d stays feasible for small eps because the slack constraints are strict, so x is not extreme.
- **Session 167. Tensor products of operators and the Kronecker product.** Eigenvalues: if A and B are upper triangular in bases (e_i) and (f_j), A (x) B is upper triangular in the lexicographically ordered basis e_i (x) f_j with diagonal a_ii b_jj.
- **Session 173. Properties of the partial trace.** Support lemma: tr(((I-P) (x) I) M) = tr((I-P) tr_B M) = 0 with M >= 0 forces M((I-P) (x) I) = 0.
- **Session 196. The partial-transpose criterion.** Credit the criterion to A. Peres, Phys. Rev. Lett. 77, 1413 (1996).
- **Session 260. The Coffman-Kundu-Wootters inequality.** W: rho_AB = (1/3)|00><00| + (2/3)|Psi+><Psi+|; ensemble vectors lie in its range, a|00> + b|Psi+> has 2|det| = |b|^2, and C is homogeneous of degree 2, so every ensemble averages <Psi+|rho_AB|Psi+> = 2/3.
- **Session 270. The Wigner-Araki-Yanase theorem.** Follow Loveridge and Busch (2011), Sec. 2. Left side: <phi_i|L_S|phi_j> + <phi_i|phi_j><xi|L_P|xi>, the second term zero. Right side: the L_S term has Q_i Q_j = 0 on the probe, the L_P term has P_i P_j = 0 on the system.
- **Session 295. Events, light cones and spacelike separation.** Cited by local-causality for the common past of two measurements.
- **Session 310. Fine's theorem II: joint distributions of three +-1 variables.** Follow Fine (PRL 48, 291; J. Math. Phys. 23, 1306, 1982) and Halliwell, Phys. Lett. A 378, 2945 (2014), Sec. IV: each sign pattern s and its negation bound the triple moment to an interval of length 2(1 + pair terms); pair positivity makes the intervals meet.
- **Session 311. Fine's theorem III: sufficiency of CHSH in general.** Follow Fine (1982). Triple (A0,B0,B1) gives C_B0B1 in [|E00+E01|-1, 1-|E00-E01|], similarly for A1; each meets the (B0,B1) pair-positivity interval because the gluing of fine-triples always exists; Helly in one dimension finishes. Cite Halliwell (2014) only for the zero-average case, whose explicit construction goes to the problems.
- **Session 319. The CHSH value of two-qubit Werner states.** With A0 = +-I, condition on Alice's A1 outcome a1: the CHSH operator on Bob's side becomes +-(B0+B1) + a1(B0-B1), which is 2B0 or 2B1 up to sign, of norm at most 2; likewise for the other cases. The spin bound is the parallelogram law; it is attained by the angles of chsh-quantum-value at p = 1.
- **Session 320. A local model for Werner states with p <= 1/2.** Write b = (a.b)a + b_perp; E[sgn(a.lambda) b_perp.lambda] = 0 by the rotation by pi about a, and E|a.lambda| = 1/2. A qubit projective measurement is trivial (+-I) or a spin direction, and two-outcome statistics are fixed by marginals and correlation.
- **Session 322. The vertices of the CHSH no-signalling polytope.** Follow Barrett et al. (2005), Sec. II.
- **Session 324. Jordan's lemma for two +-1 observables.** If A0A1 v = lambda v, then A0 v is an eigenvector with eigenvalue conj(lambda), A1 v = lambda A0 v, and span{v, A0 v} is invariant under both; induct on the orthogonal complement, which is invariant since A0, A1 are self-adjoint. Rabelo, Zhi, Scarani, PRL 109, 180401 (2012), Lemma 1.
- **Session 339. Classical causal explanations of Bell correlations are fine-tuned.** Define fine-tuning as an observed conditional independence that is not implied by the causal graph. For each mechanism, write the observed marginal as a sum over lambda and show the lambda-level dependence must be nonzero.
- **Session 356. Frame functions on the sphere S^2.** Follow the corrected Cooke-Keane-Moran proof in the Chalmers thesis 'Gleasons sats' (odr.chalmers.se/handle/20.500.12380/257144), not CKM's original, which has an oversight in Piron's lemma and an erroneous topological step in the extreme-value proposition.  An independent full proof: A. Dvurecenskij, Gleason's Theorem and Its Applications (Kluwer, 1993), Ch. 3.
- **Session 357. A functional equation on [0,1].** Follow the corrected Cooke-Keane-Moran proof in the Chalmers thesis 'Gleasons sats' (odr.chalmers.se/handle/20.500.12380/257144), not CKM's original, which has an oversight in Piron's lemma and an erroneous topological step in the extreme-value proposition.
- **Session 358. Frame functions do not rise along descending circles.** Follow the corrected Cooke-Keane-Moran proof in the Chalmers thesis 'Gleasons sats' (odr.chalmers.se/handle/20.500.12380/257144), not CKM's original, which has an oversight in Piron's lemma and an erroneous topological step in the extreme-value proposition. Proof: with t' on C(s) orthogonal to t, f(t) + f(t') = f(s) + c, and a frame through t' and a point of E_p gives f(t') > c - eps.
- **Session 359. Piron's lemma: reaching lower points by descending circles.** Follow the corrected Cooke-Keane-Moran proof in the Chalmers thesis 'Gleasons sats' (odr.chalmers.se/handle/20.500.12380/257144), not CKM's original, which has an oversight in Piron's lemma and an erroneous topological step in the extreme-value proposition. Use the corrected version of this lemma.
- **Session 360. Gleason in R^3: the symmetric case.** Follow the corrected Cooke-Keane-Moran proof in the Chalmers thesis 'Gleasons sats' (odr.chalmers.se/handle/20.500.12380/257144), not CKM's original, which has an oversight in Piron's lemma and an erroneous topological step in the extreme-value proposition.
- **Session 361. Nonnegative frame functions attain their extremes.** Follow the corrected Cooke-Keane-Moran proof in the Chalmers thesis 'Gleasons sats' (odr.chalmers.se/handle/20.500.12380/257144), not CKM's original, which has an oversight in Piron's lemma and an erroneous topological step in the extreme-value proposition. CKM's topological argument here is wrong; follow the thesis's corrected Proposition 2.
- **Session 362. Gleason's theorem in R^3.** Follow the corrected Cooke-Keane-Moran proof in the Chalmers thesis 'Gleasons sats' (odr.chalmers.se/handle/20.500.12380/257144), not CKM's original, which has an oversight in Piron's lemma and an erroneous topological step in the extreme-value proposition. The thesis's Lemma 8 (assembly).
- **Session 363. From R^3 to R^d and C^d.** Follow the corrected Cooke-Keane-Moran proof in the Chalmers thesis 'Gleasons sats' (odr.chalmers.se/handle/20.500.12380/257144), not CKM's original, which has an oversight in Piron's lemma and an erroneous topological step in the extreme-value proposition. The thesis's Lemmas 9-12.
- **Session 377. The Kochen-Specker qubit model: a psi-epistemic example.** By rotation invariance take n = e_z and m = (sin t, 0, cos t); the probability is a double integral in (z, phi) computed in closed form. Non-orthogonal means n != -n'.
- **Session 386. The insolubility theorem: a mixed apparatus does not help.** Certain pointer value k gives U(phi_k (x) a_j) in H (x) Q_k for each j; the (1,2) block is (1/2) sum_j r_j |U(phi_1 a_j)><U(phi_2 a_j)|, and unitarity keeps the vectors orthonormal in j.
- **Session 395. Einselection: the predictability sieve.** In the (y,z) block M = [[-gamma,-omega],[omega,0]] the slow eigenvalue is about -omega^2/gamma; its RIGHT eigenvector has y = -(omega/gamma)z, its LEFT eigenvector y = +(omega/gamma)z, and the late-time amplitude is maximised along the left one (check: gamma=1, omega=0.1, t=50 gives optimal y/z = 0.101).
- **Session 403. Measurements as inference maps.** Follow T. Breuer, Philos. Sci. 62, 197-214 (1995), secs. 3.1-3.2.
- **Session 404. Measurement from inside: proper inclusion and meshing.** Breuer 1995, secs. 3.3-3.4.
- **Session 405. Breuer's theorem: no complete measurement from inside.** Breuer 1995, secs. 3.4-3.5. Prop. 1: if theta(S_A) = {s}, meshing forces S_A = {s|_A}, so theta({s|_A}) = {s} and likewise {s'} for s' != s with the same restriction, a contradiction. Prop. 2: s1 in theta(S^1) forces s_A in S^1, s2 in theta(S^2) forces s_A in S^2, and theta({s_A}) contains both s1, s2 and lies in both sets. Stress that counting arguments are not the proof.
- **Session 406. Breuer's theorem and EPR correlations.** Breuer 1995, sec. 4.
- **Session 407. What measurement from inside can still do.** Breuer 1995, sec. 5. Optional remark or problem: a unitary on S = A (x) R followed by a projective readout of A has effects U^dagger(Q_j (x) I_R)U, whose ranks are multiples of dim R.
- **Session 425. Consistent histories.** Coarse-graining h and h' gives class operator C_h + C_h', so p(h or h') = p(h) + p(h') + 2 Re D(h,h'). Source: R. B. Griffiths, Consistent Quantum Theory (CUP 2002); locate Griffiths' published reply to Frauchiger-Renner and verify the reference before writing.
