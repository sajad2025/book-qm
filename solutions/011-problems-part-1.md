# Solutions to 1.11. Problems for Part 1

The solutions use the results of Sessions 2 to 10, cited by number. "Session 7 (Section 7.8)" refers to the corollary there, in the form recalled in Section 11.1: for $u, v \ge 0$ and $k \in \mathbb{N}$, $u^k \le v^k$ implies $u \le v$, and $u^k \lt v^k$ implies $u \lt v$.

## Check

**1.** (a) Let $P(n)$ be the statement $\sum_{k=1}^{n} k^3 = n^2(n+1)^2/4$. For $n = 1$ both sides are $1$, since $1 \cdot 4/4 = 1$. Suppose $P(n)$. Then

$$
\sum_{k=1}^{n+1} k^3 = \frac{n^2(n+1)^2}{4} + (n+1)^3 = \frac{(n+1)^2\bigl[n^2 + 4(n+1)\bigr]}{4} = \frac{(n+1)^2(n^2 + 4n + 4)}{4} .
$$

Since $(n+2)^2 = n^2 + 4n + 4$, the right side is $(n+1)^2(n+2)^2/4$, which is $P(n+1)$. By induction (Session 3), $P(n)$ holds for every $n \in \mathbb{N}$.

(b) Expanding, $n^2(n+1)^2 = n^2(n^2 + 2n + 1) = n^4 + 2n^3 + n^2$. Dividing by $4n^4$,

$$
\frac{1}{n^4}\sum_{k=1}^{n} k^3 = \frac{1}{4} + \frac{1}{2}\cdot\frac{1}{n} + \frac{1}{4}\cdot\frac{1}{n}\cdot\frac{1}{n} .
$$

Since $1/n \to 0$ (Session 5), the product rule gives $(1/n)(1/n) \to 0$, and the sum and product rules (Session 5) give the limit $\frac{1}{4} + 0 + 0 = \frac{1}{4}$.

(c) For $n = 10$, the left side of (a) is $1 + 8 + 27 + 64 + 125 + 216 + 343 + 512 + 729 + 1000 = 3025$, and the right side is $100 \cdot 121/4 = 12100/4 = 3025$. Then $\frac{1}{10000}\cdot 3025 = 0.3025$, and the expression in (b) gives

$$
\frac{1}{4} + \frac{1}{20} + \frac{1}{400} = \frac{100}{400} + \frac{20}{400} + \frac{1}{400} = \frac{121}{400} = 0.3025 .
$$

**2.** (a) The polynomial $p$ is continuous on $\mathbb{R}$ (Session 7, Section 7.4), and so its restriction to each closed interval below is continuous there (Session 9, Lemma 2, part 1). Its values at the integers from $-2$ to $2$ are

$$
p(-2) = -32 + 10 + 1 = -21, \quad p(-1) = -1 + 5 + 1 = 5, \quad p(0) = 1, \quad p(1) = 1 - 5 + 1 = -3, \quad p(2) = 32 - 10 + 1 = 23 .
$$

On $[-2,-1]$, $p(-2) \lt 0 \lt p(-1)$; on $[0,1]$, $p(0) \gt 0 \gt p(1)$; on $[1,2]$, $p(1) \lt 0 \lt p(2)$. The intermediate value theorem (Session 7) gives a point in each closed interval where $p = 0$. None of these points is an endpoint, since $p$ is nonzero at every endpoint. So $p$ has a zero in each of $(-2,-1)$, $(0,1)$ and $(1,2)$. The three intervals are disjoint, so the three zeros are distinct.

(b) By Session 9 (Corollary 1), $p$ is differentiable on $\mathbb{R}$ with

$$
p'(x) = 5x^4 - 5 = 5(x^2 - 1)(x^2 + 1) = 5(x-1)(x+1)(x^2+1).
$$

Since $x^2 + 1 \ge 1 \gt 0$, the product is zero only if $x - 1 = 0$ or $x + 1 = 0$ (in a field, a product of nonzero numbers is nonzero). So the zeros of $p'$ are exactly $1$ and $-1$.

Suppose $p$ had four distinct zeros $r_1 \lt r_2 \lt r_3 \lt r_4$. For each $i$, the restriction of $p$ to $[r_i, r_{i+1}]$ is continuous on $[r_i, r_{i+1}]$ and differentiable on $(r_i, r_{i+1})$ with derivative $p'$ (Session 9, Lemmas 1 and 2), and it is $0$ at both ends. Rolle's theorem (Session 9) gives $s_i \in (r_i, r_{i+1})$ with $p'(s_i) = 0$, for $i = 1, 2, 3$. The open intervals $(r_1,r_2)$, $(r_2,r_3)$ and $(r_3,r_4)$ are disjoint, so $s_1, s_2, s_3$ are three distinct zeros of $p'$. This contradicts the count of two. So $p$ has at most three zeros, and by (a) exactly three: one in each interval of (a).

(c) Halve the interval four times, using the intermediate value theorem each time, as in (a).

