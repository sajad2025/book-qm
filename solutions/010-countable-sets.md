# Solutions to 1.10. Countable sets

## Check

**1.** (a) The table of 10.3 ends with $p_{10} = (1, 4)$. Its first coordinate is $1$, so the second case of the rule gives $p_{11} = (5, 1)$. The first case then applies four times:
$$
p_{12} = (4, 2), \quad p_{13} = (3, 3), \quad p_{14} = (2, 4), \quad p_{15} = (1, 5).
$$

(b) Continue: $p_{15} = (1, 5)$ gives $p_{16} = (6, 1)$, then $p_{17} = (5, 2)$, $p_{18} = (4, 3)$, $p_{19} = (3, 4)$. So $m = 19$.

The same number comes from a formula. The proof of the Lemma in 10.3 shows that if $(s-1, 1) = p_{m_s}$, then $(s, 1) = p_{m_s + s - 1}$. Starting from $m_2 = 1$ and putting $m_{s+1} = m_s + (s - 1)$, induction on $s$ from $2$ (Session 3) gives $(s-1, 1) = p_{m_s}$ for every $s \ge 2$. A second induction from $2$ gives
$$
m_s = 1 + \frac{(s-2)(s-1)}{2} \quad \text{for every } s \ge 2 .
$$
For $s = 2$ the right side is $1 + 0 = 1 = m_2$. If it holds for $s$, then
$$
m_{s+1} = 1 + \frac{(s-2)(s-1)}{2} + (s - 1) = 1 + \frac{(s-1)(s - 2 + 2)}{2} = 1 + \frac{\bigl((s+1)-2\bigr)\bigl((s+1)-1\bigr)}{2},
$$
which is the statement for $s + 1$. The Claim in the proof of the Lemma gives $(j, k) = p_{m_s + k - 1}$ with $s = j + k$. For $(3, 4)$: $s = 7$, $m_7 = 1 + 5 \cdot 6/2 = 16$, and $m = 16 + 4 - 1 = 19$.

(c) The enumeration of 10.4 is $c_m = z_n / k$ where $p_m = (k, n)$, and $z_1 = 0$, $z_2 = 1$, $z_3 = -1$, $z_4 = 2$, $z_5 = -2$. So

- $p_{11} = (5, 1)$: $c_{11} = z_1 / 5 = 0$;
- $p_{12} = (4, 2)$: $c_{12} = z_2 / 4 = 1/4$;
- $p_{13} = (3, 3)$: $c_{13} = z_3 / 3 = -1/3$;
- $p_{14} = (2, 4)$: $c_{14} = z_4 / 2 = 1$;
- $p_{15} = (1, 5)$: $c_{15} = z_5 / 1 = -2$.

**2.** Step 1. $[a_0, b_0] = [0, 1]$ and $\ell = 1$, so $K = [0, 1/3]$ and $K' = [2/3, 1]$. Since $x_1 = 0 \in K$, $[a_1, b_1] = K' = [2/3, 1]$.

Step 2. $\ell = 1/3$, so $K = [2/3, 2/3 + 1/9] = [2/3, 7/9]$ and $K' = [1 - 1/9, 1] = [8/9, 1]$. Now $2/3 \le 3/4$ because $8 \le 9$, and $3/4 \le 7/9$ because $27 \le 28$. So $x_2 \in K$, and $[a_2, b_2] = K' = [8/9, 1]$.

Step 3. $\ell = 1/9$, so $K = [8/9, 8/9 + 1/27] = [24/27, 25/27]$ and $K' = [26/27, 1]$. Now $24/27 \le 9/10$ because $240 \le 243$, and $9/10 \le 25/27$ because $243 \le 250$. So $x_3 \in K$, and $[a_3, b_3] = K' = [26/27, 1]$.

