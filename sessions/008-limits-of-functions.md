# 1.8. Limits of functions at a point

*Theorem. Builds on Sessions 5 and 7.*

**Claim.** $\lim_{y \to x} f(y) = L$, defined with $\varepsilon$ and $\delta$, holds if and only if $f(y_n) \to L$ for every sequence $y_n \to x$ with $y_n \neq x$. So limits of functions are unique and obey the sum, product and quotient rules, and $f$ is continuous at $x$ if and only if $\lim_{y \to x} f(y) = f(x)$.

Session 5 built limits of sequences. Session 7 built continuity, which compares $f(y)$ with $f(x)$. This session builds the limit of $f(y)$ as $y$ approaches $x$, which never looks at $f(x)$ at all and does not need $f$ to be defined at $x$. The derivative is a limit of this kind: the quotient $(f(x+h) - f(x))/h$ is not defined at $h = 0$, and its behaviour as $h$ approaches $0$ is what matters. The main theorem of the session turns every question about such limits into a question about sequences, so that the rules of Session 5 carry over without new work.

## 8.1 Recall

From Session 2: a statement may be proved by proving its contrapositive (Section 2.5). In a negation, a restriction on a quantified variable stays in place and only the final clause is negated (Section 2.4). So the negation of "for every $\varepsilon \gt 0$ there exists $\delta \gt 0$ such that for every $y \in D$ with $Q(y)$, $P(y)$" is "there exists $\varepsilon \gt 0$ such that for every $\delta \gt 0$ there exists $y \in D$ with $Q(y)$ and not $P(y)$".

From Session 4: $\mathbb{R}$ is an ordered field, and for any two reals $u$, $v$ exactly one of $u \lt v$, $u = v$, $u \gt v$ holds (trichotomy, (O1), Section 4.3). So "not $a \lt \varepsilon$" means $a \ge \varepsilon$. For real $s$ and $t$, $\min\{s, t\}$ is the minimum of the set $\{s, t\}$ (Section 4.4): it is $s$ if $s \le t$, and $t$ otherwise; in the second case $t \lt s$ by trichotomy. So it is at most $s$ and at most $t$, and it equals one of them, so it is positive when $s$ and $t$ are.

From Session 5: the absolute value satisfies $\lvert -a \rvert = \lvert a \rvert$, $\lvert a \rvert \gt 0$ when $a \neq 0$, $\lvert ab \rvert = \lvert a \rvert \lvert b \rvert$, $\lvert a \rvert \lt r$ if and only if $-r \lt a \lt r$, and the triangle inequality $\lvert a + b \rvert \le \lvert a \rvert + \lvert b \rvert$ (Section 5.2). A real sequence $(a_n)$ converges to $a$, written $a_n \to a$, if for every $\varepsilon \gt 0$ there exists $N \in \mathbb{N}$ such that $\lvert a_n - a \rvert \lt \varepsilon$ for every $n \ge N$ (Section 5.3). A sequence has at most one limit (Section 5.4). A constant sequence $c, c, c, \dots$ converges to $c$, and $1/n \to 0$ (Section 5.3). If $a_n \to a$ and $b_n \to b$, then $a_n + b_n \to a + b$ and $a_n b_n \to ab$ (Section 5.6); if moreover $b \neq 0$ and $b_n \neq 0$ for every $n$, then $a_n / b_n \to a/b$ (Section 5.7). If $a_n \to a$, then $p(a_n) \to p(a)$ for every polynomial $p$ with real coefficients (the corollary on powers and polynomials, Section 5.6). If $a_n \to a$, $b_n \to b$ and $a_n \le b_n$ for every $n$, then $a \le b$ (Section 5.8). If $a_n \le c_n \le b_n$ for every $n$ and $a_n \to L$ and $b_n \to L$, then $c_n \to L$ (the squeeze rule, Section 5.9).

From Session 7: if $K \ge 0$ and $\lvert x_n - x \rvert \le K/n$ for every $n \in \mathbb{N}$, then $x_n \to x$ (the test for convergence, Section 7.1). An interval is a set $I \subseteq \mathbb{R}$ with at least two points such that, whenever $u, w \in I$ and $u \lt v \lt w$, also $v \in I$ (Section 7.2). A function $f : D \to \mathbb{R}$ is continuous at $x \in D$ if for every $\varepsilon \gt 0$ there exists $\delta \gt 0$ such that $\lvert f(y) - f(x) \rvert \lt \varepsilon$ for every $y \in D$ with $\lvert y - x \rvert \lt \delta$ (Section 7.2). This holds if and only if $f(x_n) \to f(x)$ for every sequence $(x_n)$ in $D$ with $x_n \to x$ (the sequential characterisation of continuity, Section 7.3). A decimal with $k$ digits after the point is the fraction whose numerator is the natural number or zero written by its digits with the point removed, and whose denominator is $10^k$; for example $0.07 = 7/100$ (Section 7.9).

