# Solutions to Session 3. Mathematical induction and finite sums

References to (R), (R0), (S1)-(S7), (P1)-(P3) and Lemmas 1-5 are to Session 3. "Laws of powers (a)-(f)" refers to the Corollary of that name in Section 3.6, and "sums of constants" to the Corollary $\sum_{k=1}^{n} c = nc$ there. In particular $1^m = 1$ for every $m \ge 0$, by laws of powers (f).

## Check

**1.** Row 4 is $1, 4, 6, 4, 1$ (Section 3.10). Row 5 begins and ends with $\binom{5}{0} = \binom{5}{5} = 1$. By Pascal's rule (Lemma 5 with $n = 4$),

$$
\binom{5}{1} = \binom{4}{0} + \binom{4}{1} = 1 + 4 = 5, \qquad \binom{5}{2} = \binom{4}{1} + \binom{4}{2} = 4 + 6 = 10,
$$

$$
\binom{5}{3} = \binom{4}{2} + \binom{4}{3} = 6 + 4 = 10, \qquad \binom{5}{4} = \binom{4}{3} + \binom{4}{4} = 4 + 1 = 5.
$$

So row 5 is $1, 5, 10, 10, 5, 1$. By the binomial theorem with $n = 5$,

$$
(a+b)^5 = a^5 + 5a^4 b + 10 a^3 b^2 + 10 a^2 b^3 + 5 a b^4 + b^5.
$$

At $a = b = 1$ every product $a^{5-k} b^k$ equals $1 \cdot 1 = 1$. The left side is $2^5$, and $2^2 = 4$, $2^3 = 8$, $2^4 = 16$, $2^5 = 32$ by (R). The right side is $1 + 5 + 10 + 10 + 5 + 1 = 32$. The two sides agree.

**2.** (a) By the geometric sum with $x = 1/2 \ne 1$ and $n = 5$, using $(1/2)^6 = 1/64$ (by laws of powers (b) and (f), $(1/2)^6 \cdot 2^6 = (\tfrac12 \cdot 2)^6 = 1^6 = 1$, so $(1/2)^6 = 1/2^6$, and $2^6 = 64$ by (R)),

$$
\sum_{k=0}^{5} (1/2)^k = \frac{1 - 1/64}{1 - 1/2} = \frac{63/64}{1/2} = \frac{63}{64} \cdot 2 = \frac{63}{32}.
$$

Adding directly over the common denominator $32$:

$$
1 + \frac12 + \frac14 + \frac18 + \frac1{16} + \frac1{32} = \frac{32 + 16 + 8 + 4 + 2 + 1}{32} = \frac{63}{32}.
$$

(b) Let $n \in \mathbb{N}$. By Lemma 1, $n \ge 1 \gt 0$, so $1/n \gt 0$; and $-1 \lt -0 = 0$ (negate $0 \lt 1$), so $1/n \gt -1$ and in particular $1/n \ge -1$. Bernoulli's inequality with $x = 1/n$ gives

$$
\Bigl(1 + \frac1n\Bigr)^n \ge 1 + n \cdot \frac1n = 1 + 1 = 2.
$$

**3.** Let $k \in \mathbb{N}$. Then $k \gt 0$ and $k + 1 \gt 0$, so $k$, $k + 1$ and $k(k+1)$ are nonzero. By the rule for adding fractions,

$$
\frac1k - \frac1{k+1} = \frac1k + \frac{-1}{k+1} = \frac{1 \cdot (k+1) + (-1) \cdot k}{k(k+1)} = \frac{1}{k(k+1)}.
$$

Put $a_k = -1/k$ for $k \in \mathbb{N}$. Then $a_{k+1} - a_k = -\frac1{k+1} + \frac1k = \frac1{k(k+1)}$. By telescoping (S5),

$$
\sum_{k=1}^{n} \frac{1}{k(k+1)} = \sum_{k=1}^{n} (a_{k+1} - a_k) = a_{n+1} - a_1 = -\frac{1}{n+1} + 1 = \frac{(n+1) - 1}{n+1} = \frac{n}{n+1}.
$$

For $n = 4$, over the common denominator $60$:

$$
\frac12 + \frac16 + \frac1{12} + \frac1{20} = \frac{30 + 10 + 5 + 3}{60} = \frac{48}{60} = \frac45,
$$

which is $n/(n+1)$ at $n = 4$.

**4.** By the binomial theorem with $a = b = 1$, and $1^{n-k} 1^k = 1 \cdot 1 = 1$,

$$
2^n = (1 + 1)^n = \sum_{k=0}^{n} \binom{n}{k} 1^{n-k} 1^k = \sum_{k=0}^{n} \binom{n}{k}.
$$

By the binomial theorem with $a = 1$ and $b = -1$,

$$
\bigl(1 + (-1)\bigr)^n = \sum_{k=0}^{n} \binom{n}{k} 1^{n-k} (-1)^k = \sum_{k=0}^{n} (-1)^k \binom{n}{k}.
$$