Steps $n \ge 4$. We show by induction from $3$ that $[a_n, b_n] = [26/27,\, 26/27 + 1/3^n]$ for every $n \ge 3$. For $n = 3$, $3^3 = 27$ and $26/27 + 1/27 = 1$, which matches Step 3. Suppose it holds for $n - 1 \ge 3$. Then $\ell = 1/3^{n-1}$, and $\ell/3 = 1/3^n$ because $3^n = 3^{n-1} \cdot 3$ (Session 3). So the left third is $K = [26/27,\, 26/27 + 1/3^n]$. Every point of $K$ is at least $26/27 \gt 0$, so $x_n = 0 \notin K$, and the rule gives $[a_n, b_n] = K$. This is the statement for $n$.

The point $c$. The proof of the nested-interval lemma takes $c = \sup\{a_m : m \in \mathbb{N}\}$. The left endpoints are $a_1 = 2/3$, $a_2 = 8/9$ and $a_m = 26/27$ for $m \ge 3$, and $2/3 \lt 8/9 \lt 26/27$. So the set is $\{2/3, 8/9, 26/27\}$, whose largest element $26/27$ is its least upper bound: it is an upper bound, and any upper bound is at least $26/27$. So $c = 26/27$.

The terms of the sequence are $0$, $3/4$, $9/10$ and $0$. $26/27 \ne 0$; $26/27 \ne 3/4$ because $26 \cdot 4 = 104 \ne 81 = 27 \cdot 3$; $26/27 \ne 9/10$ because $260 \ne 243$. So $c$ differs from every $x_n$, as the proof promises.

**3.** Two facts about bounds are used throughout. For $p \lt q$:

- (i) $\sup\{t : p \lt t \lt q\} = q$ and $\sup\{t : p \le t \lt q\} = q$. The number $q$ is an upper bound. If $w \lt q$, then $t = (\max\{w, p\} + q)/2$ lies in both sets and $t \gt w$, so $w$ is not an upper bound.
- (ii) $\inf\{t : p \lt t \le q\} = p$ and $\inf\{t : p \lt t \lt q\} = p$. The number $p$ is a lower bound. If $w \gt p$, then $t = (p + \min\{w, q\})/2$ lies in both sets and $t \lt w$.

Also, if a set has an upper bound that belongs to the set, that element is its least upper bound, since every upper bound is at least as large as every element. The same holds for lower bounds.

*$f$ is nondecreasing.* On $[0, 1)$ the values are $f(x) = x \lt 1$. At $1$ the value is $2$. On $(1, 2]$ the values are $x + 1$, with $2 \lt x + 1 \le 3$. On $(2, 3]$ the value is $5$. So every value at a point of an earlier piece is less than every value at a point of a later piece, in the order $[0,1)$, $\{1\}$, $(1,2]$, $(2,3]$. Inside each piece $f$ is $x \mapsto x$, $x \mapsto x + 1$ or constant, each nondecreasing. So $x \le y$ implies $f(x) \le f(y)$.

*The values $L(x)$ and $R(x)$.* Write $V_{\lt x} = \{f(t) : t \in I,\ t \lt x\}$ and $V_{\gt x} = \{f(t) : t \in I,\ t \gt x\}$.

1. $x = 0$. No point of $I$ is below $0$, so $L(0) = f(0) = 0$. The set $V_{\gt 0}$ is the union of $(0, 1)$, $\{2\}$, $(2, 3]$ and $\{5\}$. Every element is positive, and by (ii) for every $w \gt 0$ some element of $(0, 1)$ is less than $\min\{w, 1\}$. So $R(0) = 0$.
2. $0 \lt x \lt 1$. $V_{\lt x} = [0, x)$, so $L(x) = x$ by (i). $V_{\gt x}$ is the union of $(x, 1)$ and numbers at least $2$; $x$ is a lower bound, and by (ii) no $w \gt x$ is one. So $R(x) = x$.
3. $x = 1$. $V_{\lt 1} = [0, 1)$, so $L(1) = 1$. $V_{\gt 1}$ is the union of $(2, 3]$ and $\{5\}$, so $R(1) = 2$ by (ii). Here $L(1) = 1 \lt 2 = R(1)$.
4. $1 \lt x \lt 2$. $V_{\lt x}$ is the union of $[0, 1)$, $\{2\}$ and $(2, x+1)$. Every element is less than $x + 1$, and by (i) no $w \lt x + 1$ is an upper bound of $(2, x + 1)$. So $L(x) = x + 1$. $V_{\gt x}$ is the union of $(x + 1, 3]$ and $\{5\}$, so $R(x) = x + 1$ by (ii).
5. $x = 2$. $V_{\lt 2}$ is the union of $[0, 1)$, $\{2\}$ and $(2, 3)$, so $L(2) = 3$ by (i) and the bound $3$. $V_{\gt 2} = \{5\}$, so $R(2) = 5$. Here $L(2) = 3 \lt 5 = R(2)$.
6. $2 \lt x \lt 3$. $V_{\lt x}$ contains $5$ (from any $t$ in $(2, x)$) and every element is at most $f(x) = 5$, so $L(x) = 5$. $V_{\gt x} = \{5\}$, so $R(x) = 5$.
7. $x = 3$. No point of $I$ is above $3$, so $R(3) = f(3) = 5$. $V_{\lt 3}$ contains $5$ and is bounded by $5$, so $L(3) = 5$.

