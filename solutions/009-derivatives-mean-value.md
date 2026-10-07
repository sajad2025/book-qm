# Solutions to Session 9. Derivatives and the mean value theorem

Theorem, lemma and corollary numbers refer to Session 9 unless another session is named.

## Check

**1.** (a) Write $p = fg$ with $f(x) = x^2 + 1$ and $g(x) = x^3 - 2x$. By Corollary 1, $f'(x) = 2x$ and $g'(x) = 3x^2 - 2$. By the product rule (Theorem 1 part 2),

$$
p'(x) = 2x (x^3 - 2x) + (x^2 + 1)(3x^2 - 2) = (2x^4 - 4x^2) + (3x^4 - 2x^2 + 3x^2 - 2) = 5x^4 - 3x^2 - 2 .
$$

Expanding first,

$$
p(x) = x^5 - 2x^3 + x^3 - 2x = x^5 - x^3 - 2x ,
$$

and Corollary 1 gives $p'(x) = 5x^4 - 3x^2 - 2$. The two answers agree.

(b) On $(-1, \infty)$, $x + 1 \gt 0$, so the denominator has no zero and the quotient rule (Theorem 1 part 4) applies. The numerator $x - 1$ and the denominator $x + 1$ are polynomials, so by Corollary 1 (restricted by Lemma 2 part 1) both have derivative $1$ at every point of $(-1, \infty)$. So

$$
r'(x) = \frac{1 \cdot (x + 1) - (x - 1) \cdot 1}{(x + 1)^2} = \frac{2}{(x + 1)^2} .
$$

(c) Since $(x + \tfrac12)^2 = x^2 + x + \tfrac14$,

$$
x^2 + x + 1 = \left( x + \tfrac12 \right)^2 + \tfrac34 \ge \tfrac34 \gt 0 .
$$

Let $f(x) = x^2 + x + 1$, $J = (0, \infty)$ and $g(v) = \sqrt{v}$ for $v \in J$. Then $f(\mathbb{R}) \subseteq J$, $f'(x) = 2x + 1$ (Corollary 1), and $g'(v) = 1/(2\sqrt{v})$ for $v \in J$ (Lemma 3 and Lemma 2 part 1). The chain rule (Theorem 2) gives

$$
h'(x) = \frac{1}{2\sqrt{x^2 + x + 1}} \cdot (2x + 1) = \frac{2x + 1}{2\sqrt{x^2 + x + 1}} .
$$

**2.** (a) $f(x) = x^2$ is differentiable on $\mathbb{R}$ with $f'(c) = 2c$ (Corollary 1). Restricted to $[a,b]$ (Lemma 2 part 1), it is continuous on $[a,b]$ (Lemma 1) and has derivative $2c$ at every $c \in (a,b)$. The chord has slope

$$
\frac{b^2 - a^2}{b - a} = \frac{(b - a)(b + a)}{b - a} = a + b .
$$

The equation $2c = a + b$ has the single solution $c = (a + b)/2$. It lies in $(a, b)$, because $a \lt b$ gives $2a \lt a + b \lt 2b$.

(b) On $[1, 2]$, $x \ne 0$. By Section 9.3 (the case $n = 1$ of $x^{-n}$) and Lemma 2 part 1, $f(x) = 1/x$ is differentiable at every point of $[1,2]$ with $f'(c) = -1/c^2$, and it is continuous there by Lemma 1. The chord has slope

$$
\frac{f(2) - f(1)}{2 - 1} = \frac{1}{2} - 1 = -\frac{1}{2} .
$$

The equation $-1/c^2 = -1/2$ is $c^2 = 2$. A $c$ in $(1,2)$ is positive, so by the uniqueness of the nonnegative square root (Session 7), $c = \sqrt{2}$. To see that $\sqrt{2} \in (1, 2)$: for $u, v \ge 0$, $u^2 \lt v^2$ implies $u \lt v$, because the corollary in Section 7.8 (Session 7) gives $u \le v$ from $u^2 \le v^2$, and $u \ne v$ because $u^2 \ne v^2$. From $1 \lt 2 \lt 4$, that is $1^2 \lt (\sqrt{2})^2 \lt 2^2$, we get $1 \lt \sqrt{2} \lt 2$. So $c = \sqrt{2}$, and it is the only such point.

**3.** **At $0$.** For $y \ne 0$ the difference quotient is

$$
\frac{y \lvert y \rvert - 0}{y - 0} = \lvert y \rvert .
$$

