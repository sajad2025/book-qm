# Solutions to Session 7. Continuous functions on an interval

Section numbers such as 7.3 refer to the sections of Session 7.

## Check

**1.** (a) Fix $x \in \mathbb{R}$ and $\varepsilon \gt 0$, and let $\delta = \varepsilon/2$, which is positive (Session 4, Section 4.3). If $\lvert y - x \rvert \lt \delta$, then

$$
\lvert f(y) - f(x) \rvert = \lvert (2y + 1) - (2x + 1) \rvert = \lvert 2(y - x) \rvert = 2 \lvert y - x \rvert \lt 2 \cdot \frac{\varepsilon}{2} = \varepsilon .
$$

So $f$ is continuous at $x$. Since $x$ was arbitrary, $f$ is continuous on $\mathbb{R}$.

(b) Here $f(-2) = 4$, and $y^2 - 4 = (y + 2)(y - 2)$, so $\lvert y^2 - 4 \rvert = \lvert y + 2 \rvert \, \lvert y - 2 \rvert$.

1. If $\lvert y + 2 \rvert \lt 1$, then $-1 \lt y + 2 \lt 1$, so $-3 \lt y \lt -1$, so $-5 \lt y - 2 \lt -3$. In particular $-5 \lt y - 2 \lt 5$, that is, $\lvert y - 2 \rvert \lt 5$. Multiplying by $\lvert y + 2 \rvert \ge 0$ gives $\lvert y^2 - 4 \rvert \le 5 \lvert y + 2 \rvert$.
2. Take $\delta$ to be the smaller of $1$ and $\varepsilon/5$. For $\varepsilon = 1/10$ this is $\delta = 1/50$.
3. If $\lvert y - (-2) \rvert = \lvert y + 2 \rvert \lt 1/50$, then $\lvert y + 2 \rvert \lt 1$, so step 1 applies, and

$$
\lvert y^2 - 4 \rvert \le 5 \lvert y + 2 \rvert \lt 5 \cdot \frac{1}{50} = \frac{1}{10} .
$$

So $\delta = 1/50$ works.

**2.** The polynomial $p$ is continuous on $\mathbb{R}$ (Section 7.4), and so is its restriction to any closed interval. At the ends of $[1,2]$:

$$
p(1) = 1 - 1 - 1 = -1 \lt 0, \qquad p(2) = 8 - 2 - 1 = 5 \gt 0 .
$$

Since $p(1) \le 0 \le p(2)$, the intermediate value theorem (Section 7.7) gives $c \in [1,2]$ with $p(c) = 0$, a zero of $p$.

Now halve the interval three times. Each time, the sign of $p$ at the midpoint decides which half has a negative value at its left end and a positive value at its right end; the intermediate value theorem on that half gives a zero in it.

1. At $3/2$: $p(3/2) = \dfrac{27}{8} - \dfrac{12}{8} - \dfrac{8}{8} = \dfrac{7}{8} \gt 0$. Since $p(1) \lt 0 \lt p(3/2)$, there is a zero in $[1, 3/2]$.
2. At $5/4$: $p(5/4) = \dfrac{125}{64} - \dfrac{80}{64} - \dfrac{64}{64} = -\dfrac{19}{64} \lt 0$. Since $p(5/4) \lt 0 \lt p(3/2)$, there is a zero in $[5/4, 3/2]$.
3. At $11/8$: $p(11/8) = \dfrac{1331}{512} - \dfrac{704}{512} - \dfrac{512}{512} = \dfrac{115}{512} \gt 0$. Since $p(5/4) \lt 0 \lt p(11/8)$, there is a zero in $[5/4, 11/8]$.

The interval $[5/4, 11/8] = [10/8, 11/8]$ has length $1/8$ and contains a zero. (The arithmetic: $11^3 = 1331$ and $11 \cdot 64 = 704$; $5^3 = 125$ and $5 \cdot 16 = 80$.)

**3.** The function is continuous on $[0,2]$ by Section 7.4, since $1 + x^2 \ge 1 \gt 0$ (a square is nonnegative, Session 4).

*Minimum.* For $x \in [0,2]$, $x \ge 0$ and $1/(1 + x^2) \gt 0$, so $f(x) = x \cdot 1/(1 + x^2) \ge 0 = f(0)$. The minimum is $0$, attained at $x = 0$. It is attained only there: $f(x) = 0$ forces $x = 0$, because $x = f(x)(1 + x^2)$.

