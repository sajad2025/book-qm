# Session 5. Limits of real sequences

*Theorem. Builds on Sessions 3 and 4.*

**Claim.** The absolute value satisfies the triangle inequality. A real sequence has at most one limit, convergent sequences are bounded, limits respect sums, products, quotients and non-strict inequalities, the squeeze rule holds, and $r^n \to 0$ when $\lvert r \rvert \lt 1$.

## 5.1 Recall

The proofs use the following, and nothing else.

From Session 2: functions, the negation of quantified statements, and proof by contradiction and by contraposition.

From Session 3:
- Induction, also in the form that starts from $0$. A statement about "$k \ge 0$" concerns $k = 0$ and every $k \in \mathbb{N}$.
- Every $n \in \mathbb{N}$ satisfies $n \ge 1$, so $n \gt 0$. If $n \in \mathbb{N}$ and $n \ne 1$, then $n - 1 \in \mathbb{N}$. If $m, n \in \mathbb{N}$, then $m + n \in \mathbb{N}$; if moreover $m \lt n$, then $n - m \in \mathbb{N}$ and $m + 1 \le n$. If $k, n \in \mathbb{N}$ and $k \le n + 1$, then $k \le n$ or $k = n + 1$.
- For real $x$, $y$ and $m, n \ge 0$: $x^0 = 1$, $x^{n+1} = x^n x$, $x^{m+n} = x^m x^n$ and $(xy)^n = x^n y^n$; if $x \gt 0$ then $x^n \gt 0$; and $1^n = 1$.
- Finite sums $\sum_{k=1}^{n} x_k$, defined by recursion, with $\sum_{k=1}^{n+1} x_k = \sum_{k=1}^{n} x_k + x_{n+1}$ (the rule (R)).
- *Bernoulli's inequality*: $(1 + x)^n \ge 1 + nx$ for every $x \ge -1$ and every $n \ge 0$.

From Session 4, for real $x$, $y$, $z$, $w$:
- The field rules, cited as 4.2(a) to 4.2(h). Among them $(-x)y = -(xy)$, $(-1)y = -y$ and $(-x)(-y) = xy$, so $(-1)(-1) = 1$.
- Exactly one of $x \lt y$, $x = y$, $x \gt y$ holds (*trichotomy*), so "not $x \lt y$" means $y \le x$. Both $\lt$ and $\le$ are transitive.
- $x \lt y$ gives $x + z \lt y + z$. $x \lt y$ with $z \le w$ gives $x + z \lt y + w$, and $x \le y$ with $z \le w$ gives $x + z \le y + w$.
- $x \lt y$ with $z \gt 0$ gives $xz \lt yz$, and $x \lt y$ with $z \lt 0$ gives $xz \gt yz$. $x \le y$ with $z \ge 0$ gives $xz \le yz$: for $z \gt 0$ this is 4.3(b) with $\le$, and for $z = 0$ both sides are $0$ by 4.2(c). In particular a product of two numbers $\ge 0$ is $\ge 0$.
- $x \gt 0$ and $y \gt 0$ give $xy \gt 0$, and $x \ne 0$ gives $x^2 \gt 0$, so $1 \gt 0$.
- $x \gt 0$ gives $1/x \gt 0$. $0 \lt x \lt y$ gives $0 \lt 1/y \lt 1/x$, and $0 \lt x \le y$ gives $1/y \le 1/x$ (the *rule for reciprocals*).
- $0 \lt 1 \lt 2$ and $0 \lt \tfrac12$; and $x \lt y$ gives $x \lt \tfrac{x + y}{2} \lt y$ (4.3(g)). So for $\varepsilon \gt 0$, $0 \lt \varepsilon/2 \lt \varepsilon$, and $\varepsilon/2 + \varepsilon/2 = \varepsilon$.
- The *Archimedean property*: for every real $x$ there exists $n \in \mathbb{N}$ with $n \gt x$.

## 5.2 Absolute value

A limit says that numbers become close. Closeness is measured by the absolute value.

**Definition.** The **absolute value** of a real number $x$ is

$$
\lvert x \rvert = \begin{cases} x & \text{if } x \ge 0, \\ -x & \text{if } x \lt 0. \end{cases}
$$

The **distance** between $x$ and $y$ is $\lvert x - y \rvert$. For real $s$ and $t$, $\max\{s, t\}$ is $t$ if $s \le t$ and $s$ otherwise. It is at least $s$ and at least $t$: in the second case $t \lt s$ by trichotomy. For three numbers, $\max\{s, t, u\} = \max\{s, \max\{t, u\}\}$, which is at least each of $s$, $t$, $u$.

**Lemma (properties of the absolute value).** For all real $x$, $y$, $z$, $w$ and $r$, and every $n \in \mathbb{N}$:
1. $\lvert x \rvert \ge 0$, $\lvert 0 \rvert = 0$, and $\lvert x \rvert \gt 0$ when $x \ne 0$;
2. $\lvert -x \rvert = \lvert x \rvert$ and $-\lvert x \rvert \le x \le \lvert x \rvert$;
3. if $z \ge 0$ and $z = w$ or $z = -w$, then $z = \lvert w \rvert$;
4. $\lvert xy \rvert = \lvert x \rvert \lvert y \rvert$, and $\lvert 1/x \rvert = 1/\lvert x \rvert$ when $x \ne 0$;
5. $\lvert x \rvert \lt r$ if and only if $-r \lt x \lt r$, and $\lvert x \rvert \le r$ if and only if $-r \le x \le r$;
6. $\lvert x + y \rvert \le \lvert x \rvert + \lvert y \rvert$ (the **triangle inequality**);
7. $\bigl\lvert \lvert x \rvert - \lvert y \rvert \bigr\rvert \le \lvert x - y \rvert$ (the **reverse triangle inequality**);
8. $\lvert x^n \rvert = \lvert x \rvert^n$;
9. $\bigl\lvert \sum_{k=1}^{n} x_k \bigr\rvert \le \sum_{k=1}^{n} \lvert x_k \rvert$ for all real $x_1, \dots, x_n$ (the triangle inequality for finite sums).