Let $(y_n)$ tend to $0$ with $y_n \ne 0$. Then $\bigl\lvert \lvert y_n \rvert - 0 \bigr\rvert = \lvert y_n - 0 \rvert$, so $\lvert y_n \rvert \to 0$ by the definition of convergence. By Session 8, $f'(0) = 0 = 2 \lvert 0 \rvert$.

**At $x \gt 0$.** If $\lvert y - x \rvert \lt x$, then $y \gt x - x = 0$, so $\lvert y \rvert = y$ and $f(y) = y^2$. By Lemma 2 part 2 with $r = x$, the derivative of $f$ at $x$ equals that of $y \mapsto y^2$, which is $2x = 2\lvert x \rvert$ (Corollary 1).

**At $x \lt 0$.** If $\lvert y - x \rvert \lt -x$, then $y \lt x + (-x) = 0$, so $\lvert y \rvert = -y$ and $f(y) = -y^2$. By Lemma 2 part 2 with $r = -x$, and Theorem 1 part 3 with Corollary 1, $f'(x) = -2x = 2 \lvert x \rvert$.

So $f'(x) = 2 \lvert x \rvert$ for every $x$.

**$f'$ at $0$.** If $y_n \to 0$, then $2 \lvert y_n \rvert \to 0 = f'(0)$ as above and by Session 5, so $f'$ is continuous at $0$ (Session 7). Suppose $f'$ were differentiable at $0$. By Theorem 1 part 3, $\tfrac12 f'$, which is $x \mapsto \lvert x \rvert$, would be differentiable at $0$. Section 9.2 shows that it is not. So $f'$ is not differentiable at $0$.

## Prove

**4.** Let $x \gt 0$ and $a = x^{1/n}$. Then $a \ge 0$ and $a^n = x$ (Session 7). Also $a \gt 0$, since $a = 0$ would give $x = 0^n = 0$. For $y \ge 0$ let $b = y^{1/n}$, so $b \ge 0$ and $b^n = y$.

**The identity.** Let $S = \sum_{k=0}^{n-1} b^{n-1-k} a^k$. The difference of powers (Session 3, Section 3.7), with $u = b$ and $v = a$, gives

$$
(b - a) S = b^n - a^n = y - x .
$$

**A lower bound for $S$.** Each term $b^{n-1-k} a^k$ is a product of nonnegative numbers, so it is $\ge 0$. The term with $k = n - 1$ is $a^{n-1} \gt 0$. So $S \ge a^{n-1} \gt 0$. Hence $b - a = (y - x)/S$. Since $S \gt 0$, taking absolute values (Session 5) gives $\lvert b - a \rvert = \lvert y - x \rvert / S$, and $S \ge a^{n-1} \gt 0$ gives $1/S \le 1/a^{n-1}$ (Session 4, Section 4.3(e)), so, multiplying by $\lvert y - x \rvert \ge 0$ (Section 4.3(b)),

$$
\lvert b - a \rvert \le \frac{\lvert y - x \rvert}{a^{n-1}} .
$$

**The limit.** The exponent $n$ is fixed, so index the sequence by $m$. Let $(y_m)$ be a sequence in $[0, \infty)$ with $y_m \ne x$ and $y_m \to x$, let $b_m = y_m^{1/n}$, and let $S_m$ be the sum $S$ with $b_m$ in place of $b$. The bound gives $0 \le \lvert b_m - a \rvert \le \lvert y_m - x \rvert / a^{n-1}$, and the right side tends to $0$ by Session 5, so $b_m \to a$ by the squeeze rule. Let $p(t) = \sum_{k=0}^{n-1} a^k t^{n-1-k}$, a polynomial in $t$ with real coefficients, so that $S_m = p(b_m)$. By the corollary on powers and polynomials (Session 5, Section 5.6), $S_m \to p(a) = \sum_{k=0}^{n-1} a^{n-1} = n a^{n-1} \gt 0$, using $a^k a^{n-1-k} = a^{n-1}$ (Session 3, laws of powers (a)). Since $y_m \ne x$ and $(b_m - a) S_m = y_m - x$, $b_m \ne a$, and

$$
\frac{b_m - a}{y_m - x} = \frac{1}{S_m} \to \frac{1}{n a^{n-1}}
$$

by the quotient rule (Session 5; every $S_m \gt 0$). By Session 8,

$$
r'(x) = \frac{1}{n a^{n-1}} = \frac{a}{n a^n} = \frac{x^{1/n}}{n x} .
$$