- $p(1/2) = 1/32 - 5/2 + 1 = 1/32 - 3/2 \lt 0$ and $p(0) = 1 \gt 0$, so there is a zero in $(0, 1/2)$.
- $p(1/4) = 1/1024 - 5/4 + 1 = 1/1024 - 1/4 \lt 0$, so there is a zero in $(0, 1/4)$.
- $p(1/8) = 1/32768 - 5/8 + 1 = 3/8 + 1/32768 \gt 0$, so there is a zero in $(1/8, 1/4)$.
- $p(3/16) = 243/1048576 - 15/16 + 1 = 1/16 + 243/1048576 \gt 0$, so there is a zero in $(3/16, 1/4)$.

By (b), $p$ has only one zero in $(0,1)$, so this is the zero of (a), and $(3/16, 1/4)$ is an interval of length $1/16$ that contains it.

## Prove

**3.** (a) *The case $c \ge 1$.* Write $u_n = c^{1/n}$, the root of Session 7. First, $u_n \ge 1$: if $u_n \lt 1$, then Session 3 (laws of powers (e)) with $s = u_n \ge 0$ and $t = 1$ gives $c = u_n^n \lt 1^n = 1$, a contradiction. Let $h_n = u_n - 1 \ge 0$. Since $h_n \ge 0 \ge -1$, Bernoulli's inequality (Session 3) gives

$$
c = (1 + h_n)^n \ge 1 + n h_n, \qquad \text{so} \qquad 0 \le h_n \le \frac{c - 1}{n} .
$$

The right side tends to $(c-1)\cdot 0 = 0$ by the product rule (Session 5), and the constant sequence $0$ tends to $0$. By the squeeze rule (Session 5), $h_n \to 0$, so $u_n = 1 + h_n \to 1$.

*The case $0 \lt c \lt 1$.* Let $d = 1/c$. Since $0 \lt c \lt 1$, Session 4 (Section 4.3, (e)) gives $d = 1/c \gt 1/1 = 1$. By Session 3 (laws of powers (b)), $(c^{1/n} d^{1/n})^n = (c^{1/n})^n (d^{1/n})^n = c\,d = 1$. The number $c^{1/n} d^{1/n}$ is nonnegative, and so is $1$, with $1^n = 1$. The $n$-th root of $1$ is unique (Session 7), so $c^{1/n} d^{1/n} = 1$. Hence $d^{1/n} \neq 0$ and $c^{1/n} = 1/d^{1/n}$. By the first case $d^{1/n} \to 1 \neq 0$, so by the quotient rule (Session 5) $c^{1/n} \to 1/1 = 1$.

(b) Let $d_n = n^{1/n} - 1$. Since $n \ge 1$, the argument at the start of (a) gives $n^{1/n} \ge 1$, so $d_n \ge 0$. For $n \ge 2$, the binomial theorem (Session 3) gives

$$
n = (1 + d_n)^n = \sum_{j=0}^{n} \binom{n}{j} d_n^j \ge \binom{n}{2} d_n^2 = \frac{n(n-1)}{2} d_n^2 .
$$

Here $n - 2 \ge 0$, and (R) twice gives $n! = (n-2)!\,(n-1)\,n$; with $2! = 2$, $\binom{n}{2} = \frac{(n-2)!\,(n-1)n}{2\,(n-2)!} = \frac{n(n-1)}{2}$. The binomial theorem gives this term as $\binom{n}{2} 1^{n-2} d_n^2$, and $1^{n-2} = 1$ (laws of powers (f)). Write $t_j = \binom{n}{j} d_n^j$; each $t_j \ge 0$, since $\binom{n}{j} \gt 0$ (Session 3, Section 3.8) and $d_n^j \ge 0$ (laws of powers (d)). By the definition of a sum from 0, then (S4) with $m = 2$ and (R), $\sum_{j=0}^{n} t_j = t_0 + t_1 + t_2 + \sum_{j=3}^{n} t_j$. The last sum is $\ge 0$ by (S3) and (S2), and $t_0, t_1 \ge 0$, so the sum is at least $t_2$. Dividing by $n(n-1)/2 \gt 0$ gives $d_n^2 \le 2/(n-1)$.

Let $\varepsilon \gt 0$. By the Archimedean property (Session 4) there is $N \in \mathbb{N}$ with $N \gt 1 + 2/\varepsilon^2$; then $N \ge 2$. For $n \ge N$, $n - 1 \gt 2/\varepsilon^2$, so $d_n^2 \le 2/(n-1) \lt \varepsilon^2$. Since $d_n \ge 0$ and $\varepsilon \gt 0$, Session 7 (Section 7.8) with exponent $2$ gives $d_n \lt \varepsilon$. So $\lvert d_n - 0 \rvert \lt \varepsilon$ for every $n \ge N$, that is, $d_n \to 0$, and $n^{1/n} = 1 + d_n \to 1$.

Bernoulli's inequality alone gives only $n \ge 1 + n d_n$, that is, $d_n \le (n-1)/n$, which does not tend to $0$. The binomial theorem keeps the quadratic term, and the quadratic term is what makes the bound shrink.