By Lemma 2 of 10.7, $f$ is continuous exactly where $L(x) = R(x)$, so
$$
D = \{1, 2\}.
$$
The jump at $1$ is $(1, 2)$, which contains the rational $3/2$. The jump at $2$ is $(3, 5)$, which contains the rational $4$. The jumps are disjoint, as Lemma 1 requires: $R(1) = 2 \le 3 = L(2)$.

## Prove

**4.** By the parity lemma (Session 3, Section 3.3), every $m \in \mathbb{N}$ equals $2n - 1$ or $2n$ for some $n \in \mathbb{N}$, not both, and $n$ is unique. So the rule $c_{2n-1} = a_n$, $c_{2n} = b_n$ defines exactly one term $c_m$ for each $m$.

Every $c_m$ is some $a_n \in A$ or some $b_n \in B$, so it lies in $A \cup B$. Let $x \in A \cup B$. If $x \in A$, then $x = a_n$ for some $n$, because $(a_n)$ enumerates $A$, and $x = c_{2n - 1}$. If $x \in B$, then $x = b_n$ for some $n$, and $x = c_{2n}$. So the range of $(c_m)$ is $A \cup B$.

**5.** If $A = \emptyset$ or $B = \emptyset$, then $A \times B = \emptyset$, which is countable. Otherwise let $(a_j)$ enumerate $A$ and $(b_k)$ enumerate $B$, and define
$$
g : \mathbb{N} \times \mathbb{N} \to A \times B, \qquad g(j, k) = (a_j, b_k).
$$
Let $(x, y) \in A \times B$. Then $x = a_j$ for some $j$ and $y = b_k$ for some $k$, so $(x, y) = g(j, k)$. Hence $A \times B = g(\mathbb{N} \times \mathbb{N})$. The set $\mathbb{N} \times \mathbb{N}$ is countable by the Lemma of 10.3, so its image $A \times B$ is countable by 10.2.

Since $\mathbb{Q}$ is countable (10.4), taking $A = B = \mathbb{Q}$ shows that $\mathbb{Q} \times \mathbb{Q}$ is countable.

**6.** Suppose $f$ is not continuous at some $x \in [a, b]$. We derive a contradiction. Use the numbers $L(x)$ and $R(x)$ of 10.7 for the interval $I = [a, b]$. By Lemma 2 of 10.7, $L(x) \ne R(x)$, and by Lemma 1, $L(x) \lt R(x)$.

*The jump lies between $f(a)$ and $f(b)$.* If $x \gt a$, then $a$ is a point of $I$ below $x$, so $f(a)$ belongs to the set whose least upper bound is $L(x)$, and $f(a) \le L(x)$. If $x = a$, then no point of $I$ is below $x$, and $L(x) = f(a)$. In both cases $f(a) \le L(x)$. In the same way, $R(x) \le f(b)$.

*A value in the jump.* Put $\ell = R(x) - L(x) \gt 0$, $w_1 = L(x) + \ell/3$ and $w_2 = L(x) + 2\ell/3$. Then $L(x) \lt w_1 \lt w_2 \lt R(x)$, and $w_1 \ne w_2$, so at least one of them differs from $f(x)$. Call it $w$. Then
$$
f(a) \le L(x) \lt w \lt R(x) \le f(b),
$$
so $f(a) \lt w \lt f(b)$. By hypothesis $w = f(t)$ for some $t \in [a, b]$.

