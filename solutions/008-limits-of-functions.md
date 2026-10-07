# Solutions to 1.8. Limits of functions at a point

Section numbers such as "Section 8.4" refer to Session 8.

## Check

**1.** **The bound.** Multiply out: $(y - 2)(y + 2) = y^2 + 2y - 2y - 4 = y^2 - 4$. So $\lvert y^2 - 4 \rvert = \lvert y - 2 \rvert \, \lvert y + 2 \rvert$.

Suppose $0 \lt \lvert y - 2 \rvert \lt 1$. Then $-1 \lt y - 2 \lt 1$ (Session 5), so $1 \lt y \lt 3$ and $3 \lt y + 2 \lt 5$. Since $y + 2 \gt 0$, $\lvert y + 2 \rvert = y + 2 \lt 5$. Since $\lvert y - 2 \rvert \gt 0$, multiplying gives

$$
\lvert y^2 - 4 \rvert = \lvert y - 2 \rvert \, \lvert y + 2 \rvert \lt 5 \lvert y - 2 \rvert .
$$

**The limit.** The point $2$ is an accumulation point of $\mathbb{R}$ by Lemma 2 of Section 8.2. Let $\varepsilon \gt 0$ and put $\delta = \min\{1, \varepsilon/5\}$, which is positive and at most $1$ and at most $\varepsilon/5$ (Section 8.1). Let $0 \lt \lvert y - 2 \rvert \lt \delta$. Then $\lvert y - 2 \rvert \lt 1$, so the bound applies:

$$
\lvert y^2 - 4 \rvert \lt 5 \lvert y - 2 \rvert \lt 5 \delta \le 5 \cdot \frac{\varepsilon}{5} = \varepsilon .
$$

So $\lim_{y \to 2} y^2 = 4$.

**The number.** For $\varepsilon = 0.01$, $\delta = \min\{1, 0.002\} = 0.002$. The point $y = 2.001$ has $\lvert y - 2 \rvert = 0.001$, which is positive and less than $0.002$. Then $y^2 = (2 + 0.001)^2 = 4 + 2 \cdot 2 \cdot 0.001 + 0.001^2 = 4 + 0.004 + 0.000001 = 4.004001$ and $\lvert y^2 - 4 \rvert = 0.004001$. This is less than $5 \lvert y - 2 \rvert = 0.005$, which is less than $0.01$.

**2.** **Accumulation point.** Let $\delta \gt 0$. The point $y = 4 + \delta/2$ satisfies $y \gt 4$, because $\delta/2 \gt 0$. So $y \ge 0$ and $y \neq 4$, that is, $y \in D$. Also $\lvert y - 4 \rvert = \delta/2$ is positive and less than $\delta$.

**Simplification.** Let $y \in D$ and write $s = \sqrt{y}$. By Session 7, $s \ge 0$ and $s^2 = y$. If $s = 2$, then $y = s^2 = 4$, which is excluded from $D$; so $s \neq 2$. Multiplying out, $(s - 2)(s + 2) = s^2 - 4 = y - 4$. Also $s + 2 \ge 2 \gt 0$. So

$$
f(y) = \frac{s - 2}{(s - 2)(s + 2)} = \frac{1}{s + 2} ,
$$

where the factor $s - 2$ cancels because it is nonzero.

**The bound.** Put the difference over a common denominator:

$$
f(y) - \frac14 = \frac{4 - (s + 2)}{4 (s + 2)} = \frac{2 - s}{4 (s + 2)} .
$$

Since $(2 - s)(2 + s) = 4 - s^2 = 4 - y$ and $2 + s \neq 0$, we have $2 - s = (4 - y)/(2 + s)$. Substituting,

$$
f(y) - \frac14 = \frac{4 - y}{4 (s + 2)^2} .
$$

From $s + 2 \ge 2 \gt 0$, multiplying the inequality by $s + 2$ and then by $2$ gives $(s + 2)^2 \ge 2(s + 2) \ge 4$. So $4 (s + 2)^2 \ge 16$. Since $4(s+2)^2 \gt 0$, Session 5, Section 5.2, Parts 2 and 4, give $\lvert f(y) - \tfrac14 \rvert = \lvert y - 4 \rvert / (4(s+2)^2)$. From $0 \lt 16 \le 4(s+2)^2$, the rule for reciprocals (Session 4, 4.3(e)) gives $1/(4(s+2)^2) \le 1/16$, and multiplying by $\lvert y - 4 \rvert \ge 0$ gives

$$
\Bigl\lvert f(y) - \frac14 \Bigr\rvert = \frac{\lvert y - 4 \rvert}{4 (s + 2)^2} \le \frac{\lvert y - 4 \rvert}{16} .
$$

**The limit.** Let $\varepsilon \gt 0$ and put $\delta = 16 \varepsilon$. If $y \in D$ and $0 \lt \lvert y - 4 \rvert \lt \delta$, then $\lvert f(y) - \tfrac14 \rvert \le \lvert y - 4 \rvert / 16 \lt \delta / 16 = \varepsilon$. So $\lim_{y \to 4} f(y) = 1/4$.