For $n = 2$ this is $\sqrt{x}/(2x) = 1/(2\sqrt{x})$, since $x = (\sqrt{x})^2$, which is Lemma 3.

**5.** (a) Let $x \lt y$ in $I$. As in the proof of Theorem 6, $[x, y] \subseteq I$, every point of $(x,y)$ is an interior point of $I$, and the restriction of $f$ to $[x,y]$ satisfies the hypotheses of the mean value theorem (Lemma 2 part 1). Theorem 5 gives $c \in (x, y)$ with $f(y) - f(x) = f'(c)(y - x)$. Both factors are positive, so $f(y) - f(x) \gt 0$.

(b) Let $f(x) = x^3$. By Corollary 1, $f'(c) = 3c^2$. For $c \ne 0$, $c^2 \gt 0$: if $c \gt 0$ it is a product of positives, and if $c \lt 0$ then $c^2 = (-c)^2$ with $-c \gt 0$. So $f'(c) \gt 0$ for every $c \ne 0$.

By Lemma 4, the interior points of $[0, \infty)$ are the $c \gt 0$, where $f'(c) \gt 0$. The function is continuous there (Lemma 1 and Lemma 2 part 1). By (a), $f$ is strictly increasing on $[0, \infty)$. In the same way it is strictly increasing on $(-\infty, 0]$, whose interior points are the $c \lt 0$ (Lemma 4).

Now let $x \lt y$. If $0 \le x$, both lie in $[0, \infty)$ and $f(x) \lt f(y)$. If $y \le 0$, both lie in $(-\infty, 0]$ and $f(x) \lt f(y)$. Otherwise $x \lt 0 \lt y$, and $f(x) \lt f(0) \lt f(y)$. So $f$ is strictly increasing on $\mathbb{R}$, while $f'(0) = 0$. A strictly increasing differentiable function need not have $f' \gt 0$ everywhere, so the converse of (a) is false.

**6.** Let $A = f(b) - f(a)$ and $B = g(b) - g(a)$, and $h = A g - B f$ on $[a, b]$.

**Continuity.** By the algebra of continuous functions (Session 7), $h$ is continuous on $[a,b]$.

**Differentiability.** By Theorem 1 parts 1 and 3, $h$ is differentiable at every $c \in (a, b)$ with $h'(c) = A g'(c) - B f'(c)$.

**Equal end values.**

$$
h(a) = \bigl( f(b) - f(a) \bigr) g(a) - \bigl( g(b) - g(a) \bigr) f(a) = f(b) g(a) - g(b) f(a) ,
$$

because the terms $-f(a) g(a)$ and $+g(a) f(a)$ cancel. Likewise

$$
h(b) = \bigl( f(b) - f(a) \bigr) g(b) - \bigl( g(b) - g(a) \bigr) f(b) = - f(a) g(b) + g(a) f(b) ,
$$

because $f(b) g(b)$ and $-g(b) f(b)$ cancel. So $h(a) = h(b)$.

**Conclusion.** Rolle's theorem (Theorem 4) gives $c \in (a, b)$ with $h'(c) = 0$, that is $A g'(c) = B f'(c)$, which is the claim.

**The case $g(x) = x$.** Then $g'(c) = 1$ and $B = b - a$, so the claim reads $f(b) - f(a) = (b - a) f'(c)$, which is Theorem 5.

## Extend

**7.** Let $n \in \mathbb{N}$ and $h(x) = (1 + x)^n - 1 - nx$ on $[-1, \infty)$.

**The derivative.** Take $f(x) = 1 + x$ and $g(v) = v^n$, both on $\mathbb{R}$. By Corollary 1, $f'(x) = 1$ and $g'(v) = n v^{n-1}$. The chain rule (Theorem 2) gives the derivative $n(1 + x)^{n-1}$ for $(1 + x)^n$. With Theorem 1 parts 1 and 3 and Corollary 1,

$$
h'(x) = n (1 + x)^{n-1} - n = n \bigl( (1 + x)^{n-1} - 1 \bigr) .
$$

The computation holds at every real $x$, so $x \mapsto (1 + x)^n - 1 - nx$ is continuous on $\mathbb{R}$ by Lemma 1, and by Lemma 2 part 1 its restrictions to $[0, \infty)$ and to $[-1, 0]$ are continuous and have derivative $h'(c)$ at every interior point $c$.