*Proof.* Part 1. If $x \ge 0$ then $\lvert x \rvert = x \ge 0$, in particular $\lvert 0 \rvert = 0$, and $\lvert x \rvert \gt 0$ when $x \gt 0$. If $x \lt 0$, adding $-x$ to both sides gives $0 \lt -x = \lvert x \rvert$. So $\lvert x \rvert \ge 0$ always, and $\lvert x \rvert \gt 0$ whenever $x \ne 0$.

Part 2. If $x \gt 0$ then $-x \lt 0$, so $\lvert -x \rvert = -(-x) = x = \lvert x \rvert$. If $x = 0$ both sides are $0$. If $x \lt 0$ then $-x \gt 0$, so $\lvert -x \rvert = -x = \lvert x \rvert$. For the inequalities: if $x \ge 0$ then $x = \lvert x \rvert$ and $-\lvert x \rvert = -x \le 0 \le x$. If $x \lt 0$ then $-\lvert x \rvert = x$, and $x \lt 0 \lt -x = \lvert x \rvert$.

Part 3. If $z = w$, then $w \ge 0$ and $\lvert w \rvert = w = z$. If $z = -w$, then $w = -z \le 0$; when $w \lt 0$, $\lvert w \rvert = -w = z$, and when $w = 0$, $z = 0 = \lvert w \rvert$.

Part 4. By the definition, $\lvert x \rvert = sx$ and $\lvert y \rvert = ty$ with each of $s, t$ equal to $1$ or $-1$, using $-x = (-1)x$ (Session 4). Then $\lvert x \rvert \lvert y \rvert = (st)(xy)$ with $st$ equal to $1$ or $-1$, since $(-1)(-1) = 1$ (Session 4). Also $\lvert x \rvert \lvert y \rvert \ge 0$, as a product of two numbers that are $\ge 0$ by Part 1. Part 3 with $z = \lvert x \rvert \lvert y \rvert$ and $w = xy$ gives $\lvert x \rvert \lvert y \rvert = \lvert xy \rvert$. If $x \ne 0$, then $\lvert x \rvert \, \lvert 1/x \rvert = \lvert x \cdot (1/x) \rvert = \lvert 1 \rvert = 1$, and $\lvert x \rvert \ne 0$ by Part 1, so $\lvert 1/x \rvert = 1/\lvert x \rvert$ by 4.2(e).

Part 5. Suppose $\lvert x \rvert \lt r$. By Part 2, $x \le \lvert x \rvert \lt r$, and $-x \le \lvert -x \rvert = \lvert x \rvert \lt r$; adding $x - r$ to both sides of $-x \lt r$ gives $-r \lt x$. Conversely, suppose $-r \lt x \lt r$. If $x \ge 0$ then $\lvert x \rvert = x \lt r$. If $x \lt 0$, adding $r - x$ to both sides of $-r \lt x$ gives $-x \lt r$, that is, $\lvert x \rvert \lt r$. The same argument with $\le$ throughout proves the second statement.

Part 6. By Part 2, $-\lvert x \rvert \le x \le \lvert x \rvert$ and $-\lvert y \rvert \le y \le \lvert y \rvert$. Adding gives $-(\lvert x \rvert + \lvert y \rvert) \le x + y \le \lvert x \rvert + \lvert y \rvert$, and Part 5 with $r = \lvert x \rvert + \lvert y \rvert$ gives $\lvert x + y \rvert \le \lvert x \rvert + \lvert y \rvert$.

Part 7. Since $x = (x - y) + y$, Part 6 gives $\lvert x \rvert \le \lvert x - y \rvert + \lvert y \rvert$, so $\lvert x \rvert - \lvert y \rvert \le \lvert x - y \rvert$. Exchanging $x$ and $y$ gives $\lvert y \rvert - \lvert x \rvert \le \lvert y - x \rvert$, and $\lvert y - x \rvert = \lvert -(x - y) \rvert = \lvert x - y \rvert$ by Part 2. By 4.3(a) and 4.2(d), $-\lvert x - y \rvert \le -(\lvert y \rvert - \lvert x \rvert) = \lvert x \rvert - \lvert y \rvert$. So $-\lvert x - y \rvert \le \lvert x \rvert - \lvert y \rvert \le \lvert x - y \rvert$, and Part 5 with $r = \lvert x - y \rvert$ finishes.

Part 8. Induction on $n$ (Session 3). For $n = 1$ both sides are $\lvert x \rvert$. If $\lvert x^n \rvert = \lvert x \rvert^n$, then Part 4 gives $\lvert x^{n+1} \rvert = \lvert x^n x \rvert = \lvert x^n \rvert \, \lvert x \rvert = \lvert x \rvert^n \lvert x \rvert = \lvert x \rvert^{n+1}$.

Part 9. Induction on $n$ (Session 3). For $n = 1$ both sides are $\lvert x_1 \rvert$. If the inequality holds for $n$, then the rule (R), Part 6 and the induction hypothesis give