**3.** The point $1$ is an accumulation point of $\mathbb{R}$ by Lemma 2.

**Right of $1$.** Let $y_n = 1 + 1/n$. Then $y_n \neq 1$, and $\lvert y_n - 1 \rvert = 1/n$, so $y_n \to 1$ by the test for convergence (Session 7) with $K = 1$. Since $y_n \ge 1$, $f(y_n) = y_n + 1 = 2 + 1/n$. The constant sequence $2, 2, 2, \dots$ tends to $2$ and $1/n \to 0$ (Session 5), so the sum rule of Session 5 gives $f(y_n) \to 2$.

**Left of $1$.** Let $z_n = 1 - 1/n$. Then $z_n \neq 1$ and $\lvert z_n - 1 \rvert = 1/n$, so $z_n \to 1$ by the same test. Since $z_n \lt 1$,

$$
f(z_n) = 3 \Bigl(1 - \frac1n\Bigr)^2 = 3 \Bigl(1 - \frac2n + \frac1{n^2}\Bigr) = 3 - \frac6n + \frac3{n^2} .
$$

The constant sequences $6$ and $3$ converge to $6$ and $3$ (Session 5), so by the product rule of Session 5, $6/n = 6 \cdot (1/n) \to 6 \cdot 0 = 0$ and $3/n^2 = 3 \cdot (1/n)(1/n) \to 0$. By the sum rule, $f(z_n) \to 3 - 0 + 0 = 3$.

**No limit.** Suppose $\lim_{y \to 1} f(y) = L$. The sequential criterion (Section 8.4) applies to both sequences, so $f(y_n) \to L$ and $f(z_n) \to L$. A sequence has at most one limit (Session 5), so $L = 2$ and $L = 3$. That is impossible. So $f$ has no limit at $1$.

## Prove

**4.** (a) Lemma 1 gives a sequence $(y_n)$ in $D$ with $y_n \neq x$ for every $n$ and $y_n \to x$. By the sequential criterion, $f(y_n) \to L$ and $g(y_n) \to M$. Since $y_n \neq x$, the hypothesis gives $f(y_n) \le g(y_n)$ for every $n$. Limits of sequences respect non-strict inequalities (Session 5), so $L \le M$.

(b) Take $D = \mathbb{R}$, $x = 0$, $f(y) = 0$ and $g(y) = \lvert y \rvert$. For $y \neq 0$, $\lvert y \rvert \gt 0$, so $f(y) \lt g(y)$. The point $0$ is an accumulation point of $\mathbb{R}$ (Lemma 2). The constant $f$ tends to $0$ (Section 8.3). The absolute value is continuous at $0$ (Session 7, Section 7.2, Lemma (three continuous functions)), so Section 8.6 gives $\lim_{y \to 0} \lvert y \rvert = \lvert 0 \rvert = 0$. Here $L = M = 0$, so $L \lt M$ fails although $f(y) \lt g(y)$ for every $y \neq 0$.

**5.** (a) Let $(y_n)$ be a sequence in $D$ with $y_n \neq x$ for every $n$ and $y_n \to x$. By the sequential criterion, $f(y_n) \to L$ and $h(y_n) \to L$. Since $y_n \neq x$, $f(y_n) \le g(y_n) \le h(y_n)$ for every $n$. The squeeze rule for sequences (Session 5) gives $g(y_n) \to L$. The sequence was arbitrary, so the sequential criterion gives $\lim_{y \to x} g(y) = L$.

(b) Let $D = \mathbb{R} \setminus \{0\}$. The point $0$ is an accumulation point of $D$ (Example in Section 8.4). Put $f(y) = -y^2$, $g(y) = y \lvert y \rvert$ and $h(y) = y^2$. We check $f(y) \le g(y) \le h(y)$ for $y \in D$, by cases.

- If $y \gt 0$, then $\lvert y \rvert = y$ and $g(y) = y^2$. Since $y^2 \ge 0$, $-y^2 \le y^2 = g(y) = h(y)$.
- If $y \lt 0$, then $\lvert y \rvert = -y$ and $g(y) = -y^2$. Since $y^2 \ge 0$, $f(y) = -y^2 = g(y) \le y^2$.

The polynomials $-y^2$ and $y^2$ tend to their values at $0$, both $0$, by the corollary of Section 8.5. Part (a) gives $\lim_{y \to 0} y \lvert y \rvert = 0$.

**6.** Apply the definition of the limit with $\varepsilon = 1$. It gives $\delta \gt 0$ such that $\lvert f(y) - L \rvert \lt 1$ for every $y \in D$ with $0 \lt \lvert y - x \rvert \lt \delta$. For such $y$, write $f(y) = (f(y) - L) + L$. The triangle inequality (Session 5) gives

$$
\lvert f(y) \rvert \le \lvert f(y) - L \rvert + \lvert L \rvert \lt 1 + \lvert L \rvert .
$$