**4.** All the numbers $1 + 1/n$, $a_n$ and $b_n$ are positive, so every division below is by a positive number. The rules $(u/v)^m = u^m/v^m$ and $u^{m+1} = u^m u$ are laws of powers (Session 3).

(a) Write $a_n = \bigl(\frac{n+1}{n}\bigr)^{n+1} \cdot \frac{n}{n+1}$ and $a_{n+1} = \bigl(\frac{n+2}{n+1}\bigr)^{n+1}$. Then

$$
\frac{a_{n+1}}{a_n} = \Bigl( \frac{n+2}{n+1} \cdot \frac{n}{n+1} \Bigr)^{n+1} \cdot \frac{n+1}{n} = \Bigl( \frac{n(n+2)}{(n+1)^2} \Bigr)^{n+1} \cdot \frac{n+1}{n} = \Bigl( 1 - \frac{1}{(n+1)^2} \Bigr)^{n+1} \cdot \frac{n+1}{n},
$$

since $n(n+2) = (n+1)^2 - 1$. Bernoulli's inequality (Session 3) with $x = -1/(n+1)^2 \ge -1$ and exponent $n+1$ gives

$$
\Bigl( 1 - \frac{1}{(n+1)^2} \Bigr)^{n+1} \ge 1 - \frac{n+1}{(n+1)^2} = 1 - \frac{1}{n+1} = \frac{n}{n+1} .
$$

So $a_{n+1}/a_n \ge \frac{n}{n+1}\cdot\frac{n+1}{n} = 1$, and multiplying by $a_n \gt 0$ gives $a_{n+1} \ge a_n$.

(b) Write $b_n = \bigl(\frac{n+1}{n}\bigr)^{n+1}$ and $b_{n+1} = \bigl(\frac{n+2}{n+1}\bigr)^{n+1} \cdot \frac{n+2}{n+1}$. Then

$$
\frac{b_n}{b_{n+1}} = \Bigl( \frac{n+1}{n} \cdot \frac{n+1}{n+2} \Bigr)^{n+1} \cdot \frac{n+1}{n+2} = \Bigl( 1 + \frac{1}{n(n+2)} \Bigr)^{n+1} \cdot \frac{n+1}{n+2},
$$

since $(n+1)^2 = n(n+2) + 1$. Bernoulli's inequality with $x = 1/(n(n+2)) \ge 0$ gives

$$
\Bigl( 1 + \frac{1}{n(n+2)} \Bigr)^{n+1} \ge 1 + \frac{n+1}{n(n+2)} = \frac{n^2 + 2n + n + 1}{n(n+2)} = \frac{n^2 + 3n + 1}{n(n+2)} .
$$

Multiplying by $\frac{n+1}{n+2} \gt 0$,

$$
\frac{b_n}{b_{n+1}} \ge \frac{(n^2 + 3n + 1)(n+1)}{n(n+2)^2} = \frac{n^3 + 4n^2 + 4n + 1}{n^3 + 4n^2 + 4n} \ge 1 ,
$$

where the numerator was expanded as $n^3 + n^2 + 3n^2 + 3n + n + 1$ and the denominator as $n(n^2 + 4n + 4)$. Multiplying by $b_{n+1} \gt 0$ gives $b_n \ge b_{n+1}$.

(c) Since $b_n = a_n (1 + 1/n)$ and $a_n \gt 0$, $b_n - a_n = a_n/n \gt 0$, so $a_n \lt b_n$. By (b) and Session 6 (comparison of terms, nonincreasing case), $b_n \le b_1 = 2^2 = 4$ for every $n$. So $(a_n)$ is nondecreasing and bounded above by $4$. By the monotone convergence theorem (Session 6) it converges to some $L$, and $a_m \le L$ for every $m$. By the sum and product rules (Session 5) and $1/n \to 0$, $b_n = a_n(1 + 1/n) \to L \cdot (1 + 0) = L$.

By (b), $(b_n)$ is nonincreasing, and it is bounded below by $0$. By Session 6 (corollary, nonincreasing case) it converges to a limit $L'$ with $L' \le b_m$ for every $m$. Since $b_n \to L$, uniqueness of limits (Session 5) gives $L' = L$. So $a_m \le L \le b_m$ for every $m$.

For $m = 5$, $1 + 1/5 = 6/5$, and

$$
a_5 = \frac{6^5}{5^5} = \frac{7776}{3125} = 2.48832, \qquad b_5 = \frac{6^6}{5^6} = \frac{46656}{15625} = 2.985984 .
$$

So $2.48832 \le L \le 2.985984$. The interval is wide: since $a_m \ge a_1 = 2$ (Session 6, comparison of terms), $b_m - a_m = a_m/m \ge 2/m$, so the width of the interval is at least $2/m$.

**5.** (a) *Positivity.* By induction (Session 3): $a_1 \gt 0$, and if $a_n \gt 0$ then $c/a_n \gt 0$, so $a_{n+1}$ is half a sum of two positive numbers and is positive.

