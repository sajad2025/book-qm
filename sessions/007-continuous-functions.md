# Session 7. Continuous functions on an interval

*Theorem. Builds on Session 6.*

**Claim.** A real function on an interval is continuous at a point $x$ if and only if $f(x_n) \to f(x)$ for every sequence $(x_n)$ in the interval with $x_n \to x$. A continuous function on $[a,b]$ is bounded, attains its maximum and its minimum, and takes every value between $f(a)$ and $f(b)$. In particular every $a \ge 0$ has a unique $n$-th root $a^{1/n} \ge 0$, by the intermediate value theorem applied to $x^n$.

## 7.1 What this session uses

**Recall.** The session uses the following results from earlier sessions.

- *Session 2.* The negation of a statement with quantifiers is formed by exchanging "for every" and "there exists" and negating the inner statement. A statement may be proved by contraposition or by contradiction.
- *Session 3.* The principle of induction. Bernoulli's inequality: $(1+x)^n \ge 1 + nx$ for every $n \in \mathbb{N}$ and every $x \ge -1$. The laws of powers: $(uv)^n = u^n v^n$; if $u \ge 0$ then $u^n \ge 0$; and if $0 \le u \lt v$ and $n \in \mathbb{N}$, then $u^n \lt v^n$.
- *Session 4.* The axioms of an ordered field, with the usual rules for inequalities: if $u \le v$ and $w \ge 0$ then $uw \le vw$; if $u \lt v$ and $w \gt 0$ then $uw \lt vw$; multiplying an inequality by $-1$ reverses it; if $0 \lt u \le v$ then $0 \lt 1/v \le 1/u$ (Section 4.3(e)); a product of nonnegative numbers is nonnegative, and so is every square $t^2$; for any two reals exactly one of $u \lt v$, $u = v$, $u \gt v$ holds. The intervals $[a,b]$, $(a,b)$, $[a,b)$ and $(a,b]$ for $a \lt b$, and the example that $[0,1)$ has supremum $1$ and no maximum (Section 4.4). The least-upper-bound property: every nonempty set $S \subseteq \mathbb{R}$ that is bounded above has a least upper bound $\sup S$. The Archimedean property: for every real $t$ there is $N \in \mathbb{N}$ with $N \gt t$. The positive number $\sqrt{2}$ with square $2$ (Section 4.8).
- *Session 5.* The absolute value and its properties: $\lvert t \rvert \ge 0$, $\lvert -t \rvert = \lvert t \rvert$, $-\lvert t \rvert \le t \le \lvert t \rvert$, $\lvert uv \rvert = \lvert u \rvert \lvert v \rvert$, $\lvert t \rvert \lt c$ if and only if $-c \lt t \lt c$ (and the same with $\le$), the triangle inequality $\lvert u + v \rvert \le \lvert u \rvert + \lvert v \rvert$, and the reverse triangle inequality $\bigl\lvert \lvert u \rvert - \lvert v \rvert \bigr\rvert \le \lvert u - v \rvert$. A sequence $(a_n)$ converges to $a$, written $a_n \to a$, if for every $\varepsilon \gt 0$ there is $N \in \mathbb{N}$ with $\lvert a_n - a \rvert \lt \varepsilon$ for every $n \ge N$. A sequence has at most one limit. A convergent sequence is bounded. A constant sequence converges to its constant value. If $a_n \to a$ and $b_n \to b$ then $a_n + b_n \to a + b$ and $a_n b_n \to ab$, and if also $b_n \ne 0$ for every $n$ and $b \ne 0$ then $a_n / b_n \to a/b$. If $a_n \to a$, then $p(a_n) \to p(a)$ for every polynomial $p$ with real coefficients (the corollary on powers and polynomials). If $a_n \to a$, $b_n \to b$ and $a_n \le b_n$ for every $n$, then $a \le b$. The sequence $1/n$ converges to $0$. If $d_n \to 0$ and $\lvert x_n - x \rvert \le d_n$ for every $n$, then $x_n \to x$ (the corollary of the squeeze rule).
- *Session 6.* A subsequence of $(x_n)$ is $(x_{n_k})$ with $n_1 \lt n_2 \lt n_3 \lt \dots$ natural numbers, and then $n_k \ge k$ for every $k$ (the lemma on growing indices). Every subsequence of a convergent sequence converges to the same limit. Bolzano-Weierstrass: every bounded real sequence has a convergent subsequence.

One small fact is used several times, so it is proved once here.

**Lemma (a test for convergence).** Let $K \ge 0$ and $x \in \mathbb{R}$. If $\lvert x_n - x \rvert \le K/n$ for every $n \in \mathbb{N}$, then $x_n \to x$.

*Proof.* The sequence $1/n$ converges to $0$, and the constant sequence $K$ converges to $K$ (Session 5). By the product rule (Session 5), $K/n = K \cdot (1/n) \to K \cdot 0 = 0$. The corollary of the squeeze rule (Session 5), with $d_n = K/n$, gives $x_n \to x$. ∎

## 7.2 Continuity at a point

Throughout, $D$ is a subset of $\mathbb{R}$ and $f : D \to \mathbb{R}$ is a function.

**Definition.** The function $f$ is **continuous at** a point $x \in D$ if for every $\varepsilon \gt 0$ there exists $\delta \gt 0$ such that

$$
\lvert f(y) - f(x) \rvert \lt \varepsilon \quad \text{for every } y \in D \text{ with } \lvert y - x \rvert \lt \delta .
$$