*No point takes that value.* $t \ne x$, since $f(x) \ne w$. If $t \lt x$, then $f(t) \le L(x)$, because $L(x)$ is an upper bound of the values below $x$; so $f(t) \lt w$. If $t \gt x$, then $f(t) \ge R(x)$, because $R(x)$ is a lower bound of the values above $x$; so $f(t) \gt w$. Either way $f(t) \ne w$, a contradiction.

So $f$ is continuous at every point of $[a, b]$.

## Extend

**7.** *A rule.* The proof of 10.5 is a rule: given reals $u \lt v$ and the sequence $(c_k)$, it defines the intervals $[a_k, b_k]$ by a recursion in which every step is determined (take the left third if $c_k$ is not in it, otherwise the right third), and then the point $c = \sup\{a_k : k \in \mathbb{N}\}$. Write $P(u, v)$ for this point. The proof shows $P(u, v) \in [u, v]$ and $P(u, v) \ne c_k$ for every $k$, so $P(u, v) \notin C$. No selection is made: each step and the supremum are determined by $u$, $v$ and $(c_k)$.

*The sequence.* An interval has at least two points (Session 7), so $I$ contains a point $w \ne x$; fix one. Put $h = \lvert w - x \rvert \gt 0$.

If $w \gt x$, put $u_n = x + h/(2n)$ and $v_n = x + h/n$. If $w \lt x$, put $u_n = x - h/n$ and $v_n = x - h/(2n)$. In both cases $u_n \lt v_n$, and both lie between $x$ and $w$ (inclusive), since $0 \lt h/(2n) \lt h/n \le h$. Define
$$
y_n = P(u_n, v_n).
$$
Then $y_n \in [u_n, v_n]$, so $y_n$ lies between $x$ and $w$, and $y_n \in I$ because $I$ is an interval containing $x$ and $w$ (if $y_n$ equals $x$ or $w$ it is in $I$; otherwise it lies strictly between $x$ and $w$). Also $y_n \notin C$. So $(y_n)$ is a sequence in $I \setminus C$.

*Convergence.* Every point of $[u_n, v_n]$ is within $h/n$ of $x$, so $\lvert y_n - x \rvert \le h/n$. Let $\varepsilon \gt 0$. By the Archimedean property (Session 4) there is $N \in \mathbb{N}$ with $N \gt h/\varepsilon$. For $n \ge N$,
$$
\lvert y_n - x \rvert \le \frac{h}{n} \le \frac{h}{N} \lt \varepsilon .
$$
So $y_n \to x$ by the definition of the limit (Session 5).

**8.** (a) Each $s^{(k)}_k$ is $0$ or $1$, so $d_k = 1 - s^{(k)}_k$ is $1$ or $0$. So $d \in S$.

Fix $n$. Then $d_n = 1 - s^{(n)}_n$. If $d_n = s^{(n)}_n$, then $2 s^{(n)}_n = 1$ and $s^{(n)}_n = 1/2$, which is neither $0$ nor $1$. So $d_n \ne s^{(n)}_n$. Two sequences are functions on $\mathbb{N}$, and functions that differ at the point $n$ are different, so $d \ne s^{(n)}$.

So $d$ is an element of $S$ outside the range of $n \mapsto s^{(n)}$. Since the sequence was arbitrary, no sequence has range $S$. The set $S$ is not empty, since the constant sequence $0, 0, 0, \dots$ is in it. So $S$ is uncountable.

(b) Let $P$ be the set of all subsets of $\mathbb{N}$, and define $\chi : P \to S$ by $\chi(E)_k = 1$ if $k \in E$ and $\chi(E)_k = 0$ if $k \notin E$. For any $s \in S$, the set $E = \{k \in \mathbb{N} : s_k = 1\}$ has $\chi(E) = s$, so $\chi(P) = S$. If $P$ were countable, $S = \chi(P)$ would be countable by 10.2, contradicting (a). So $P$ is uncountable.
