# Session 6. Monotone sequences, subsequences and Cauchy sequences

*Theorem. Builds on Session 5.*

**Claim.** Every bounded monotone real sequence converges, every bounded real sequence has a convergent subsequence (Bolzano-Weierstrass), and a real sequence converges if and only if it is Cauchy.

Session 5 proved facts about a sequence that is already known to converge. This session gives ways to prove that a sequence converges when its limit is not known in advance. The least-upper-bound property of Session 4 is the source of all three results: it enters once, in the proof of the monotone convergence theorem, and the other two results are built on that theorem.

## 6.1 Recall

The proofs use the following.

From Session 2: the negation of "for every $x$, $P(x)$" is "there exists $x$ with not $P(x)$", and the negation of "there exists $x$ with $P(x)$" is "for every $x$, not $P(x)$".

From Session 3:
- Proof by induction, also in the form that starts from 0 (Section 3.3). The *well-ordering* of $\mathbb{N}$ (Section 3.4): every nonempty subset of $\mathbb{N}$ has a least element.
- *Definition by recursion* (Section 3.5): given a set $X$, an element $c \in X$ and, for each $n \in \mathbb{N}$, a function $g_n : X \to X$, there is exactly one sequence $(s_n)$ in $X$ with $s_1 = c$ and $s_{n+1} = g_n(s_n)$ for every $n$.
- Every $n \in \mathbb{N}$ satisfies $n \ge 1$, so $n \gt 0$ (Lemma 1). If $n \in \mathbb{N}$ and $n \ne 1$, then $n - 1 \in \mathbb{N}$ (Lemma 2). If $m, n \in \mathbb{N}$, then $m + n \in \mathbb{N}$ and $mn \in \mathbb{N}$ (Lemma 3). If $p \lt q$ are natural numbers, then $q - p \in \mathbb{N}$ and $q \ge p + 1$ (Lemma 4(a)).
- The rules for finite sums (S1) to (S6), the sums of constants $\sum_{k=1}^{n} c = nc$, and the laws of powers (Section 3.6), and the geometric sum (Section 3.7).

From Session 4:
- $\mathbb{R}$ is an ordered field. Every nonempty subset $S$ of $\mathbb{R}$ that is bounded above has a least upper bound $\sup S$, and every nonempty subset that is bounded below has a greatest lower bound $\inf S$.
- The *approximation property*: if $S$ is nonempty and $L = \sup S$, then for every $\varepsilon \gt 0$ there exists $x \in S$ with $x \gt L - \varepsilon$.
- The *Archimedean property*: for every real $x$ there exists $n \in \mathbb{N}$ with $n \gt x$.

From Session 5:
- **Absolute value.** $\lvert x \rvert \le c$ if and only if $-c \le x \le c$, and likewise with $\lt$; $\lvert -x \rvert = \lvert x \rvert$; $\lvert xy \rvert = \lvert x \rvert \lvert y \rvert$; the triangle inequality $\lvert x + y \rvert \le \lvert x \rvert + \lvert y \rvert$, and its form for finite sums, $\bigl\lvert \sum_{k=1}^{n} x_k \bigr\rvert \le \sum_{k=1}^{n} \lvert x_k \rvert$ (Section 5.2). The larger of two numbers $s$, $t$ is written $\max\{s, t\}$.
- **Convergence.** $a_n \to a$ means: for every $\varepsilon \gt 0$ there exists $N \in \mathbb{N}$ such that $\lvert a_n - a \rvert \lt \varepsilon$ for every $n \ge N$. A sequence is convergent if it has a limit, and divergent otherwise.
- **Bounded.** $(a_n)$ is bounded if there exists $M$ with $\lvert a_n \rvert \le M$ for every $n$.
- A sequence has at most one limit, and a convergent sequence is bounded. For every sequence and every $m \in \mathbb{N}$ there exists $B \ge 0$ with $\lvert a_k \rvert \le B$ for every natural number $k \le m$ (the lemma on finitely many terms).
- If $a_n \to a$ and $b_n \to b$, then $a_n + b_n \to a + b$ and $a_n b_n \to ab$; if also $b \ne 0$ and $b_n \ne 0$ for every $n$, then $a_n / b_n \to a/b$. A constant sequence $c, c, c, \dots$ converges to $c$.
- **Non-strict inequalities.** If $a_n \to a$, $b_n \to b$ and $a_n \le b_n$ for every $n$, then $a \le b$.
- **Geometric sequence.** If $\lvert r \rvert \lt 1$, then $r^n \to 0$.

