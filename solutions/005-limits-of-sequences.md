# Solutions to 1.5. Limits of real sequences

Section numbers refer to Session 5.

## Check

**1.** Put both terms over the common denominator $n + 3$:

$$
a_n - 2 = \frac{2n + 1 - 2(n + 3)}{n + 3} = \frac{2n + 1 - 2n - 6}{n + 3} = \frac{-5}{n + 3} .
$$

Since $n + 3 \gt 0$, $5/(n + 3) \gt 0$, and Section 5.2, Part 2 gives $\lvert a_n - 2 \rvert = \lvert -5/(n + 3) \rvert = 5/(n + 3)$. Because $0 \lt n \lt n + 3$, the rule for reciprocals gives $1/(n + 3) \lt 1/n$, and multiplying by $5 \gt 0$ gives

$$
\lvert a_n - 2 \rvert = \frac{5}{n + 3} \lt \frac{5}{n} .
$$

Let $\varepsilon \gt 0$. By the Archimedean property there exists $N \in \mathbb{N}$ with $N \gt 5/\varepsilon$. For $n \ge N$ we have $n \gt 5/\varepsilon \gt 0$, so $1/n \lt \varepsilon/5$ by the rule for reciprocals, and $5/n \lt \varepsilon$ on multiplying by $5$. Hence $\lvert a_n - 2 \rvert \lt \varepsilon$ for every $n \ge N$, and $a_n \to 2$.

For $\varepsilon = 1/10$: multiplying both sides by the positive number $10(n + 3)$, or by its reciprocal to go back, the inequality $5/(n + 3) \lt 1/10$ holds if and only if $50 \lt n + 3$, that is, $n \gt 47$. So it holds for every $n \ge 48$, and $N = 48$ works. It fails at $n = 47$, where $5/50 = 1/10$, which is not less than $1/10$. Every $N \le 47$ has $n = 47 \ge N$ among the indices it must cover, so no $N \le 47$ works. The smallest $N$ is $48$.

**2.** Since $n^3 \ne 0$, divide numerator and denominator by $n^3$:

$$
\frac{n^3 - 2n}{4n^3 + n^2 + 1} = \frac{1 - 2/n^2}{4 + 1/n + 1/n^3} .
$$

The steps:
1. $1/n \to 0$ (Section 5.3).
2. $1/n^2 = (1/n)(1/n) \to 0$, and $1/n^3 = (1/n)(1/n^2)$, by 4.2(h) and $n \cdot n^2 = n^3$ (Session 3), so $1/n^3 \to 0 \cdot 0 = 0$; both by the product rule (Section 5.6).
3. $2/n^2 \to 2 \cdot 0 = 0$ by Section 5.6, Part 3, so the numerator $1 - 2/n^2 \to 1 - 0 = 1$ by the difference rule, with the constant sequence $(1)$ converging to $1$ (Section 5.3).
4. The denominator $4 + 1/n + 1/n^3 \to 4 + 0 + 0 = 4$ by the sum rule applied twice.
5. Every term $1/n$ and $1/n^3$ is positive, so the denominator is greater than $4$ and never $0$. Its limit $4$ is not $0$.

The quotient rule (Section 5.7) gives the limit $1/4$.

**3.** Since $1/2 \gt 0$ and $2/3 \gt 0$, Section 5.2 gives $\lvert 1/2 \rvert = 1/2$ and $\lvert 2/3 \rvert = 2/3$. Both are less than $1$: $1/2 \lt 1$ by 4.3(g) (Session 4), and multiplying $2 \lt 3$ by $1/3 \gt 0$ gives $2/3 \lt 1$. So Section 5.10 gives $(1/2)^n \to 0$ and $(2/3)^n \to 0$.

The denominator never vanishes. First, $0 \lt (2/3)^n \le 1$ for every $n$, by induction (Session 3): for $n = 1$, $0 \lt 2/3 \le 1$; if $0 \lt (2/3)^n \le 1$, then $(2/3)^{n+1} = (2/3)^n (2/3)$ is a product of positive numbers, so it is positive, and multiplying $(2/3)^n \le 1$ by $2/3 \gt 0$ shows that it is at most $2/3 \lt 1$. Hence $3 - (2/3)^n \ge 3 - 1 = 2 \gt 0$.