The function is **continuous on** $D$ if it is continuous at every point of $D$. A **continuous function on** $D$ is a function that is continuous on $D$.

The number $\varepsilon$ is a tolerance on the output. The number $\delta$ says how close to $x$ the input must be for the output to lie within that tolerance of $f(x)$. The $\delta$ may depend on $\varepsilon$ and on $x$. Only points $y$ of $D$ are tested.

By the rules for negation (Session 2), $f$ is *not* continuous at $x$ if and only if

$$
\exists\, \varepsilon \gt 0 \ \ \forall\, \delta \gt 0 \ \ \exists\, y \in D : \quad \lvert y - x \rvert \lt \delta \ \text{ and } \ \lvert f(y) - f(x) \rvert \ge \varepsilon .
$$

Session 4 named the four intervals $[a,b]$, $(a,b)$, $[a,b)$ and $(a,b]$ with $a \lt b$. From now on the word has a wider meaning, which includes those four.

**Definition.** An **interval** is a set $I \subseteq \mathbb{R}$ with at least two points such that, whenever $u, w \in I$ and $u \lt v \lt w$, also $v \in I$.

For $a \lt b$ the four intervals of Session 4 are intervals in this sense. Each of the four has at least two points: by 4.3(g) of Session 4, $m = (a+b)/2$ satisfies $a \lt m \lt b$, and $m' = (a+m)/2$ satisfies $a \lt m' \lt m$, so $m'$ and $m$ are two points of $(a,b)$, which is contained in all four. For betweenness, let $u, w$ lie in one of the four and $u \lt v \lt w$. Then $a \le u \lt v$ and $v \lt w \le b$, so $v \in (a,b)$, and so $v$ lies in each of the four. The sets $[0, \infty) = \{x \in \mathbb{R} : x \ge 0\}$ and $(0, \infty) = \{x \in \mathbb{R} : x \gt 0\}$ contain $1$ and $2$ (4.3(g)), and if $0 \le u \lt v$ then $v \gt 0$, so both are intervals. $\mathbb{R}$ contains $0$ and $1$ and every $v$, so it is an interval too. The session's theorems about $[a,b]$ always take $a \lt b$.

**Lemma (three continuous functions).** The following functions $\mathbb{R} \to \mathbb{R}$ are continuous on $\mathbb{R}$:

1. a constant function $f(x) = c$;
2. the identity $f(x) = x$;
3. the absolute value $f(x) = \lvert x \rvert$.

*Proof.* Fix $x \in \mathbb{R}$ and $\varepsilon \gt 0$.

1. Take $\delta = 1$. For every $y$, $\lvert f(y) - f(x) \rvert = \lvert c - c \rvert = 0 \lt \varepsilon$.
2. Take $\delta = \varepsilon$. If $\lvert y - x \rvert \lt \delta$ then $\lvert f(y) - f(x) \rvert = \lvert y - x \rvert \lt \varepsilon$.
3. Take $\delta = \varepsilon$. If $\lvert y - x \rvert \lt \delta$, the reverse triangle inequality (Session 5) gives $\bigl\lvert \lvert y \rvert - \lvert x \rvert \bigr\rvert \le \lvert y - x \rvert \lt \varepsilon$. ∎

**Example (a jump).** Let $H : \mathbb{R} \to \mathbb{R}$ be $H(x) = 0$ for $x \lt 0$ and $H(x) = 1$ for $x \ge 0$.

- $H$ is not continuous at $0$. Take $\varepsilon = 1/2$. Given any $\delta \gt 0$, let $y = -\delta/2$. Then $\lvert y - 0 \rvert = \delta/2 \lt \delta$, and $y \lt 0$, so $\lvert H(y) - H(0) \rvert = \lvert 0 - 1 \rvert = 1 \ge 1/2$. This is the negation displayed above.
- $H$ is continuous at every $x \gt 0$. Take $\delta = x$. If $\lvert y - x \rvert \lt x$ then $-x \lt y - x$, so $y \gt 0$, and $\lvert H(y) - H(x) \rvert = \lvert 1 - 1 \rvert = 0 \lt \varepsilon$.
- $H$ is continuous at every $x \lt 0$. Take $\delta = -x \gt 0$. If $\lvert y - x \rvert \lt -x$ then $y - x \lt -x$, so $y \lt 0$, and $\lvert H(y) - H(x) \rvert = 0 \lt \varepsilon$.

The $\delta$ chosen at $x \gt 0$ is $x$ itself, and it shrinks as $x$ approaches $0$. Continuity is a property at each point separately.

## 7.3 Continuity through sequences

**Theorem (sequential characterisation of continuity).** Let $f : D \to \mathbb{R}$ and $x \in D$. Then $f$ is continuous at $x$ if and only if $f(x_n) \to f(x)$ for every sequence $(x_n)$ of points of $D$ with $x_n \to x$.

*Proof.* Suppose first that $f$ is continuous at $x$. Let $(x_n)$ be a sequence of points of $D$ with $x_n \to x$, and let $\varepsilon \gt 0$.

1. Continuity at $x$ gives $\delta \gt 0$ with $\lvert f(y) - f(x) \rvert \lt \varepsilon$ for every $y \in D$ with $\lvert y - x \rvert \lt \delta$.
2. The definition of $x_n \to x$ (Session 5), used with the positive number $\delta$ in place of $\varepsilon$, gives $N \in \mathbb{N}$ with $\lvert x_n - x \rvert \lt \delta$ for every $n \ge N$.
3. For every $n \ge N$, the point $x_n$ lies in $D$ and satisfies $\lvert x_n - x \rvert \lt \delta$, so step 1 applies with $y = x_n$: $\lvert f(x_n) - f(x) \rvert \lt \varepsilon$.