*The error identity.* The number $r = \sqrt{c}$ satisfies $r \ge 0$ and $r^2 = c$ (Session 7), and $r \neq 0$ because $c \neq 0$; so $r \gt 0$. Then

$$
a_{n+1} - r = \frac{a_n^2 + c}{2a_n} - \frac{2 r a_n}{2 a_n} = \frac{a_n^2 - 2 r a_n + r^2}{2 a_n} = \frac{(a_n - r)^2}{2 a_n} .
$$

(b) *A lower bound.* By (a), $a_{n+1} - r$ is a square divided by a positive number, so $a_{n+1} \ge r$ for every $n \ge 1$. That is, $a_n \ge r$ for every $n \ge 2$.

*Monotonicity.* For $n \ge 2$,

$$
a_n - a_{n+1} = \frac{2a_n^2}{2a_n} - \frac{a_n^2 + c}{2a_n} = \frac{a_n^2 - c}{2 a_n} = \frac{(a_n - r)(a_n + r)}{2a_n} \ge 0 ,
$$

because $a_n - r \ge 0$, $a_n + r \gt 0$ and $a_n \gt 0$.

*Convergence.* Let $d_n = a_{n+1}$ for $n \ge 1$. Then $(d_n)$ is nonincreasing and bounded below by $r$, so it converges (Session 6) to some $L$, and $L \ge r$ by the non-strict inequality rule (Session 5), applied to $d_n$ and the constant sequence $r$. In particular $L \gt 0$. Since $d_n = a_{n+1}$, Session 5 (Lemma (tails), with $k = 1$) gives $a_n \to L$, and $a_{n+1} \to L$ by definition of $(d_n)$.

*The limit.* Multiply the recursion by $2a_n$: $2 a_n a_{n+1} = a_n^2 + c$ for every $n$. By the product and sum rules (Session 5), the left side tends to $2L^2$ and the right side to $L^2 + c$. A limit is unique (Session 5), so $2L^2 = L^2 + c$, that is, $L^2 = c$. Since $L \ge 0$, $L$ is the nonnegative square root of $c$, which is unique (Session 7). So $L = r$, and $a_n \to r$.

(c) With $c = 2$ and $a_1 = 1$:

$$
a_2 = \tfrac{1}{2}\bigl(1 + 2\bigr) = \tfrac{3}{2}, \qquad
a_3 = \tfrac{1}{2}\Bigl(\tfrac{3}{2} + \tfrac{4}{3}\Bigr) = \tfrac{1}{2}\cdot\tfrac{9 + 8}{6} = \tfrac{17}{12}, \qquad
a_4 = \tfrac{1}{2}\Bigl(\tfrac{17}{12} + \tfrac{24}{17}\Bigr) = \tfrac{1}{2}\cdot\tfrac{289 + 288}{204} = \tfrac{577}{408} .
$$

*A lower bound on $r$.* Since $(4/3)^2 = 16/9 \lt 18/9 = 2 = r^2$, and $4/3 \ge 0$, $r \ge 0$, Session 7 (Section 7.8) gives $4/3 \lt r$.

*The errors.* Let $e_n = a_n - r$. By (b), $e_n \ge 0$ for $n \ge 2$. First, $e_2 = 3/2 - r \lt 3/2 - 4/3 = 1/6$. For $n \ge 2$, $a_n \ge r \gt 4/3$, so $2a_n \gt 8/3 \gt 0$ and $1/(2a_n) \lt 3/8$ (Session 4). Since $e_n^2 \ge 0$, (a) gives $e_{n+1} = e_n^2/(2a_n) \le \frac{3}{8} e_n^2$. If $0 \le e_n \le \beta$, then $e_n^2 \le \beta^2$ by (P3) of Session 3. So

$$
e_3 \le \frac{3}{8}\cdot\frac{1}{36} = \frac{1}{96}, \qquad e_4 \le \frac{3}{8}\cdot\frac{1}{96^2} = \frac{3}{8 \cdot 9216} = \frac{3}{73728} = \frac{1}{24576} .
$$

So $0 \le 577/408 - \sqrt{2} \le 1/24576$. Each step squares the bound on the error and multiplies it by $3/8$: from $1/6$ to $1/96$ to $1/24576$.

**6.** (a) *Values.* $x_2 = 1/2$, $x_3 = 1/(5/2) = 2/5$, $x_4 = 1/(12/5) = 5/12$, $x_5 = 1/(29/12) = 12/29$.

*Not monotone.* $x_3 = 2/5 \lt 1/2 = x_2$, so the sequence is not nondecreasing. $x_3 = 2/5 = 24/60 \lt 25/60 = 5/12 = x_4$, so it is not nonincreasing.

*Bounds.* By induction (Session 3). $x_1 = 0 \in [0, \frac{1}{2}]$. Suppose $0 \le x_n \le \frac{1}{2}$. Then $2 + x_n \ge 2 \gt 0$, so $x_{n+1} = 1/(2 + x_n) \gt 0$. And $1/(2 + x_n) \le 1/2$ is equivalent, after multiplying by the positive number $2(2 + x_n)$, to $2 \le 2 + x_n$, which holds. So $0 \le x_{n+1} \le \frac{1}{2}$.