By the sum rule the numerator converges to $1 + 0 = 1$, and by the difference rule the denominator converges to $3 - 0 = 3 \ne 0$. The quotient rule gives

$$
\lim_{n \to \infty} \frac{1 + (1/2)^n}{3 - (2/3)^n} = \frac{1}{3} .
$$

## Prove

**4.** Suppose $a_n \to a$, and let $\varepsilon \gt 0$. Take $N$ with $\lvert a_n - a \rvert \lt \varepsilon$ for every $n \ge N$. By the reverse triangle inequality (Section 5.2, Part 7), for every $n \ge N$,

$$
\bigl\lvert \lvert a_n \rvert - \lvert a \rvert \bigr\rvert \le \lvert a_n - a \rvert \lt \varepsilon .
$$

So $\lvert a_n \rvert \to \lvert a \rvert$.

Example: $a_n = (-1)^n$. By Section 5.2, Part 8, $\lvert a_n \rvert = \lvert -1 \rvert^n = 1^n = 1$ for every $n$, a constant sequence, so $\lvert a_n \rvert \to 1$. But $(a_n)$ diverges (Section 5.5).

For the last part: $\lvert a_n \rvert \ge 0$ by Section 5.2, Part 1, so $\bigl\lvert \lvert a_n \rvert - 0 \bigr\rvert = \lvert a_n \rvert = \lvert a_n - 0 \rvert$. The statement "$\lvert a_n - 0 \rvert \lt \varepsilon$ for every $n \ge N$" is therefore the same as "$\bigl\lvert \lvert a_n \rvert - 0 \bigr\rvert \lt \varepsilon$ for every $n \ge N$", for every $\varepsilon$ and every $N$. So the definitions of $a_n \to 0$ and $\lvert a_n \rvert \to 0$ say the same thing, and each holds if and only if the other does.

**5.** Since $(b_n)$ is bounded, there exists $M$ with $\lvert b_n \rvert \le M$ for every $n$. Then $M \ge \lvert b_1 \rvert \ge 0$, so $M' = M + 1 \gt 0$ and $\lvert b_n \rvert \le M'$ for every $n$.

Let $\varepsilon \gt 0$. Take $N$ with $\lvert a_n \rvert = \lvert a_n - 0 \rvert \lt \varepsilon$ for every $n \ge N$. For such $n$, Section 5.2, Part 4 gives

$$
\lvert a_n b_n - 0 \rvert = \lvert a_n \rvert \, \lvert b_n \rvert \le \lvert a_n \rvert \, M' \le M' \varepsilon ,
$$

where the first inequality multiplies $\lvert b_n \rvert \le M'$ by $\lvert a_n \rvert \ge 0$ and the second multiplies $\lvert a_n \rvert \lt \varepsilon$ by $M' \gt 0$. The lemma "$C\varepsilon$ is enough" (Section 5.3) with $C = M'$ gives $a_n b_n \to 0$.

Application: $a_n = 1/n \to 0$ (Section 5.3), and $b_n = (-1)^n$ is bounded, with $\lvert b_n \rvert = 1$ (Section 5.2). So $(-1)^n / n \to 0$.

The product rule of Section 5.6 assumes that both sequences converge. Here $((-1)^n)$ diverges (Section 5.5), so the product rule does not apply. In the proof of the product rule, the term $a_n(b_n - b)$ needed only that $(a_n)$ is bounded and that $b_n - b \to 0$. Here $(b_n)$ plays the bounded factor and $a_n \to 0$ plays the factor that tends to $0$, so the same estimate works without any limit of $(b_n)$.

**6.** Put $h = \lvert r \rvert - 1$. Then $h \gt 0$ (Session 4), and $-1 \lt 0 \lt h$, on adding $-1$ to $0 \lt 1$, so $h \ge -1$, and Bernoulli's inequality (Session 3) gives, with Section 5.2, Part 8,

$$
\lvert r^n \rvert = \lvert r \rvert^n = (1 + h)^n \ge 1 + nh \gt nh
$$

for every $n$. Suppose $(r^n)$ were bounded, with $\lvert r^n \rvert \le M$ for every $n$. By the Archimedean property there exists $n \in \mathbb{N}$ with $n \gt M/h$, and multiplying by $h \gt 0$ gives $nh \gt M$. For this $n$, $\lvert r^n \rvert \gt nh \gt M$, a contradiction. So $(r^n)$ is unbounded. A convergent sequence is bounded (Section 5.5), so by contraposition (Session 2) $(r^n)$ diverges.