*Maximum.* For every real $x$,

$$
\frac{1}{2} - \frac{x}{1 + x^2} = \frac{(1 + x^2) - 2x}{2(1 + x^2)} = \frac{(x - 1)^2}{2(1 + x^2)} \ge 0 ,
$$

since the numerator is a square and the denominator is positive. So $f(x) \le 1/2 = f(1)$. The maximum is $1/2$, attained at $x = 1$, and only there, since equality needs $(x-1)^2 = 0$.

*The set of values.* The two bounds give $0 \le f(x) \le 1/2$ for every $x \in [0,2]$, so $f([0,2]) \subseteq [0, 1/2]$. Conversely, let $0 \le y \le 1/2$. The restriction of $f$ to $[0,1]$ is continuous, with $f(0) = 0 \le y \le 1/2 = f(1)$. The intermediate value theorem gives $c \in [0,1]$ with $f(c) = y$, and $c \in [0,2]$. So $[0, 1/2] \subseteq f([0,2])$. The two inclusions give $f([0,2]) = [0, 1/2]$.

## Prove

**4.** Since $f(x) \gt 0$, the number $\varepsilon = f(x)/2$ is positive. Continuity at $x$ gives $\delta \gt 0$ such that $\lvert f(y) - f(x) \rvert \lt f(x)/2$ for every $y \in D$ with $\lvert y - x \rvert \lt \delta$. For such $y$, the rule $\lvert t \rvert \lt c \Leftrightarrow -c \lt t \lt c$ (Session 5) gives $-f(x)/2 \lt f(y) - f(x)$. Adding $f(x)$ to both sides,

$$
f(y) \gt f(x) - \frac{f(x)}{2} = \frac{f(x)}{2} .
$$

In particular $f(y) \gt 0$ for every such $y$.

**5.** Let $g(x) = f(x) - x$ on $[0,1]$. It is $f$ plus $(-1)$ times the identity, so it is continuous by Sections 7.2 and 7.4. At the ends,

$$
g(0) = f(0) - 0 = f(0) \ge 0, \qquad g(1) = f(1) - 1 \le 0 ,
$$

using $0 \le f(0)$ and $f(1) \le 1$. So $g(1) \le 0 \le g(0)$: the value $0$ lies between $g(0)$ and $g(1)$. The intermediate value theorem (Section 7.7) gives $c \in [0,1]$ with $g(c) = 0$, that is, $f(c) = c$.

**6.** Write $T = \lvert \alpha \rvert + \lvert \beta \rvert + \lvert \gamma \rvert$, so $R = 1 + T$ and $R \ge 1$. Two inequalities about $R$ are used:

- $R^2 - R = R(R - 1) \ge 0$, so $R \le R^2$;
- $R^2 \ge R \ge 1$.

*The value at $R$.* Each term is bounded below using $t \ge -\lvert t \rvert$ (Session 5):

- $\alpha R^2 \ge -\lvert \alpha R^2 \rvert = -\lvert \alpha \rvert R^2$, since $R^2 \ge 0$;
- $\beta R \ge -\lvert \beta R \rvert = -\lvert \beta \rvert R$, since $R \ge 0$; and $-\lvert \beta \rvert R \ge -\lvert \beta \rvert R^2$, since $R \le R^2$ and $\lvert \beta \rvert \ge 0$;
- $\gamma \ge -\lvert \gamma \rvert \ge -\lvert \gamma \rvert R^2$, since $1 \le R^2$.

Adding,

$$
p(R) = R^3 + \alpha R^2 + \beta R + \gamma \ge R^3 - T R^2 = R^2 (R - T) = R^2 \cdot 1 \ge 1 \gt 0 .
$$

*The value at $-R$.* Now each term is bounded above using $t \le \lvert t \rvert$:

- $\alpha R^2 \le \lvert \alpha \rvert R^2$;
- $-\beta R \le \lvert -\beta R \rvert = \lvert \beta \rvert R \le \lvert \beta \rvert R^2$;
- $\gamma \le \lvert \gamma \rvert \le \lvert \gamma \rvert R^2$.

Since $(-R)^3 = -R^3$ and $(-R)^2 = R^2$,

$$
p(-R) = -R^3 + \alpha R^2 - \beta R + \gamma \le -R^3 + T R^2 = -R^2 (R - T) = -R^2 \le -1 \lt 0 .
$$