## 8.2 Accumulation points

A limit at $x$ describes $f(y)$ for $y$ near $x$ and different from $x$. Such $y$ must exist in the domain, or there is nothing to describe.

**Definition.** Let $D \subseteq \mathbb{R}$. A real number $x$ is an **accumulation point** of $D$ if for every $\delta \gt 0$ there exists $y \in D$ with $0 \lt \lvert y - x \rvert \lt \delta$.

The literature also says *limit point*. The point $x$ may or may not belong to $D$. For example, $1$ is an accumulation point of $D = \mathbb{R} \setminus \{1\}$: given $\delta \gt 0$, the point $y = 1 + \delta/2$ is not $1$, because $\delta/2 \gt 0$, so it lies in $D$; and $\lvert y - 1 \rvert = \delta/2$, which is positive and less than $\delta$.

**Lemma 1.** If $x$ is an accumulation point of $D$, there exists a sequence $(y_n)$ with $y_n \in D$, $y_n \neq x$ for every $n$, and $y_n \to x$.

*Proof.* For each $n \in \mathbb{N}$, apply the definition with $\delta = 1/n$, which is positive (Session 5, Section 5.3). It gives a point $y_n \in D$ with $0 \lt \lvert y_n - x \rvert \lt 1/n$, and one such point for each $n$ gives a sequence (countable choice, Session 7, Section 7.3). The first inequality says $y_n \neq x$. The second gives $y_n \to x$, by the test for convergence (Session 7) with $K = 1$. ∎

**Lemma 2.** Let $I$ be an interval. Then every $x \in I$ is an accumulation point of $I$.

*Proof.* By the definition of an interval (Session 7), $I$ has two different points $c$ and $d$. Let $x \in I$. The point $x$ cannot equal both $c$ and $d$. Choose $w = d$ if $x \neq d$, and $w = c$ if $x = d$. Then $w \in I$ and $w \neq x$.

Let $\delta \gt 0$. Put $s = \min\{\delta, \lvert w - x \rvert\}$ and $t = s/2$. Since $w \neq x$, $\lvert w - x \rvert \gt 0$ (Session 5), so $s \gt 0$ and $t \gt 0$. Since $s - t = s/2 \gt 0$, $t \lt s$; and $s \le \delta$, $s \le \lvert w - x \rvert$. So $t \lt \delta$ and $t \lt \lvert w - x \rvert$.

- If $w \gt x$, then $\lvert w - x \rvert = w - x$. Put $y = x + t$. From $0 \lt t \lt w - x$, $x \lt y \lt x + (w - x) = w$.
- If $w \lt x$, then $\lvert w - x \rvert = -(w - x) = x - w$. Put $y = x - t$. From $0 \lt t \lt x - w$, $w = x - (x - w) \lt y \lt x$.

In both cases $y$ lies strictly between the two points $x$ and $w$ of $I$, so $y \in I$ by the definition of an interval. And $y - x$ is $t$ or $-t$, with $t \gt 0$, so $\lvert y - x \rvert = t$ (Session 5, Section 5.2, Part 3), which is positive and less than $\delta$. ∎

The point $y$ found differs from $x$, so $x$ is also an accumulation point of $I \setminus \{x\}$.

## 8.3 The limit of a function

**Definition.** Let $D \subseteq \mathbb{R}$, let $f : D \to \mathbb{R}$, and let $x$ be an accumulation point of $D$. A real number $L$ is a **limit of $f$ at $x$** if for every $\varepsilon \gt 0$ there exists $\delta \gt 0$ such that

$$
\lvert f(y) - L \rvert \lt \varepsilon \quad \text{for every } y \in D \text{ with } 0 \lt \lvert y - x \rvert \lt \delta .
$$

We then say that $f(y)$ **tends to** $L$ as $y$ tends to $x$. Section 8.4 shows that there is at most one such $L$; only then is it written $\lim_{y \to x} f(y)$.

Two features of the definition matter later.

- The condition $0 \lt \lvert y - x \rvert$ excludes $y = x$. The value $f(x)$, if it exists, plays no part.
- Only points of $D$ are tested. A limit depends on the domain as well as on the formula.