## Extend

**7.** Three facts about finite sums are needed. Sums are those of Session 3, and (R), (S1) to (S4) are its rules.

First, $\bigl\lvert \sum_{k=1}^{n} x_k \bigr\rvert \le \sum_{k=1}^{n} \lvert x_k \rvert$ for all real $x_1, \dots, x_n$. This is Section 5.2, Part 9.

Second, $\sum_{k=1}^{n} c = nc$ for every real $c$ and every $n \ge 0$. This is the corollary on sums of constants in Session 3.

Third, if $0 \le y_k \le c$ for $k = 1, \dots, p$, then $0 \le \sum_{k=1}^{p} y_k \le pc$. This is (S3), comparing with the sum of zeros, which is $0$ by (S2), and with the sum of the constant $c$, which is $pc$ by the second fact.

Now the proof. By the second fact, (S1) and (S2) with $c = -1$,

$$
s_n - a = \frac{1}{n} \sum_{k=1}^{n} a_k - \frac{1}{n} \sum_{k=1}^{n} a = \frac{1}{n} \sum_{k=1}^{n} (a_k - a) .
$$

Since $1/n \gt 0$, Section 5.2, Part 4 and the first fact give

$$
\lvert s_n - a \rvert = \frac{1}{n} \Bigl\lvert \sum_{k=1}^{n} (a_k - a) \Bigr\rvert \le \frac{1}{n} \sum_{k=1}^{n} \lvert a_k - a \rvert .
$$

Let $\varepsilon \gt 0$. Take $N_1$ with $\lvert a_k - a \rvert \lt \varepsilon$ for every $k \ge N_1$. Put $m = N_1 - 1$, which is $0$ if $N_1 = 1$ and lies in $\mathbb{N}$ otherwise (Session 3), and

$$
A = \sum_{k=1}^{m} \lvert a_k - a \rvert .
$$

Then $A \ge 0$ by (S3), comparing with the sum of $m$ zeros, which is $0$ by (S2), and $A$ is a fixed number that does not depend on $n$. Let $n \ge N_1$, and put $p = n - m$. If $m = 0$, then $p = n$; otherwise $n \ge N_1 \gt m$, and $p \in \mathbb{N}$ by Session 3. The splitting rule (S4) gives

$$
\sum_{k=1}^{n} \lvert a_k - a \rvert = A + \sum_{j=1}^{p} \lvert a_{m+j} - a \rvert .
$$

Every index $m + j$ is at least $m + 1 = N_1$, so each term of the last sum lies between $0$ and $\varepsilon$, and the third fact bounds the sum by $p\varepsilon$. Also $p = n - N_1 + 1 \le n$, because $N_1 \ge 1$, and multiplying $p \le n$ by $\varepsilon/n \gt 0$ gives $p\varepsilon/n \le \varepsilon$. Multiplying by $1/n \gt 0$,

$$
\lvert s_n - a \rvert \le \frac{A}{n} + \frac{p\,\varepsilon}{n} \le \frac{A}{n} + \varepsilon .
$$

By the Archimedean property there exists $N_2 \in \mathbb{N}$ with $N_2 \gt A/\varepsilon$, so $N_2 \varepsilon \gt A$ and $A/N_2 \lt \varepsilon$. For $n \ge N_2$, the rule for reciprocals gives $1/n \le 1/N_2$, and multiplying by $A \ge 0$ gives $A/n \le A/N_2 \lt \varepsilon$. Let $N = \max\{N_1, N_2\}$. For every $n \ge N$,

$$
\lvert s_n - a \rvert \le \frac{A}{n} + \varepsilon \lt 2\varepsilon .
$$

The lemma "$C\varepsilon$ is enough" (Section 5.3) with $C = 2$ gives $s_n \to a$.

For $a_n = (-1)^n$, let $t_n = \sum_{k=1}^{n} a_k$, so $s_n = t_n / n$. We show by induction (Session 3) that $t_n = (a_n - 1)/2$. For $n = 1$: $t_1 = -1 = (-1 - 1)/2$. Suppose $t_n = (a_n - 1)/2$. Since $a_{n+1} = (-1)^n (-1) = -a_n$ (Sessions 3 and 4), (R) gives