## 6.2 Monotone sequences

**Definition.** A real sequence $(a_n)$ is **nondecreasing** if $a_n \le a_{n+1}$ for every $n \in \mathbb{N}$, and **nonincreasing** if $a_n \ge a_{n+1}$ for every $n$. It is **monotone** if it is nondecreasing or nonincreasing. It is **bounded above** if there exists $M$ with $a_n \le M$ for every $n$, and **bounded below** if there exists $K$ with $a_n \ge K$ for every $n$.

A bounded sequence is bounded above and below: if $\lvert a_n \rvert \le M$ for every $n$, then $-M \le a_n \le M$ for every $n$ (Session 5).

The definition compares neighbouring terms only. The first lemma extends the comparison to any two terms.

**Lemma (comparison of terms).** If $(a_n)$ is nondecreasing, then $a_m \le a_n$ whenever $m \le n$. If $(a_n)$ is nonincreasing, then $a_m \ge a_n$ whenever $m \le n$.

*Proof.* Let $(a_n)$ be nondecreasing, and fix $m \in \mathbb{N}$. For each $j \ge 0$ let $P(j)$ be the statement $a_m \le a_{m+j}$; here $m + j$ is $m$ if $j = 0$, and lies in $\mathbb{N}$ by Session 3, Lemma 3, otherwise. $P(0)$ reads $a_m \le a_m$, which holds. Suppose $P(j)$ holds. Then $a_m \le a_{m+j}$, and $a_{m+j} \le a_{m+j+1}$ because the sequence is nondecreasing, so $a_m \le a_{m+j+1}$, which is $P(j+1)$. By induction from 0 (Session 3), $P(j)$ holds for every $j \ge 0$. Now let $m \le n$. If $n = m$, take $j = 0$. If $n \gt m$, then $j = n - m \in \mathbb{N}$ by Session 3, Lemma 4(a). In both cases $n = m + j$, so $a_m \le a_n$.

Let $(a_n)$ be nonincreasing, and put $b_n = -a_n$. Adding $-a_n - a_{n+1}$ to both sides of $a_{n+1} \le a_n$ gives $-a_n \le -a_{n+1}$, that is, $b_n \le b_{n+1}$. So $(b_n)$ is nondecreasing, and the first part gives $-a_m \le -a_n$ whenever $m \le n$. Adding $a_m + a_n$ to both sides gives $a_n \le a_m$. ∎

**Theorem (monotone convergence).** A nondecreasing sequence $(a_n)$ that is bounded above converges, and its limit is $L = \sup\{a_n : n \in \mathbb{N}\}$. Moreover $a_n \le L$ for every $n$.

*Proof.* Let $S = \{a_n : n \in \mathbb{N}\}$. The set $S$ is nonempty, since it contains $a_1$. It is bounded above, since some $M$ satisfies $a_n \le M$ for every $n$, and that $M$ is an upper bound of $S$. By the least-upper-bound property (Session 4), $L = \sup S$ exists. Because $L$ is an upper bound of $S$, $a_n \le L$ for every $n$.

Let $\varepsilon \gt 0$. By the approximation property (Session 4), some element of $S$ exceeds $L - \varepsilon$: there exists $N \in \mathbb{N}$ with $a_N \gt L - \varepsilon$.

Let $n \ge N$. By the comparison lemma, $a_N \le a_n$. Therefore

$$
L - \varepsilon \lt a_N \le a_n \le L \lt L + \varepsilon .
$$

So $-\varepsilon \lt a_n - L \lt \varepsilon$, that is, $\lvert a_n - L \rvert \lt \varepsilon$ (Session 5). This holds for every $n \ge N$, so $a_n \to L$. ∎

The proof never needed a guess for the limit. The least-upper-bound property supplied it.