Since $\varepsilon \gt 0$ was arbitrary, $f(x_n) \to f(x)$.

For the converse we prove the contrapositive (Session 2): if $f$ is not continuous at $x$, then some sequence $(x_n)$ in $D$ has $x_n \to x$ but not $f(x_n) \to f(x)$. Suppose $f$ is not continuous at $x$. By the negation in Section 7.2, there is $\varepsilon_0 \gt 0$ such that for every $\delta \gt 0$ some $y \in D$ has $\lvert y - x \rvert \lt \delta$ and $\lvert f(y) - f(x) \rvert \ge \varepsilon_0$.

1. For each $n \in \mathbb{N}$, apply this with $\delta = 1/n$, and call the point it provides $x_n$. So $x_n \in D$, $\lvert x_n - x \rvert \lt 1/n$ and $\lvert f(x_n) - f(x) \rvert \ge \varepsilon_0$. This step picks one point for each of the infinitely many $n$ at once. That such a sequence exists is the **axiom of countable choice**: if $A_n$ is a nonempty set for each $n \in \mathbb{N}$, there is a sequence $(x_n)$ with $x_n \in A_n$ for every $n$. Here $A_n$ is the set of $y \in D$ with $\lvert y - x \rvert \lt 1/n$ and $\lvert f(y) - f(x) \rvert \ge \varepsilon_0$. It is an axiom of set theory, not one of the rules of proof of Session 2, and the book assumes it from here on, citing it as countable choice (Section 7.3). Where a later proof avoids it, the text says so.
2. By the test for convergence (Section 7.1) with $K = 1$, $x_n \to x$.
3. Suppose $f(x_n) \to f(x)$. Then the definition of convergence with $\varepsilon = \varepsilon_0$ gives $N$ with $\lvert f(x_n) - f(x) \rvert \lt \varepsilon_0$ for every $n \ge N$, and in particular for $n = N$. This contradicts step 1 at $n = N$. So $f(x_n)$ does not converge to $f(x)$. ∎

The theorem holds for any set $D$; the claim states it for an interval. It turns questions about continuity into questions about sequences, for which Sessions 5 and 6 supply the rules. It also gives a short way to show that a function is not continuous: one sequence suffices. For the jump $H$ of Section 7.2, the sequence $x_n = -1/n$ converges to $0$ (the test with $K = 1$, since $\lvert x_n - 0 \rvert = 1/n$). Also $H(x_n) = 0$ for every $n$, so $(H(x_n))$ is the constant sequence $0$ and converges to $0$ (Session 5). Since $0 \ne 1 = H(0)$, uniqueness of limits (Session 5) shows that $H(x_n)$ does not converge to $H(0)$.

## 7.4 Sums, products and quotients

For $f, g : D \to \mathbb{R}$ and $c \in \mathbb{R}$, the functions $f + g$, $cf$ and $fg$ on $D$ have values $(f+g)(y) = f(y) + g(y)$, $(cf)(y) = c\,f(y)$ and $(fg)(y) = f(y)\,g(y)$. If $g(y) \ne 0$ for every $y \in D$, then $(f/g)(y) = f(y)/g(y)$. We write $-f$ for $(-1)f$.

**Theorem (algebra of continuous functions).** Let $f, g : D \to \mathbb{R}$ be continuous at $x \in D$, and let $c \in \mathbb{R}$. Then:

1. $f + g$, $cf$ and $fg$ are continuous at $x$;
2. if $g(y) \ne 0$ for every $y \in D$, then $f/g$ is continuous at $x$.

*Proof.* We use the theorem of Section 7.3 in both directions. Let $(x_n)$ be any sequence in $D$ with $x_n \to x$. By Section 7.3, $f(x_n) \to f(x)$ and $g(x_n) \to g(x)$.

1. By the sum rule of Session 5, $f(x_n) + g(x_n) \to f(x) + g(x)$, that is, $(f+g)(x_n) \to (f+g)(x)$. The constant sequence $c, c, c, \dots$ converges to $c$ (Session 5), so the product rule gives $c f(x_n) \to c f(x)$. The product rule also gives $f(x_n) g(x_n) \to f(x) g(x)$.
2. Here $g(x_n) \ne 0$ for every $n$ and $g(x) \ne 0$, because $x_n$ and $x$ lie in $D$. The quotient rule of Session 5 gives $f(x_n)/g(x_n) \to f(x)/g(x)$.

In each case the new function sends every sequence in $D$ converging to $x$ to a sequence converging to its value at $x$. By Section 7.3 it is continuous at $x$. ∎

Session 3, Section 3.5, restricted a function on $\{1, \dots, n+1\}$ to $\{1, \dots, n\}$. In general, a **restriction** of $f : D \to \mathbb{R}$ to a subset $D_0 \subseteq D$ is the function $D_0 \to \mathbb{R}$ with the same values. If $f$ is continuous at $x \in D_0$, so is its restriction: a $\delta$ that works for every $y \in D$ with $\lvert y - x \rvert \lt \delta$ works in particular for every such $y \in D_0$.