$$
t_{n+1} = t_n + a_{n+1} = \frac{a_n - 1}{2} - a_n = \frac{-a_n - 1}{2} = \frac{a_{n+1} - 1}{2} .
$$

By Section 5.2, $\lvert a_n \rvert = 1$, so Parts 4 and 6 give $\lvert t_n \rvert = \lvert a_n + (-1) \rvert / 2 \le (\lvert a_n \rvert + \lvert -1 \rvert)/2 = 1$, and

$$
\lvert s_n - 0 \rvert = \frac{\lvert t_n \rvert}{n} \le \frac{1}{n} .
$$

Since $1/n \to 0$, the corollary of the squeeze rule (Section 5.9) gives $s_n \to 0$. But $((-1)^n)$ diverges (Section 5.5). The converse of the first part is false.

**8.** Each ratio $a_{n+1}/a_n$ is positive, so $L \ge 0$ by the corollary in Section 5.8. Put $r = (1 + L)/2$. Then $r - L = (1 - L)/2 \gt 0$ and $1 - r = (1 - L)/2 \gt 0$, since $1 - L \gt 0$ and $1/2 \gt 0$, so $L \lt r \lt 1$. Also $r \ge 1/2 \gt 0$, since $1 + L \ge 1$.

Apply the definition of $a_{n+1}/a_n \to L$ with $\varepsilon = r - L$: there exists $N$ with $\lvert a_{n+1}/a_n - L \rvert \lt \varepsilon$ for every $n \ge N$, so $a_{n+1}/a_n \lt L + \varepsilon = r$ by the second consequence in Section 5.2. Multiplying by $a_n \gt 0$ gives $a_{n+1} \lt r a_n$ for every $n \ge N$.

Next, $a_{N+k} \le r^k a_N$ for every $k \ge 0$. By induction on $k$ from $0$ (Session 3): for $k = 0$ both sides are $a_N$, since $r^0 = 1$. If $a_{N+k} \le r^k a_N$, then, since $N + k \ge N$ and $r \gt 0$,

$$
a_{N+k+1} \lt r \, a_{N+k} \le r \cdot r^k a_N = r^{k+1} a_N .
$$

Now let $n \ge N$, and put $k = n - N$: it is $0$ if $n = N$, and lies in $\mathbb{N}$ if $n \gt N$ (Session 3). So $a_n = a_{N+k} \le r^k a_N$. By the laws of powers (Session 3), $r^k r^N = r^{k+N} = r^n$ and $r^N \gt 0$, so $r^k = r^n / r^N$ by 4.2(e), and

$$
0 \lt a_n \le \frac{a_N}{r^N} \, r^n .
$$

Let $C = a_N / r^N$. Since $\lvert r \rvert = r \lt 1$, Section 5.10 gives $r^n \to 0$, and Section 5.6, Part 3 gives $C r^n \to 0$. As $\lvert a_n - 0 \rvert = a_n \le C r^n$ for every $n \ge N$, the corollary of the squeeze rule (Section 5.9) gives $a_n \to 0$.

Application: $a_n = n/2^n$ is positive, since $n \gt 0$ and $2^n \gt 0$ (Session 3). Using $2^{n+1} = 2^n \cdot 2$,

$$
\frac{a_{n+1}}{a_n} = \frac{n + 1}{2^{n+1}} \cdot \frac{2^n}{n} = \frac{n + 1}{2n} = \frac{1}{2} + \frac{1}{2} \cdot \frac{1}{n} \to \frac{1}{2} + \frac{1}{2} \cdot 0 = \frac{1}{2} ,
$$

by the sum and product rules. Since $1/2 \lt 1$, $n/2^n \to 0$.

Two sequences with ratio limit $1$:
- $a_n = 1$ for every $n$. Each ratio is $1$, so the ratios converge to $1$, and $a_n \to 1$, not to $0$.
- $a_n = 1/n$. The ratio is $\dfrac{1/(n+1)}{1/n} = \dfrac{n}{n + 1} = \dfrac{1}{1 + 1/n}$. Since $1 + 1/n \to 1 \ne 0$ and $1 + 1/n \gt 0$, the quotient rule gives ratios converging to $1/1 = 1$. Here $a_n \to 0$ (Section 5.3).

So when the ratio limit is $1$, the ratios alone do not decide whether $a_n \to 0$.