**Corollary (nonincreasing case).** A nonincreasing sequence $(a_n)$ that is bounded below converges, and its limit $L$ satisfies $L \le a_n$ for every $n$.

*Proof.* Let $K$ satisfy $a_n \ge K$ for every $n$, and put $b_n = -a_n$. As in the proof of the comparison lemma, $(b_n)$ is nondecreasing. From $a_n \ge K$ it follows that $b_n \le -K$, so $(b_n)$ is bounded above. By the theorem, $b_n \to L'$ for some $L'$, with $b_n \le L'$ for every $n$. Now $a_n = (-1) \cdot b_n$. The constant sequence $-1, -1, \dots$ converges to $-1$, so by the product rule (Session 5), $a_n \to (-1) L' = -L'$. Put $L = -L'$. From $b_n \le L'$ it follows that $a_n = -b_n \ge -L' = L$. ∎

**Corollary (bounded monotone sequences).** Every bounded monotone sequence converges.

*Proof.* A bounded sequence is bounded above and below. If it is nondecreasing, the theorem applies. If it is nonincreasing, the previous corollary applies. ∎

## 6.3 Subsequences

A subsequence keeps infinitely many terms of a sequence, in their original order, and discards the rest.

**Definition.** Let $(a_n)$ be a sequence. Let $n_1, n_2, n_3, \dots$ be natural numbers with $n_1 \lt n_2 \lt n_3 \lt \cdots$, that is, $n_k \lt n_{k+1}$ for every $k \in \mathbb{N}$. The sequence whose $k$-th term is $a_{n_k}$ is a **subsequence** of $(a_n)$, written $(a_{n_k})$.

For example, $n_k = 2k$ gives the subsequence $a_2, a_4, a_6, \dots$ of even-indexed terms, and $n_k = k + 1$ gives the tail $a_2, a_3, a_4, \dots$; these are subsequences, since $2k$ and $k + 1$ lie in $\mathbb{N}$ (Session 3, Lemma 3), $2(k+1) = 2k + 2 \gt 2k$ and $(k+1) + 1 \gt k + 1$. The index $k$ counts terms of the subsequence; $n_k$ is where the $k$-th of them sits in the original sequence.

**Lemma (indices grow).** If $n_1 \lt n_2 \lt \cdots$ are natural numbers, then $n_k \ge k$ for every $k \in \mathbb{N}$.

*Proof.* By induction on $k$ (Session 3). For $k = 1$: $n_1 \in \mathbb{N}$, so $n_1 \ge 1$ (Session 3, Lemma 1). Suppose $n_k \ge k$. Since $n_{k+1} \gt n_k$ and both are natural numbers, $n_{k+1} \ge n_k + 1$ (Session 3), and $n_k + 1 \ge k + 1$. So $n_{k+1} \ge k + 1$. ∎

**Lemma (subsequences of a convergent sequence).** If $a_n \to a$, then every subsequence $(a_{n_k})$ satisfies $a_{n_k} \to a$.

*Proof.* Let $\varepsilon \gt 0$. Since $a_n \to a$, there exists $N$ such that $\lvert a_n - a \rvert \lt \varepsilon$ for every $n \ge N$. Let $k \ge N$. By the previous lemma, $n_k \ge k \ge N$, so $\lvert a_{n_k} - a \rvert \lt \varepsilon$. This holds for every $k \ge N$, so $a_{n_k} \to a$. ∎

**Corollary (a test for divergence).** If a sequence has two subsequences that converge to different limits, the sequence diverges.

*Proof.* Suppose $a_{n_k} \to b$ and $a_{m_k} \to c$ with $b \ne c$. If $a_n \to a$ for some $a$, the lemma gives $a_{n_k} \to a$ and $a_{m_k} \to a$. A sequence has at most one limit (Session 5), so $a = b$ and $a = c$, hence $b = c$, a contradiction. So no $a$ is a limit of $(a_n)$. ∎