A **zero** of a function $f : D \to \mathbb{R}$ is a point $x \in D$ with $f(x) = 0$.

**Corollary (polynomials and rational functions).** Every polynomial $p(x) = a_0 + a_1 x + \dots + a_m x^m$ with real coefficients (Session 5) is continuous on $\mathbb{R}$. If $q$ is another polynomial and $D \subseteq \mathbb{R}$ is a set with $q(y) \ne 0$ for every $y \in D$, then the quotient $p/q$, called a **rational function**, is continuous on $D$.

*Proof.* Fix $x \in \mathbb{R}$, and let $(x_n)$ be any sequence with $x_n \to x$. By the corollary on powers and polynomials (Session 5), $p(x_n) \to p(x)$. By Section 7.3, $p$ is continuous at $x$.

For the quotient, the restrictions of $p$ and $q$ to $D$ are continuous at every point of $D$, and $q(y) \ne 0$ for every $y \in D$. Part 2 of the algebra theorem gives that $p/q$ is continuous on $D$. ∎

So, for instance, $x \mapsto x^3 - 3x$ is continuous on $\mathbb{R}$, $x \mapsto 1/x$ is continuous on $(0, \infty)$, and $x \mapsto x/(1 + x^2)$ is continuous on $\mathbb{R}$, because $1 + x^2 \ge 1 \gt 0$.

## 7.5 Bounded on a closed interval

For $a \lt b$ the interval $[a,b]$ is called a **closed interval**, and $(a,b)$ an **open interval**. A function $f : D \to \mathbb{R}$ is **bounded** if there is $M \in \mathbb{R}$ with $\lvert f(x) \rvert \le M$ for every $x \in D$.

The next three theorems are about a closed interval $[a,b]$. The first two (Sections 7.5 and 7.6) use the following consequence of the Bolzano-Weierstrass theorem (Session 6); the third (Section 7.7) uses the least-upper-bound property instead.

**Lemma (sequences in a closed interval).** Every sequence $(x_n)$ with $a \le x_n \le b$ for every $n$ has a subsequence that converges to a point $c$ with $a \le c \le b$.

*Proof.* Let $M = \lvert a \rvert + \lvert b \rvert$. Since $\lvert a \rvert \ge 0$, $\lvert b \rvert \ge 0$ and $-\lvert t \rvert \le t \le \lvert t \rvert$ (Session 5), for every $n$

$$
x_n \le b \le \lvert b \rvert \le M \qquad \text{and} \qquad x_n \ge a \ge -\lvert a \rvert \ge -M ,
$$

so $-M \le x_n \le M$, that is, $\lvert x_n \rvert \le M$ (Session 5). The sequence is bounded, so Bolzano-Weierstrass (Session 6) gives a subsequence $(x_{n_k})$ converging to some $c$. For every $k$, $a \le x_{n_k} \le b$. The constant sequences $a$ and $b$ converge to $a$ and $b$, so the rule for non-strict inequalities (Session 5) gives $a \le c$ and $c \le b$. ∎

A closed end matters. The sequence $x_n = 1 - 1/n$ lies in $[0, 1)$, since $0 \lt 1/n \le 1$ (Session 4), and $\lvert x_n - 1 \rvert = 1/n$, so $x_n \to 1$ (Section 7.1, $K = 1$). By Session 6 every subsequence also converges to $1$, and by uniqueness of limits (Session 5) to nothing else. Since $1 \notin [0,1)$, no subsequence converges to a point of $[0,1)$. In the same way, every subsequence of $1/n$ in $(0,1]$ converges to $0 \notin (0,1]$.

**Theorem (boundedness theorem).** If $f : [a,b] \to \mathbb{R}$ is continuous, then $f$ is bounded: there is $M \in \mathbb{R}$ with $\lvert f(x) \rvert \le M$ for every $x \in [a,b]$.

*Proof.* By contradiction (Session 2). Suppose no such $M$ exists.

1. Then for each $n \in \mathbb{N}$ the number $n$ is not such a bound, so there is $x_n \in [a,b]$ with $\lvert f(x_n) \rvert \gt n$. One such $x_n$ for each $n$ gives a sequence (countable choice, Section 7.3).
2. By the lemma, a subsequence $(x_{n_k})$ converges to some $c \in [a,b]$.
3. The function $f$ is continuous at $c$, so by Section 7.3, $f(x_{n_k}) \to f(c)$.
4. A convergent sequence is bounded (Session 5), so there is $K$ with $\lvert f(x_{n_k}) \rvert \le K$ for every $k$.
5. By the Archimedean property (Session 4) there is $k \in \mathbb{N}$ with $k \gt K$. By step 1 and the lemma on growing indices (Session 6), $\lvert f(x_{n_k}) \rvert \gt n_k \ge k \gt K$.

Step 5 contradicts step 4. So a bound $M$ exists. ∎

## 7.6 The extreme value theorem

**Definition.** Let $f : D \to \mathbb{R}$. A point $q \in D$ is a **maximum point** of $f$ if $f(x) \le f(q)$ for every $x \in D$; then $f(q)$ is the **maximum** of $f$ on $D$, and $f$ **attains** its maximum at $q$. A **minimum point** $p$, with $f(p) \le f(x)$ for every $x \in D$, and the **minimum** $f(p)$ are defined in the same way.

So the maximum of $f$, when it exists, is the largest element of the set of values $f(D)$.

**Theorem (extreme value theorem).** If $f : [a,b] \to \mathbb{R}$ is continuous, there are points $p, q \in [a,b]$ with

