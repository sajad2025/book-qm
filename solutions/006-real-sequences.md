# Solutions to Session 6. Monotone sequences, subsequences and Cauchy sequences

Each solution uses only Session 6 and Sessions 2 to 5, cited by number. Exercise 7 also uses the fact about $\mathbb{Q}$ granted in its statement.

## Check

**1.** $a_2 = \frac{2 \cdot 1 + 3}{3} = \frac53$ and $a_3 = \frac{2 \cdot \frac53 + 3}{3} = \frac{\frac{10}{3} + \frac93}{3} = \frac{\frac{19}{3}}{3} = \frac{19}{9}$.

*$a_n \lt 3$ for every $n$.* By induction (Session 3). For $n = 1$: $1 \lt 3$. Suppose $a_n \lt 3$. Then $2 a_n \lt 6$, so $2 a_n + 3 \lt 9$, and dividing by $3 \gt 0$ gives $a_{n+1} \lt 3$.

*Nondecreasing.* For every $n$,

$$
a_{n+1} - a_n = \frac{2 a_n + 3 - 3 a_n}{3} = \frac{3 - a_n}{3} \gt 0 ,
$$

since $a_n \lt 3$.

*The limit.* The sequence is nondecreasing and bounded above by $3$, so by the monotone convergence theorem (Session 6) $a_n \to L$ for some $L$. The tail $(a_{k+1})$ is a subsequence ($n_k = k + 1$), so $a_{k+1} \to L$. The same sequence is $\frac{2 a_k + 3}{3} = \frac23 a_k + 1$, and by the sum and product rules with constant sequences (Session 5) it converges to $\frac23 L + 1$. By uniqueness of limits (Session 5),

$$
L = \frac23 L + 1 .
$$

Multiplying by $3$: $3L = 2L + 3$, so $L = 3$. Hence $a_n \to 3$.

**2.** *A preliminary limit.* $1/n \to 0$ (Session 5, Section 5.3). Here $2k$ and $2k + 1$ are natural numbers (Session 3, Lemma 3), and $2(k+1) = 2k + 2 \gt 2k$ and $2(k+1) + 1 \gt 2k + 1$. So $\frac{1}{2k}$ and $\frac{1}{2k+1}$ are subsequences of $(1/n)$, and both converge to $0$ (Session 6, Section 6.3).

*Even terms.* $n_k = 2k$ is strictly increasing (Section 6.3), so $(a_{2k})$ is a subsequence. Since $(-1)^{2k} = 1$ (Section 6.3),

$$
a_{2k} = \frac{2k}{2k+1} = \frac{(2k + 1) - 1}{2k+1} = 1 - \frac{1}{2k+1} .
$$

By the sum rule with the constant sequence $1$ (Session 5), $a_{2k} \to 1 - 0 = 1$.

*Odd terms.* $n_k = 2k - 1$ is strictly increasing (Section 6.3), so $(a_{2k-1})$ is a subsequence. Since $(-1)^{2k-1} = -1$ (Section 6.3),

$$
a_{2k-1} = -\frac{2k-1}{2k} = -\left(\frac{2k}{2k} - \frac{1}{2k}\right) = -\left(1 - \frac{1}{2k}\right) = -1 + \frac{1}{2k} ,
$$

so $a_{2k-1} \to -1 + 0 = -1$.

*Conclusion.* The two subsequences converge to $1$ and $-1$, which differ. By the test for divergence (Session 6), $(a_n)$ diverges. The sequence is bounded by $1$, since $\lvert a_n \rvert = \frac{n}{n+1} \lt 1$, and either subsequence is a convergent subsequence of the kind the Bolzano-Weierstrass theorem promises.

**3.** *The inequality.* For $k \ge 2$,

$$
\frac{1}{k-1} - \frac1k = \frac{k - (k-1)}{k(k-1)} = \frac{1}{k(k-1)} .
$$

Since $k \ge 2$, $k - 1 \ge 1 \gt 0$, so $0 \lt k(k-1) = k^2 - k \lt k^2$. By the rule for reciprocals (Session 4, 4.3(e)), $\frac{1}{k(k-1)} \gt \frac{1}{k^2}$.