For example, let $a_n = (-1)^n$, and let $k \in \mathbb{N}$. Here $2k \ge 2$, so $2k \ne 1$ and $2k - 1 \in \mathbb{N}$ (Session 3, Lemmas 1 to 3); and $2(k+1) - 1 = (2k - 1) + 2 \gt 2k - 1$, so $n_k = 2k - 1$, like $n_k = 2k$, gives a subsequence. Since $(-1)(-1) = 1$ (Session 4), the laws of powers (Session 3) give $(-1)^{2k} = ((-1)^2)^k = 1^k = 1$, and $(-1)^{2k-1} = (-1)^{2k-1} \cdot (-1)(-1) = (-1)^{2k} \cdot (-1) = -1$. So $a_{2k} = 1$ and $a_{2k-1} = -1$ for every $k$. These constant subsequences converge to $1$ and to $-1$ (Session 5), so $(a_n)$ diverges.

## 6.4 The Bolzano-Weierstrass theorem

The theorem is reached in two steps. The first is a fact about every real sequence, bounded or not: it has a monotone subsequence. The second applies monotone convergence to that subsequence.

**Definition.** An index $m \in \mathbb{N}$ is a **peak** of the sequence $(a_n)$ if $a_m \ge a_n$ for every $n \gt m$.

A peak is an index whose term no later term exceeds. If $(a_n)$ is nonincreasing, every index is a peak, by the comparison lemma (Section 6.2). The sequence $a_n = n$ has no peak, since $a_{m+1} = m + 1 \gt m = a_m$ for every $m$.

**Lemma (monotone subsequence).** Every real sequence has a monotone subsequence.

*Proof.* Exactly one of the following holds, since the second is the negation of the first (Session 2).

(A) For every $N \in \mathbb{N}$ there exists a peak $m$ with $m \gt N$.

(B) There exists $N \in \mathbb{N}$ such that no $m \gt N$ is a peak.

In each case the indices of the subsequence are defined by recursion (Session 3), with each index the least one that will do. Well-ordering makes each choice definite.

*Case (A).* Let $x \in \mathbb{N}$. By (A) with $N = x$ there exists a peak $m \gt x$, so the set of peaks greater than $x$ is a nonempty subset of $\mathbb{N}$. By well-ordering (Session 3) it has a least element; call it $g(x)$. This defines $g : \mathbb{N} \to \mathbb{N}$. By recursion (Session 3) with $X = \mathbb{N}$, there is a sequence with $n_1 = g(1)$ and $n_{k+1} = g(n_k)$ for every $k$. Each $n_k$ is a peak, and $n_{k+1} \gt n_k$, so $(a_{n_k})$ is a subsequence. Since $n_k$ is a peak and $n_{k+1} \gt n_k$, $a_{n_k} \ge a_{n_{k+1}}$ for every $k$. The subsequence is nonincreasing.

*Case (B).* Fix such an $N$, and let $X$ be the set of natural numbers greater than $N$. Let $x \in X$. Then $x$ is not a peak, so by the negation of "$a_x \ge a_n$ for every $n \gt x$" (Session 2) there exists $n \gt x$ for which $a_x \ge a_n$ is false, that is, $a_n \gt a_x$ (Session 4). So the set of $n \in \mathbb{N}$ with $n \gt x$ and $a_n \gt a_x$ is nonempty. Let $g(x)$ be its least element (Session 3). Then $g(x) \gt x \gt N$, so $g(x) \in X$; this defines $g : X \to X$. Also $N + 1 \in \mathbb{N}$ (Session 3, Lemma 3) and $N + 1 \gt N$, so $N + 1 \in X$. By recursion (Session 3) there is a sequence $(n_k)$ in $X$ with $n_1 = N + 1$ and $n_{k+1} = g(n_k)$ for every $k$. For every $k$, $n_k \in X$, so $n_{k+1} = g(n_k)$ satisfies $n_{k+1} \gt n_k$ and $a_{n_{k+1}} \gt a_{n_k}$. The subsequence $(a_{n_k})$ is nondecreasing. ∎

**Theorem (Bolzano-Weierstrass).** Every bounded real sequence has a convergent subsequence.

*Proof.* Let $\lvert a_n \rvert \le M$ for every $n$. By the monotone subsequence lemma, $(a_n)$ has a monotone subsequence $(a_{n_k})$. Its terms are terms of $(a_n)$, so $\lvert a_{n_k} \rvert \le M$ for every $k$, and $(a_{n_k})$ is bounded. By the corollary on bounded monotone sequences (Section 6.2), $(a_{n_k})$ converges. ∎