$$
f(p) \le f(x) \le f(q) \quad \text{for every } x \in [a,b] .
$$

*Proof.* We find $q$ first.

1. Let $S = f([a,b]) = \{ f(x) : x \in [a,b] \}$. It is nonempty, since $f(a) \in S$. By the boundedness theorem (Section 7.5) there is $M$ with $\lvert f(x) \rvert \le M$, so $f(x) \le \lvert f(x) \rvert \le M$ for every $x$ (Session 5), and $S$ is bounded above. By the least-upper-bound property (Session 4), $s^* = \sup S$ exists.
2. Let $n \in \mathbb{N}$. Since $s^* - 1/n \lt s^*$ and $s^*$ is the least upper bound, $s^* - 1/n$ is not an upper bound of $S$. So there is $x_n \in [a,b]$ with $f(x_n) \gt s^* - 1/n$, and one such $x_n$ for each $n$ gives a sequence (countable choice, Section 7.3). Since $s^*$ is an upper bound, also $f(x_n) \le s^*$.
3. By the lemma of Section 7.5, a subsequence $(x_{n_k})$ converges to some $q \in [a,b]$. By continuity at $q$ and Section 7.3, $f(x_{n_k}) \to f(q)$.
4. By the lemma on growing indices (Session 6), $n_k \ge k \gt 0$, so $1/n_k \le 1/k$ (Session 4). With step 2, for every $k$,

$$
0 \le s^* - f(x_{n_k}) \lt \frac{1}{n_k} \le \frac{1}{k} ,
$$

so $\lvert f(x_{n_k}) - s^* \rvert \le 1/k$. The test for convergence (Section 7.1, with $K = 1$) gives $f(x_{n_k}) \to s^*$.
5. By steps 3 and 4 and uniqueness of limits (Session 5), $f(q) = s^*$. Since $s^*$ is an upper bound of $S$, $f(x) \le f(q)$ for every $x \in [a,b]$.

For $p$, the function $-f$ is continuous on $[a,b]$ (Section 7.4). By what has been proved, there is $p \in [a,b]$ with $-f(x) \le -f(p)$ for every $x$. Multiplying by $-1$ (Session 4) gives $f(p) \le f(x)$ for every $x \in [a,b]$. ∎

So $f([a,b])$ has a largest element $f(q)$ and a smallest element $f(p)$. The supremum of the set of values is a value.

The theorem is usually named after K. Weierstrass. B. Bolzano had proved it earlier, in §24 of his *Functionenlehre*, written in the early 1830s and first published in *Bernard Bolzano's Schriften*, Band 1 (Royal Bohemian Society of Sciences, Prague, 1930).

## 7.7 The intermediate value theorem

**Theorem (intermediate value theorem).** Let $f : [a,b] \to \mathbb{R}$ be continuous, and let $y$ be a real number between $f(a)$ and $f(b)$, that is, $f(a) \le y \le f(b)$ or $f(b) \le y \le f(a)$. Then there is $c \in [a,b]$ with $f(c) = y$.

*Proof.* We first reduce to one case. Suppose the theorem is proved whenever $f(a) \le y \le f(b)$. If instead $f(b) \le y \le f(a)$, let $g = -f$, which is continuous (Section 7.4). Multiplying by $-1$ (Session 4) gives $g(a) \le -y \le g(b)$, so the first case gives $c$ with $g(c) = -y$, that is, $f(c) = y$.

So let $f(a) \le y \le f(b)$. If $y = f(a)$, take $c = a$. If $y = f(b)$, take $c = b$. It remains to treat $f(a) \lt y \lt f(b)$.

1. *The set.* Let $S = \{ x \in [a,b] : f(x) \lt y \}$. Then $a \in S$, because $f(a) \lt y$, and $b$ is an upper bound of $S$. By the least-upper-bound property (Session 4), $c = \sup S$ exists. Since $a \in S$ and $c$ is an upper bound, $a \le c$. Since $b$ is an upper bound and $c$ is the least one, $c \le b$. So $c \in [a,b]$.
2. *Approach from the left: $f(c) \le y$.* Let $n \in \mathbb{N}$. Since $c - 1/n$ is less than the least upper bound $c$, it is not an upper bound, so there is $s_n \in S$ with $s_n \gt c - 1/n$; one such $s_n$ for each $n$ gives a sequence (countable choice, Section 7.3). Also $s_n \le c$. So $0 \le c - s_n \lt 1/n$, and the test for convergence (Section 7.1, $K = 1$) gives $s_n \to c$. By Section 7.3, $f(s_n) \to f(c)$. Each $s_n$ is in $S$, so $f(s_n) \lt y$ for every $n$. The rule for non-strict inequalities (Session 5), comparing with the constant sequence $y$, gives $f(c) \le y$.
3. *Then $c \lt b$.* By step 2, $f(c) \le y \lt f(b)$, so $f(c) \ne f(b)$, so $c \ne b$. With $c \le b$ this gives $c \lt b$.
4. *Approach from the right: $f(c) \ge y$.* For $n \in \mathbb{N}$ let $t_n = c + (b - c)/n$. Since $n \ge 1$, $0 \lt 1/n \le 1$ (Session 4), and multiplying by $b - c \gt 0$ gives $0 \lt (b-c)/n \le b - c$. So $c \lt t_n \le b$. Also $a \le c \lt t_n$, so $t_n \in [a,b]$. Every element of $S$ is at most $c$, and $t_n \gt c$, so $t_n \notin S$; since $t_n \in [a,b]$, this means $f(t_n) \ge y$. Next, $\lvert t_n - c \rvert = (b - c)/n$, so the test for convergence with $K = b - c$ gives $t_n \to c$. By Section 7.3, $f(t_n) \to f(c)$, and the rule for non-strict inequalities gives $f(c) \ge y$.