*The bound.* Let $m \gt n$. Splitting the sum (Session 3),

$$
s_m - s_n = \sum_{k=n+1}^{m} \frac{1}{k^2} .
$$

Every term is positive, so by (S3) and (S2) (Session 3) the sum is at least a sum of zeros, which is $0$: $s_m - s_n \ge 0$. Every index in the sum satisfies $k \ge n + 1 \ge 2$, so each term is at most $\frac{1}{k-1} - \frac1k$, and by (S3) (Session 3)

$$
s_m - s_n \le \sum_{k=n+1}^{m} \left( \frac{1}{k-1} - \frac1k \right) = \frac1n - \frac1m .
$$

The last equality is telescoping, (S5) of Session 3. Put $q = m - n \in \mathbb{N}$ and $t_j = -\frac{1}{n + j - 1}$ for $j \in \mathbb{N}$. By the meaning of a sum from $n + 1$ (Session 3, Section 3.6), the sum is $\sum_{j=1}^{q} \bigl( \frac{1}{n+j-1} - \frac{1}{n+j} \bigr) = \sum_{j=1}^{q} (t_{j+1} - t_j)$, and (S5) gives $t_{q+1} - t_1 = -\frac1m + \frac1n$. Finally $\frac1n - \frac1m \lt \frac1n$ because $\frac1m \gt 0$. So $0 \le s_m - s_n \lt \frac1n$.

*Cauchy.* Let $\varepsilon \gt 0$, and choose $N \in \mathbb{N}$ with $N \gt \frac1\varepsilon$ (Session 4), so that $\frac1N \lt \varepsilon$. Let $m, n \ge N$. If $m = n$, then $\lvert s_m - s_n \rvert = 0 \lt \varepsilon$. If $m \gt n$, then $\lvert s_m - s_n \rvert = s_m - s_n \lt \frac1n \le \frac1N \lt \varepsilon$. If $n \gt m$, the same argument with $m$ and $n$ exchanged gives $\lvert s_n - s_m \rvert \lt \varepsilon$, and $\lvert s_m - s_n \rvert = \lvert s_n - s_m \rvert$ (Session 5). So $(s_n)$ is a Cauchy sequence, and by the Cauchy criterion (Session 6) it converges.

The same bound gives a second proof. The sequence is nondecreasing, since $s_{n+1} - s_n = \frac{1}{(n+1)^2} \gt 0$, and taking $n = 1$ gives $s_m \lt s_1 + 1 = 2$ for every $m \gt 1$, and $s_1 = 1 \lt 2$. So it is bounded above by $2$ and converges by the monotone convergence theorem. Neither proof says what the limit is.

## Prove

**4.** Let $(a_n)$ be nonincreasing and bounded below, and let $T = \{a_n : n \in \mathbb{N}\}$. The set $T$ is nonempty and bounded below, so $g = \inf T$ exists by Session 4, Section 4.5. Since $g$ is a lower bound of $T$, $g \le a_n$ for every $n$.

Let $\varepsilon \gt 0$. Then $g + \varepsilon \gt g$. If $g + \varepsilon$ were a lower bound of $T$, then $g + \varepsilon \le g$, because $g$ is the greatest lower bound; this contradicts $g \lt g + \varepsilon$ (Session 4). So $g + \varepsilon$ is not a lower bound, and by negation (Session 2) there exists $N$ for which $g + \varepsilon \le a_N$ is false, that is, $a_N \lt g + \varepsilon$ (Session 4). Let $n \ge N$. By the comparison lemma for nonincreasing sequences (Session 6), $a_n \le a_N$. So

$$
g - \varepsilon \lt g \le a_n \le a_N \lt g + \varepsilon ,
$$

and $\lvert a_n - g \rvert \lt \varepsilon$ (Session 5). This holds for every $n \ge N$, so $a_n \to g$.

**5.** Every $n \in \mathbb{N}$ equals $2k$ or $2k - 1$ for some $k \in \mathbb{N}$, by the parity lemma (Session 3, Section 3.3).