So $B = 1 + \lvert L \rvert$ works with this $\delta$.

## Extend

**7.** (a) Let $\delta \gt 0$. Since $x$ is an accumulation point of $D_+$, there is $y \in D_+$ with $0 \lt \lvert y - x \rvert \lt \delta$. Since $D_+ \subseteq D$, this $y$ lies in $D$. So $x$ is an accumulation point of $D$.

(b) **Suppose $\lim_{y \to x} f(y) = L$.** Let $\varepsilon \gt 0$, and take $\delta$ from the definition for $f$ on $D$. Let $y \in D_+$ with $0 \lt \lvert y - x \rvert \lt \delta$. Then $y \in D$, so $\lvert f(y) - L \rvert \lt \varepsilon$. This is the definition of the limit at $x$ for $f$ restricted to $D_+$, so the right limit is $L$. The same argument with $D_-$ in place of $D_+$ shows that the left limit is $L$.

**Suppose both one-sided limits equal $L$.** Let $\varepsilon \gt 0$. The right limit gives $\delta_+ \gt 0$ with $\lvert f(y) - L \rvert \lt \varepsilon$ for every $y \in D_+$ with $0 \lt \lvert y - x \rvert \lt \delta_+$. The left limit gives $\delta_- \gt 0$ with the same property on $D_-$. Put $\delta = \min\{\delta_+, \delta_-\}$, which is positive and at most $\delta_+$ and at most $\delta_-$ (Section 8.1). Let $y \in D$ with $0 \lt \lvert y - x \rvert \lt \delta$. Then $y \neq x$, so either $y \gt x$ or $y \lt x$ (the order of Session 4).

- If $y \gt x$, then $y \in D_+$ and $\lvert y - x \rvert \lt \delta \le \delta_+$, so $\lvert f(y) - L \rvert \lt \varepsilon$.
- If $y \lt x$, then $y \in D_-$ and $\lvert y - x \rvert \lt \delta \le \delta_-$, so $\lvert f(y) - L \rvert \lt \varepsilon$.

So $\lim_{y \to x} f(y) = L$, where $x$ is an accumulation point of $D$ by (a).

(c) Here $D = \mathbb{R}$ and $x = 1$, so $D_+ = \{y \in \mathbb{R} : y \gt 1\}$ and $D_- = \{y \in \mathbb{R} : y \lt 1\}$. Given $\delta \gt 0$, the points $1 + \delta/2 \in D_+$ and $1 - \delta/2 \in D_-$ (because $\delta/2 \gt 0$) lie at distance $\delta/2$ from $1$, which is positive and less than $\delta$, so $1$ is an accumulation point of both.

On $D_+$, $f(y) = y + 1$, a polynomial, so the corollary of Section 8.5 (with $D_+$ in the role of $D$) gives the right limit $1 + 1 = 2$. On $D_-$, $f(y) = 3y^2$, so the same corollary gives the left limit $3 \cdot 1^2 = 3$.

If $f$ had a limit $L$ at $1$, part (b) would make both one-sided limits equal to $L$. Each one-sided limit is a limit of a function, so it is unique (Section 8.4), and this would give $2 = L = 3$. That is impossible, so $f$ has no limit at $1$.

**8.** (a) The composition $y \mapsto h(g(y))$ is defined on $D$, because every value $g(y)$ lies in $E$. Let $(y_n)$ be a sequence in $D$ with $y_n \neq x$ for every $n$ and $y_n \to x$.

1. By the sequential criterion (Section 8.4), $g(y_n) \to M$.
2. The sequence $(g(y_n))$ lies in $E$ and tends to $M$, and $h$ is continuous at $M$. By the sequential form of continuity (Session 7), $h(g(y_n)) \to h(M)$.

The sequence was arbitrary, so the sequential criterion, applied to $y \mapsto h(g(y))$ on $D$, gives $\lim_{y \to x} h(g(y)) = h(M)$.

Step 2 uses Session 7 rather than the sequential criterion for $h$, because $g(y_n)$ may equal $M$. In part (b) it equals $M$ for every $n$, and that is what makes the equation fail there.

(b) The point $0$ is an accumulation point of $\mathbb{R}$ (Lemma 2), and $g(y) = 0$ for every $y$, so $\lim_{y \to 0} g(y) = 0$ (Section 8.3); here $M = 0$. Section 8.8 showed $\lim_{z \to 0} h(z) = 0$. But $h(g(y)) = h(0) = 1$ for every $y$, so $y \mapsto h(g(y))$ is the constant $1$, and its limit at $0$ (indeed at every point) is $1$ (Section 8.3). Since $1 \neq 0$,

$$
\lim_{y \to 0} h(g(y)) = 1 \neq 0 = \lim_{z \to 0} h(z) .
$$

The hypothesis of continuity in (a) cannot be weakened to the existence of a limit. The cause is that $g(y)$ equals $M$ for $y$ near $x$, where $h$ is evaluated at the one point its limit ignores.