The theorem is named after B. Bolzano and K. Weierstrass. Bolzano's paper *Rein analytischer Beweis des Lehrsatzes, daß zwischen je zwey Werthen, die ein entgegengesetztes Resultat gewähren, wenigstens eine reelle Wurzel der Gleichung liege* (Prague, 1817) proved, as a step towards the intermediate value theorem, a least-upper-bound lemma by repeatedly halving an interval. In his Berlin lectures of the 1860s and 1870s, Weierstrass proved by the same halving method a form of the theorem for sets: every bounded set with infinitely many elements has a point such that every interval $(u, v)$ that contains it contains infinitely many elements of the set. He made it a standard tool.

## 6.5 Cauchy sequences

The definition of $a_n \to a$ mentions $a$. To use it, one must already have a candidate for the limit. The following condition mentions only the terms.

**Definition.** A real sequence $(a_n)$ is a **Cauchy sequence** if for every $\varepsilon \gt 0$ there exists $N \in \mathbb{N}$ such that $\lvert a_m - a_n \rvert \lt \varepsilon$ for all $m, n \ge N$.

In words: beyond some index, any two terms are within $\varepsilon$ of each other. The theorem of this section is that this condition is equivalent to convergence. The proof uses three lemmas and the Bolzano-Weierstrass theorem.

**Lemma (convergent implies Cauchy).** If $a_n \to a$, then $(a_n)$ is a Cauchy sequence.

*Proof.* Let $\varepsilon \gt 0$. Since $\varepsilon/2 \gt 0$, there exists $N$ with $\lvert a_n - a \rvert \lt \varepsilon/2$ for every $n \ge N$. Let $m, n \ge N$. By the triangle inequality (Session 5),

$$
\lvert a_m - a_n \rvert = \lvert (a_m - a) + (a - a_n) \rvert \le \lvert a_m - a \rvert + \lvert a - a_n \rvert \lt \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon .
$$

Here $\lvert a - a_n \rvert = \lvert -(a_n - a) \rvert = \lvert a_n - a \rvert$ (Session 5). ∎

**Lemma (Cauchy implies bounded).** Every Cauchy sequence is bounded.

*Proof.* Apply the definition with $\varepsilon = 1$: there exists $N$ such that $\lvert a_m - a_n \rvert \lt 1$ for all $m, n \ge N$. Take $m = N$. For every $n \ge N$, the triangle inequality (Session 5) gives

$$
\lvert a_n \rvert = \lvert (a_n - a_N) + a_N \rvert \le \lvert a_n - a_N \rvert + \lvert a_N \rvert \lt 1 + \lvert a_N \rvert .
$$

If $N = 1$, put $M = 1 + \lvert a_N \rvert$; every $n$ satisfies $n \ge 1 = N$, so $\lvert a_n \rvert \le M$. If $N \ne 1$, then $N - 1 \in \mathbb{N}$ (Session 3). The lemma on finitely many terms (Session 5) gives $B \ge 0$ with $\lvert a_k \rvert \le B$ for every natural number $k \le N - 1$. Put $M = \max\{B, 1 + \lvert a_N \rvert\}$. Let $n \in \mathbb{N}$. If $n \ge N$, then $\lvert a_n \rvert \lt 1 + \lvert a_N \rvert \le M$. Otherwise $n \lt N$, so $n + 1 \le N$ (Session 3), that is, $n \le N - 1$, and $\lvert a_n \rvert \le B \le M$. So $\lvert a_n \rvert \le M$ for every $n$. ∎

**Lemma (a Cauchy sequence follows its subsequences).** If $(a_n)$ is a Cauchy sequence and some subsequence satisfies $a_{n_k} \to a$, then $a_n \to a$.

*Proof.* Let $\varepsilon \gt 0$. Since $(a_n)$ is Cauchy, there exists $N$ with $\lvert a_m - a_n \rvert \lt \varepsilon/2$ for all $m, n \ge N$. Since $a_{n_k} \to a$, there exists $K$ with $\lvert a_{n_k} - a \rvert \lt \varepsilon/2$ for every $k \ge K$.