Steps 2 and 4 give $f(c) = y$. ∎

In the case $f(a) \lt y \lt f(b)$ the point $c$ is neither $a$ nor $b$, since $f(a) \ne y \ne f(b)$. The proof used the least-upper-bound property once, to produce $c$.

The case $y = 0$, with $f(a)$ and $f(b)$ of opposite signs, is called Bolzano's theorem. B. Bolzano proved it in *Rein analytischer Beweis des Lehrsatzes, daß zwischen je zwey Werthen, die ein entgegengesetztes Resultat gewähren, wenigstens eine reelle Wurzel der Gleichung liege* (Prague, 1817).

## 7.8 The n-th root

Session 6 called a sequence nondecreasing or nonincreasing according to how its terms are ordered. The same words are used for functions on an interval.

**Definition.** Let $I$ be an interval and $f : I \to \mathbb{R}$. The function $f$ is **nondecreasing** if $x \lt y$ in $I$ implies $f(x) \le f(y)$, **nonincreasing** if $x \lt y$ in $I$ implies $f(x) \ge f(y)$, and **monotone** if it is nondecreasing or nonincreasing. It is **strictly increasing** if $x \lt y$ in $I$ implies $f(x) \lt f(y)$.

By the laws of powers (Session 3), if $n \in \mathbb{N}$ and $0 \le u \lt v$, then $u^n \lt v^n$. In the words just defined, $x \mapsto x^n$ is strictly increasing on $[0, \infty)$.

**Corollary.** Let $n \in \mathbb{N}$ and $u, v \ge 0$.

1. If $u^n = v^n$, then $u = v$.
2. If $u^n \le v^n$, then $u \le v$.

*Proof.* 1. If $u \lt v$, Session 3 gives $u^n \lt v^n$. If $v \lt u$, Session 3 gives $v^n \lt u^n$. Both contradict $u^n = v^n$, so the remaining case of the trichotomy (Session 4) holds: $u = v$.
2. By contraposition (Session 2): if $u \gt v$, Session 3 gives $u^n \gt v^n$, which is not $u^n \le v^n$. ∎

**Theorem (existence and uniqueness of n-th roots).** Let $n \in \mathbb{N}$ and $a \ge 0$. There is exactly one real number $r \ge 0$ with $r^n = a$.

*Proof.* *Existence.* Let $g(x) = x^n$ on $[0, a + 1]$. Since $a \ge 0$, $0 \lt 1 \le a + 1$, so this is a closed interval, and $g$ is continuous on it: it is the restriction of a polynomial (Section 7.4). At the left end, $n - 1 \ge 0$, so (R) of Session 3, and (M1) and 4.2(c) of Session 4, give $g(0) = 0^n = 0^{n-1} \cdot 0 = 0 \le a$. At the right end, Bernoulli's inequality (Session 3) with $x = a \ge -1$ gives

$$
g(a+1) = (1 + a)^n \ge 1 + na .
$$

Since $n \ge 1$ and $a \ge 0$, $na - a = (n - 1) a \ge 0$, so $na \ge a$, and $1 + na \gt na \ge a$. Hence

$$
g(0) \le a \le g(a + 1) .
$$

Apply the intermediate value theorem (Section 7.7) to $g$ on $[0, a+1]$, with $0$ and $a + 1$ in place of the ends $a$ and $b$ there, and with the value $a$ in place of $y$. It gives $r \in [0, a+1]$ with $r^n = a$. In particular $r \ge 0$.

*Uniqueness.* If $r \ge 0$ and $r' \ge 0$ both satisfy $r^n = a = r'^n$, part 1 of the corollary gives $r = r'$. ∎

**Definition.** For $n \in \mathbb{N}$ and $a \ge 0$, the number $r$ of the theorem is the **$n$-th root** of $a$, written $a^{1/n}$. For $n = 2$ it is the **square root**, written $\sqrt{a}$.

For example, $0^{1/n} = 0$ and $1^{1/n} = 1$, since $0^n = 0$ (shown in the proof above) and $1^n = 1$ (Session 3), and the root is unique. The uniqueness is what makes $a^{1/n}$ a definite number: any argument that finds some $r \ge 0$ with $r^n = a$ has found $a^{1/n}$.

## 7.9 Worked example

**Continuity of $x^2$ at $3$ from the definition.** Let $f(x) = x^2$ and $\varepsilon \gt 0$. We look for $\delta$ with $\lvert y^2 - 9 \rvert \lt \varepsilon$ whenever $\lvert y - 3 \rvert \lt \delta$.