The left side is $0^n$. For $n \in \mathbb{N}$, $n - 1 \ge 0$ (Lemma 2, or $n - 1 = 0$ when $n = 1$), so by (R), $0^n = 0^{n-1} \cdot 0 = 0$. Hence the sum is $0$ for every $n \in \mathbb{N}$.

For $n = 0$ the sum is the single term $(-1)^0 \binom{0}{0} = 1$, in agreement with $0^0 = 1$. So the second statement is false for $n = 0$, which is why the exercise asks for $n \in \mathbb{N}$.

## Prove

**5.** Let $P(n)$ be the statement $\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$.

The division by $6$ is allowed: $6 \in \mathbb{N}$, so $6 \ge 1 \gt 0$ by Lemma 1.

Base case. The left side of $P(1)$ is $1^2 = 1$. The right side is $\frac{1 \cdot 2 \cdot 3}{6} = \frac66 = 1$.

Inductive step. Assume $P(n)$. By (R) and the induction hypothesis, writing $(n+1)^2 = \frac{6(n+1)^2}{6}$, adding fractions with the same denominator (Section 3.2) and using the distributive law,

$$
\sum_{k=1}^{n+1} k^2 = \frac{n(n+1)(2n+1)}{6} + (n+1)^2 = \frac{n(n+1)(2n+1) + 6(n+1)^2}{6} = \frac{(n+1)\bigl(n(2n+1) + 6(n+1)\bigr)}{6}.
$$

Inside the bracket, $n(2n+1) + 6(n+1) = 2n^2 + n + 6n + 6 = 2n^2 + 7n + 6$. Also

$$
(n+2)(2n+3) = 2n^2 + 3n + 4n + 6 = 2n^2 + 7n + 6.
$$

Since $2(n+1) + 1 = 2n + 3$,

$$
\sum_{k=1}^{n+1} k^2 = \frac{(n+1)(n+2)(2n+3)}{6} = \frac{(n+1)\bigl((n+1)+1\bigr)\bigl(2(n+1)+1\bigr)}{6},
$$

which is $P(n+1)$. By induction, $P(n)$ holds for every $n \in \mathbb{N}$.

**6.** Let $x \ge -1$, $x \ne 0$, and $n \in \mathbb{N}$ with $n \ge 2$. Then $n \ne 1$, so $m = n - 1 \in \mathbb{N}$ by Lemma 2, and $m \ge 1$ by Lemma 1.

By Bernoulli's inequality, $(1+x)^m \ge 1 + mx$. Adding $1$ to $x \ge -1$ gives $1 + x \ge 0$. Multiplying by $1 + x$, and using (R),

$$
(1+x)^n = (1+x)^m (1+x) \ge (1 + mx)(1+x) = 1 + (m+1)x + mx^2 = 1 + nx + mx^2.
$$

Since $x \ne 0$, $x^2 \gt 0$. Multiplying $0 \lt x^2$ by $m \gt 0$ gives $0 \lt mx^2$. Adding $1 + nx$ to both sides gives $1 + nx \lt 1 + nx + mx^2$. Together,

$$
(1+x)^n \ge 1 + nx + mx^2 \gt 1 + nx,
$$

so $(1+x)^n \gt 1 + nx$.

Both extra hypotheses are needed. For $n = 1$ the two sides are both $1 + x$. For $x = 0$ the two sides are both $1$.

**7.** Let $P(n)$ be the statement: for every $k$ with $0 \le k \le n$, $\binom{n}{k} \in \mathbb{N}$. We prove $P(n)$ for every $n \ge 0$ by induction from 0.

Base case. If $0 \le k \le 0$ then $k = 0$, since every element of $\mathbb{N}$ is at least $1$ (Lemma 1). And $\binom{0}{0} = 1 \in \mathbb{N}$.

Inductive step. Assume $P(n)$, and let $0 \le k \le n + 1$. There are three cases.
- $k = 0$. Then $\binom{n+1}{0} = 1 \in \mathbb{N}$.
- $k = n + 1$. Then $\binom{n+1}{n+1} = 1 \in \mathbb{N}$.
- $k \in \mathbb{N}$ and $k \ne n + 1$. If $n = 0$, then $k \le 1$ and $k \ge 1$ (Lemma 1) give $k = 1 = n + 1$, so this case does not occur. So $n \in \mathbb{N}$, and by Lemma 4(b), $k \le n$. By Pascal's rule (Lemma 5), $\binom{n+1}{k} = \binom{n}{k-1} + \binom{n}{k}$. Here $0 \le k - 1 \le n$ (as in the proof of Lemma 5) and $0 \le k \le n$, so both terms lie in $\mathbb{N}$ by $P(n)$. Their sum lies in $\mathbb{N}$ by Lemma 3.

These cases cover every $k$ with $0 \le k \le n+1$: either $k = 0$ or $k \in \mathbb{N}$. So $P(n+1)$ holds, and by induction $P(n)$ holds for every $n \ge 0$.