Let $\varepsilon \gt 0$. Since $a_{2k} \to a$, there exists $K_1$ with $\lvert a_{2k} - a \rvert \lt \varepsilon$ for every $k \ge K_1$. Since $a_{2k-1} \to a$, there exists $K_2$ with $\lvert a_{2k-1} - a \rvert \lt \varepsilon$ for every $k \ge K_2$. Let $K$ be the larger of $K_1$ and $K_2$, and put $N = 2K$. Let $n \ge N$.

- If $n = 2k$, then $2k \ge 2K$, so $k \ge K \ge K_1$, and $\lvert a_n - a \rvert = \lvert a_{2k} - a \rvert \lt \varepsilon$.
- If $n = 2k - 1$, then $2k = n + 1 \gt 2K$, so $k \gt K \ge K_2$, and $\lvert a_n - a \rvert = \lvert a_{2k-1} - a \rvert \lt \varepsilon$.

In both cases $\lvert a_n - a \rvert \lt \varepsilon$, so $a_n \to a$.

**6.** Let $(a_n)$ be monotone with a subsequence $a_{n_k} \to a$. A convergent sequence is bounded (Session 5), so there exists $M$ with $\lvert a_{n_k} \rvert \le M$ for every $k$.

*Nondecreasing case.* Let $n \in \mathbb{N}$. Take $k = n$: by the lemma on growing indices (Session 6), $n_n \ge n$, so by the comparison lemma (Session 6) $a_n \le a_{n_n} \le \lvert a_{n_n} \rvert \le M$ (Session 5, Section 5.2, Part 2). Hence $(a_n)$ is bounded above by $M$, and it converges by the monotone convergence theorem.

*Nonincreasing case.* The sequence $(-a_n)$ is nondecreasing, as in the proof of the comparison lemma (Session 6), and its subsequence $(-a_{n_k})$ converges to $-a$ by the product rule with the constant sequence $-1$ (Session 5). By the first case, $(-a_n)$ converges, say to $c$. Then $a_n = (-1)(-a_n) \to -c$ by the product rule.

In either case, the limit equals $a$: the subsequence $(a_{n_k})$ of the convergent sequence converges to the same limit (Session 6), and limits are unique (Session 5).

## Extend

**7.** *(a) No rational square root of 2.* By the parity lemma (Session 3, Section 3.3), every natural number is even ($2j$ with $j \in \mathbb{N}$) or odd ($2j - 1$ with $j \in \mathbb{N}$), and not both.

First, the square of an odd number is odd. If $p = 2j - 1$, then

$$
p^2 = 4j^2 - 4j + 1 = 2(2j^2 - 2j + 1) - 1 ,
$$

and $2j^2 - 2j + 1 = 2j(j - 1) + 1$ is a natural number: if $j = 1$ it is $1$, and otherwise $j - 1 \in \mathbb{N}$ (Session 3, Lemma 2), so $2j(j - 1) \in \mathbb{N}$ and $2j(j - 1) + 1 \in \mathbb{N}$ (Session 3, Lemma 3). So if $p^2$ is even, $p$ is not odd, hence $p$ is even.

Suppose $q^2 = 2$ with $q = \frac{p}{s}$, $p$ an integer and $s \in \mathbb{N}$. Then $p^2 = 2s^2$. Since $(-p)^2 = p^2$, we may replace $p$ by $-p$ if needed and assume $p \ge 0$. And $p \ne 0$, since $0 \ne 2s^2$. So $p \in \mathbb{N}$. It is therefore enough to prove, for every $r \in \mathbb{N}$, the statement

$Q(r)$: for every $s \in \mathbb{N}$ with $s \le r$, no $p \in \mathbb{N}$ satisfies $p^2 = 2s^2$.

*The key step.* Suppose $p, s \in \mathbb{N}$ and $p^2 = 2s^2$. Then $p^2$ is even, so $p$ is even: $p = 2p'$ with $p' \in \mathbb{N}$. Then $4p'^2 = 2s^2$, so $s^2 = 2p'^2$. Then $s^2$ is even, so $s$ is even: $s = 2s'$ with $s' \in \mathbb{N}$. Then $4s'^2 = 2p'^2$, so $p'^2 = 2s'^2$. Also $s' \lt s' + s' = s$.