1. Factor: $y^2 - 9 = (y - 3)(y + 3)$, so $\lvert y^2 - 9 \rvert = \lvert y - 3 \rvert \, \lvert y + 3 \rvert$.
2. Control the second factor. If $\lvert y - 3 \rvert \lt 1$, then $2 \lt y \lt 4$, so $5 \lt y + 3 \lt 7$ and $\lvert y + 3 \rvert \lt 7$. Then $\lvert y^2 - 9 \rvert \le 7 \lvert y - 3 \rvert$.
3. Choose $\delta$ to be the smaller of $1$ and $\varepsilon/7$. Then $\delta \le 1$ and $\delta \le \varepsilon/7$, and $\delta \gt 0$, since $1 \gt 0$ and $\varepsilon/7 \gt 0$ (Session 4). If $\lvert y - 3 \rvert \lt \delta$, then $\lvert y - 3 \rvert \lt 1$, so step 2 applies, and $\lvert y - 3 \rvert \lt \varepsilon/7$, so

$$
\lvert y^2 - 9 \rvert \le 7 \lvert y - 3 \rvert \lt 7 \cdot \frac{\varepsilon}{7} = \varepsilon .
$$

So $f$ is continuous at $3$.

For $\varepsilon = 1/10$ this gives $\delta = 1/70$. A check at one point: $y = 3 + 1/80$ has $\lvert y - 3 \rvert = 1/80 \lt 1/70$, and

$$
y^2 - 9 = \Bigl(3 + \frac{1}{80}\Bigr)^2 - 9 = 9 + 2 \cdot 3 \cdot \frac{1}{80} + \frac{1}{6400} - 9 = \frac{480}{6400} + \frac{1}{6400} = \frac{481}{6400} ,
$$

which is positive, so $\lvert y^2 - 9 \rvert = \frac{481}{6400} \lt \frac{640}{6400} = \frac{1}{10}$.

Section 7.4 gives the same conclusion without any $\delta$: $x^2$ is a polynomial. The direct proof shows what the definition asks for.

**Locating $\sqrt{2}$.** By Section 7.8, $\sqrt{2}$ exists. It is the number $\sqrt{2}$ of Session 4, Section 4.8, since both are nonnegative with square $2$ and the root is unique. Since $1^2 = 1 \le 2 \le 4 = 2^2$ and $2 = (\sqrt{2})^2$, part 2 of the corollary of Section 7.8 gives $1 \le \sqrt{2} \le 2$.

The same corollary locates it more closely. A **decimal** with $k$ digits after the point, $k \in \mathbb{N}$, is the fraction whose numerator is the natural number or zero written by all its digits with the point removed, and whose denominator is $10^k$. For example $1.4 = 14/10$, $1.41 = 141/100$ and $0.07 = 7/100$. Then

$$
\Bigl(\frac{14}{10}\Bigr)^2 = \frac{196}{100} \lt \frac{200}{100} = 2 \lt \frac{225}{100} = \Bigl(\frac{15}{10}\Bigr)^2 .
$$

Part 2 of the corollary gives $1.4 \le \sqrt{2} \le 1.5$. Neither is an equality, since $1.4^2 \ne 2$ and $1.5^2 \ne 2$. So $1.4 \lt \sqrt{2} \lt 1.5$. One more digit:

$$
\Bigl(\frac{141}{100}\Bigr)^2 = \frac{19881}{10000} \lt \frac{20000}{10000} = 2 \lt \frac{20164}{10000} = \Bigl(\frac{142}{100}\Bigr)^2 ,
$$

so $1.41 \lt \sqrt{2} \lt 1.42$. The intermediate value theorem, in Section 7.8, showed that the number exists. The order of the powers then locates it.

**Extreme values of $x^3 - 3x$ on $[0,2]$.** Let $f(x) = x^3 - 3x$ on $[0,2]$. It is continuous (Section 7.4), so the extreme value theorem says it has a maximum and a minimum there. Three values: $f(0) = 0$, $f(1) = 1 - 3 = -2$, $f(2) = 8 - 6 = 2$.

1. *The minimum is $-2$, at $x = 1$.* Expanding,

$$
(x - 1)^2 (x + 2) = (x^2 - 2x + 1)(x + 2) = x^3 + 2x^2 - 2x^2 - 4x + x + 2 = x^3 - 3x + 2 .
$$

So $f(x) + 2 = (x - 1)^2 (x + 2)$. On $[0,2]$, $(x-1)^2 \ge 0$ and $x + 2 \gt 0$, so $f(x) + 2 \ge 0$, that is, $f(x) \ge -2 = f(1)$.

2. *The maximum is $2$, at $x = 2$.* Expanding,

$$
(2 - x)(x + 1)^2 = (2 - x)(x^2 + 2x + 1) = 2x^2 + 4x + 2 - x^3 - 2x^2 - x = -x^3 + 3x + 2 .
$$

So $2 - f(x) = (2 - x)(x + 1)^2$. On $[0,2]$, $2 - x \ge 0$ and $(x + 1)^2 \ge 0$, so $2 - f(x) \ge 0$, that is, $f(x) \le 2 = f(2)$.

3. *Every value in between is taken.* Apply the intermediate value theorem to the restriction of $f$ to $[1,2]$, where $f(1) = -2$ and $f(2) = 2$. Every $y$ with $-2 \le y \le 2$ equals $f(c)$ for some $c \in [1,2] \subseteq [0,2]$.

Together, $f([0,2]) = [-2, 2]$. The maximum is at an end of the interval and the minimum is inside it. The intermediate value theorem on the whole of $[0,2]$ would only give the values between $f(0) = 0$ and $f(2) = 2$; the negative values come from the subinterval $[1,2]$.

## 7.10 What fails without the hypotheses

Each hypothesis of Sections 7.5-7.7 is needed. In each example below, one hypothesis is dropped and the conclusion fails.