**A fact about powers.** For $m \ge 0$: if $v \ge 1$ then $v^m \ge 1$, and if $0 \le v \le 1$ then $v^m \le 1$. By induction on $m$ (Session 3). For $m = 0$, $v^0 = 1$. If $v \ge 1$ and $v^m \ge 1$, then $v^{m+1} = v^m \cdot v \ge v^m \cdot 1 \ge 1$, multiplying $v \ge 1$ by $v^m \gt 0$. If $0 \le v \le 1$ and $v^m \le 1$, then $v^{m+1} = v^m \cdot v \le v^m \cdot 1 \le 1$, multiplying $v \le 1$ by $v^m \ge 0$.

**On $[0, \infty)$.** By Lemma 4, the interior points are the $c \gt 0$. There $1 + c \ge 1$, so $(1 + c)^{n-1} \ge 1$ and $h'(c) \ge 0$. By Theorem 6 part 2, $h$ is nondecreasing on $[0, \infty)$, so for $x \ge 0$, $h(x) \ge h(0) = 1 - 1 - 0 = 0$.

**On $[-1, 0]$.** By Lemma 4, the interior points are the $c$ with $-1 \lt c \lt 0$. There $0 \lt 1 + c \lt 1$, so $(1 + c)^{n-1} \le 1$ and $h'(c) \le 0$. By Theorem 6 part 3, $h$ is nonincreasing on $[-1, 0]$, so for $-1 \le x \le 0$, $h(x) \ge h(0) = 0$.

Every $x \ge -1$ lies in one of the two intervals, so $h(x) \ge 0$, that is $(1 + x)^n \ge 1 + nx$.

**8.** (a) Let $g(x) = f(x) - \lambda x$ on $[a, b]$. By Corollary 1 (restricted by Lemma 2 part 1) and Theorem 1 parts 1 and 3, $g$ is differentiable at every point of $[a,b]$ with $g'(x) = f'(x) - \lambda$, so

$$
g'(a) = f'(a) - \lambda \lt 0, \qquad g'(b) = f'(b) - \lambda \gt 0 .
$$

By Lemma 1, $g$ is continuous on $[a, b]$, so by the extreme value theorem (Session 7) there is a minimum point $p \in [a, b]$: $g(p) \le g(y)$ for every $y \in [a, b]$.

*$p \ne a$.* Write $p_a$ for the difference quotient of $g$ at $a$. Apply the definition of $g'(a)$ (Session 8) with $\varepsilon = -g'(a) \gt 0$: there is $\delta \gt 0$ with $\lvert p_a(y) - g'(a) \rvert \lt -g'(a)$ for every $y \in [a,b]$ with $0 \lt \lvert y - a \rvert \lt \delta$. For such $y$, $p_a(y) \lt g'(a) + (-g'(a)) = 0$. Take $y = \min\{a + \delta/2, b\}$. Then $a \lt y \le b$ and $0 \lt y - a \le \delta/2 \lt \delta$. So

$$
g(y) - g(a) = p_a(y) (y - a) \lt 0 ,
$$

a negative times a positive. Hence $g(y) \lt g(a)$, and $a$ is not a minimum point.

*$p \ne b$.* Write $p_b$ for the difference quotient of $g$ at $b$. With $\varepsilon = g'(b) \gt 0$ there is $\delta' \gt 0$ with $\lvert p_b(y) - g'(b) \rvert \lt g'(b)$, so $p_b(y) \gt 0$, for every $y \in [a,b]$ with $0 \lt \lvert y - b \rvert \lt \delta'$. Take $y = \max\{b - \delta'/2, a\}$. Then $a \le y \lt b$ and $0 \lt b - y \lt \delta'$. So

$$
g(y) - g(b) = p_b(y) (y - b) \lt 0 ,
$$

a positive times a negative. Hence $g(y) \lt g(b)$, and $b$ is not a minimum point.

*Conclusion.* So $p \in (a, b)$. By Lemma 4 part 1, $p$ is an interior point of $[a,b]$, and $g$ has a local minimum there. By Theorem 3, $g'(p) = 0$, that is $f'(p) = \lambda$. Take $c = p$.

(b) Suppose $F : [-1, 1] \to \mathbb{R}$ is differentiable at every point of $[-1, 1]$ with $F'(x) = H(x)$ for every $x$. Then $F'(-1) = H(-1) = 0$ and $F'(1) = H(1) = 1$, and $0 \lt \tfrac12 \lt 1$. By (a) there is $c \in (-1, 1)$ with $F'(c) = \tfrac12$. But $F'(c) = H(c)$, which is $0$ or $1$. This contradiction shows that no such $F$ exists.