Let $k = \max\{K, N\}$. Then $k \ge K$, so $\lvert a_{n_k} - a \rvert \lt \varepsilon/2$. Also $n_k \ge k \ge N$ by the lemma on growing indices (Section 6.3). Now let $n \ge N$. Both $n$ and $n_k$ are at least $N$, so $\lvert a_n - a_{n_k} \rvert \lt \varepsilon/2$. By the triangle inequality (Session 5),

$$
\lvert a_n - a \rvert \le \lvert a_n - a_{n_k} \rvert + \lvert a_{n_k} - a \rvert \lt \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon .
$$

This holds for every $n \ge N$, so $a_n \to a$. ∎

**Theorem (Cauchy criterion).** A real sequence converges if and only if it is a Cauchy sequence.

*Proof.* If $(a_n)$ converges, it is Cauchy by the first lemma. Conversely, let $(a_n)$ be Cauchy. By the second lemma it is bounded. By the Bolzano-Weierstrass theorem it has a subsequence $(a_{n_k})$ with $a_{n_k} \to a$ for some $a$. By the third lemma, $a_n \to a$. ∎

The criterion is often stated as "$\mathbb{R}$ is complete": every Cauchy sequence converges. Session 4 used the word for the least-upper-bound property, the completeness axiom, and the proof above rests on that axiom, through Bolzano-Weierstrass and monotone convergence. Granted the arithmetic of the rationals, $\mathbb{Q}$ is an ordered field without that property (Session 4), and Exercise 7 builds a Cauchy sequence of rationals with no rational limit. Sequences of this kind are named after A.-L. Cauchy, who used the criterion for series in his *Cours d'analyse* (Paris, 1821).

## 6.6 Worked example

Define a sequence by recursion (Session 3):

$$
a_1 = \frac12, \qquad a_{n+1} = \frac{2 a_n}{1 + a_n} \quad (n \in \mathbb{N}).
$$

The recursion theorem needs a function defined at every number. Here it is $g(x) = \frac{2x}{1+x}$ for $x \ne -1$, with $g(-1) = 0$, and $a_{n+1} = g(a_n)$. By Step 1 below every $a_n$ is positive, so the value at $-1$ is never used.

The first terms are

$$
a_2 = \frac{2 \cdot \frac12}{1 + \frac12} = \frac{1}{\frac32} = \frac23, \qquad
a_3 = \frac{\frac43}{1 + \frac23} = \frac{\frac43}{\frac53} = \frac45, \qquad
a_4 = \frac{\frac85}{1 + \frac45} = \frac{\frac85}{\frac95} = \frac89 .
$$

They rise towards $1$. The claim is that $a_n \to 1$. The proof uses the monotone convergence theorem to show that a limit exists, and the lemma on subsequences to find it.

*Step 1: $0 \lt a_n \lt 1$ for every $n$.* By induction (Session 3). For $n = 1$: $0 \lt \frac12 \lt 1$. Suppose $0 \lt a_n \lt 1$. Then $a_n \ne -1$, so $a_{n+1} = \frac{2 a_n}{1 + a_n}$. Also $1 + a_n \gt 1 \gt 0$ and $2 a_n \gt 0$, so $a_{n+1}$, a quotient of two positive numbers, is positive. And

$$
1 - a_{n+1} = \frac{(1 + a_n) - 2 a_n}{1 + a_n} = \frac{1 - a_n}{1 + a_n} ,
$$

where both $1 - a_n$ and $1 + a_n$ are positive, so $1 - a_{n+1} \gt 0$, that is, $a_{n+1} \lt 1$.

*Step 2: the sequence is nondecreasing.* For every $n$,

$$
a_{n+1} - a_n = \frac{2 a_n - a_n (1 + a_n)}{1 + a_n} = \frac{a_n - a_n^2}{1 + a_n} = \frac{a_n (1 - a_n)}{1 + a_n} .
$$

By Step 1, $a_n \gt 0$, $1 - a_n \gt 0$ and $1 + a_n \gt 0$, so $a_{n+1} - a_n \gt 0$.