*Induction on $r$ (Session 3).* $Q(1)$: if $s \le 1$ then $s = 1$, which is odd. By the key step, a solution of $p^2 = 2 \cdot 1^2$ would make $1$ even, and no natural number is both. So $Q(1)$ holds. Suppose $Q(r)$ holds, and suppose $p^2 = 2s^2$ with $p, s \in \mathbb{N}$ and $s \le r + 1$. By $Q(r)$, $s \gt r$. The key step gives $p'^2 = 2s'^2$ with $s' \lt s \le r + 1$, so $s' \le r$ (Session 3). This contradicts $Q(r)$. So $Q(r+1)$ holds.

Hence $Q(r)$ holds for every $r$, and no rational $q$ satisfies $q^2 = 2$.

*(b) Positive rationals.* The recursion theorem (Session 3) needs a function defined at every number: here $g(x) = \frac{x}{2} + \frac1x$ for $x \ne 0$, with $g(0) = 0$, and $a_{n+1} = g(a_n)$. By induction, every $a_n$ is a positive rational. $a_1 = 2$ is one. If $a_n$ is a positive rational, then $a_n \ne 0$, so $a_{n+1} = \frac{a_n}{2} + \frac{1}{a_n}$. The numbers $\frac{a_n}{2}$ and $\frac{1}{a_n}$ are positive (Session 4) and rational, by the fact granted in the statement (Session 4, Section 4.9), and so is their sum $a_{n+1}$. In particular the value $g(0)$ is never used.

*(c) The identity.* By the identity $(a \pm b)^2 = a^2 \pm 2ab + b^2$ (Session 4, Section 4.8), with $a = \frac{a_n}{2}$ and $b = \frac{1}{a_n}$, and since $\bigl(\frac{a_n}{2}\bigr)^2 = \frac{a_n^2}{4}$ and $\bigl(\frac{1}{a_n}\bigr)^2 = \frac{1}{a_n^2}$ (Session 4, 4.2(h)),

$$
a_{n+1}^2 - 2 = \frac{a_n^2}{4} + 2 \cdot \frac{a_n}{2} \cdot \frac{1}{a_n} + \frac{1}{a_n^2} - 2 = \frac{a_n^2}{4} + 1 + \frac{1}{a_n^2} - 2 = \frac{a_n^2}{4} - 1 + \frac{1}{a_n^2} ,
$$

and by the same identity with the minus sign,

$$
\left( \frac{a_n}{2} - \frac{1}{a_n} \right)^2 = \frac{a_n^2}{4} - 2 \cdot \frac{a_n}{2} \cdot \frac{1}{a_n} + \frac{1}{a_n^2} = \frac{a_n^2}{4} - 1 + \frac{1}{a_n^2} .
$$

The two right sides agree. A square in an ordered field is nonnegative (Session 4), so $a_{n+1}^2 \ge 2$ for every $n \ge 1$, that is, $a_n^2 \ge 2$ for every $n \ge 2$. For $n = 1$, $a_1^2 = 4 \ge 2$. So $a_n^2 \ge 2$ for every $n$.

*(d) Nonincreasing.* For every $n$,

$$
a_{n+1} - a_n = \frac{1}{a_n} - \frac{a_n}{2} = \frac{2 - a_n^2}{2 a_n} .
$$

The numerator is at most $0$ by (c) and the denominator is positive by (b), so $a_{n+1} - a_n \le 0$.

*(e) The limit.* By (b) and (d), $(a_n)$ is nonincreasing and bounded below by $0$. By the nonincreasing case of monotone convergence (Session 6), $a_n \to L$ for some real $L$. From $a_n \gt 0$ and the rule for non-strict inequalities with the constant sequence $0$ (Session 5), $L \ge 0$. By the product rule, $a_n^2 \to L^2$, and from $a_n^2 \ge 2$ the same rule gives $L^2 \ge 2$. Since $0^2 = 0 \lt 2$, $L \ne 0$, so $L \gt 0$.