(b) The function $g$ is defined on $I = (-2, \infty)$, where $2 + t \neq 0$. The function $t \mapsto 2 + t$ is a polynomial with derivative $1$ (Session 9, Corollary 1), and it is nonzero on $I$. By Session 9 (Lemma 2, part 1, and Theorem 1, part 4, with $f = 1$), $g$ is differentiable on $I$, with $g'(t) = -1/(2+t)^2$. It is continuous on $I$ by Session 9 (Lemma 1).

Let $0 \le s \lt t$. By Session 9 (Lemma 2, part 1), the restriction of $g$ to $[s,t]$ is continuous on $[s,t]$ and differentiable on $(s,t)$, with derivative $g'$. The mean value theorem (Session 9) gives $\xi \in (s,t)$ with $g(t) - g(s) = g'(\xi)(t - s)$. Since $\xi \gt s \ge 0$, $2 + \xi \gt 2$, so $(2 + \xi)^2 \gt 4$ (Session 3, laws of powers (e)) and $\lvert g'(\xi) \rvert = 1/(2+\xi)^2 \lt 1/4$. Hence $\lvert g(t) - g(s) \rvert = \lvert g'(\xi) \rvert (t - s) \le \frac{1}{4}(t - s) = \frac{1}{4}\lvert t - s \rvert$. If $s = t$ both sides are $0$, and if $s \gt t$ exchange the names. So the bound holds for all $s, t \ge 0$.

(c) *Consecutive differences.* We show $\lvert x_{n+1} - x_n \rvert \le \frac{1}{2}(\frac{1}{4})^{n-1}$ by induction (Session 3). For $n = 1$, $\lvert x_2 - x_1 \rvert = \frac{1}{2}$. Suppose the bound holds for $n$. Since $x_{n+2} = g(x_{n+1})$, $x_{n+1} = g(x_n)$ and both $x_n, x_{n+1} \ge 0$ by (a), part (b) gives

$$
\lvert x_{n+2} - x_{n+1} \rvert \le \tfrac{1}{4}\lvert x_{n+1} - x_n \rvert \le \tfrac{1}{4}\cdot\tfrac{1}{2}\bigl(\tfrac{1}{4}\bigr)^{n-1} = \tfrac{1}{2}\bigl(\tfrac{1}{4}\bigr)^{n} .
$$

*Distant terms.* Let $m \gt n$ and $q = m - n \in \mathbb{N}$. Put $y_i = x_{n+i} - x_{n+i-1}$ for $1 \le i \le q$. By (S5) of Session 3 applied to the sequence $i \mapsto x_{n+i-1}$, $\sum_{i=1}^{q} y_i = x_{n+q} - x_n = x_m - x_n$. By the triangle inequality for finite sums (Session 5, Section 5.2, Part 9), $\lvert x_m - x_n \rvert \le \sum_{i=1}^{q} \lvert y_i \rvert$.

By the bound on consecutive differences and the laws of powers (a) of Session 3, $\lvert y_i \rvert \le \frac{1}{2}(\frac{1}{4})^{n+i-2} = \frac{1}{2}(\frac{1}{4})^{n-1}(\frac{1}{4})^{i-1}$. So (S3), (S2) and (S6) of Session 3 and the geometric sum (Session 3) give

$$
\lvert x_m - x_n \rvert \le \sum_{i=1}^{q} \tfrac{1}{2}\bigl(\tfrac{1}{4}\bigr)^{n-1}\bigl(\tfrac{1}{4}\bigr)^{i-1} = \tfrac{1}{2}\bigl(\tfrac{1}{4}\bigr)^{n-1} \sum_{i=0}^{q-1} \bigl(\tfrac{1}{4}\bigr)^{i} = \tfrac{1}{2}\bigl(\tfrac{1}{4}\bigr)^{n-1} \cdot \frac{1 - (1/4)^{q}}{3/4} \le \tfrac{2}{3}\bigl(\tfrac{1}{4}\bigr)^{n-1},
$$

using $(1/4)^{q} \gt 0$.

*Comparison with $1/n$.* Bernoulli's inequality (Session 3) with exponent $n - 1 \ge 0$ gives $4^{n-1} = (1 + 3)^{n-1} \ge 1 + 3(n - 1) = 3n - 2 \ge n$ for every $n \in \mathbb{N}$. By the laws of powers (b) of Session 3, $(\frac{1}{4})^{n-1} 4^{n-1} = 1^{n-1} = 1$, so $(\frac{1}{4})^{n-1} = 1/4^{n-1} \le 1/n$. Hence

$$
\lvert x_m - x_n \rvert \le \frac{2}{3n} \qquad \text{for all } m \gt n .
$$