**The interval is not closed.** Let $f(x) = 1/x$ on $(0, 1]$. It is continuous (Section 7.4). It is not bounded: given any $M$, let $x = 1/(\lvert M \rvert + 1)$. Since $\lvert M \rvert + 1 \ge 1 \gt 0$, Session 4 gives $0 \lt x \le 1$, and $f(x) = \lvert M \rvert + 1 \gt M$, because $M \le \lvert M \rvert$ (Session 5). The sequence $x_n = 1/n$ lies in $(0,1]$ and converges to $0$, which is not in $(0,1]$; this is where the proof of Section 7.5 breaks.

Let $f(x) = x$ on $[0, 1)$. It is continuous (Section 7.4) and bounded, since $\lvert x \rvert = x \lt 1$ there. Its set of values is $f([0,1)) = [0,1)$, which has supremum $1$ and no maximum (Session 4, Section 4.4). By Section 7.6, a maximum of $f$ would be a largest element of this set. So $f$ has no maximum.

**The interval is not bounded.** Let $f(x) = x$ on $[0, \infty)$. Given any $M$, the point $x = \lvert M \rvert + 1$ lies in $[0, \infty)$ and has $f(x) = \lvert M \rvert + 1 \gt M$ (Session 5). So $f$ is not bounded.

**The function is not continuous.** Let $g$ on $[0,1]$ be $g(x) = x$ for $0 \le x \lt 1$ and $g(1) = 0$. Its set of values is $\{x \in \mathbb{R} : 0 \le x \lt 1\} \cup \{0\} = [0,1)$, the same set as in the previous example, which has no largest element (Session 4, Section 4.4). So $g$ has no maximum. The failure is at one point: $x_n = 1 - 1/n$ lies in $[0,1)$ and converges to $1$, and $g(x_n) = 1 - 1/n \to 1$ (both by the test of Section 7.1, $K = 1$), while $g(1) = 0$. By uniqueness of limits (Session 5) and Section 7.3, $g$ is not continuous at $1$.

Let $h$ on $[0,1]$ be $h(0) = 0$ and $h(x) = 1/x$ for $0 \lt x \le 1$. It is not bounded, by the computation for $1/x$ above. It is not continuous at $0$: the sequence $1/n$ lies in $[0,1]$ and converges to $0$, while $h(1/n) = n$ is not bounded (Archimedean property, Session 4), so it does not converge (Session 5), and Section 7.3 applies.

The jump $H$ of Section 7.2, restricted to $[-1, 1]$, has $H(-1) = 0$ and $H(1) = 1$, and takes only the values $0$ and $1$. The value $1/2$ lies between $H(-1)$ and $H(1)$ and is not taken. The restriction is not continuous at $0$: the sequence $x_n = -1/n$ of Section 7.3 lies in $[-1,1]$, since $0 \lt 1/n \le 1$, converges to $0$, and has $H(x_n) \to 0 \ne 1 = H(0)$. So the intermediate value theorem fails because $H$ is not continuous at $0$.

## Exercises

*Check*

1. (a) Prove from the definition of Section 7.2 that $f(x) = 2x + 1$ is continuous at every $x \in \mathbb{R}$. (b) For $f(x) = x^2$ at $x = -2$ and $\varepsilon = 1/10$, find a $\delta \gt 0$ that works, following the worked example of Section 7.9, and prove that it works.
2. Let $p(x) = x^3 - x - 1$. Show that $p$ has a zero (Section 7.4) in $[1,2]$. By evaluating $p$ at midpoints, find an interval of length $1/8$ that contains a zero.
3. Let $f(x) = x/(1 + x^2)$ on $[0,2]$. Find the maximum and the minimum of $f$, with the points where they are attained, and prove that $f([0,2]) = [0, 1/2]$.

*Prove*

4. (Sign preservation.) Let $f : D \to \mathbb{R}$ be continuous at $x \in D$ with $f(x) \gt 0$. Prove that there is $\delta \gt 0$ with $f(y) \gt f(x)/2$ for every $y \in D$ with $\lvert y - x \rvert \lt \delta$.
5. (A fixed point.) Let $f : [0,1] \to \mathbb{R}$ be continuous with $0 \le f(x) \le 1$ for every $x \in [0,1]$. Prove that there is $c \in [0,1]$ with $f(c) = c$.
6. Let $p(x) = x^3 + \alpha x^2 + \beta x + \gamma$ with real $\alpha, \beta, \gamma$, and let $R = 1 + \lvert \alpha \rvert + \lvert \beta \rvert + \lvert \gamma \rvert$. Prove that $p(R) \gt 0$ and $p(-R) \lt 0$, and conclude that $p$ has a zero in $[-R, R]$.
7. Let $n \in \mathbb{N}$. (a) Prove that $(ab)^{1/n} = a^{1/n} b^{1/n}$ for all $a, b \ge 0$. (b) Prove that $0 \le a \lt b$ implies $a^{1/n} \lt b^{1/n}$.

*Extend*

8. Let $n \in \mathbb{N}$. (a) Prove that $(s + v)^n \ge s^n + v^n$ for all $s, v \ge 0$. (b) Deduce that $\lvert a^{1/n} - b^{1/n} \rvert \le \lvert a - b \rvert^{1/n}$ for all $a, b \ge 0$. (c) Deduce that $x \mapsto x^{1/n}$ is continuous on $[0, \infty)$.

Solutions: [solutions/007-continuous-functions.md](../solutions/007-continuous-functions.md).