The first feature can be stated as a lemma.

**Lemma 3.** Let $f, g : D \to \mathbb{R}$, let $x$ be an accumulation point of $D$, and suppose $f(y) = g(y)$ for every $y \in D$ with $y \neq x$. If $f(y)$ tends to $L$ as $y$ tends to $x$, so does $g(y)$.

*Proof.* Let $\varepsilon \gt 0$, and take the $\delta$ that the definition gives for $f$. Let $y \in D$ with $0 \lt \lvert y - x \rvert \lt \delta$. Then $y \neq x$, so $g(y) = f(y)$, and $\lvert g(y) - L \rvert = \lvert f(y) - L \rvert \lt \varepsilon$. ∎

**Two basic limits.** Let $x$ be an accumulation point of $D$ and let $c \in \mathbb{R}$.

- The constant function $f(y) = c$ tends to $c$. For every $\varepsilon \gt 0$, take $\delta = 1$: every $y \in D$ gives $\lvert f(y) - c \rvert = 0 \lt \varepsilon$.
- The identity $f(y) = y$ tends to $x$. For every $\varepsilon \gt 0$, take $\delta = \varepsilon$: if $0 \lt \lvert y - x \rvert \lt \delta$, then $\lvert f(y) - x \rvert = \lvert y - x \rvert \lt \varepsilon$.

## 8.4 Limits through sequences

**Theorem (sequential criterion).** Let $f : D \to \mathbb{R}$, let $x$ be an accumulation point of $D$, and let $L \in \mathbb{R}$. Then $f(y)$ tends to $L$ as $y$ tends to $x$ if and only if the following holds: for every sequence $(y_n)$ with $y_n \in D$ and $y_n \neq x$ for every $n$, and $y_n \to x$, the sequence $f(y_n)$ converges to $L$.

*Proof.* **The limit implies the sequence condition.** Suppose $f(y)$ tends to $L$, and let $(y_n)$ be a sequence in $D$ with $y_n \neq x$ for every $n$ and $y_n \to x$. Let $\varepsilon \gt 0$.

1. The definition of the limit gives $\delta \gt 0$ such that $\lvert f(y) - L \rvert \lt \varepsilon$ for every $y \in D$ with $0 \lt \lvert y - x \rvert \lt \delta$.
2. Apply the definition of $y_n \to x$ (Session 5) with $\delta$ in the role of $\varepsilon$. It gives $N$ such that $\lvert y_n - x \rvert \lt \delta$ for every $n \ge N$.
3. Let $n \ge N$. Then $y_n \in D$, $\lvert y_n - x \rvert \lt \delta$ by step 2, and $\lvert y_n - x \rvert \gt 0$ because $y_n \neq x$. So step 1 applies to $y = y_n$: $\lvert f(y_n) - L \rvert \lt \varepsilon$.

Since $\varepsilon$ was arbitrary, $f(y_n) \to L$.

**The sequence condition implies the limit.** We prove the contrapositive (Session 2): if $f(y)$ does not tend to $L$, then some sequence violates the sequence condition. Suppose $f(y)$ does not tend to $L$. The definition has the form recalled from Session 2 in Section 8.1, with $Q(y)$ the condition $0 \lt \lvert y - x \rvert \lt \delta$ and $P(y)$ the inequality $\lvert f(y) - L \rvert \lt \varepsilon$; and "not $P(y)$" is $\lvert f(y) - L \rvert \ge \varepsilon$ by the order of Session 4. So:

$$
\exists\, \varepsilon \gt 0 \;\; \forall\, \delta \gt 0 \;\; \exists\, y \in D : \quad 0 \lt \lvert y - x \rvert \lt \delta \;\text{ and }\; \lvert f(y) - L \rvert \ge \varepsilon .
$$

Fix such an $\varepsilon$.

1. For each $n \in \mathbb{N}$, apply the displayed statement with $\delta = 1/n$, which is positive (Session 5, Section 5.3). It gives $y_n \in D$ with $0 \lt \lvert y_n - x \rvert \lt 1/n$ and $\lvert f(y_n) - L \rvert \ge \varepsilon$; one such $y_n$ for each $n$ gives a sequence (countable choice, Session 7, Section 7.3).
2. By the first inequality, $y_n \neq x$. By the second and the test for convergence (Session 7) with $K = 1$, $y_n \to x$.
3. Suppose $f(y_n) \to L$. Then, for this same $\varepsilon$, there would be $N$ with $\lvert f(y_n) - L \rvert \lt \varepsilon$ for every $n \ge N$, and in particular for $n = N$. This contradicts $\lvert f(y_N) - L \rvert \ge \varepsilon$ from step 1. So $f(y_n)$ does not converge to $L$.