*Step 3: the limit exists.* By Steps 1 and 2 the sequence is nondecreasing and bounded above by $1$. By the monotone convergence theorem (Section 6.2), $a_n \to L$ for some $L$, and $a_n \le L$ for every $n$. In particular $L \ge a_1 = \frac12$.

*Step 4: an equation for $L$.* The tail $a_2, a_3, a_4, \dots$ is the subsequence with $n_k = k + 1$, so $a_{k+1} \to L$ (Section 6.3). The same sequence is $\frac{2 a_k}{1 + a_k}$. By the rules of Session 5, $2 a_k \to 2L$ and $1 + a_k \to 1 + L$. Here $1 + L \ge \frac32$, so $1 + L \ne 0$, and $1 + a_k \ne 0$ for every $k$ by Step 1. The quotient rule (Session 5) gives $\frac{2 a_k}{1 + a_k} \to \frac{2L}{1 + L}$. A sequence has at most one limit (Session 5), so

$$
L = \frac{2L}{1 + L} .
$$

*Step 5: solve.* Multiplying by $1 + L$ gives $L + L^2 = 2L$, so $L^2 - L = 0$, that is, $L (L - 1) = 0$. Since $L \ge \frac12$, $L \ne 0$; multiplying by $L^{-1}$ gives $L - 1 = 0$. So $L = 1$, and $a_n \to 1$.

The equation of Step 4 has two solutions, $0$ and $1$. It is the bound $L \ge \frac12$ from Step 3 that selects $1$. With the starting value $a_1 = 0$ instead, the same recursion gives $a_n = 0$ for every $n$, whose limit is the other solution.

## 6.7 What fails without the hypotheses

*Monotone but not bounded.* The sequence $a_n = n$ is nondecreasing. It is not bounded: for every $M$ the Archimedean property (Session 4) gives $n \in \mathbb{N}$ with $n \gt M$, and $\lvert a_n \rvert = n \gt M$ since $n \gt 0$. A convergent sequence is bounded (Session 5), so $(n)$ diverges. No subsequence of $(n)$ converges either. If $n_1 \lt n_2 \lt \cdots$, then $n_k \ge k$ by the lemma on growing indices (Section 6.3); for every $M$ take $k \in \mathbb{N}$ with $k \gt M$ (Session 4), and then $n_k \ge k \gt M$. So every subsequence is unbounded, and diverges (Session 5). The Bolzano-Weierstrass theorem needs boundedness.

*Bounded but not monotone.* The sequence $(-1)^n$ is bounded by $1$ and diverges (Section 6.3). The Bolzano-Weierstrass theorem still applies to it, and gives a convergent subsequence only: $a_2, a_4, a_6, \dots$ converges to $1$.

*Solving for a limit that does not exist.* Steps 4 and 5 of Section 6.6 assume a limit $L$ and find it. Without Step 3 the conclusion can be false. Take $a_1 = 1$ and $a_{n+1} = 2 a_n$. If $a_n \to L$, the argument of Step 4 gives $L = 2L$, so $L = 0$. But $a_n \ge n$ for every $n$: $a_1 = 1 \ge 1$, and if $a_n \ge n$ then $a_{n+1} = 2 a_n \ge 2n = n + n \ge n + 1$. For every $M$ the Archimedean property (Session 4) gives $n \gt M$, and then $\lvert a_n \rvert = a_n \ge n \gt M$, since $a_n \ge n \gt 0$; so $(a_n)$ is not bounded. A convergent sequence is bounded (Session 5), so $(a_n)$ has no limit.

*Close neighbouring terms do not make a sequence Cauchy.* Let $H_n = \sum_{k=1}^{n} \frac1k$. Neighbouring terms differ by $H_{n+1} - H_n = \frac{1}{n+1}$, which tends to $0$: given $\varepsilon \gt 0$, choose $N \in \mathbb{N}$ with $N \gt \frac{1}{\varepsilon}$ (Session 4); then $\frac1N \lt \varepsilon$, and for $n \ge N$,

$$
0 \lt \frac{1}{n+1} \lt \frac1n \le \frac1N \lt \varepsilon .
$$