## Extend

**8.** (a) By induction on $n$. Let $P(n)$ be the statement: for all numbers $x_1, \dots, x_n$ with $0 \le x_k \le 1$ for every $k$, $\prod_{k=1}^{n} (1 - x_k) \ge 1 - \sum_{k=1}^{n} x_k$.

Base case. For $n = 1$ both sides equal $1 - x_1$.

Inductive step. Assume $P(n)$, and let $x_1, \dots, x_{n+1}$ be numbers with $0 \le x_k \le 1$ for every $k$. Write $A = \prod_{k=1}^{n} (1 - x_k)$ and $S = \sum_{k=1}^{n} x_k$. The numbers $x_1, \dots, x_n$ satisfy the hypotheses, so $A \ge 1 - S$ by $P(n)$. Since $x_{n+1} \le 1$, $1 - x_{n+1} \ge 0$. Multiplying by it, and using (R),

$$
\prod_{k=1}^{n+1} (1 - x_k) = A (1 - x_{n+1}) \ge (1 - S)(1 - x_{n+1}) = 1 - S - x_{n+1} + S x_{n+1}.
$$

Each $x_k \ge 0$, so $S \ge \sum_{k=1}^{n} 0 = 0$ by (S3) and (S2). Then $S x_{n+1} \ge 0$, a product of two numbers $\ge 0$. Adding $1 - S - x_{n+1}$ to both sides of $S x_{n+1} \ge 0$, and using (R) for the sum,

$$
1 - S - x_{n+1} + S x_{n+1} \ge 1 - (S + x_{n+1}) = 1 - \sum_{k=1}^{n+1} x_k.
$$

The two displays give $P(n+1)$.

(b) Let $-1 \le x \le 0$. Negating both inequalities gives $0 \le -x \le 1$, since $-0 = (-0) + 0 = 0 + (-0) = 0$ and $-(-1) = 1$. For $n = 0$ Bernoulli's inequality reads $1 \ge 1$. For $n \in \mathbb{N}$, apply (a) with $x_k = -x$ for every $k$. The left side is $\prod_{k=1}^{n} (1 + x) = (1+x)^n$. The sum is $\sum_{k=1}^{n} (-x) = n(-x) = -nx$, by sums of constants. So (a) gives

$$
(1 + x)^n \ge 1 - (-nx) = 1 + nx.
$$


(c) Let $-2 \le x \lt -1$, and put $y = 1 + x$. Adding $1$ to $-2 \le x$ and to $x \lt -1$ gives $-1 \le y \lt 0$.

*Claim: $-1 \le y^n \le 1$ for every $n \ge 0$.* By induction from 0. For $n = 0$, $y^0 = 1$; and $-1 \lt 0 \lt 1$, since negating $0 \lt 1$ gives $-1 \lt -0 = 0$ (as in (b)). Step: assume $-1 \le y^n \le 1$, and put $p = y^n$, so that $y^{n+1} = py$ by (R). There are two cases.
- $p \ge 0$. Multiplying $y \le 0$ by $p$ gives $py \le 0 \lt 1$. Multiplying $-1 \le y$ by $p$ gives $-p = (-1)p \le py$. Negating $p \le 1$ gives $-1 \le -p$, so $-1 \le py$.
- $p \lt 0$. Adding $-p$ to both sides of $p \lt 0$ gives $0 \lt -p$. Multiplying $y \lt 0$ by $-p \gt 0$ gives $-(py) = y(-p) \lt 0$, and adding $py$ to both sides gives $0 \lt py$, so $-1 \lt py$. Multiplying $-1 \le y$ by $-p \gt 0$ gives $p = (-1)(-p) \le y(-p) = -(py)$, and negating gives $py \le -p$. Negating $-1 \le p$ gives $-p \le 1$. So $py \le 1$.

In both cases $-1 \le y^{n+1} \le 1$, which proves the claim.

*Bernoulli's inequality.* For $n = 0$ both sides are $1$. For $n = 1$ both sides are $1 + x$. Let $n \in \mathbb{N}$ with $n \ne 1$. Then $n - 1 \in \mathbb{N}$ by Lemma 2, so $n - 1 \ge 1$ by Lemma 1, and $n \ge 2$. Since $x \lt -1$ and $n \gt 0$, $nx \lt n \cdot (-1) = -n$, so $1 + nx \lt 1 - n$. Negating $n \ge 2$ gives $-n \le -2$, so $1 - n \le 1 - 2 = -1$. With the claim,

$$
1 + nx \lt 1 - n \le -1 \le y^n = (1 + x)^n .
$$

So $(1 + x)^n \ge 1 + nx$ for every $n \ge 0$. Together with Bernoulli's inequality for $x \ge -1$, the inequality holds for every $n \ge 0$ whenever $x \ge -2$. So $x \ge -1$ is not the largest range that works for every $n$ at once. It is the range that the inductive step of Section 3.9 can carry, since that step multiplies by $1 + x$ and needs $1 + x \ge 0$.