The sequence $(y_n)$ lies in $D$, avoids $x$ and tends to $x$, and $f(y_n)$ does not converge to $L$. So the sequence condition fails. ∎

**Corollary (uniqueness).** Let $f : D \to \mathbb{R}$ and let $x$ be an accumulation point of $D$. If $f(y)$ tends to $L$ and to $L'$ as $y$ tends to $x$, then $L = L'$.

*Proof.* Lemma 1 gives a sequence $(y_n)$ in $D$ with $y_n \neq x$ and $y_n \to x$. By the theorem, $f(y_n) \to L$ and $f(y_n) \to L'$. A sequence has at most one limit (Session 5), so $L = L'$. ∎

**Definition.** When $f(y)$ tends to $L$ as $y$ tends to $x$, the corollary makes $L$ unique. It is called the limit of $f$ at $x$, and written

$$
\lim_{y \to x} f(y) = L .
$$

We also write $f(y) \to L$ as $y \to x$. When the domain must be named, we say "as $y \to x$ in $D$".

The theorem also gives the standard way to show that a limit does not exist: produce two sequences that avoid $x$ and tend to $x$, along which $f$ has different limits.

**Example (no limit).** Let $D = \mathbb{R} \setminus \{0\}$ and $f(y) = y / \lvert y \rvert$, so $f(y) = 1$ for $y \gt 0$ and $f(y) = -1$ for $y \lt 0$. The point $0$ is an accumulation point of $D$, by the argument given for $1$ in Section 8.2. Put $y_n = 1/n$ and $z_n = -1/n$. Both lie in $D$ and are nonzero, and $\lvert y_n - 0 \rvert = \lvert z_n - 0 \rvert = 1/n$, so both tend to $0$ by the test for convergence (Session 7) with $K = 1$. Now $f(y_n) = 1$ for every $n$, so $f(y_n) \to 1$, and $f(z_n) = -1$ for every $n$, so $f(z_n) \to -1$ (constant sequences, Session 5). If $f$ had a limit $L$ at $0$, the theorem would give $f(y_n) \to L$ and $f(z_n) \to L$, so $L = 1$ and $L = -1$ by uniqueness of limits of sequences (Session 5). That is impossible, so $f$ has no limit at $0$.

## 8.5 Sum, product and quotient rules

The sequential criterion moves the rules of Session 5 from sequences to functions. Each proof has the same four steps: take a sequence, apply the criterion in one direction, apply Session 5, and apply the criterion in the other direction.

**Theorem (sum and product rules).** Let $f, g : D \to \mathbb{R}$, let $x$ be an accumulation point of $D$, and suppose $\lim_{y \to x} f(y) = L$ and $\lim_{y \to x} g(y) = M$. Then

$$
\lim_{y \to x} \bigl( f(y) + g(y) \bigr) = L + M, \qquad \lim_{y \to x} f(y)\, g(y) = L M .
$$

*Proof.* Let $(y_n)$ be a sequence in $D$ with $y_n \neq x$ for every $n$ and $y_n \to x$. By the sequential criterion (Section 8.4), $f(y_n) \to L$ and $g(y_n) \to M$. By the sum and product rules for sequences (Session 5), $f(y_n) + g(y_n) \to L + M$ and $f(y_n) g(y_n) \to LM$. The sequence was arbitrary, so the sequential criterion, applied to the functions $y \mapsto f(y) + g(y)$ and $y \mapsto f(y) g(y)$ on $D$, gives the two limits. ∎

A quotient $f(y)/g(y)$ is defined only where $g(y) \neq 0$. The next lemma shows that this excludes no points close to $x$ when the limit of $g$ is not $0$.

**Lemma 4.** Let $g : D \to \mathbb{R}$, let $x$ be an accumulation point of $D$, and suppose $\lim_{y \to x} g(y) = M$ with $M \neq 0$. Then:

1. there exists $r \gt 0$ such that $\lvert g(y) \rvert \gt \lvert M \rvert / 2$ for every $y \in D$ with $0 \lt \lvert y - x \rvert \lt r$;
2. $x$ is an accumulation point of $D_0 = \{ y \in D : g(y) \neq 0 \}$.