$$
\Bigl\lvert \sum_{k=1}^{n+1} x_k \Bigr\rvert = \Bigl\lvert \sum_{k=1}^{n} x_k + x_{n+1} \Bigr\rvert \le \Bigl\lvert \sum_{k=1}^{n} x_k \Bigr\rvert + \lvert x_{n+1} \rvert \le \sum_{k=1}^{n} \lvert x_k \rvert + \lvert x_{n+1} \rvert = \sum_{k=1}^{n+1} \lvert x_k \rvert .
$$

∎

For example, $\lvert -1 \rvert = 1$ by Part 2, so Part 8 and $1^n = 1$ (Session 3) give $\lvert (-1)^n \rvert = 1^n = 1$ for every $n \in \mathbb{N}$.

Two consequences are used in almost every proof below. First, for all real $a$, $b$, $c$, Part 6 with $x = a - b$ and $y = b - c$ gives

$$
\lvert a - c \rvert \le \lvert a - b \rvert + \lvert b - c \rvert .
$$

Second, for all real $x$, $c$ and $r$, $\lvert x - c \rvert \lt r$ holds if and only if $c - r \lt x \lt c + r$. Indeed, Part 5 says that $\lvert x - c \rvert \lt r$ holds if and only if $-r \lt x - c \lt r$, and adding $c$ to each part, or $-c$ to go back, turns this into $c - r \lt x \lt c + r$. The same holds with $\le$ in place of $\lt$.

## 5.3 Sequences and their limits

A real sequence is a function $a : \mathbb{N} \to \mathbb{R}$ (Session 3, Section 3.5). Its value $a_n$ at $n$ is called its $n$-th **term**, and the sequence is written $(a_n)$.

**Definition.** Let $(a_n)$ be a real sequence and $a$ a real number. The sequence **converges to** $a$ if for every $\varepsilon \gt 0$ there exists $N \in \mathbb{N}$ such that

$$
\lvert a_n - a \rvert \lt \varepsilon \quad \text{for every } n \ge N .
$$

Then $a$ is a **limit** of $(a_n)$, and we write $a_n \to a$. The sequence **converges** if it converges to some real number, and **diverges** otherwise.

The number $N$ may depend on $\varepsilon$: a smaller $\varepsilon$ usually needs a larger $N$. If some $N$ works for a given $\varepsilon$, then every $N' \ge N$ works too, because $n \ge N'$ gives $n \ge N$. By the rules for negation in Session 2, $(a_n)$ does not converge to $a$ exactly when

$$
\exists \varepsilon \gt 0 \;\; \forall N \in \mathbb{N} \;\; \exists n \ge N : \; \lvert a_n - a \rvert \ge \varepsilon .
$$

**Example (constant sequences).** Let $a_n = c$ for every $n$. For every $\varepsilon \gt 0$, take $N = 1$. Then $\lvert a_n - c \rvert = 0 \lt \varepsilon$ for every $n \ge 1$. So $a_n \to c$: the constant sequence $(c)$ converges to $c$.

**Example ($1/n \to 0$).** Let $\varepsilon \gt 0$. By the Archimedean property (Session 4) there exists $N \in \mathbb{N}$ with $N \gt 1/\varepsilon$. For $n \ge N$ we have $n \ge N \gt 1/\varepsilon \gt 0$, so the rule for reciprocals gives $1/n \lt 1/(1/\varepsilon)$, and $1/(1/\varepsilon) = \varepsilon$ by 4.2(e). Since $n \gt 0$, $1/n \gt 0$, so $\lvert 1/n - 0 \rvert = 1/n \lt \varepsilon$. So $1/n \to 0$.

Two lemmas shorten the proofs that follow. The first lets a proof end with a bound $C\varepsilon$ in place of $\varepsilon$.

**Lemma ($C\varepsilon$ is enough).** Let $C \gt 0$ be fixed. Suppose that for every $\varepsilon \gt 0$ there exists $N \in \mathbb{N}$ with $\lvert a_n - a \rvert \le C\varepsilon$ for every $n \ge N$. Then $a_n \to a$.

*Proof.* Let $\varepsilon \gt 0$. Since $2 \gt 0$ and $C \gt 0$, $2C \gt 0$ and $1/(2C) \gt 0$, so $\varepsilon' = \varepsilon / (2C) \gt 0$. The hypothesis applied to $\varepsilon'$ gives $N$ with $\lvert a_n - a \rvert \le C \varepsilon' = \varepsilon/2$ for every $n \ge N$. Since $\varepsilon/2 \lt \varepsilon$ (Section 5.1), $\lvert a_n - a \rvert \lt \varepsilon$ for every $n \ge N$. ∎

The second says that convergence depends only on the terms from some point on.

**Lemma (tails).** Let $k \ge 0$ and $b_n = a_{n+k}$ for every $n \in \mathbb{N}$. Then $a_n \to a$ if and only if $b_n \to a$.

Here $n + k \in \mathbb{N}$: it is $n$ if $k = 0$, and a sum of two natural numbers otherwise (Session 3). So $(b_n)$ is a real sequence.

*Proof.* Suppose $a_n \to a$, and let $\varepsilon \gt 0$. Take $N$ with $\lvert a_n - a \rvert \lt \varepsilon$ for every $n \ge N$. For $n \ge N$ we have $n + k \ge n \ge N$, so $\lvert b_n - a \rvert = \lvert a_{n+k} - a \rvert \lt \varepsilon$.

Conversely, suppose $b_n \to a$, and let $\varepsilon \gt 0$. Take $N$ with $\lvert b_n - a \rvert \lt \varepsilon$ for every $n \ge N$, and put $N' = N + k$, a natural number as above. Let $n \ge N'$, and put $m = n - k$. If $k = 0$, then $m = n \in \mathbb{N}$. If $k \in \mathbb{N}$, then $n \ge N + k \gt k$ because $N \gt 0$, so $m \in \mathbb{N}$ (Session 3). In both cases subtracting $k$ from $n \ge N + k$ gives $m \ge N$, so $\lvert a_n - a \rvert = \lvert b_m - a \rvert \lt \varepsilon$. ∎

