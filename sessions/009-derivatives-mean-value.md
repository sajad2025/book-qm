# Session 9. Derivatives and the mean value theorem

*Theorem. Builds on Sessions 7 and 8.*

**Claim.** The derivative obeys the sum, product, quotient and chain rules, an interior extremum of a differentiable function has $f' = 0$, and Rolle's theorem and the mean value theorem follow, so $f' = 0$ on an interval forces $f$ to be constant and $f' \ge 0$ forces $f$ to be nondecreasing.

The session defines the derivative as a limit of difference quotients and proves each part of the claim in turn. Every limit is computed through sequences, by Session 8, so that every step reduces to the rules for limits of sequences in Session 5. The route follows W. Rudin, *Principles of Mathematical Analysis*, 3rd ed., Ch. 5.

## 9.1 Recall

**Induction and powers (Session 3).** Proof by induction (Section 3.2). The laws of powers (Section 3.6): $x^0 = 1$, $x^{m+n} = x^m x^n$, $x^n \gt 0$ when $x \gt 0$, and $x^n \lt y^n$ when $0 \le x \lt y$ and $n \in \mathbb{N}$. The difference of powers (Section 3.7): $u^n - v^n = (u - v)\sum_{j=0}^{n-1} u^{n-1-j} v^j$.

**Order (Session 4).** Every square is nonnegative (Section 4.3(d)), and if $0 \lt u \le v$ then $0 \lt 1/v \le 1/u$ (Section 4.3(e)). The Archimedean property (Section 4.7): for every real $t$ there is a natural number $N \gt t$.

**Intervals (Session 7).** An interval is a set $I \subseteq \mathbb{R}$ with at least two points such that $u, w \in I$ and $u \lt v \lt w$ imply $v \in I$. Examples are $[a,b]$, $(a,b)$, $[a,b)$ and $(a,b]$ for $a \lt b$, and $\mathbb{R}$ (Session 7, Section 7.2).

For real $a$ and $b$, the **half-lines** $[a, \infty) = \{x \in \mathbb{R} : x \ge a\}$, $(a, \infty) = \{x \in \mathbb{R} : x \gt a\}$, $(-\infty, b] = \{x \in \mathbb{R} : x \le b\}$ and $(-\infty, b) = \{x \in \mathbb{R} : x \lt b\}$ are intervals too. Each has at least two points, such as $a + 1 \lt a + 2$ or $b - 2 \lt b - 1$. If $u, w \in [a, \infty)$ and $u \lt v \lt w$, then $a \le u \lt v$, so $v \in [a, \infty)$. If $u, w \in (-\infty, b]$ and $u \lt v \lt w$, then $v \lt w \le b$. The half-lines $(a, \infty)$ and $(-\infty, b)$ are checked in the same way with strict inequalities.

**Limits of functions (Session 8).** Let $D \subseteq \mathbb{R}$, let $g : D \to \mathbb{R}$, and let $x$ be an accumulation point of $D$: for every $\delta \gt 0$ some $y \in D$ has $0 \lt \lvert y - x \rvert \lt \delta$. Then $g(y)$ tends to $L$ as $y$ tends to $x$ if for every $\varepsilon \gt 0$ there exists $\delta \gt 0$ such that $\lvert g(y) - L \rvert \lt \varepsilon$ for every $y \in D$ with $0 \lt \lvert y - x \rvert \lt \delta$. Session 8 proves that there is at most one such $L$, written $\lim_{y \to x} g(y)$, and that $g(y)$ tends to $L$ if and only if $g(y_n) \to L$ for every sequence $(y_n)$ of points of $D$ with $y_n \ne x$ and $y_n \to x$ (the sequential criterion). It also proves that a function $f$ on $D$, with $x \in D$, is continuous at $x$ if and only if $\lim_{y \to x} f(y) = f(x)$.

Session 8 (Lemma 2) also shows that every point $x$ of an interval $I$ is an accumulation point of $I$. The points it supplies differ from $x$, so $x$ is also an accumulation point of $I \setminus \{x\}$. So the definition, the sequential criterion and the uniqueness of the limit all apply to a function defined on $I$ or on $I \setminus \{x\}$.

**Continuity (Session 7).** A function $f : I \to \mathbb{R}$ is continuous at $x$ if and only if $f(x_n) \to f(x)$ for every sequence $(x_n)$ in $I$ with $x_n \to x$. Here the terms $x_n$ may equal $x$. Constant functions, the identity and the absolute value are continuous on $\mathbb{R}$. Sums, constant multiples, products and quotients (with nonzero denominator) of functions continuous at $x$ are continuous at $x$ (the algebra of continuous functions), and so is the restriction of a function continuous at $x$ to a subset containing $x$. A function continuous on $[a,b]$ has a minimum point $p$ and a maximum point $q$: $f(p) \le f(y) \le f(q)$ for every $y \in [a,b]$ (the extreme value theorem). Every $a \ge 0$ has a unique square root $\sqrt{a} \ge 0$. If $n \in \mathbb{N}$, $u, v \ge 0$ and $u^n \le v^n$, then $u \le v$ (Section 7.8, corollary). A function $f : I \to \mathbb{R}$ is nondecreasing if $x \lt y$ in $I$ implies $f(x) \le f(y)$, nonincreasing if $x \lt y$ in $I$ implies $f(x) \ge f(y)$, and strictly increasing if $x \lt y$ in $I$ implies $f(x) \lt f(y)$.

**Sequences (Sessions 5 and 7).** A constant sequence converges to its value. Limits of sequences are unique, convergent sequences are bounded, and if $a_n \to a$ and $b_n \to b$ then $a_n + b_n \to a + b$, $a_n b_n \to ab$, and $a_n / b_n \to a / b$ when $b \ne 0$ and every $b_n \ne 0$. If $a_n \le b_n$ for every $n$, then $a \le b$. The squeeze rule holds. The test for convergence (Session 7): if $K \ge 0$ and $\lvert x_n - x \rvert \le K/n$ for every $n \in \mathbb{N}$, then $x_n \to x$.

## 9.2 The derivative