*Proof.* (1) Since $M \neq 0$, $\lvert M \rvert \gt 0$ (Session 5), so $\lvert M \rvert / 2 \gt 0$. Apply the definition of the limit with $\varepsilon = \lvert M \rvert / 2$, and call the resulting $\delta$ by the name $r$. Let $y \in D$ with $0 \lt \lvert y - x \rvert \lt r$, so that $\lvert g(y) - M \rvert \lt \lvert M \rvert / 2$. Write $M = (M - g(y)) + g(y)$. Since $\lvert M - g(y) \rvert = \lvert -(g(y) - M) \rvert = \lvert g(y) - M \rvert$ (Session 5), the triangle inequality (Session 5) gives

$$
\lvert M \rvert \le \lvert M - g(y) \rvert + \lvert g(y) \rvert \lt \tfrac{1}{2} \lvert M \rvert + \lvert g(y) \rvert .
$$

Subtracting $\tfrac12 \lvert M \rvert$ from both sides gives $\lvert g(y) \rvert \gt \tfrac12 \lvert M \rvert$.

(2) Let $\delta \gt 0$ and put $\delta' = \min\{\delta, r\}$, which is positive (Section 8.1). Since $x$ is an accumulation point of $D$, there is $y \in D$ with $0 \lt \lvert y - x \rvert \lt \delta'$. Since $\delta' \le r$, (1) gives $\lvert g(y) \rvert \gt \lvert M \rvert / 2 \gt 0$, so $g(y) \neq 0$ and $y \in D_0$. And $\lvert y - x \rvert \lt \delta' \le \delta$. ∎

**Theorem (quotient rule).** Let $f, g : D \to \mathbb{R}$, let $x$ be an accumulation point of $D$, and suppose $\lim_{y \to x} f(y) = L$ and $\lim_{y \to x} g(y) = M$ with $M \neq 0$. Let $D_0 = \{ y \in D : g(y) \neq 0 \}$. Then $x$ is an accumulation point of $D_0$, and

$$
\lim_{y \to x} \frac{f(y)}{g(y)} = \frac{L}{M} \qquad (y \to x \text{ in } D_0).
$$

*Proof.* Lemma 4 gives the first statement. Let $(y_n)$ be a sequence in $D_0$ with $y_n \neq x$ for every $n$ and $y_n \to x$. Since $D_0 \subseteq D$, the sequential criterion applied to $f$ and to $g$ on $D$ gives $f(y_n) \to L$ and $g(y_n) \to M$. Each $y_n$ lies in $D_0$, so $g(y_n) \neq 0$ for every $n$. The quotient rule for sequences (Session 5) gives $f(y_n)/g(y_n) \to L/M$. The sequence was arbitrary, so the sequential criterion, applied to $y \mapsto f(y)/g(y)$ on $D_0$, gives the limit. ∎

**Corollary (polynomials and rational functions).** Let $D \subseteq \mathbb{R}$, let $x$ be an accumulation point of $D$, and let $p(y) = a_0 + a_1 y + \dots + a_m y^m$ for real $y$, with real coefficients. Then $\lim_{y \to x} p(y) = p(x)$, as $y \to x$ in $D$. If $q$ is another polynomial with $q(x) \neq 0$, then $\lim_{y \to x} p(y)/q(y) = p(x)/q(x)$, as $y \to x$ in $\{ y \in D : q(y) \neq 0 \}$.

*Proof.* Let $(y_n)$ be a sequence in $D$ with $y_n \neq x$ for every $n$ and $y_n \to x$. By the corollary on powers and polynomials (Session 5), $p(y_n) \to p(x)$. The sequence was arbitrary, so the sequential criterion (Section 8.4) gives $\lim_{y \to x} p(y) = p(x)$. In the same way $\lim_{y \to x} q(y) = q(x)$, and $q(x) \neq 0$, so the quotient rule gives the second claim. ∎

## 8.6 Limits and continuity

Continuity at $x$ (Session 7) asks that $f(y)$ be close to $f(x)$ for every $y$ close to $x$, including $y = x$. The limit asks the same for $y \neq x$, with $f(x)$ in place of $L$. At $y = x$ the continuity condition reads $\lvert f(x) - f(x) \rvert = 0 \lt \varepsilon$, which always holds. So the two conditions differ only in a case that is always satisfied.

**Theorem.** Let $f : D \to \mathbb{R}$, and let $x \in D$ be an accumulation point of $D$. Then $f$ is continuous at $x$ if and only if $\lim_{y \to x} f(y) = f(x)$.