Now suppose two sequences agree from some index $K \in \mathbb{N}$ on: $a'_n = a_n$ for every $n \ge K$. Put $k = K - 1$, which is $0$ if $K = 1$ and lies in $\mathbb{N}$ otherwise (Session 3). For every $n \in \mathbb{N}$, $n + k \ge 1 + k = K$, so both sequences have the same tail $b_n = a_{n+k} = a'_{n+k}$. The lemma, applied twice, gives $a_n \to a$ if and only if $b_n \to a$, if and only if $a'_n \to a$. So changing finitely many terms changes neither whether a sequence converges nor its limit.

## 5.4 A sequence has at most one limit

**Theorem (uniqueness of limits).** If $a_n \to a$ and $a_n \to b$, then $a = b$.

*Proof.* We argue by contradiction (Session 2). Suppose $a \ne b$. Then $a - b \ne 0$, since $a - b = 0$ would give $a = b$ on adding $b$. So $\lvert a - b \rvert \gt 0$ by Section 5.2, Part 1, and $\varepsilon = \lvert a - b \rvert / 2 \gt 0$, with $\varepsilon + \varepsilon = \lvert a - b \rvert$ (Section 5.1). Take $N_1$ with $\lvert a_n - a \rvert \lt \varepsilon$ for every $n \ge N_1$, and $N_2$ with $\lvert a_n - b \rvert \lt \varepsilon$ for every $n \ge N_2$. Let $n = \max\{N_1, N_2\}$. Then

$$
\lvert a - b \rvert \le \lvert a - a_n \rvert + \lvert a_n - b \rvert \lt \varepsilon + \varepsilon = \lvert a - b \rvert ,
$$

where the first step is the first consequence in Section 5.2 and $\lvert a - a_n \rvert = \lvert a_n - a \rvert$ by Section 5.2, Part 2. So $\lvert a - b \rvert \lt \lvert a - b \rvert$, which trichotomy forbids. Hence $a = b$. ∎

The theorem justifies speaking of *the* limit of a convergent sequence, written $\lim_{n \to \infty} a_n$.

## 5.5 Convergent sequences are bounded

**Definition.** A real sequence $(a_n)$ is **bounded** if there exists a real $M$ with $\lvert a_n \rvert \le M$ for every $n \in \mathbb{N}$. It is **unbounded** if it is not bounded: for every real $M$ there exists $n$ with $\lvert a_n \rvert \gt M$.

The first terms of any sequence are bounded.

**Lemma (finitely many terms).** For every real sequence $(a_n)$ and every $m \in \mathbb{N}$ there exists $B \ge 0$ with $\lvert a_k \rvert \le B$ for every $k \in \mathbb{N}$ with $k \le m$.

*Proof.* Induction on $m$ (Session 3). For $m = 1$, take $B = \lvert a_1 \rvert$, which is $\ge 0$ by Section 5.2, Part 1; a natural number $k \le 1$ is $1$, since $k \ge 1$ (Session 3). Suppose $B$ works for $m$, and put $B' = \max\{B, \lvert a_{m+1} \rvert\} \ge B \ge 0$. Let $k \in \mathbb{N}$ with $k \le m + 1$. By Session 3, $k \le m$ or $k = m + 1$. In the first case $\lvert a_k \rvert \le B \le B'$; in the second $\lvert a_k \rvert = \lvert a_{m+1} \rvert \le B'$. ∎

**Theorem (convergent implies bounded).** If $a_n \to a$, there exists $M \gt 0$ with $\lvert a_n \rvert \le M$ for every $n$.

*Proof.* Apply the definition of convergence with $\varepsilon = 1$: there exists $N$ with $\lvert a_n - a \rvert \lt 1$ for every $n \ge N$. For such $n$, the triangle inequality gives

$$
\lvert a_n \rvert = \lvert (a_n - a) + a \rvert \le \lvert a_n - a \rvert + \lvert a \rvert \lt 1 + \lvert a \rvert .
$$

If $N = 1$, put $M = 1 + \lvert a \rvert$; every $n$ satisfies $n \ge 1 = N$. If $N \ne 1$, then $N - 1 \in \mathbb{N}$ (Session 3). Take $B$ as in the lemma with $m = N - 1$, and put $M = \max\{B, 1 + \lvert a \rvert\}$. Let $n \in \mathbb{N}$. If $n \ge N$, then $\lvert a_n \rvert \lt 1 + \lvert a \rvert \le M$. Otherwise $n \lt N$ by trichotomy, so $n + 1 \le N$ (Session 3) and $n \le N - 1$, and $\lvert a_n \rvert \le B \le M$. In both cases $M \ge 1 + \lvert a \rvert \ge 1 \gt 0$, since $\lvert a \rvert \ge 0$. ∎

**What fails: the converse.** A bounded sequence need not converge. Let $a_n = (-1)^n$. By Section 5.2, $\lvert a_n \rvert = 1$ for every $n$, so the sequence is bounded, with $M = 1$. Suppose $a_n \to a$. Take $N$ with $\lvert a_n - a \rvert \lt 1$ for every $n \ge N$. Since $a_{N+1} = (-1)^N (-1) = -a_N$ (Sessions 3 and 4), $\lvert a_N - a_{N+1} \rvert = \lvert 2 a_N \rvert = \lvert 2 \rvert \, \lvert a_N \rvert = 2$, by Section 5.2, Part 4 and $\lvert 2 \rvert = 2$. But