*Cauchy.* Let $\varepsilon \gt 0$. By the Archimedean property (Session 4) there is $N \in \mathbb{N}$ with $N \gt 2/(3\varepsilon)$. For $m \gt n \ge N$, $\lvert x_m - x_n \rvert \le 2/(3n) \le 2/(3N) \lt \varepsilon$. If $m = n$ the difference is $0 \lt \varepsilon$, and if $m \lt n$ exchange the names, since $\lvert x_m - x_n \rvert = \lvert x_n - x_m \rvert$. So $\lvert x_m - x_n \rvert \lt \varepsilon$ for all $m, n \ge N$, and $(x_n)$ is Cauchy. It converges (Session 6).

(d) Let $L$ be the limit. Since $0 \le x_n \le \frac{1}{2}$ for every $n$, $0 \le L \le \frac{1}{2}$ (Session 5). By (b),

$$
0 \le \lvert x_{n+1} - g(L) \rvert = \lvert g(x_n) - g(L) \rvert \le \tfrac{1}{4}\lvert x_n - L \rvert .
$$

The right side tends to $0$, because $x_n \to L$ means exactly that $\lvert x_n - L \rvert \to 0$, and then the product rule (Session 5) applies. By the squeeze rule (Session 5), $x_{n+1} \to g(L)$. Also $x_{n+1} \to L$ (Session 5, Lemma (tails), with $k = 1$). A limit is unique (Session 5), so $L = 1/(2 + L)$. Multiplying by $2 + L \gt 0$, $L^2 + 2L = 1$, so $(L + 1)^2 = 2$. Since $L + 1 \ge 1 \gt 0$, $L + 1$ is the nonnegative square root of $2$, which is unique (Session 7). So $L = \sqrt{2} - 1$.

As a check, the bound before the comparison with $1/n$ gives, for every $m \gt 5$, $\lvert x_m - x_5 \rvert \le \frac{2}{3}(\frac{1}{4})^{4} = \frac{1}{384}$, that is, $x_5 - \frac{1}{384} \le x_m \le x_5 + \frac{1}{384}$. The non-strict inequality rule (Session 5), applied to the sequence $(x_{m+5})$, which tends to $L$ by Session 5 (Lemma (tails), with $k = 5$), passes both bounds to the limit, so $\lvert x_5 - L \rvert \le \frac{1}{384}$. By Problem 5 (c), $L = \sqrt{2} - 1$ lies within $1/24576$ below $577/408 - 1 = 169/408$. And $169/408 - 12/29 = (4901 - 4896)/11832 = 5/11832$. By the triangle inequality, $\lvert x_5 - L \rvert \le 5/11832 + 1/24576$. Since $5/11832 \lt 6/11832 = 1/1972 \lt 1/768$ and $1/24576 \lt 1/768$, this is less than $2/768 = 1/384$, as it must be.

(e) Write $u = \sqrt{n+1}$ and $v = \sqrt{n}$, both positive: each is $\ge 0$ (Session 7), and neither is $0$, since $0^2 = 0$ while $n + 1$ and $n$ are nonzero. The difference of powers (Session 3, Section 3.7) with $k = 2$ gives $(u - v)(u + v) = u^2 - v^2 = (n + 1) - n = 1$. Since $u + v \ge v \gt 0$,

$$
0 \lt c_{n+1} - c_n = \frac{1}{u + v} \le \frac{1}{v} = \frac{1}{\sqrt{n}} .
$$

Let $\varepsilon \gt 0$, and take $N \in \mathbb{N}$ with $N \gt 1/\varepsilon^2$ (Session 4). For $n \ge N$, $(1/\varepsilon)^2 \lt n = (\sqrt{n})^2$, so $\sqrt{n} \gt 1/\varepsilon$ by Session 7 (Section 7.8), and $c_{n+1} - c_n \lt \varepsilon$. So $c_{n+1} - c_n \to 0$.

But $(c_n)$ is unbounded: let $M$ be real. If $M \le 0$, then $\lvert c_1 \rvert = 1 \gt M$. If $M \gt 0$, take $n \in \mathbb{N}$ with $n \gt M^2$ (Session 4); then $\sqrt{n} \gt M$ in the same way. A convergent sequence is bounded (Session 5), so $(c_n)$ does not converge, and by Session 6 it is not Cauchy. In (c) the differences decreased geometrically, so every sum of them from the $n$-th on stayed below $\frac{2}{3}(\frac{1}{4})^{n-1}$. Here the sum of the first $n$ differences is $c_{n+1} - c_1 = \sqrt{n+1} - 1$, which is unbounded.

**7.** Throughout, $r(x)$ is the unique $u \ge 0$ with $u^k = x$ (Session 7).

(a) Let $x \ge 0$ and $y \gt 0$, and write $u = r(x)$, $v = r(y)$. Then $v \gt 0$: $v \ge 0$, and $v = 0$ would give $y = 0^k = 0$. By the difference of powers (Session 3, Section 3.7),

$$
x - y = u^k - v^k = (u - v)\, S, \qquad S = \sum_{j=0}^{k-1} u^{k-1-j} v^{j} .
$$