*Proof.* Suppose $f$ is continuous at $x$, and let $\varepsilon \gt 0$. Continuity gives $\delta \gt 0$ with $\lvert f(y) - f(x) \rvert \lt \varepsilon$ for every $y \in D$ with $\lvert y - x \rvert \lt \delta$. Every $y \in D$ with $0 \lt \lvert y - x \rvert \lt \delta$ is among these. So $f(y)$ tends to $f(x)$.

Suppose $\lim_{y \to x} f(y) = f(x)$, and let $\varepsilon \gt 0$. The definition of the limit gives $\delta \gt 0$ with $\lvert f(y) - f(x) \rvert \lt \varepsilon$ for every $y \in D$ with $0 \lt \lvert y - x \rvert \lt \delta$. Let $y \in D$ with $\lvert y - x \rvert \lt \delta$. Either $y \neq x$, and then $0 \lt \lvert y - x \rvert \lt \delta$ and the inequality holds; or $y = x$, and then $\lvert f(y) - f(x) \rvert = 0 \lt \varepsilon$. So $f$ is continuous at $x$. ∎

By Lemma 2 the theorem applies at every point of an interval. Session 7 proved directly that polynomials and rational functions are continuous; at every point of the domain that is an accumulation point of it, in particular at every point of an interval, the theorem and the corollary of Section 8.5 give a second route.

**Source.** The order of the results follows W. Rudin, *Principles of Mathematical Analysis*, 3rd ed., Ch. 4, Definition 4.1 to Theorem 4.6, there stated for metric spaces and here for subsets of $\mathbb{R}$.

## 8.7 Worked example

Let $D = \mathbb{R} \setminus \{2\}$ and

$$
f(y) = \frac{y^3 - 8}{y - 2} .
$$

The formula has no value at $y = 2$. We show $\lim_{y \to 2} f(y) = 12$, first from the definition with an explicit $\delta$, then by the rules, then along one sequence.

**The point is an accumulation point.** Given $\delta \gt 0$, the point $y = 2 + \delta/2$ is not $2$, because $\delta/2 \gt 0$, so it lies in $D$; and $\lvert y - 2 \rvert = \delta/2$ is positive and less than $\delta$.

**Simplify for $y \neq 2$.** Multiply out:

$$
(y - 2)(y^2 + 2y + 4) = y^3 + 2y^2 + 4y - 2y^2 - 4y - 8 = y^3 - 8 .
$$

For $y \in D$ the factor $y - 2$ is nonzero, so $f(y) = y^2 + 2y + 4$.

**Factor the error.** For $y \in D$,

$$
f(y) - 12 = y^2 + 2y - 8 = (y - 2)(y + 4),
$$

since $(y - 2)(y + 4) = y^2 + 4y - 2y - 8$. So $\lvert f(y) - 12 \rvert = \lvert y - 2 \rvert \, \lvert y + 4 \rvert$.

**Bound the other factor.** If $\lvert y - 2 \rvert \lt 1$, then $-1 \lt y - 2 \lt 1$ (Session 5), so $1 \lt y \lt 3$ and $5 \lt y + 4 \lt 7$. Since $y + 4 \gt 0$, $\lvert y + 4 \rvert = y + 4 \lt 7$.

**Choose $\delta$.** Let $\varepsilon \gt 0$ and put $\delta = \min\{1, \varepsilon/7\}$, which is positive and at most $1$ and at most $\varepsilon/7$ (Section 8.1). Let $y \in D$ with $0 \lt \lvert y - 2 \rvert \lt \delta$. Then $\lvert y - 2 \rvert \lt 1$, so $\lvert y + 4 \rvert \lt 7$, and

$$
\lvert f(y) - 12 \rvert = \lvert y - 2 \rvert \, \lvert y + 4 \rvert \le 7 \lvert y - 2 \rvert \lt 7 \delta \le 7 \cdot \frac{\varepsilon}{7} = \varepsilon .
$$

So $\lim_{y \to 2} f(y) = 12$.

**One number.** For $\varepsilon = 0.07$ the recipe gives $\delta = \min\{1, 0.01\} = 0.01$. Take $y = 2.009$, which satisfies $0 \lt \lvert y - 2 \rvert \lt 0.01$. Then

$$
y^2 = (2 + 0.009)^2 = 4 + 2 \cdot 2 \cdot 0.009 + 0.009^2 = 4 + 0.036 + 0.000081 = 4.036081,
$$

$2y = 4.018$, and $f(y) = 4.036081 + 4.018 + 4 = 12.054081$. So $\lvert f(y) - 12 \rvert = 0.054081$, which is less than $7 \lvert y - 2 \rvert = 0.063$, which is less than $\varepsilon = 0.07$.