$$
2 = \lvert a_N - a_{N+1} \rvert \le \lvert a_N - a \rvert + \lvert a - a_{N+1} \rvert \lt 1 + 1 = 2 ,
$$

where the first step is the first consequence in Section 5.2, and $\lvert a - a_{N+1} \rvert = \lvert a_{N+1} - a \rvert \lt 1$ by Section 5.2, Part 2, since $N + 1 \ge N$. This is a contradiction. So $((-1)^n)$ diverges. By contraposition (Session 2), the theorem also says that an unbounded sequence diverges.

## 5.6 Sums and products

**Theorem (sum and product rules).** Suppose $a_n \to a$ and $b_n \to b$, and let $c$ be real. Then
1. $a_n + b_n \to a + b$;
2. $a_n b_n \to ab$;
3. $c a_n \to ca$ and $a_n - b_n \to a - b$.

*Proof.* Part 1. Let $\varepsilon \gt 0$. Take $N_1$ with $\lvert a_n - a \rvert \lt \varepsilon$ for every $n \ge N_1$, and $N_2$ with $\lvert b_n - b \rvert \lt \varepsilon$ for every $n \ge N_2$. Let $N = \max\{N_1, N_2\}$. For every $n \ge N$, the triangle inequality gives

$$
\lvert (a_n + b_n) - (a + b) \rvert = \lvert (a_n - a) + (b_n - b) \rvert \le \lvert a_n - a \rvert + \lvert b_n - b \rvert \lt 2\varepsilon .
$$

The lemma "$C\varepsilon$ is enough" (Section 5.3) with $C = 2$ gives $a_n + b_n \to a + b$.

Part 2. By Section 5.5 there exists $M \gt 0$ with $\lvert a_n \rvert \le M$ for every $n$. Adding and subtracting $a_n b$,

$$
a_n b_n - ab = a_n (b_n - b) + b (a_n - a) .
$$

Let $\varepsilon \gt 0$, and take $N_1$, $N_2$ and $N = \max\{N_1, N_2\}$ as in Part 1. For every $n \ge N$, the triangle inequality and Section 5.2, Part 4 give

$$
\lvert a_n b_n - ab \rvert \le \lvert a_n \rvert \, \lvert b_n - b \rvert + \lvert b \rvert \, \lvert a_n - a \rvert \le M\varepsilon + \lvert b \rvert \varepsilon = (M + \lvert b \rvert)\,\varepsilon .
$$

The second step bounds each term. Multiplying $\lvert a_n \rvert \le M$ by $\lvert b_n - b \rvert \ge 0$, and then $\lvert b_n - b \rvert \lt \varepsilon$ by $M \gt 0$, gives $\lvert a_n \rvert \, \lvert b_n - b \rvert \le M \lvert b_n - b \rvert \le M\varepsilon$. Multiplying $\lvert a_n - a \rvert \le \varepsilon$ by $\lvert b \rvert \ge 0$ gives $\lvert b \rvert \, \lvert a_n - a \rvert \le \lvert b \rvert \varepsilon$. Here $M + \lvert b \rvert \gt 0$, so the lemma "$C\varepsilon$ is enough" with $C = M + \lvert b \rvert$ gives $a_n b_n \to ab$.

Part 3. The constant sequence $(c)$ converges to $c$ (Section 5.3), so Part 2 gives $c a_n \to ca$. With $c = -1$, $-b_n \to -b$, and Part 1 gives $a_n - b_n = a_n + (-b_n) \to a - b$. ∎

Induction carries the sum and product rules to powers and polynomials. A **polynomial** with real **coefficients** $c_0, \dots, c_m$, where $m \ge 0$, is the function $p : \mathbb{R} \to \mathbb{R}$ with $p(x) = \sum_{k=0}^{m} c_k x^k = c_0 + c_1 x + \dots + c_m x^m$ (sums from $0$, Session 3, Section 3.6).

**Corollary (powers and polynomials).** If $a_n \to a$, then $a_n^k \to a^k$ for every $k \in \mathbb{N}$. If $p$ is a polynomial with real coefficients, then $p(a_n) \to p(a)$.

*Proof.* Induction on $k$ (Session 3). For $k = 1$ the statement is the hypothesis. If $a_n^k \to a^k$, then $a_n^{k+1} = a_n^k a_n \to a^k a = a^{k+1}$ by the product rule. For the polynomial, induction on $m$ from $0$ (Session 3). For $m = 0$, $p(x) = c_0 x^0 = c_0$, so $p(a_n) = c_0$ is a constant sequence and converges to $c_0 = p(a)$. Suppose the statement holds for every polynomial with coefficients $c_0, \dots, c_m$, and let $p$ have coefficients $c_0, \dots, c_{m+1}$. By (R0) (Session 3), $p(x) = q(x) + c_{m+1} x^{m+1}$, where $q$ is the polynomial with coefficients $c_0, \dots, c_m$. Then $q(a_n) \to q(a)$ by the induction hypothesis, $c_{m+1} a_n^{m+1} \to c_{m+1} a^{m+1}$ by the first statement and Part 3, and the sum rule gives $p(a_n) \to p(a)$. ∎

## 5.7 Quotients

A quotient $a_n / b_n$ needs $b_n \ne 0$. The first lemma shows that a sequence with a nonzero limit stays away from zero from some point on.

**Lemma (away from zero).** If $b_n \to b$ and $b \ne 0$, there exists $N_0$ with $\lvert b_n \rvert \gt \lvert b \rvert / 2$ for every $n \ge N_0$. In particular $b_n \ne 0$ for every $n \ge N_0$.