Let $I$ be an interval, $f : I \to \mathbb{R}$ and $x \in I$. The **difference quotient** of $f$ at $x$ is the function

$$
q_x(y) = \frac{f(y) - f(x)}{y - x}, \qquad y \in I, \ y \ne x .
$$

It is the slope of the line through the points $(x, f(x))$ and $(y, f(y))$ of the graph.

**Definition.** The function $f$ is **differentiable at** $x$ if $\lim_{y \to x} q_x(y)$ exists. The limit is the **derivative** of $f$ at $x$, written $f'(x)$. If $f$ is differentiable at every point of a set $S \subseteq I$, it is **differentiable on** $S$, and $x \mapsto f'(x)$ is the function $f'$ on $S$.

If $x$ is the minimum or the maximum of $I$ (Session 4, Section 4.4), as $a$ and $b$ are for $[a,b]$, every $y \in I$ with $y \ne x$ lies on one side of $x$, and the definition uses only those $y$. No separate one-sided definition is needed.

**The derivative is well defined.** By Section 9.1, $x$ is an accumulation point of $I \setminus \{x\}$, the domain of $q_x$, so the limit, when it exists, is unique (Session 8).

**How limits are computed here.** To show $f'(x) = L$, it is enough by the sequential criterion (Session 8) to take an arbitrary sequence $(y_n)$ in $I$ with $y_n \ne x$ and $y_n \to x$, and show $q_x(y_n) \to L$. Every proof below has this form.

**Example (constants and the identity).** If $f(y) = c$ for every $y$, then $q_x(y) = 0$ for every $y \ne x$, so $f'(x) = 0$. If $f(y) = y$, then $q_x(y) = (y - x)/(y - x) = 1$, so $f'(x) = 1$. If $f(y) = -y$, then $q_x(y) = (-y + x)/(y - x) = -1$, so $f'(x) = -1$.

**Example (the absolute value at 0).** Let $f(y) = \lvert y \rvert$ on $\mathbb{R}$ and $x = 0$. Then $q_0(y) = \lvert y \rvert / y$, which is $1$ for $y \gt 0$ and $-1$ for $y \lt 0$. The sequences $1/(n+1)$ and $-1/(n+1)$ are nonzero and tend to $0$ by the test for convergence (Session 7) with $K = 1$, since $1/(n+1) \lt 1/n$. They give $q_0 = 1$ and $q_0 = -1$ at every term. If $f'(0) = L$ existed, the sequential criterion (Session 8) would give $1 \to L$ and $-1 \to L$, so $L = 1$ and $L = -1$ (Session 5). So $\lvert y \rvert$ is not differentiable at $0$. It is continuous at $0$, since the absolute value is continuous on $\mathbb{R}$ (Session 7, the lemma on three continuous functions). So continuity does not imply differentiability. The converse does hold.

**Lemma 1 (differentiable implies continuous).** If $f$ is differentiable at $x$, then $f$ is continuous at $x$.

*Proof.* Let $(y_n)$ be a sequence in $I$ with $y_n \ne x$ and $y_n \to x$. Since $y_n \ne x$,

$$
f(y_n) = f(x) + q_x(y_n)  (y_n - x) .
$$

By Session 8, $q_x(y_n) \to f'(x)$. By Session 5, $y_n - x \to 0$, so $q_x(y_n)(y_n - x) \to f'(x) \cdot 0 = 0$, and $f(y_n) \to f(x)$. By Session 8 this says $\lim_{y \to x} f(y) = f(x)$, which by Session 8 means $f$ is continuous at $x$. ∎

Two facts about domains are needed when a function is studied on a smaller interval, or when it is given by different formulas on different pieces.

**Lemma 2 (restriction and locality).** Let $f : I \to \mathbb{R}$ and $x \in I$.

1. Let $J \subseteq I$ be an interval with $x \in J$. If $f$ is continuous at $x$, so is its restriction $f|_J$ to $J$ (Session 7, Section 7.4), the function $J \to \mathbb{R}$ with the same values as $f$. If $f$ is differentiable at $x$, so is $f|_J$, with the same derivative.
2. Let $g : I \to \mathbb{R}$, and suppose there is $r \gt 0$ with $g(y) = f(y)$ for every $y \in I$ with $\lvert y - x \rvert \lt r$. If $f$ is differentiable at $x$, so is $g$, and $g'(x) = f'(x)$.

*Proof.* 1. The statement about continuity is in Session 7. For the derivative, the difference quotient of $f|_J$ at $x$ is $q_x$ restricted to $J \setminus \{x\}$. A sequence $(y_n)$ in $J$ with $y_n \ne x$ and $y_n \to x$ is such a sequence in $I$, so Session 8 applied to $f$ gives $q_x(y_n) \to f'(x)$. Since this holds for every such sequence, Session 8 applied to $f|_J$ gives $(f|_J)'(x) = f'(x)$.