**By the rules.** The polynomial $p(y) = y^2 + 2y + 4$ satisfies $\lim_{y \to 2} p(y) = p(2) = 4 + 4 + 4 = 12$ as $y \to 2$ in $D$, by the corollary of Section 8.5. Since $f(y) = p(y)$ for every $y \in D$, $f$ equals the restriction of $p$ to $D$ (Session 7, Section 7.4). So $\lim_{y \to 2} f(y) = 12$ again.

**Along a sequence.** Let $y_n = 2 + 1/n$. Since $1/n \gt 0$, $y_n \neq 2$, so $y_n \in D$; and $y_n \to 2$ by the test for convergence (Session 7) with $K = 1$, since $\lvert y_n - 2 \rvert = 1/n$. Then

$$
f(y_n) = \Bigl(2 + \frac1n\Bigr)^2 + 2\Bigl(2 + \frac1n\Bigr) + 4 = 4 + \frac4n + \frac1{n^2} + 4 + \frac2n + 4 = 12 + \frac6n + \frac1{n^2} .
$$

Since $1/n \to 0$ and constant sequences converge (Session 5), the product rule gives $6/n = 6 \cdot (1/n) \to 0$ and $1/n^2 = (1/n)(1/n) \to 0$, and the sum rule gives $f(y_n) \to 12$, as the sequential criterion requires.

## 8.8 What fails

**Without an accumulation point, a limit is not unique.** Let $D = \{0\} \cup [1, 2]$, $f(y) = y$, and $x = 0$. Every $y \in D$ with $y \neq 0$ satisfies $y \ge 1$. So with $\delta = 1$ there is no $y \in D$ with $0 \lt \lvert y - 0 \rvert \lt 1$, and $0$ is not an accumulation point of $D$. If the definition of Section 8.3 were applied anyway, then for any $L$ and any $\varepsilon \gt 0$ the choice $\delta = 1$ would satisfy it vacuously (Session 2, Section 2.4), because there is no $y$ to test. Every real number would be a "limit". The hypothesis that $x$ is an accumulation point is what Lemma 1 needs, and Lemma 1 is what the uniqueness proof needs.

**Without $y_n \neq x$, the sequential criterion is false.** Let $f : \mathbb{R} \to \mathbb{R}$ be given by $f(0) = 1$ and $f(y) = 0$ for $y \neq 0$. The point $0$ is an accumulation point of $\mathbb{R}$ (Lemma 2). The constant function $0$ tends to $0$ (Section 8.3), and $f$ agrees with it at every $y \neq 0$, so Lemma 3 gives $\lim_{y \to 0} f(y) = 0$. But the constant sequence $y_n = 0$ tends to $0$, and $f(y_n) = 1$ for every $n$, so $f(y_n) \to 1$, not $0$. The criterion must exclude such sequences. The same function shows a limit that differs from the value: the limit at $0$ is $0$ and $f(0) = 1$, so by Section 8.6 the function is not continuous at $0$.

**Without $M \neq 0$, the quotient rule fails.** Let $f(y) = y$ and $g(y) = y^2$ on $\mathbb{R}$. The point $0$ is an accumulation point of $\mathbb{R}$ (Lemma 2), and both tend to $0$ as $y \to 0$, by the corollary of Section 8.5. Where $g(y) \neq 0$, that is for $y \neq 0$ (Session 4, 4.2(c) and 4.2(g)), the quotient is $y/(y \cdot y) = 1/y$; its domain $\mathbb{R} \setminus \{0\}$ has $0$ as an accumulation point (Example of Section 8.4). The points $y_n = 1/n$ are nonzero and tend to $0$ (Session 5), and $1/y_n = n$ (Session 4, 4.2(e)). If $1/y$ had a limit $L$ at $0$, the sequential criterion would give $n \to L$; but $(n)$ diverges (Session 5, Section 5.7, a zero limit in the denominator). So $1/y$ has no limit at $0$. No rule can assign a value to the quotient $0/0$ of the two limits. With $f(y) = y$ and $g(y) = y$, both limits are again $0$, and $f(y)/g(y) = 1$ for $y \neq 0$, which tends to $1$. With $f(y) = 2y$ and $g(y) = y$, both limits are $0$ once more, and $f(y)/g(y) = 2$ for $y \neq 0$, which tends to $2$. The limits of $f$ and $g$ alone do not decide the limit of the quotient.

## Exercises

*Check*