*Proof.* Here $\lvert b \rvert \gt 0$ by Section 5.2, Part 1, so $\lvert b \rvert / 2 \gt 0$. Take $N_0$ with $\lvert b_n - b \rvert \lt \lvert b \rvert / 2$ for every $n \ge N_0$. For such $n$,

$$
\lvert b \rvert = \lvert (b - b_n) + b_n \rvert \le \lvert b - b_n \rvert + \lvert b_n \rvert \lt \frac{\lvert b \rvert}{2} + \lvert b_n \rvert ,
$$

using $\lvert b - b_n \rvert = \lvert b_n - b \rvert$ (Section 5.2, Part 2). Subtracting $\lvert b \rvert / 2$ from both sides gives $\lvert b_n \rvert \gt \lvert b \rvert / 2 \gt 0$. So $b_n \ne 0$, since $b_n = 0$ would give $\lvert b_n \rvert = 0$ (Section 5.2, Part 1). ∎

**Theorem (quotient rule).** Suppose $a_n \to a$ and $b_n \to b$, with $b \ne 0$ and $b_n \ne 0$ for every $n$. Then $1/b_n \to 1/b$ and $a_n / b_n \to a/b$.

*Proof.* Take $N_0$ as in the lemma. For $n \ge N_0$,

$$
\left\lvert \frac{1}{b_n} - \frac{1}{b} \right\rvert = \left\lvert \frac{b - b_n}{b_n b} \right\rvert = \frac{\lvert b_n - b \rvert}{\lvert b_n \rvert \, \lvert b \rvert} \le \frac{\lvert b_n - b \rvert}{(\lvert b \rvert / 2) \, \lvert b \rvert} = \frac{2}{\lvert b \rvert^2} \, \lvert b_n - b \rvert .
$$

The first step is 4.2(h). The second uses Section 5.2, Parts 2 and 4. For the third, multiplying $\lvert b_n \rvert \gt \lvert b \rvert / 2$ by $\lvert b \rvert \gt 0$ gives $\lvert b_n \rvert \, \lvert b \rvert \gt (\lvert b \rvert / 2) \lvert b \rvert \gt 0$; the rule for reciprocals gives $1/(\lvert b_n \rvert \, \lvert b \rvert) \lt 1/((\lvert b \rvert / 2) \lvert b \rvert)$; and multiplying by $\lvert b_n - b \rvert \ge 0$ gives the third step. Let $\varepsilon \gt 0$, and take $N_1$ with $\lvert b_n - b \rvert \lt \varepsilon$ for every $n \ge N_1$. For $n \ge \max\{N_0, N_1\}$, multiplying by $2/\lvert b \rvert^2 \gt 0$,

$$
\left\lvert \frac{1}{b_n} - \frac{1}{b} \right\rvert \le \frac{2}{\lvert b \rvert^2} \, \varepsilon ,
$$

and the lemma "$C\varepsilon$ is enough" with $C = 2/\lvert b \rvert^2$ gives $1/b_n \to 1/b$. Then $a_n / b_n = a_n \cdot (1/b_n) \to a \cdot (1/b) = a/b$ by the product rule. ∎

If $b \ne 0$ but some terms $b_n$ vanish, the lemma shows that they all have $n \lt N_0$. Put $k = N_0 - 1 \ge 0$. The sequences $n \mapsto a_{n+k}$ and $n \mapsto b_{n+k}$ converge to $a$ and $b$ by the lemma on tails (Section 5.3), and $b_{n+k} \ne 0$ for every $n$, since $n + k \ge N_0$. The theorem applies to them.

**What fails: a zero limit in the denominator.** Let $b_n = 1/n$, so $b_n \ne 0$ for every $n$ and $b_n \to 0$. Then $1/b_n = n$. For every real $M$ the Archimedean property gives $n \in \mathbb{N}$ with $n \gt M$, and $\lvert n \rvert = n$ since $n \gt 0$. So $(n)$ is unbounded, and by Section 5.5 it diverges. The hypothesis $b \ne 0$ cannot be dropped.

## 5.8 Limits preserve non-strict inequalities

**Theorem (limits and $\le$).** Suppose $a_n \to a$ and $b_n \to b$, and that there exists $K \in \mathbb{N}$ with $a_n \le b_n$ for every $n \ge K$. Then $a \le b$.

*Proof.* Suppose instead that $a \gt b$. Then $a - b \gt 0$ (Session 4), so $\varepsilon = (a - b)/2 \gt 0$, and

$$
a - \varepsilon = \frac{2a - (a - b)}{2} = \frac{a + b}{2} = \frac{2b + (a - b)}{2} = b + \varepsilon .
$$

Take $N_1$ with $\lvert a_n - a \rvert \lt \varepsilon$ for every $n \ge N_1$; by the second consequence in Section 5.2, $a_n \gt a - \varepsilon$ for these $n$. Take $N_2$ with $\lvert b_n - b \rvert \lt \varepsilon$ for every $n \ge N_2$; then $b_n \lt b + \varepsilon$ for these $n$. Let $n = \max\{K, N_1, N_2\}$. Then

$$
b_n \lt b + \varepsilon = a - \varepsilon \lt a_n ,
$$

which contradicts $a_n \le b_n$ by trichotomy. So $a \le b$. ∎

**Corollary.** If $a_n \to a$, $K \in \mathbb{N}$ and $a_n \le c$ for every $n \ge K$, then $a \le c$. If $a_n \ge c$ for every $n \ge K$, then $a \ge c$.