Yet $(H_n)$ is not Cauchy. For each $n$,

$$
H_{2n} - H_n = \sum_{k=n+1}^{2n} \frac1k = \sum_{j=1}^{n} \frac{1}{n+j} \ge \sum_{j=1}^{n} \frac{1}{2n} = \frac{1}{2n} \sum_{j=1}^{n} 1 = \frac{1}{2n} \cdot n = \frac12 .
$$

The first equality splits the sum $H_{2n}$ at $k = n$, by (S4) (Session 3), and the second is the meaning of a sum from $n + 1$ (Session 3). For the inequality, each $j \le n$ gives $0 \lt n + j \le 2n$, so $\frac{1}{n+j} \ge \frac{1}{2n}$ (Session 4), and (S3) (Session 3) compares the sums. The next equality is (S2), and $\sum_{j=1}^{n} 1 = n$ by the corollary on sums of constants (Session 3). Now take $\varepsilon = \frac12$. For every $N$, the indices $m = 2N$ and $n = N$ are both at least $N$, and $\lvert H_m - H_n \rvert \ge \frac12$. So no $N$ works, and by the Cauchy criterion $(H_n)$ diverges. Since $(H_n)$ is nondecreasing, the monotone convergence theorem shows more: $(H_n)$ is not bounded above, for otherwise it would converge.

## Exercises

*Check*

1. Let $a_1 = 1$ and $a_{n+1} = \frac{2 a_n + 3}{3}$. Compute $a_2$ and $a_3$. Prove that $a_n \lt 3$ for every $n$ and that $(a_n)$ is nondecreasing. Conclude that $(a_n)$ converges, and find its limit.

2. Let $a_n = (-1)^n \frac{n}{n+1}$. Find the limits of the subsequences $(a_{2k})$ and $(a_{2k-1})$, and conclude that $(a_n)$ diverges.

3. Let $s_n = \sum_{k=1}^{n} \frac{1}{k^2}$. Using $\frac{1}{k^2} \lt \frac{1}{k-1} - \frac1k$ for $k \ge 2$, prove that $0 \le s_m - s_n \lt \frac1n$ whenever $m \gt n$. Conclude that $(s_n)$ is a Cauchy sequence, and hence converges.

*Prove*

4. A nonempty set of reals that is bounded below has a greatest lower bound (Session 4). Following the proof of the monotone convergence theorem, prove directly that a nonincreasing sequence bounded below converges to $\inf\{a_n : n \in \mathbb{N}\}$.

5. Prove that if $a_{2k} \to a$ and $a_{2k-1} \to a$, then $a_n \to a$.

6. Prove that a monotone sequence with a convergent subsequence converges.

*Extend*

7. ($\mathbb{Q}$ is not complete.) Grant, as in Session 4 (Section 4.9), that sums, products and quotients of rationals are rational. (a) Prove that no rational number $q$ satisfies $q^2 = 2$. This is fact (ii) of Section 4.9, which Session 4 assumed; use the parity lemma (Session 3, Section 3.3). (b) Let $a_1 = 2$ and $a_{n+1} = \frac{a_n}{2} + \frac{1}{a_n}$. Prove that every $a_n$ is a positive rational number. (c) Prove that $a_{n+1}^2 - 2 = \left( \frac{a_n}{2} - \frac{1}{a_n} \right)^2$, and deduce that $a_n^2 \ge 2$ for every $n$. (d) Prove that $(a_n)$ is nonincreasing. (e) Prove that $a_n \to L$ for some real $L \gt 0$ with $L^2 = 2$. (f) Conclude that $(a_n)$ is a Cauchy sequence of rational numbers with no rational limit.

8. (Contractive sequences.) Let $0 \le r \lt 1$, and let $(a_n)$ satisfy $\lvert a_{n+2} - a_{n+1} \rvert \le r \lvert a_{n+1} - a_n \rvert$ for every $n$. Prove that $(a_n)$ is a Cauchy sequence, and hence converges. (Session 5 gives $r^n \to 0$.)

Solutions: [solutions/006-real-sequences.md](../solutions/006-real-sequences.md).