1. Show from the definition that $\lim_{y \to 2} y^2 = 4$ on $\mathbb{R}$. First show that $\lvert y^2 - 4 \rvert \lt 5 \lvert y - 2 \rvert$ whenever $0 \lt \lvert y - 2 \rvert \lt 1$, then take $\delta = \min\{1, \varepsilon/5\}$. Find $\delta$ for $\varepsilon = 0.01$, and check the inequality $\lvert y^2 - 4 \rvert \lt 0.01$ at $y = 2.001$.

2. Let $D = [0, \infty) \setminus \{4\}$ and $f(y) = (\sqrt{y} - 2)/(y - 4)$, where $\sqrt{y}$ is the nonnegative square root of Session 7. Show that $4$ is an accumulation point of $D$, that $f(y) = 1/(\sqrt{y} + 2)$ on $D$, and that $\lvert f(y) - \tfrac14 \rvert \le \lvert y - 4 \rvert / 16$ on $D$. Conclude that $\lim_{y \to 4} f(y) = 1/4$, with $\delta = 16 \varepsilon$.

3. Let $f : \mathbb{R} \to \mathbb{R}$ be given by $f(y) = 3y^2$ for $y \lt 1$ and $f(y) = y + 1$ for $y \ge 1$. Compute the limits of $f(1 + 1/n)$ and $f(1 - 1/n)$, and conclude that $f$ has no limit at $1$.

*Prove*

4. Let $f, g : D \to \mathbb{R}$, let $x$ be an accumulation point of $D$, and suppose $\lim_{y \to x} f(y) = L$ and $\lim_{y \to x} g(y) = M$.
   (a) If $f(y) \le g(y)$ for every $y \in D$ with $y \neq x$, show that $L \le M$.
   (b) Show by an example that $f(y) \lt g(y)$ for every $y \neq x$ does not force $L \lt M$.

5. (Squeeze rule.) Let $f, g, h : D \to \mathbb{R}$, let $x$ be an accumulation point of $D$, and suppose $f(y) \le g(y) \le h(y)$ for every $y \in D$ with $y \neq x$.
   (a) If $\lim_{y \to x} f(y) = \lim_{y \to x} h(y) = L$, show that $\lim_{y \to x} g(y) = L$.
   (b) Use (a) to show that $\lim_{y \to 0} y \lvert y \rvert = 0$ on $\mathbb{R} \setminus \{0\}$.

6. (Local boundedness.) Let $f : D \to \mathbb{R}$, let $x$ be an accumulation point of $D$, and suppose $\lim_{y \to x} f(y) = L$. Show that there exist $\delta \gt 0$ and $B \in \mathbb{R}$ such that $\lvert f(y) \rvert \le B$ for every $y \in D$ with $0 \lt \lvert y - x \rvert \lt \delta$. (Hint: apply the definition with $\varepsilon = 1$ and, as in Lemma 4 (1), write $f(y) = (f(y) - L) + L$ before using the triangle inequality.)

*Extend*

7. (One-sided limits.) Let $f : D \to \mathbb{R}$ and $x \in \mathbb{R}$. Put $D_+ = \{ y \in D : y \gt x \}$ and $D_- = \{ y \in D : y \lt x \}$, and suppose $x$ is an accumulation point of both. The **right limit** $\lim_{y \to x^+} f(y)$ is the limit at $x$ of $f$ restricted to $D_+$, and the **left limit** $\lim_{y \to x^-} f(y)$ is the limit at $x$ of $f$ restricted to $D_-$.
   (a) Show that $x$ is an accumulation point of $D$.
   (b) Show that $\lim_{y \to x} f(y) = L$ if and only if both one-sided limits exist and equal $L$.
   (c) Compute both one-sided limits of the function of Exercise 3 at $1$, and explain how (b) gives a second proof that it has no limit there.

8. (Limits and composition.) Let $g : D \to \mathbb{R}$, let $x$ be an accumulation point of $D$, and suppose $\lim_{y \to x} g(y) = M$. Let $E \subseteq \mathbb{R}$ contain $M$ and every value $g(y)$, and let $h : E \to \mathbb{R}$ be continuous at $M$.
   (a) Show that $\lim_{y \to x} h(g(y)) = h(M)$.
   (b) Show that if $h$ is only assumed to have a limit at $M$, the equation $\lim_{y \to x} h(g(y)) = \lim_{z \to M} h(z)$ can fail: take $D = E = \mathbb{R}$, $g(y) = 0$ for every $y$, and $h$ the function of Section 8.8 with $h(0) = 1$ and $h(z) = 0$ for $z \neq 0$.

Solutions: [solutions/008-limits-of-functions.md](../solutions/008-limits-of-functions.md).