Every term of $S$ is a product of nonnegative numbers, so it is nonnegative (Session 3, laws of powers (d)), and the term with $j = k-1$ is $v^{k-1} \gt 0$. By (R0) of Session 3, $S = \sum_{j=0}^{k-2} u^{k-1-j} v^j + v^{k-1}$ (here $k - 2 \ge 0$), and the first sum is $\ge 0$ by (S3) and (S2) for sums from 0. So $S \ge v^{k-1} \gt 0$. Taking absolute values (Session 5, Section 5.2), $\lvert x - y \rvert = \lvert u - v \rvert\, S$, so

$$
\lvert r(x) - r(y) \rvert = \lvert u - v \rvert = \frac{\lvert x - y \rvert}{S} \le \frac{\lvert x - y \rvert}{v^{k-1}} .
$$

*Continuity at $y \gt 0$.* Let $x_n \to y$ with $x_n \ge 0$. Then $0 \le \lvert r(x_n) - r(y) \rvert \le \lvert x_n - y \rvert / v^{k-1}$, and the right side tends to $0$ by the product rule (Session 5). By the squeeze rule (Session 5), $\lvert r(x_n) - r(y) \rvert \to 0$, that is, $r(x_n) \to r(y)$. By Session 7, $r$ is continuous at $y$.

(b) For every $m \ge 0$ and $n \in \mathbb{N}$, $n^m \ge 1^m = 1$, by (P3) of Session 3 with every factor $1 \le n$. Let $h_n = 1/n^k$. Then $n^k = n \cdot n^{k-1} \ge n$, so $0 \lt h_n \le 1/n$, and $h_n \to 0$ by the squeeze rule (Session 5). Since $1/n \ge 0$ and $(1/n)^k = h_n$, uniqueness of the $k$-th root (Session 7) gives $r(h_n) = 1/n$. So

$$
\frac{r(h_n) - r(0)}{h_n} = \frac{1/n}{1/n^k} = n^{k-1} = n \cdot n^{k-2} \ge n ,
$$

using $k \ge 2$. Given any $M$, the Archimedean property (Session 4) gives $n \gt M$, so the sequence of quotients is unbounded and has no limit (Session 5). Since $h_n \gt 0$ and $h_n \to 0$, if the difference quotient of $r$ at $0$ had a limit, the sequential criterion (Session 8) would make it the limit of this sequence. So it has no limit at $0$, and $r$ is not differentiable at $0$ (Session 9, Section 9.2).

**8.** (a) Since $f(u) \neq f(v)$, also $u \neq v$. Exchanging the names if necessary, take $u \lt v$. Since $u, v \in [a,b]$, $a \le u$ and $v \le b$, so $[u,v] \subseteq [a,b]$. The restriction of $f$ to $[u,v]$ is continuous (Session 7, Section 7.4). Let $\alpha = \min\{f(u), f(v)\}$ and $\beta = \max\{f(u), f(v)\}$. Then $\alpha$ and $\beta$ are the two numbers $f(u)$ and $f(v)$ in some order, and $\alpha \lt \beta$ because they differ.

Let $\alpha \le y \le \beta$. Then $y$ lies between $f(u)$ and $f(v)$, so the intermediate value theorem (Session 7) gives $c \in [u,v]$ with $f(c) = y$. Since $c \in [a,b]$, $y \in f([a,b])$. So $[\alpha, \beta] \subseteq f([a,b])$.

The interval $[\alpha, \beta]$ is uncountable (Session 10, Section 10.5). A set that contains an uncountable subset is uncountable (Session 10, Section 10.2). So $f([a,b])$ is uncountable.

(b) Suppose $f([a,b])$ is countable. By (a), in the contrapositive form (Session 2), $f(u) = f(v)$ for all $u, v \in [a,b]$. Taking $v = a$, $f(u) = f(a)$ for every $u \in [a,b]$, so $f$ is constant.

If every value of $f$ is rational, then $f([a,b]) \subseteq \mathbb{Q}$. The set $\mathbb{Q}$ is countable (Session 10, Section 10.4), so its subset $f([a,b])$ is countable (Session 10, Section 10.2), and $f$ is constant by the first part.

(c) *Continuity at a point of $[0,1]$.* Let $x \in [0,1]$ and $\varepsilon \gt 0$, and take $\delta = 1$. Let $y \in D$ with $\lvert y - x \rvert \lt 1$. Then $y \lt x + 1 \le 2$, so $y \notin [2,3]$, and $y \in [0,1]$. So $g(y) = 0 = g(x)$, and $\lvert g(y) - g(x) \rvert = 0 \lt \varepsilon$.

*Continuity at a point of $[2,3]$.* Let $x \in [2,3]$, $\varepsilon \gt 0$ and $\delta = 1$. If $y \in D$ and $\lvert y - x \rvert \lt 1$, then $y \gt x - 1 \ge 1$, so $y \notin [0,1]$, and $y \in [2,3]$. So $g(y) = 1 = g(x)$.