*Proof.* Apply the theorem with the constant sequence $(c)$, which converges to $c$ (Section 5.3), as $(b_n)$ in the first case and as $(a_n)$ in the second. ∎

**What fails: strict inequalities.** Let $a_n = 0$ and $b_n = 1/n$. Then $a_n \lt b_n$ for every $n$, but both limits are $0$ (Section 5.3), so $\lim_{n \to \infty} a_n \lt \lim_{n \to \infty} b_n$ is false. A strict inequality between terms gives only a non-strict inequality between limits.

## 5.9 The squeeze rule

**Theorem (squeeze rule).** Suppose $a_n \to L$ and $b_n \to L$, and that there exists $K \in \mathbb{N}$ with $a_n \le c_n \le b_n$ for every $n \ge K$. Then $c_n \to L$.

The sequence $(c_n)$ is not assumed to converge; the theorem proves that it does.

*Proof.* Let $\varepsilon \gt 0$. Take $N_1$ with $\lvert a_n - L \rvert \lt \varepsilon$ for every $n \ge N_1$, and $N_2$ with $\lvert b_n - L \rvert \lt \varepsilon$ for every $n \ge N_2$. Let $N = \max\{K, N_1, N_2\}$. For every $n \ge N$, the second consequence in Section 5.2 gives $L - \varepsilon \lt a_n$ and $b_n \lt L + \varepsilon$, so

$$
L - \varepsilon \lt a_n \le c_n \le b_n \lt L + \varepsilon .
$$

By the second consequence in Section 5.2 again, $\lvert c_n - L \rvert \lt \varepsilon$ for every $n \ge N$. ∎

The squeeze rule is most often used in the following form.

**Corollary.** If $d_n \to 0$, $K \in \mathbb{N}$ and $\lvert c_n - L \rvert \le d_n$ for every $n \ge K$, then $c_n \to L$.

*Proof.* By the second consequence in Section 5.2, with $\le$, $L - d_n \le c_n \le L + d_n$ for every $n \ge K$. By the sum rules (Section 5.6), with the constant sequence $(L)$, $L - d_n \to L - 0 = L$ and $L + d_n \to L + 0 = L$. The squeeze rule gives $c_n \to L$. ∎

**What fails: different outer limits.** Let $a_n = -1$, $b_n = 1$ and $c_n = (-1)^n$. Since $\lvert c_n \rvert = 1$ (Section 5.2), Part 5 of the lemma there gives $a_n \le c_n \le b_n$ for every $n$, and $(a_n)$ and $(b_n)$ converge, to $-1$ and $1$. But $(c_n)$ diverges (Section 5.5). The two outer sequences must have the same limit.

## 5.10 The geometric sequence

The squeeze rule and Bernoulli's inequality (Session 3) give one limit that the exercises and later sessions use often.

**Theorem (geometric sequence).** If $\lvert r \rvert \lt 1$, then $r^n \to 0$.

*Proof.* If $r = 0$, then $r^1 = 0$, and $r^n = 0$ gives $r^{n+1} = r^n \cdot 0 = 0$. By induction $(r^n)$ is the constant sequence $(0)$, which converges to $0$. Suppose $r \ne 0$. Then $0 \lt \lvert r \rvert \lt 1$ by Section 5.2, Part 1, and the rule for reciprocals gives $1/\lvert r \rvert \gt 1/1 = 1$. Put $h = 1/\lvert r \rvert - 1$, so $h \gt 0$ and $1/\lvert r \rvert = 1 + h$. For every $n$, $nh \gt 0$ as a product of positive numbers, and adding $nh$ to $1 \gt 0$ gives $1 + nh \gt nh$. Adding $-1$ to $0 \lt 1$ gives $-1 \lt 0 \lt h$, so $h \ge -1$, and Bernoulli's inequality (Session 3) gives

$$
(1 + h)^n \ge 1 + nh \gt nh \gt 0 .
$$

By the rule $(xy)^n = x^n y^n$ (Session 3), $\lvert r \rvert^n (1 + h)^n = (\lvert r \rvert (1 + h))^n = 1^n = 1$, so $\lvert r \rvert^n = 1/(1 + h)^n$ by 4.2(e). With Section 5.2, Part 8 and the rule for reciprocals applied to $0 \lt nh \lt (1 + h)^n$,

$$
\lvert r^n - 0 \rvert = \lvert r \rvert^n = \frac{1}{(1 + h)^n} \lt \frac{1}{nh} = \frac{1}{h} \cdot \frac{1}{n} .
$$

The sequence $(1/h)(1/n)$ converges to $(1/h) \cdot 0 = 0$, by Section 5.3 and the product rule (Section 5.6). The corollary of the squeeze rule (Section 5.9) with $d_n = (1/h)(1/n)$ gives $r^n \to 0$. ∎

For $r = 1/2$, $h = 1$ and the bound reads $(1/2)^n \lt 1/n$. At $n = 10$ the bound is $1/10$, while $(1/2)^{10} = 1/2^{10} = 1/1024$ (Session 3, Section 3.7), which is less than $1/1000$. The bound is crude, but a crude bound that tends to $0$ is all the squeeze rule needs. For $r = 1$ the sequence is constant and converges to $1$; for $r = -1$ it is $((-1)^n)$, which diverges (Section 5.5); Exercise 6 treats $\lvert r \rvert \gt 1$.

## 5.11 Worked example

Let

$$
a_n = \frac{3n^2 + n}{2n^2 + 1} .
$$

The denominator satisfies $2n^2 + 1 \ge 1 \gt 0$, so every term is defined. The first terms are $a_1 = 4/3$, $a_2 = 14/9$, $a_{10} = 310/201$ and $a_{100} = 30100/20001$. Their distances to $3/2$ are $1/6$, $1/18$, $17/402$ and $197/40002$, and they suggest the limit $3/2$. We prove it twice: once with the rules, once from the definition.