*A zero.* Since $R \ge 1 \gt 0$, we have $-R \lt R$, so $[-R, R]$ is a closed interval, and $p$ is continuous on it (Section 7.4). As $p(-R) \lt 0 \lt p(R)$, the intermediate value theorem (Section 7.7) gives $c \in [-R, R]$ with $p(c) = 0$.

**7.** Let $u = a^{1/n}$ and $v = b^{1/n}$. By definition (Section 7.8), $u, v \ge 0$, $u^n = a$ and $v^n = b$.

(a) By the laws of powers (Session 3), $(uv)^n = u^n v^n = ab$. Also $uv \ge 0$, as a product of nonnegative numbers. So $uv$ is a nonnegative number whose $n$-th power is $ab$. By the uniqueness in Section 7.8, $uv = (ab)^{1/n}$, that is, $(ab)^{1/n} = a^{1/n} b^{1/n}$.

(b) By contraposition (Session 2): we show that $u \ge v$ implies $a \ge b$. If $u = v$, then $a = u^n = v^n = b$. If $u \gt v$, then $0 \le v \lt u$, and the laws of powers (Session 3) give $v^n \lt u^n$, that is, $b \lt a$. In both cases $a \ge b$. So if $0 \le a \lt b$, then $u \ge v$ is impossible, and by trichotomy (Session 4) $u \lt v$, that is, $a^{1/n} \lt b^{1/n}$.

## Extend

**8.** (a) By induction on $n$ (Session 3). For $n = 1$, $(s + v)^1 = s + v = s^1 + v^1$. Suppose $(s + v)^k \ge s^k + v^k$. Since $s + v \ge 0$, multiplying this inequality by $s + v$ keeps its direction (Session 4):

$$
(s + v)^{k+1} = (s + v)^k (s + v) \ge (s^k + v^k)(s + v) = s^{k+1} + s^k v + v^k s + v^{k+1} .
$$

The middle terms $s^k v$ and $v^k s$ are products of nonnegative numbers ($s^k, v^k \ge 0$ by the laws of powers, Session 3), so they are nonnegative, and the right side is at least $s^{k+1} + v^{k+1}$. So $(s + v)^{k+1} \ge s^{k+1} + v^{k+1}$.

(b) Both sides of the inequality are unchanged when $a$ and $b$ are exchanged, since $\lvert -t \rvert = \lvert t \rvert$ (Session 5), so we may take $a \ge b \ge 0$. Let $u = a^{1/n}$ and $v = b^{1/n}$.

1. $u \ge v$: if $a = b$ then $u = v$; if $a \gt b$ then $u \gt v$ by Exercise 7(b).
2. Let $s = u - v \ge 0$. Then $u = s + v$, and part (a) gives

$$
a = u^n = (s + v)^n \ge s^n + v^n = s^n + b ,
$$

so $s^n \le a - b$.
3. The number $a - b \ge 0$ has the root $w = (a - b)^{1/n}$, with $w^n = a - b$. So $s^n \le w^n$ with $s, w \ge 0$, and part 2 of the corollary in Section 7.8 gives $s \le w$.

Since $u \ge v$, $\lvert u - v \rvert = u - v = s$, and $\lvert a - b \rvert = a - b$. Step 3 reads $\lvert a^{1/n} - b^{1/n} \rvert \le \lvert a - b \rvert^{1/n}$.

(c) Fix $x \ge 0$ and $\varepsilon \gt 0$. Let $\delta = \varepsilon^n$, which is positive as a product of positive numbers. Let $y \ge 0$ with $\lvert y - x \rvert \lt \varepsilon^n$.

1. By Exercise 7(b), applied to $0 \le \lvert y - x \rvert \lt \varepsilon^n$, we get $\lvert y - x \rvert^{1/n} \lt (\varepsilon^n)^{1/n}$.
2. The number $\varepsilon \ge 0$ has $n$-th power $\varepsilon^n$, so by uniqueness (Section 7.8) $(\varepsilon^n)^{1/n} = \varepsilon$.
3. By part (b), $\lvert y^{1/n} - x^{1/n} \rvert \le \lvert y - x \rvert^{1/n} \lt \varepsilon$.

So $x \mapsto x^{1/n}$ is continuous at $x$. Since $x \ge 0$ was arbitrary, it is continuous on $[0, \infty)$.