So $g$ is continuous at every point of $D$. Its values are $g(0) = 0$ and $g(2) = 1$, and no others, so it takes exactly two values. Its set of values $\{0, 1\}$ is countable (Session 10), yet $g$ is not constant.

The step of (a) that fails is the intermediate value theorem. With $u = 1$ and $v = 2$, the interval $[u,v] = [1,2]$ is not contained in $D$: the point $3/2$ lies in neither $[0,1]$ nor $[2,3]$. So $g$ has no restriction to $[1,2]$, and the value $1/2$, which lies between $g(1) = 0$ and $g(2) = 1$, is not taken.

## Extend

**9.** (a) Let $f(x) = x^{p+1}$. By Session 9 (Corollary 1), $f$ is differentiable on $\mathbb{R}$ with $f'(x) = (p+1)x^p$, and so continuous on $\mathbb{R}$ (Session 9, Lemma 1). By Session 9 (Lemma 2, part 1), its restriction to $[a,b]$ is continuous on $[a,b]$ and differentiable on $(a,b)$ with the same derivative. The mean value theorem (Session 9) gives $\xi \in (a,b)$ with

$$
b^{p+1} - a^{p+1} = (p+1)\, \xi^p (b - a) .
$$

Since $0 \le a \lt \xi \lt b$, Session 3 (laws of powers (e)) gives $a^p \lt \xi^p \lt b^p$, so $a^p \le \xi^p \le b^p$. Multiplying by $(p+1)(b - a) \gt 0$ gives the two inequalities.

(b) *Lower bound.* For $k = 1, \dots, n$, apply the right inequality of (a) with $a = k - 1 \ge 0$ and $b = k$: $k^{p+1} - (k-1)^{p+1} \le (p+1)k^p$. Add these inequalities ((S3) of Session 3). By (S5) with $a_k = (k-1)^{p+1}$, the left side telescopes to $n^{p+1} - 0^{p+1} = n^{p+1}$, and by (S2) the right side is $(p+1)S_p(n)$. Dividing by $p + 1$ gives $n^{p+1}/(p+1) \le S_p(n)$.

*Upper bound.* For $k = 1, \dots, n$, apply the left inequality of (a) with $a = k$ and $b = k + 1$: $(p+1)k^p \le (k+1)^{p+1} - k^{p+1}$. Add these inequalities ((S3) of Session 3). By (S2) the left side is $(p+1)S_p(n)$, and by (S5) with $a_k = k^{p+1}$ the right side telescopes to $(n+1)^{p+1} - 1^{p+1} = (n+1)^{p+1} - 1$ (laws of powers (f)). Dividing by $p + 1 \gt 0$ gives $S_p(n) \le ((n+1)^{p+1} - 1)/(p+1)$.

(c) Divide the bounds of (b) by $n^{p+1} \gt 0$:

$$
\frac{1}{p+1} \le \frac{S_p(n)}{n^{p+1}} \le \frac{1}{p+1}\Bigl[ \Bigl(1 + \frac{1}{n}\Bigr)^{p+1} - \frac{1}{n^{p+1}} \Bigr],
$$

where $(n+1)^{p+1}/n^{p+1} = (1 + 1/n)^{p+1}$ by the laws of powers (b) of Session 3. Since $1 + 1/n \to 1$ and $1/n \to 0$ (Session 5), Session 5 (Section 5.6, Corollary (powers and polynomials)) gives $(1 + 1/n)^{p+1} \to 1^{p+1} = 1$ and $1/n^{p+1} = (1/n)^{p+1} \to 0^{p+1} = 0$. By the sum and product rules, the right side tends to $\frac{1}{p+1}(1 - 0) = \frac{1}{p+1}$. The left side is constant. By the squeeze rule (Session 5), $S_p(n)/n^{p+1} \to 1/(p+1)$.

For $p = 3$ this is the limit of Problem 1 (b), found here without a formula for $S_3(n)$, and the same argument gives it for every $p$.

(d) *For $n = 10$.* The bounds are $10^4/4 = 2500$ and $(11^4 - 1)/4 = (14641 - 1)/4 = 3660$. By Problem 1 (c), $S_3(10) = 3025$, which lies between them.

*For every $n$.* By Problem 1, $S_3(n) = n^2(n+1)^2/4 = (n^4 + 2n^3 + n^2)/4$. The lower bound is $n^4/4$, and

$$
\frac{n^4 + 2n^3 + n^2}{4} - \frac{n^4}{4} = \frac{2n^3 + n^2}{4} \ge 0 .
$$

For the upper bound, the expansion of $(1+x)^4$ in Session 3, Section 3.10, with $x = n$, gives $(n+1)^4 = n^4 + 4n^3 + 6n^2 + 4n + 1$, so

$$
\frac{(n+1)^4 - 1}{4} - \frac{n^4 + 2n^3 + n^2}{4} = \frac{2n^3 + 5n^2 + 4n}{4} \ge 0 .
$$

So both inequalities of (b) hold for $p = 3$ and every $n$.