**By the rules.** Divide numerator and denominator by $n^2 \ne 0$:

$$
a_n = \frac{3 + 1/n}{2 + 1/n^2} .
$$

1. $1/n \to 0$ (Section 5.3), so $3 + 1/n \to 3 + 0 = 3$ by the sum rule (Section 5.6).
2. $1/n^2 = (1/n)(1/n) \to 0 \cdot 0 = 0$ by the product rule, so $2 + 1/n^2 \to 2$ by the sum rule.
3. $2 + 1/n^2 \gt 0$ for every $n$, and the limit $2$ is not $0$. The quotient rule (Section 5.7) gives $a_n \to 3/2$.

**From the definition.** First compute the distance to $3/2$ exactly:

$$
a_n - \frac{3}{2} = \frac{2(3n^2 + n) - 3(2n^2 + 1)}{2(2n^2 + 1)} = \frac{6n^2 + 2n - 6n^2 - 3}{4n^2 + 2} = \frac{2n - 3}{4n^2 + 2} .
$$

For $n \ge 2$, $2n - 3 \ge 4 - 3 = 1 \gt 0$, so $\lvert a_n - 3/2 \rvert = (2n - 3)/(4n^2 + 2)$. Also $2n - 3 \lt 2n$, and $4n^2 + 2 \gt 4n^2 \gt 0$. Multiplying $2n - 3 \lt 2n$ by $1/(4n^2 + 2) \gt 0$, then multiplying the reciprocal rule's $1/(4n^2 + 2) \lt 1/(4n^2)$ by $2n \gt 0$,

$$
\left\lvert a_n - \frac{3}{2} \right\rvert = \frac{2n - 3}{4n^2 + 2} \lt \frac{2n}{4n^2 + 2} \lt \frac{2n}{4n^2} = \frac{1}{2n} \qquad (n \ge 2) .
$$

Now let $\varepsilon \gt 0$. Every $N \in \mathbb{N}$ with $N \ge 2$ and $N \ge 1/(2\varepsilon)$ works. Indeed, $N \ge 1/(2\varepsilon)$ gives $2N \ge 1/\varepsilon \gt 0$, so $1/(2N) \le \varepsilon$ by the rule for reciprocals. For $n \ge N$, $0 \lt 2N \le 2n$ gives $1/(2n) \le 1/(2N)$ in the same way, so $\lvert a_n - 3/2 \rvert \lt 1/(2n) \le \varepsilon$. Such an $N$ exists: the Archimedean property gives $N_1 \in \mathbb{N}$ with $N_1 \gt 1/(2\varepsilon)$, and $N = \max\{2, N_1\}$ will do.

For $\varepsilon = 1/100$ the condition is $N \ge 50$, and $N = 50$ works, since $1/(2 \cdot 50) = 1/100$. Check at $n = 50$: $a_{50} = 7550/5001$, and $\lvert a_{50} - 3/2 \rvert = (2 \cdot 50 - 3)/(4 \cdot 2500 + 2) = 97/10002$, which is less than $1/100$, since $100 \cdot 97 = 9700 \lt 10002$. The same formula at $n = 10$ gives $17/402$, matching $a_{10} - 3/2 = 310/201 - 3/2 = (620 - 603)/402$.

The two proofs agree, as Section 5.4 says they must. The rules give the limit quickly. The definition gives more: an explicit $N$ for each $\varepsilon$.

## Exercises

*Check*

1. Let $a_n = \dfrac{2n + 1}{n + 3}$. Show from the definition that $a_n \to 2$. For $\varepsilon = 1/10$, find the smallest $N$ such that $\lvert a_n - 2 \rvert \lt 1/10$ for every $n \ge N$.
2. Use the rules of Sections 5.3, 5.6 and 5.7 to find $\lim_{n \to \infty} \dfrac{n^3 - 2n}{4n^3 + n^2 + 1}$, justifying each step.
3. Use Section 5.10 and the rules to find $\lim_{n \to \infty} \dfrac{1 + (1/2)^n}{3 - (2/3)^n}$. Check first that the denominator never vanishes.

*Prove*

4. Prove that if $a_n \to a$ then $\lvert a_n \rvert \to \lvert a \rvert$. Show by an example that $\lvert a_n \rvert$ can converge while $(a_n)$ diverges, and prove that $a_n \to 0$ if and only if $\lvert a_n \rvert \to 0$.
5. Prove that if $a_n \to 0$ and $(b_n)$ is bounded, then $a_n b_n \to 0$, even when $(b_n)$ diverges. Apply it to $(-1)^n / n$. Explain why the product rule of Section 5.6 does not give this.
6. Prove that if $\lvert r \rvert \gt 1$, then $(r^n)$ is unbounded and therefore diverges.

*Extend*

7. (Averages.) Suppose $a_n \to a$, and let $s_n = (a_1 + a_2 + \dots + a_n)/n$. Prove that $s_n \to a$. Then show that for $a_n = (-1)^n$ the averages $s_n$ converge although $(a_n)$ does not.
8. (Ratios.) Suppose $a_n \gt 0$ for every $n$ and $a_{n+1}/a_n \to L$ with $L \lt 1$. Prove that $a_n \to 0$. Use this to show $n/2^n \to 0$. Then give two sequences of positive terms with $a_{n+1}/a_n \to 1$, one converging to $0$ and one not.

Solutions: [solutions/005-limits-of-sequences.md](../solutions/005-limits-of-sequences.md).