2. Taking $y = x$ gives $g(x) = f(x)$. Write $p_x$ for the difference quotient of $g$ at $x$. Let $(y_n)$ be a sequence in $I$ with $y_n \ne x$ and $y_n \to x$. By the definition of convergence with $\varepsilon = r$, there is $N$ with $\lvert y_n - x \rvert \lt r$ for $n \ge N$. For those $n$, $g(y_n) = f(y_n)$ and so $p_x(y_n) = q_x(y_n)$. Now let $\varepsilon \gt 0$. Since $q_x(y_n) \to f'(x)$ (Session 8), there is $N'$ with $\lvert q_x(y_n) - f'(x) \rvert \lt \varepsilon$ for $n \ge N'$. For $n \ge \max\{N, N'\}$, $\lvert p_x(y_n) - f'(x) \rvert = \lvert q_x(y_n) - f'(x) \rvert \lt \varepsilon$. So $p_x(y_n) \to f'(x)$, and Session 8 gives $g'(x) = f'(x)$. ∎

Part 2 says the derivative at $x$ depends only on the values of $f$ near $x$. For example, let $x \gt 0$. If $\lvert y - x \rvert \lt x$, then $y \gt x - x = 0$, so $\lvert y \rvert = y$. By part 2 with $r = x$, the derivative of $\lvert y \rvert$ at $x$ is that of the identity, which is $1$. Let $x \lt 0$. If $\lvert y - x \rvert \lt -x$, then $y \lt x + (-x) = 0$, so $\lvert y \rvert = -y$. By part 2 with $r = -x$, the derivative of $\lvert y \rvert$ at $x$ is that of $y \mapsto -y$, which is $-1$.

## 9.3 The sum, product and quotient rules

**Theorem 1.** Let $f, g : I \to \mathbb{R}$ be differentiable at $x \in I$, and let $c$ be real. Then:

1. (sum rule) $f + g$ is differentiable at $x$ and $(f+g)'(x) = f'(x) + g'(x)$;
2. (product rule) $fg$ is differentiable at $x$ and $(fg)'(x) = f'(x) g(x) + f(x) g'(x)$;
3. (constant multiples) $cf$ is differentiable at $x$ and $(cf)'(x) = c f'(x)$;
4. (quotient rule) if $g(y) \ne 0$ for every $y \in I$, then $f/g$ is differentiable at $x$ and

$$
\left( \frac{f}{g} \right)'(x) = \frac{f'(x) g(x) - f(x) g'(x)}{g(x)^2} .
$$

*Proof.* Write $q_x$ and $p_x$ for the difference quotients of $f$ and $g$ at $x$. Throughout, $(y_n)$ is a sequence in $I$ with $y_n \ne x$ and $y_n \to x$. By Session 8, $q_x(y_n) \to f'(x)$ and $p_x(y_n) \to g'(x)$.

1. The difference quotient of $f + g$ at $y_n$ is

$$
\frac{f(y_n) + g(y_n) - f(x) - g(x)}{y_n - x} = q_x(y_n) + p_x(y_n) ,
$$

which tends to $f'(x) + g'(x)$ by Session 5.

2. Add and subtract $f(y_n) g(x)$ in the numerator:

$$
f(y_n) g(y_n) - f(x) g(x) = f(y_n) \bigl( g(y_n) - g(x) \bigr) + g(x) \bigl( f(y_n) - f(x) \bigr) .
$$

Dividing by $y_n - x$, the difference quotient of $fg$ at $y_n$ is

$$
f(y_n)  p_x(y_n) + g(x)  q_x(y_n) .
$$

By Lemma 1, $f$ is continuous at $x$, so $f(y_n) \to f(x)$ (Session 7). By Session 5 the expression tends to $f(x) g'(x) + g(x) f'(x)$.

3. Apply part 2 to the product of the constant function $y \mapsto c$ and $f$. The constant function has derivative $0$ (Section 9.2), so $(cf)'(x) = 0 \cdot f(x) + c f'(x) = c f'(x)$.

4. First take $f = 1$. The difference quotient of $1/g$ at $y_n$ is

$$
\frac{1}{y_n - x} \left( \frac{1}{g(y_n)} - \frac{1}{g(x)} \right) = \frac{g(x) - g(y_n)}{(y_n - x)  g(y_n)  g(x)} = - p_x(y_n) \cdot \frac{1}{g(y_n)  g(x)} .
$$

By Lemma 1 and Session 7, $g(y_n) \to g(x)$, so $g(y_n) g(x) \to g(x)^2$ by Session 5. Every term $g(y_n) g(x)$ is nonzero and so is the limit $g(x)^2$, so Session 5 gives $1/(g(y_n) g(x)) \to 1/g(x)^2$. Hence the difference quotient tends to $-g'(x)/g(x)^2$, and

$$
\left( \frac{1}{g} \right)'(x) = - \frac{g'(x)}{g(x)^2} .
$$

For general $f$, write $f/g = f \cdot (1/g)$ and apply part 2:

$$
\left( \frac{f}{g} \right)'(x) = \frac{f'(x)}{g(x)} + f(x) \cdot \left( - \frac{g'(x)}{g(x)^2} \right) = \frac{f'(x) g(x) - f(x) g'(x)}{g(x)^2} .
$$

∎

**Corollary 1 (powers and polynomials).** For every $n \in \mathbb{N}$ the function $x \mapsto x^n$ is differentiable on $\mathbb{R}$ with derivative $n x^{n-1}$, where $x^0 = 1$. Every polynomial $a_0 + a_1 x + \dots + a_m x^m$ is differentiable on $\mathbb{R}$ with derivative $a_1 + 2 a_2 x + \dots + m a_m x^{m-1}$.

*Proof.* By induction on $n$ (Session 3). For $n = 1$ the derivative of the identity is $1 = 1 \cdot x^0$ (Section 9.2). Suppose the derivative of $x^n$ is $n x^{n-1}$. Since $x^{n+1} = x \cdot x^n$, the product rule gives the derivative

$$
1 \cdot x^n + x \cdot n x^{n-1} = (n+1) x^n .
$$

For the polynomial, the term $a_k x^k$ has derivative $k a_k x^{k-1}$ by the first statement of this corollary and Theorem 1 part 3, and the derivative of $a_0$ is $0$. A sum of finitely many differentiable functions has, by Theorem 1 part 1 and induction on the number of terms (Session 3), the sum of their derivatives as its derivative. ∎

A rational function $p/q$ (Session 7, Section 7.4) is differentiable at every point of any interval on which $q$ has no zero, by Corollary 1, Lemma 2 part 1 and Theorem 1 part 4. Write $x^{-n}$ for $1/x^n$. On $(0, \infty)$, $x^n \gt 0^n = 0$ (Session 7, Section 7.8), so $x^{-n}$ has derivative

$$
\frac{0 \cdot x^n - 1 \cdot n x^{n-1}}{(x^n)^2} = - \frac{n x^{n-1}}{x^{n-1} x^{n+1}} = - \frac{n}{x^{n+1}} = - n x^{-n-1} ,
$$

since $(x^n)^2 = x^{2n} = x^{n-1} x^{n+1}$ (Session 3), and the factor $x^{n-1}$ cancels because $x^{n-1} \gt 0$ for $x \gt 0$ (Session 3, laws of powers (d)).

**Lemma 3 (the square root).** The function $s(x) = \sqrt{x}$ on $[0, \infty)$ is differentiable at every $x \gt 0$, with

$$
s'(x) = \frac{1}{2 \sqrt{x}} .
$$

It is not differentiable at $0$.

*Proof.* Let $x \gt 0$. Then $\sqrt{x} \gt 0$, since $\sqrt{x} = 0$ would give $x = 0^2 = 0$. For every $y \ge 0$, $(\sqrt{y})^2 = y$, so

$$
y - x = (\sqrt{y})^2 - (\sqrt{x})^2 = (\sqrt{y} - \sqrt{x})(\sqrt{y} + \sqrt{x}) .
$$

Since $\sqrt{y} \ge 0$, the factor $\sqrt{y} + \sqrt{x}$ is at least $\sqrt{x} \gt 0$. Dividing,

$$
\sqrt{y} - \sqrt{x} = \frac{y - x}{\sqrt{y} + \sqrt{x}} .
$$

Since $\sqrt{y} + \sqrt{x} \gt 0$, taking absolute values ($\lvert uv \rvert = \lvert u \rvert \lvert v \rvert$, and $\lvert s \rvert = s$ for $s \gt 0$, Session 5) gives $\lvert \sqrt{y} - \sqrt{x} \rvert = \lvert y - x \rvert / (\sqrt{y} + \sqrt{x}) \le \lvert y - x \rvert / \sqrt{x}$, because dividing $\lvert y - x \rvert \ge 0$ by the larger positive number $\sqrt{y} + \sqrt{x} \ge \sqrt{x}$ gives the smaller result (Session 4, Section 4.3(e)). For $y \ne x$,

$$
\frac{\sqrt{y} - \sqrt{x}}{y - x} = \frac{1}{\sqrt{y} + \sqrt{x}} .
$$

Let $(y_n)$ be a sequence in $[0, \infty)$ with $y_n \ne x$ and $y_n \to x$. Put $d_n = \lvert y_n - x \rvert / \sqrt{x}$. Since $\bigl\lvert \lvert y_n - x \rvert - 0 \bigr\rvert = \lvert y_n - x \rvert$, the definition of $y_n \to x$ (Session 5) says $\lvert y_n - x \rvert \to 0$, and the product rule with the constant $1/\sqrt{x}$ gives $d_n \to 0$. Since $\lvert \sqrt{y_n} - \sqrt{x} \rvert \le d_n$, the corollary of the squeeze rule (Session 5, Section 5.9) gives $\sqrt{y_n} \to \sqrt{x}$. Then $\sqrt{y_n} + \sqrt{x} \to 2 \sqrt{x} \ne 0$, every term is nonzero, and by Session 5 the difference quotient tends to $1/(2\sqrt{x})$. Session 8 gives $s'(x) = 1/(2\sqrt{x})$.

At $x = 0$ the difference quotient is $\sqrt{y}/y = 1/\sqrt{y}$ for $y \gt 0$. Let $y_n = 1/(n+1)^2$. Since $n + 1 \ge 1$, $(n+1)^2 = (n+1)(n+1) \ge n + 1 \gt n$, so $0 \lt y_n \lt 1/n$ (Session 4), and $y_n \to 0$ by the test for convergence (Session 7) with $K = 1$. Its quotients are $1/\sqrt{y_n} = n + 1$, since $1/(n+1) \ge 0$ and its square is $y_n$. The sequence $(n+1)$ is not bounded, by the Archimedean property, so it does not converge (Session 5). By Session 8 the difference quotient has no limit at $0$. ∎

The $n$-th root is treated the same way in Exercise 4.

## 9.4 The chain rule

**Theorem 2 (chain rule).** Let $I$ and $J$ be intervals, $f : I \to \mathbb{R}$ with $f(I) \subseteq J$, and $g : J \to \mathbb{R}$. If $f$ is differentiable at $x$ and $g$ is differentiable at $u = f(x)$, then $g \circ f$ is differentiable at $x$ and

$$
(g \circ f)'(x) = g'(f(x))  f'(x) .
$$

The tempting proof writes the difference quotient of $g \circ f$ as

$$
\frac{g(f(y)) - g(f(x))}{f(y) - f(x)} \cdot \frac{f(y) - f(x)}{y - x}
$$

and lets $y \to x$. This divides by zero whenever $f(y) = f(x)$, and for a constant $f$ that happens at every $y$. The proof below avoids the division by giving the first factor a value at $u$.

*Proof.* Define $\varphi : J \to \mathbb{R}$ by

$$
\varphi(v) = \frac{g(v) - g(u)}{v - u} \quad (v \ne u), \qquad \varphi(u) = g'(u) .
$$

*Step 1.* For every $v \in J$,

$$
g(v) - g(u) = \varphi(v)  (v - u) .
$$

For $v \ne u$ this is the definition of $\varphi(v)$ multiplied by $v - u$. For $v = u$ both sides are $0$.

*Step 2.* $\varphi$ is continuous at $u$. Let $(v_n)$ be a sequence in $J$ with $v_n \ne u$ and $v_n \to u$. Each $\varphi(v_n)$ is the difference quotient of $g$ at $u$, evaluated at $v_n$, so $\varphi(v_n) \to g'(u)$ (Session 8). By the sequential criterion (Session 8), $\lim_{v \to u} \varphi(v) = g'(u) = \varphi(u)$, and by Session 8, $\varphi$ is continuous at $u$.

*Step 3.* Let $(y_n)$ be a sequence in $I$ with $y_n \ne x$ and $y_n \to x$. Put $v = f(y_n)$ in Step 1 and divide by $y_n - x \ne 0$:

$$
\frac{g(f(y_n)) - g(f(x))}{y_n - x} = \varphi(f(y_n)) \cdot \frac{f(y_n) - f(x)}{y_n - x} .
$$

By Lemma 1, $f$ is continuous at $x$, so $f(y_n) \to f(x) = u$ (Session 7). The terms $f(y_n)$ lie in $J$, and some of them may equal $u$; Session 7 allows this. Since $\varphi$ is continuous at $u$ (Step 2), Session 7 gives $\varphi(f(y_n)) \to \varphi(u) = g'(u)$. The second factor tends to $f'(x)$ by Session 8. By Session 5 the product tends to $g'(u) f'(x)$, and Session 8 gives the theorem. ∎

**Example.** Let $h(x) = \sqrt{1 + x^2}$ on $\mathbb{R}$. Take $f(x) = 1 + x^2$, $J = (0, \infty)$ and $g(v) = \sqrt{v}$ for $v \in J$. Since $x^2 \ge 0$, $f(x) \ge 1$, so $f(\mathbb{R}) \subseteq J$. By Corollary 1, $f'(x) = 2x$. By Lemma 3 and Lemma 2 part 1, $g$ is differentiable at every $v \in J$ with $g'(v) = 1/(2\sqrt{v})$. By Theorem 2,

$$
h'(x) = \frac{1}{2\sqrt{1 + x^2}} \cdot 2x = \frac{x}{\sqrt{1 + x^2}} .
$$

## 9.5 Interior extrema

**Definition.** Let $f : I \to \mathbb{R}$ and $x \in I$. The function $f$ has a **local maximum** at $x$ if there is $r \gt 0$ with $f(y) \le f(x)$ for every $y \in I$ with $\lvert y - x \rvert \lt r$. It has a **local minimum** at $x$ if the same holds with $f(y) \ge f(x)$. A **local extremum** is a local maximum or a local minimum. The point $x$ is an **interior point** of $I$ if there is $r \gt 0$ with $(x - r, x + r) \subseteq I$. A point $x$ with $f'(x) = 0$ is a **stationary point** of $f$.

**Lemma 4 (interior points).** Let $I$ be an interval.

1. If $u, w \in I$ and $u \lt c \lt w$, then $c$ is an interior point of $I$.
2. A minimum or a maximum of $I$ (Session 4, Section 4.4) is not an interior point of $I$.

So the interior points of $[a,b]$ are the points of $(a,b)$, and those of $[a, \infty)$ are the $c \gt a$ (for such $c$, apply part 1 with $u = a$ and $w = 2c - a \gt c$). In the same way the interior points of $(-\infty, b]$ are the $c \lt b$ (use $u = 2c - b$ and $w = b$). Every real $c$ is an interior point of $\mathbb{R}$, with $r = 1$.

*Proof.* 1. Let $r = \min\{c - u, w - c\} \gt 0$. If $\lvert v - c \rvert \lt r$, then $v \gt c - r \ge c - (c - u) = u$ and $v \lt c + r \le c + (w - c) = w$, so $u \lt v \lt w$ and $v \in I$ by the definition of an interval. Hence $(c - r, c + r) \subseteq I$.

2. Let $a$ be the minimum of $I$ and let $r \gt 0$. The point $a - r/2$ lies in $(a - r, a + r)$, but it is less than $a$, so it is not in $I$. No $r$ works. For a maximum $b$, use $b + r/2$ in the same way. ∎

**Theorem 3 (interior extremum).** Let $x$ be an interior point of $I$, and let $f : I \to \mathbb{R}$ be differentiable at $x$. If $f$ has a local extremum at $x$, then $f'(x) = 0$.

The result is called Fermat's theorem on stationary points, after P. de Fermat's method of maxima and minima, *Methodus ad disquirendam maximam et minimam* (circulated in manuscript in 1636, printed in his *Varia opera mathematica*, Toulouse, 1679).

*Proof.* Suppose first that $f$ has a local maximum at $x$. Take $r_1 \gt 0$ with $f(y) \le f(x)$ for $y \in I$ with $\lvert y - x \rvert \lt r_1$, and $r_2 \gt 0$ with $(x - r_2, x + r_2) \subseteq I$. Let $r = \min\{r_1, r_2\}$. Put

$$
y_n = x + \frac{r}{n+1}, \qquad z_n = x - \frac{r}{n+1} .
$$

Since $0 \lt r/(n+1) \lt r$, both $y_n$ and $z_n$ lie in $(x - r, x + r)$, which is contained in $(x - r_2, x + r_2) \subseteq I$ because $r \le r_2$, and both differ from $x$. Since $\lvert y_n - x \rvert = \lvert z_n - x \rvert = r/(n+1) \lt r/n$, both tend to $x$ by the test for convergence (Session 7) with $K = r$. Since $\lvert y_n - x \rvert = \lvert z_n - x \rvert \lt r \le r_1$, the choice of $r_1$ gives $f(y_n) \le f(x)$ and $f(z_n) \le f(x)$.

At $y_n$ the numerator $f(y_n) - f(x)$ is $\le 0$ and the denominator $r/(n+1)$ is $\gt 0$, so

$$
\frac{f(y_n) - f(x)}{y_n - x} \le 0 .
$$

These quotients tend to $f'(x)$ (Session 8), so $f'(x) \le 0$ by Session 5. At $z_n$ the numerator is $\le 0$ and the denominator $-r/(n+1)$ is $\lt 0$, so the quotients are $\ge 0$, and Session 5 gives $f'(x) \ge 0$. Hence $f'(x) = 0$.

If $f$ has a local minimum at $x$, then $-f$ has a local maximum at $x$, and by Theorem 1 part 3, $-f'(x) = (-f)'(x) = 0$. ∎

**What fails.** Each hypothesis is needed, and the converse is false.

- *Interior.* On $I = [0, 1]$ the identity has a maximum at the endpoint $1$, but its derivative there is $1$.
- *Differentiable.* The absolute value has a minimum at $0$, an interior point of $\mathbb{R}$, but no derivative there (Section 9.2).
- *The converse.* Let $f(x) = x^3$. By Corollary 1, $f'(0) = 3 \cdot 0^2 = 0$. But $f$ has no local extremum at $0$. Let $r \gt 0$. The points $r/2$ and $-r/2$ satisfy $\lvert y - 0 \rvert = r/2 \lt r$, and $f(r/2) = r^3/8 \gt 0 = f(0)$ while $f(-r/2) = -r^3/8 \lt 0$. So no $r$ works for a local maximum or a local minimum. A stationary point need not be an extremum.

## 9.6 Rolle's theorem and the mean value theorem

**Theorem 4 (Rolle's theorem).** Let $a \lt b$, and let $f : [a,b] \to \mathbb{R}$ be continuous on $[a,b]$ and differentiable at every point of $(a,b)$. If $f(a) = f(b)$, there is $c \in (a,b)$ with $f'(c) = 0$.

*Proof.* By the extreme value theorem (Session 7) there are $p, q \in [a,b]$ with

$$
f(p) \le f(y) \le f(q) \qquad \text{for every } y \in [a,b] .
$$

*Case 1: $q \in (a,b)$.* By Lemma 4 part 1, $q$ is an interior point of $[a,b]$. The inequality $f(y) \le f(q)$ holds for every $y \in [a,b]$, so $f$ has a local maximum at $q$, with any $r \gt 0$. By Theorem 3, $f'(q) = 0$. Take $c = q$.

*Case 2: $p \in (a,b)$.* The same argument with a local minimum at $p$ gives $f'(p) = 0$. Take $c = p$.

*Case 3: both $p$ and $q$ lie in $\{a, b\}$.* Since $f(a) = f(b)$, both $f(p)$ and $f(q)$ equal $f(a)$. The displayed inequality becomes $f(a) \le f(y) \le f(a)$, so $f(y) = f(a)$ for every $y \in [a,b]$. A constant function has derivative $0$ (Section 9.2). Take $c = (a+b)/2$, which lies in $(a,b)$ because $a \lt b$ gives $2a \lt a + b \lt 2b$. ∎

The result is named after M. Rolle, who proved a version of it for polynomials, without derivatives, in *Démonstration d'une méthode pour résoudre les égalitez de tous les degrez* (Paris, 1691).

**Theorem 5 (mean value theorem).** Let $a \lt b$, and let $f : [a,b] \to \mathbb{R}$ be continuous on $[a,b]$ and differentiable at every point of $(a,b)$. Then there is $c \in (a,b)$ with

$$
f(b) - f(a) = f'(c)  (b - a) .
$$

In words: the slope of the chord from $(a, f(a))$ to $(b, f(b))$ equals the slope $f'(c)$ at some point strictly between. The mean value theorem appears in J.-L. Lagrange, *Théorie des fonctions analytiques* (Paris, 1797), and is also called Lagrange's mean value theorem.

*Proof.* Let $m = (f(b) - f(a))/(b - a)$ be the slope of the chord, and subtract the chord from $f$:

$$
g(y) = f(y) - f(a) - m (y - a), \qquad y \in [a,b] .
$$

Then $g(a) = 0$, and

$$
g(b) = f(b) - f(a) - \frac{f(b) - f(a)}{b - a} (b - a) = 0 .
$$

The line $y \mapsto f(a) + m(y - a)$ is a polynomial, so by Corollary 1 it is differentiable on $\mathbb{R}$ with derivative $m$. By Lemma 1 and Lemma 2 part 1, its restriction to $[a,b]$ is continuous on $[a,b]$ and has derivative $m$ at every point of $(a,b)$. By the algebra of continuous functions (Session 7), $g$ is continuous on $[a,b]$. By Theorem 1 parts 1 and 3, $g$ is differentiable at every $c \in (a,b)$ with

$$
g'(c) = f'(c) - m .
$$

Rolle's theorem (Theorem 4) gives $c \in (a,b)$ with $g'(c) = 0$, that is $f'(c) = m$. Multiplying by $b - a$ gives the theorem. ∎

**What fails.** Rolle's theorem needs both hypotheses.

- *Differentiable inside.* Let $f(x) = \lvert x \rvert$ on $[-1, 1]$. It is continuous and $f(-1) = f(1) = 1$. By Section 9.2 and Lemma 2 part 1, its derivative is $1$ at every $c \in (0, 1)$ and $-1$ at every $c \in (-1, 0)$. It has no derivative at $0$: the sequences $1/(n+1)$ and $-1/(n+1)$ of Section 9.2 lie in $[-1, 1]$ and give difference quotients $1$ and $-1$, so the argument there applies unchanged (Session 8). No $c$ has $f'(c) = 0$.
- *Continuous at the ends.* Let $f(x) = x$ for $0 \le x \lt 1$ and $f(1) = 0$. Then $f(0) = f(1) = 0$. For $c \in (0, 1)$, every $y \in [0,1]$ with $\lvert y - c \rvert \lt 1 - c$ has $y \lt c + (1 - c) = 1$, so $f(y) = y$, and by Lemma 2 part 2, $f'(c) = 1$. No $c$ has $f'(c) = 0$. Here $f$ is not continuous at $1$: the sequence $1 - 1/(n+1)$ lies in $[0, 1)$ and tends to $1$ by the test for convergence (Session 7) with $K = 1$, but $f$ of it is the same sequence, which tends to $1 \ne 0 = f(1)$ (Session 7).

## 9.7 What the sign of the derivative says

**Theorem 6.** Let $I$ be an interval, and let $f : I \to \mathbb{R}$ be continuous on $I$ and differentiable at every interior point of $I$.

1. If $f'(c) = 0$ for every interior point $c$ of $I$, then $f$ is constant on $I$.
2. If $f'(c) \ge 0$ for every interior point $c$ of $I$, then $f$ is nondecreasing on $I$: $x \lt y$ in $I$ implies $f(x) \le f(y)$.
3. If $f'(c) \le 0$ for every interior point $c$ of $I$, then $f$ is nonincreasing on $I$: $x \lt y$ in $I$ implies $f(x) \ge f(y)$.

*Proof.* Let $x \lt y$ be points of $I$. Since $I$ is an interval, $[x,y] \subseteq I$. By Lemma 4 part 1, every $c$ with $x \lt c \lt y$ is an interior point of $I$. By Lemma 2 part 1, the restriction of $f$ to $[x,y]$ is continuous on $[x,y]$ and differentiable at every $c \in (x,y)$, with derivative $f'(c)$. The mean value theorem (Theorem 5) gives $c \in (x,y)$ with

$$
f(y) - f(x) = f'(c)  (y - x) .
$$

Here $y - x \gt 0$.

1. $f'(c) = 0$, so $f(y) = f(x)$. Any two points of $I$ are equal or can be named so that $x \lt y$, so $f$ takes one value on $I$.
2. $f'(c) \ge 0$ and $y - x \gt 0$, so $f(y) - f(x) \ge 0$.
3. $f'(c) \le 0$ and $y - x \gt 0$, so $f(y) - f(x) \le 0$. ∎

**Corollary 2.** If $f, g : I \to \mathbb{R}$ are continuous on $I$, differentiable at every interior point, and $f'(c) = g'(c)$ at every interior point $c$, then $f - g$ is constant on $I$.

*Proof.* The function $f - g$ is continuous on $I$ by the algebra of continuous functions (Session 7), and by Theorem 1 parts 1 and 3 its derivative at every interior point is $f'(c) - g'(c) = 0$. Theorem 6 part 1 finishes. ∎

**What fails.** Each example below breaks the hypotheses at a single point.

*An interior point without a derivative.* Let $H(x) = 0$ for $-1 \le x \lt 0$ and $H(x) = 1$ for $0 \le x \le 1$. By Lemma 4 the interior points of $[-1, 1]$ are the points of $(-1, 1)$. Let $c \in (-1, 0)$. Every $y \in [-1,1]$ with $\lvert y - c \rvert \lt -c$ has $y \lt c + (-c) = 0$, so $H(y) = 0$. Let $c \in (0, 1)$. Every $y \in [-1,1]$ with $\lvert y - c \rvert \lt c$ has $y \gt c - c = 0$, so $H(y) = 1$. By Lemma 2 part 2, $H'(c) = 0$ at every interior point except $0$. Yet $H$ is not constant. At $0$ it is not continuous: the sequence $-1/(n+1)$ tends to $0$ (Section 9.2) while $H$ of it is $0 \ne 1 = H(0)$ (Session 7). So by Lemma 1 it is not differentiable at $0$ either. So $H$ breaks both hypotheses at $0$, and the proof of Theorem 6 breaks for $x = -1/2$ and $y = 1/2$: the mean value theorem does not apply on $[-1/2, 1/2]$. Breaking only the derivative condition at one interior point is not enough: if $f$ is continuous on $[-1,1]$ and $f'(c) = 0$ for every $c \in (-1,1)$ with $c \ne 0$, then by Lemma 2 part 1, Theorem 6 part 1 applies on $[-1,0]$ and on $[0,1]$, whose interior points are those of $(-1,0)$ and $(0,1)$ (Lemma 4), and gives $f(y) = f(0)$ for every $y$ in either, so $f$ is constant.

*Continuity at an end.* Let $G(x) = 0$ for $0 \le x \lt 1$ and $G(1) = 1$ on $I = [0,1]$. Let $c \in (0,1)$. Every $y \in [0,1]$ with $\lvert y - c \rvert \lt 1 - c$ has $y \lt c + (1 - c) = 1$, so $G(y) = 0$, and $G'(c) = 0$ by Lemma 2 part 2. So $G' = 0$ at every interior point, yet $G(0) = 0 \ne 1 = G(1)$. Here $G$ is not continuous at $1$: the sequence $1 - 1/(n+1)$ tends to $1$ (Section 9.6), while $G$ of it is $0 \ne G(1)$ (Session 7). At interior points continuity follows from differentiability (Lemma 1), so an end is the only place where it can fail.

## 9.8 Worked example

Let $f(x) = \dfrac{x}{1 + x^2}$ on $\mathbb{R}$. The example finds its largest value with Theorems 1, 3 and 6, checks the answer by algebra, and then finds the point promised by the mean value theorem on $[0, 1]$.

**The derivative.** Since $x^2 \ge 0$, $1 + x^2 \ge 1 \gt 0$ for every $x$, so the quotient rule (Theorem 1 part 4) applies on $I = \mathbb{R}$. The numerator has derivative $1$ and the denominator $2x$ (Corollary 1). So

$$
f'(x) = \frac{1 \cdot (1 + x^2) - x \cdot 2x}{(1 + x^2)^2} = \frac{1 - x^2}{(1 + x^2)^2} = \frac{(1 - x)(1 + x)}{(1 + x^2)^2} .
$$

The denominator is positive, so the sign of $f'(x)$ is the sign of $(1 - x)(1 + x)$.

**The signs.**
- For $-1 \le x \le 1$: $1 - x \ge 0$ and $1 + x \ge 0$, so $f'(x) \ge 0$.
- For $x \ge 1$: $1 - x \le 0$ and $1 + x \ge 2 \gt 0$, so $f'(x) \le 0$.

**Monotonicity.** The function $f$ is differentiable on $\mathbb{R}$, so by Lemma 1 and Lemma 2 part 1 its restriction to any interval is continuous there, with the same derivative at each point. By Lemma 4 the interior points of $[-1, 1]$ are the points of $(-1, 1)$, and those of $[1, \infty)$ are the $c \gt 1$. Theorem 6 gives:
- on $[-1, 1]$, $f' \ge 0$ at the interior points, so $f$ is nondecreasing;
- on $[1, \infty)$, $f' \le 0$ at the interior points, so $f$ is nonincreasing.

**The largest value.** $f(1) = 1/2$. For $x \in [-1, 1]$, $x \le 1$ and $f$ is nondecreasing there, so $f(x) \le f(1)$. For $x \ge 1$, $f$ is nonincreasing there, so $f(x) \le f(1)$. For $x \le -1$, $x \lt 0$ and $1 + x^2 \gt 0$, so $f(x) \lt 0 \lt 1/2$. Hence

$$
\frac{x}{1 + x^2} \le \frac{1}{2} \qquad \text{for every real } x ,
$$

with equality at $x = 1$. The point $1$ is interior to $\mathbb{R}$ and a maximum, and indeed $f'(1) = 0$, as Theorem 3 requires.

**A check by algebra.** Multiplying by $2(1 + x^2) \gt 0$, the inequality is equivalent to $2x \le 1 + x^2$, that is $0 \le x^2 - 2x + 1 = (x - 1)^2$, which holds because squares are nonnegative. The two routes agree.

**The mean value point on $[0, 1]$.** The chord has slope

$$
\frac{f(1) - f(0)}{1 - 0} = \frac{1/2 - 0}{1} = \frac{1}{2} .
$$

Theorem 5 promises $c \in (0, 1)$ with $f'(c) = 1/2$. Find it. The equation is

$$
\frac{1 - c^2}{(1 + c^2)^2} = \frac{1}{2}, \qquad \text{that is} \qquad 2 - 2c^2 = 1 + 2c^2 + c^4 .
$$

Put $t = c^2$. Then $t^2 + 4t - 1 = 0$, so $(t + 2)^2 = t^2 + 4t + 4 = 5$. For $c \in (0, 1)$, $t + 2 \gt 0$, so $t + 2 = \sqrt{5}$ by the uniqueness of the nonnegative square root (Session 7), and

$$
t = \sqrt{5} - 2 .
$$

For $u, v \ge 0$, $u^2 \lt v^2$ implies $u \lt v$: the corollary in Section 7.8 (Session 7) gives $u \le v$ from $u^2 \le v^2$, and $u \ne v$ because $u^2 \ne v^2$. With $u = 2$, $v = \sqrt{5}$ and with $u = \sqrt{5}$, $v = 3$, the inequalities $4 \lt 5 \lt 9$ give $2 \lt \sqrt{5} \lt 3$, so $0 \lt t \lt 1$. Then $c = \sqrt{t}$ is positive, since $c = 0$ would give $t = 0$, and $c^2 = t \lt 1 = 1^2$ gives $c \lt 1$. Check: $1 + t = \sqrt{5} - 1$ and $1 - t = 3 - \sqrt{5}$, so

$$
(1 + t)^2 = 5 - 2\sqrt{5} + 1 = 6 - 2\sqrt{5} = 2(3 - \sqrt{5}) = 2(1 - t) ,
$$

which is the equation $2(1 - c^2) = (1 + c^2)^2$. The computation also shows that no other $c \in (0,1)$ works: any solution has $c^2 = \sqrt{5} - 2$ and $c \gt 0$. The theorem itself promises existence only.

## Exercises

*Check*

1. Compute the derivatives, naming the rule used at each step.
   (a) $p(x) = (x^2 + 1)(x^3 - 2x)$ on $\mathbb{R}$, once by the product rule and once by expanding first. Compare.
   (b) $r(x) = \dfrac{x - 1}{x + 1}$ on $(-1, \infty)$.
   (c) $h(x) = \sqrt{x^2 + x + 1}$ on $\mathbb{R}$. First show $x^2 + x + 1 \gt 0$ for every $x$.

2. Find every $c$ promised by the mean value theorem for
   (a) $f(x) = x^2$ on $[a, b]$, with $a \lt b$;
   (b) $f(x) = 1/x$ on $[1, 2]$.

3. Let $f(x) = x \lvert x \rvert$ on $\mathbb{R}$. Show that $f$ is differentiable at every $x$ with $f'(x) = 2 \lvert x \rvert$. Deduce that $f'$ is continuous at $0$ but not differentiable there.

*Prove*

4. Let $n \ge 2$ and let $r(x) = x^{1/n}$ on $[0, \infty)$ (Session 7). Show that for $x \gt 0$, $r$ is differentiable at $x$ with
   $$
   r'(x) = \frac{x^{1/n}}{n x} .
   $$
   Rerun the proof of Lemma 3, with the difference of powers $b^n - a^n = (b - a)(b^{n-1} + b^{n-2} a + \dots + a^{n-1})$ (Session 3, Section 3.7) in place of $y - x = (\sqrt{y} - \sqrt{x})(\sqrt{y} + \sqrt{x})$.

5. (a) Let $f$ be continuous on an interval $I$ with $f'(c) \gt 0$ at every interior point $c$. Show that $f$ is strictly increasing (Session 7): $x \lt y$ in $I$ implies $f(x) \lt f(y)$.
   (b) Show that $x \mapsto x^3$ is strictly increasing on $\mathbb{R}$, although its derivative vanishes at $0$. So the converse of (a) is false.

6. (Cauchy's mean value theorem.) Let $a \lt b$, and let $f, g$ be continuous on $[a, b]$ and differentiable at every point of $(a, b)$. Show that there is $c \in (a, b)$ with
   $$
   \bigl( f(b) - f(a) \bigr) g'(c) = \bigl( g(b) - g(a) \bigr) f'(c) .
   $$
   Apply Rolle's theorem to $h = \bigl( f(b) - f(a) \bigr) g - \bigl( g(b) - g(a) \bigr) f$. Check that $g(x) = x$ gives Theorem 5.

*Extend*

7. Session 3 proved Bernoulli's inequality $(1 + x)^n \ge 1 + nx$ for $x \ge -1$ and $n \in \mathbb{N}$ by induction. Prove it again with Theorem 6, by studying $h(x) = (1 + x)^n - 1 - nx$ on $[-1, 0]$ and on $[0, \infty)$.

8. (Darboux's theorem.) Let $a \lt b$ and let $f : [a,b] \to \mathbb{R}$ be differentiable at every point of $[a, b]$.
   (a) Show that if $f'(a) \lt \lambda \lt f'(b)$, there is $c \in (a, b)$ with $f'(c) = \lambda$. Use the minimum of $g(x) = f(x) - \lambda x$ on $[a, b]$.
   (b) Deduce that the function $H$ of Section 9.7 is not the derivative of any function on $[-1, 1]$. So a derivative on $[a,b]$ with $f'(a) \lt f'(b)$ takes every value strictly between them, which $H$, with only the values $0$ and $1$, does not.

Solutions: [solutions/009-derivatives-mean-value.md](../solutions/009-derivatives-mean-value.md).