The tail $(a_{n+1})$ is a subsequence, so $a_{n+1} \to L$ (Session 6). The same sequence is $\frac{a_n}{2} + \frac{1}{a_n}$. Since $a_n \ne 0$ for every $n$ and $L \ne 0$, the sum, product and quotient rules (Session 5) give $\frac{a_n}{2} + \frac{1}{a_n} \to \frac{L}{2} + \frac{1}{L}$. By uniqueness of limits (Session 5), $L = \frac{L}{2} + \frac1L$. Subtracting $\frac{L}{2}$ gives $\frac{L}{2} = \frac1L$, and multiplying by $2L$ gives $L^2 = 2$.

*(f) Conclusion.* The sequence converges in $\mathbb{R}$, so it is a Cauchy sequence (Session 6). The Cauchy condition speaks only of the terms, all of which are rational by (b). Suppose some rational $q$ satisfies $a_n \to q$. By uniqueness of limits (Session 5), $q = L$, so $q^2 = 2$, contradicting (a). So $(a_n)$ is a Cauchy sequence of rationals with no rational limit: the Cauchy criterion fails in $\mathbb{Q}$.

**8.** *$r^n \to 0$.* Since $\lvert r \rvert = r \lt 1$, the geometric sequence theorem (Session 5) gives $r^n \to 0$.

*Successive differences.* Put $d_n = \lvert a_{n+1} - a_n \rvert$. Then $d_n \le r^{n-1} d_1$ for every $n$, with $r^0 = 1$. By induction: for $n = 1$ both sides are $d_1$. If $d_n \le r^{n-1} d_1$, then, since $r \ge 0$, $d_{n+1} \le r d_n \le r \cdot r^{n-1} d_1 = r^n d_1$.

*A bound on $\lvert a_m - a_n \rvert$.* Let $m \gt n$. Put $q = m - n \in \mathbb{N}$ (Session 3, Lemma 4(a)), and $b_i = a_{n-1+i}$ for $i \in \mathbb{N}$, where $n - 1$ is $0$ if $n = 1$ and lies in $\mathbb{N}$ otherwise (Session 3, Lemma 2). Then $b_1 = a_n$ and $b_{q+1} = a_m$, so (S5) of Session 3 gives $a_m - a_n = \sum_{i=1}^{q} (b_{i+1} - b_i)$. By the triangle inequality for finite sums (Session 5, Section 5.2, Part 9), $\lvert a_m - a_n \rvert \le \sum_{i=1}^{q} d_{n-1+i}$. By the bound above and the laws of powers (a) (Session 3), $d_{n-1+i} \le r^{n+i-2} d_1 = d_1 r^{n-1} r^{i-1}$, so (S3) and (S2) (Session 3) give $\lvert a_m - a_n \rvert \le d_1 r^{n-1} \sum_{i=1}^{q} r^{i-1}$, and $\sum_{i=1}^{q} r^{i-1} = \sum_{i=0}^{q-1} r^i$ by (S6). With $p = q - 1 \ge 0$, the geometric sum (Session 3, Section 3.7) gives $\sum_{i=0}^{p} r^i = \frac{1 - r^{p+1}}{1 - r} \le \frac{1}{1 - r}$, since $r^{p+1} \ge 0$ and $1 - r \gt 0$. Put $C = \frac{d_1}{1 - r} \ge 0$. Then

$$
\lvert a_m - a_n \rvert \le C r^{n-1} \quad \text{whenever } m \gt n .
$$

*Cauchy.* Let $\varepsilon \gt 0$. Since $r^n \to 0$ and $\frac{\varepsilon}{C + 1} \gt 0$, there exists $N'$ with $r^n \lt \frac{\varepsilon}{C+1}$ for every $n \ge N'$. Put $N = N' + 1$. Let $m, n \ge N$. If $m = n$, then $\lvert a_m - a_n \rvert = 0 \lt \varepsilon$. If $m \gt n$, then $n - 1 \ge N'$, so

$$
\lvert a_m - a_n \rvert \le C r^{n-1} \le (C + 1) r^{n-1} \lt (C + 1) \cdot \frac{\varepsilon}{C + 1} = \varepsilon .
$$

If $n \gt m$, exchange the roles of $m$ and $n$. So $(a_n)$ is a Cauchy sequence, and by the Cauchy criterion (Session 6) it converges.
