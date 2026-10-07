# 1.10. Countable sets

*Theorem. Builds on Sessions 3, 4, 6 and 7.*

**Claim.** A set is countable if it is empty or the range of a sequence; subsets and images of countable sets are countable, a countable union of sets each given with an enumeration is countable, and $\mathbb{Q}$ is countable; no interval of positive length is countable (nested intervals), so an interval minus a countable set is dense in it; and a monotone function on an interval is continuous except at countably many points, since each jump contains its own rational.

**Recall.** The session uses the following.

- *Session 2.* A function $f : A \to B$ is surjective if $f(A) = B$, injective if $f(x) = f(y)$ forces $x = y$, and a bijection if it is both; a function is a bijection if and only if it has an inverse. The image $f(A)$ is the range of $f$.
- *Session 3.* A statement about every natural number, or about every $n \ge n_0$, is proved by induction. A sequence in a set $S$ is a function $\mathbb{N} \to S$, written $n \mapsto a_n$ or $(a_n)$, and its range is $\{a_n : n \in \mathbb{N}\}$; terms may repeat. Definition by recursion (Section 3.5): for an element $c$ of a set $S$ and functions $g_n : S \to S$, there is exactly one sequence $(s_n)$ in $S$ with $s_1 = c$ and $s_{n+1} = g_n(s_n)$ for every $n$, and the same holds for sequences indexed from 0. For $m, n \in \mathbb{N}$: Lemma 1, $n \ge 1$; Lemma 2, if $n \ne 1$, then $n - 1 \in \mathbb{N}$; Lemma 3, $m + n \in \mathbb{N}$ and $mn \in \mathbb{N}$; Lemma 4(a), if $m \lt n$, then $n - m \in \mathbb{N}$ and $m + 1 \le n$. The parity lemma (Section 3.3): every $n \in \mathbb{N}$ equals $2k$ or $2k - 1$ for exactly one $k \in \mathbb{N}$, and not both.
- *Session 4.* $\mathbb{R}$ is an ordered field. Every nonempty set bounded above has a least upper bound $\sup S$, and so every nonempty set bounded below has a greatest lower bound $\inf S = -\sup\{-s : s \in S\}$. The Archimedean property: for every real $r$ there is $n \in \mathbb{N}$ with $n \gt r$. The integers and rationals are $\mathbb{Z} = \mathbb{N} \cup \{0\} \cup \{-n : n \in \mathbb{N}\}$ and $\mathbb{Q} = \{p/q : p \in \mathbb{Z},\ q \in \mathbb{N}\}$. For real $s$ and $t$, $\min\{s, t\}$ and $\max\{s, t\}$ are the minimum and the maximum of the set $\{s, t\}$ (Section 4.4): if $s \le t$ they are $s$ and $t$, and otherwise $t$ and $s$. So each is one of $s$ and $t$, $\min\{s, t\}$ is at most both, and $\max\{s, t\}$ is at least both.
- *Session 5.* The triangle inequality $\lvert x + y \rvert \le \lvert x \rvert + \lvert y \rvert$, and $\lvert -x \rvert = \lvert x \rvert$.
- *Session 6.* If $(a_n)$ is nondecreasing, then $a_m \le a_n$ whenever $m \le n$ (comparison of terms).
- *Session 7.* An interval is a set $I \subseteq \mathbb{R}$ with at least two points such that whenever $u, w \in I$ and $u \lt v \lt w$, also $v \in I$; for $a \lt b$ the sets $[a,b]$, $(a,b)$, $[a,b)$, $(a,b]$ and $\mathbb{R}$ are intervals, and $(a,b)$ is called an open interval (Section 7.5). A function $f : I \to \mathbb{R}$ is continuous at $x \in I$ if for every $\varepsilon \gt 0$ there is $\delta \gt 0$ such that every $y \in I$ with $\lvert y - x \rvert \lt \delta$ has $\lvert f(y) - f(x) \rvert \lt \varepsilon$.

## 10.1 Countable sets

**Definition.** A set $S$ is **countable** if $S = \emptyset$ or $S$ is the range of some sequence in $S$. A sequence whose range is $S$ is an **enumeration** of $S$. A set that is not countable is **uncountable**.

So a nonempty set $S$ is countable if and only if there is a surjection $\mathbb{N} \to S$. Rudin, *Principles of Mathematical Analysis*, Definition 2.4, calls such sets "at most countable" and keeps "countable" for the infinite ones. This book uses the single word.

Four examples.

- $\emptyset$ is countable by definition.
- A set $\{s_1, \dots, s_k\}$ with $k \in \mathbb{N}$ is countable: the sequence $s_1, s_2, \dots, s_k, s_k, s_k, \dots$, that is $a_n = s_n$ for $n \le k$ and $a_n = s_k$ for $n \gt k$, has every term in the set, and each $s_i$ equals $a_i$.
- $\mathbb{N}$ is countable: the sequence $a_n = n$ has range $\mathbb{N}$.
- $\mathbb{Z}$ is countable. For $k \in \mathbb{N}$ define
$$
z_{2k} = k, \qquad z_{2k-1} = -(k - 1).
$$
By the parity lemma (Session 3, Section 3.3) each $n \in \mathbb{N}$ has exactly one of the forms $2k$ and $2k - 1$, with exactly one $k$, so this defines exactly one $z_n$ for each $n$. Each $z_n$ is an integer (Session 4): $k \in \mathbb{N}$, and $k - 1$ is $0$ if $k = 1$ and lies in $\mathbb{N}$ otherwise (Session 3, Lemma 2), so $-(k - 1)$ is $0$ or the negative of a natural number. The first terms are $z_1 = 0$, $z_2 = 1$, $z_3 = -1$, $z_4 = 2$, $z_5 = -2$. Every integer occurs: $0 = z_1$, and for $k \in \mathbb{N}$, $k = z_{2k}$ and $-k = z_{2(k+1)-1}$.

## 10.2 Subsets and images

**Theorem.** Let $A$ be countable.
1. Every subset $B \subseteq A$ is countable.
2. For every function $f : A \to T$, the image $f(A)$ is countable.

*Proof.* (1) If $B = \emptyset$, it is countable. Otherwise fix $b_0 \in B$. Then $A$ is nonempty, so it has an enumeration $(a_n)$. Define
$$
b_n = a_n \text{ if } a_n \in B, \qquad b_n = b_0 \text{ if } a_n \notin B.
$$
Every $b_n$ lies in $B$. Every $x \in B$ lies in $A$, so $x = a_n$ for some $n$, and then $a_n \in B$ gives $b_n = a_n = x$. So $(b_n)$ is an enumeration of $B$.

(2) If $A = \emptyset$, then $f(A) = \emptyset$. Otherwise let $(a_n)$ enumerate $A$ and put $c_n = f(a_n)$. Every $c_n$ lies in $f(A)$. Every element of $f(A)$ is $f(x)$ for some $x \in A$, and $x = a_n$ for some $n$, so it equals $c_n$. So $(c_n)$ enumerates $f(A)$. ∎

**Corollary.** If $g : S \to T$ is injective and $T$ is countable, then $S$ is countable.

*Proof.* $g(S) \subseteq T$ is countable by part 1. As a function $S \to g(S)$, $g$ is surjective by the definition of the image and injective by hypothesis, so it is a bijection, and it has an inverse $h : g(S) \to S$ (Session 2). Then $h(g(S)) = S$: every value of $h$ lies in $S$, and every $x \in S$ equals $h(g(x))$ with $g(x) \in g(S)$. By part 2, $S$ is countable. ∎

The contrapositive of part 1 is used below: a set that contains an uncountable subset is uncountable.

## 10.3 Countable unions

The key step is a single sequence that passes through every pair of natural numbers. List the pairs diagonal by diagonal: first the pairs with $j + k = 2$, then those with $j + k = 3$, and so on. Along the diagonal $j + k = s$, go from $(s-1, 1)$ down to $(1, s-1)$. As a recursion (Session 3, Section 3.5) in the set $\mathbb{N} \times \mathbb{N}$:
$$
p_1 = (1, 1), \qquad
p_{m+1} = \begin{cases} (j-1,\, k+1) & \text{if } p_m = (j, k) \text{ with } j \ne 1, \\ (k+1,\, 1) & \text{if } p_m = (1, k). \end{cases}
$$
The rule maps $\mathbb{N} \times \mathbb{N}$ into itself: if $j \ne 1$, then $j - 1 \in \mathbb{N}$ (Session 3, Lemma 2), and $k + 1 \in \mathbb{N}$ (Session 3, Lemma 3). The first ten terms are

| $m$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| $p_m$ | (1,1) | (2,1) | (1,2) | (3,1) | (2,2) | (1,3) | (4,1) | (3,2) | (2,3) | (1,4) |

**Lemma.** Every pair $(j, k) \in \mathbb{N} \times \mathbb{N}$ equals $p_m$ for some $m$. So $\mathbb{N} \times \mathbb{N}$ is countable.

*Proof.* First a claim about one diagonal.

*Claim.* Let $s \in \mathbb{N}$ with $s \ge 2$, and suppose $p_m = (s-1, 1)$. Then $p_{m+i} = (s-1-i,\, 1+i)$ for $i = 0$ and for every $i \in \mathbb{N}$ with $i \le s - 2$.

By induction on $i$ from 0 (Session 3). For $i = 0$ this is the hypothesis. Suppose it holds for $i$, and $i + 1 \le s - 2$. Then the first coordinate of $p_{m+i}$ is $s - 1 - i \ge 2$, so it is not $1$, and the first case of the rule gives $p_{m+i+1} = (s-2-i,\, 2+i)$. That is the statement for $i + 1$.

Next, by induction on $s$ from $2$ (Session 3), the pair $(s-1, 1)$ is a term of the sequence. For $s = 2$: $(1, 1) = p_1$. Suppose $(s-1, 1) = p_m$. By the Claim with $i = s - 2$, $p_{m+s-2} = (1, s-1)$. Its first coordinate is $1$, so the second case of the rule gives $p_{m+s-1} = (s, 1)$. That is the statement for $s + 1$.

Now let $(j, k)$ be any pair and put $s = j + k$. Then $s \in \mathbb{N}$ (Session 3, Lemma 3) and $s \ge 2$, since $j, k \ge 1$ (Session 3, Lemma 1). So $(s-1, 1) = p_m$ for some $m$. Put $i = k - 1$; then $i = 0$ if $k = 1$, and $i \in \mathbb{N}$ otherwise (Session 3, Lemma 2), and $i \le s - 2$ because $j \ge 1$. The Claim gives $p_{m+k-1} = (s-k,\, k) = (j, k)$. ∎

**Theorem (countable unions).** Let $J$ be a countable set, and for each $i \in J$ let $A_i$ be a set. Suppose each nonempty $A_i$ is given together with an enumeration $n \mapsto a_{i,n}$. Then the union $U = \bigcup_{i \in J} A_i$ is countable.

*Proof.* If $J = \emptyset$, then $U = \emptyset$. Otherwise let $(i_k)$ enumerate $J$. If $U = \emptyset$, it is countable. Otherwise fix $u \in U$. For each $m$, let $p_m = (k, n)$ and define
$$
c_m = a_{i_k,\, n} \text{ if } A_{i_k} \ne \emptyset, \qquad c_m = u \text{ if } A_{i_k} = \emptyset.
$$
Every $c_m$ lies in $U$. Let $x \in U$. Then $x \in A_i$ for some $i \in J$, and $i = i_k$ for some $k$. The set $A_{i_k}$ contains $x$, so it is nonempty, and $x = a_{i_k, n}$ for some $n$. By the Lemma, $(k, n) = p_m$ for some $m$, and then $c_m = a_{i_k, n} = x$. So $(c_m)$ enumerates $U$. ∎

The words "given together with an enumeration" are part of the hypothesis, and the proof uses them: $c_m$ is defined from the given $a_{i,n}$. If one knew only that each $A_i$ has some enumeration, one would first have to select one enumeration for each of infinitely many $i$ at once. That selection is an instance of the axiom of countable choice. The book assumes that axiom (Session 7, Section 7.3), but this theorem does not need it: it is stated with given enumerations, so that the enumeration of the union is explicit and its proof makes no such selection. In every use of the theorem in this session the enumerations are written down.

**Corollary.** If $A$ and $B$ are countable, so is $A \cup B$.

*Proof.* Take $J = \{1, 2\}$, countable by 10.1, with $A_1 = A$ and $A_2 = B$. For each of the two sets that is nonempty, fix one enumeration. Fixing two is an ordinary step of proof; the axiom of countable choice concerns infinitely many selections at once. The theorem applies. ∎

## 10.4 The rationals

**Theorem.** $\mathbb{Q}$ is countable.

*Proof.* By the definition of $\mathbb{Q}$ (Session 4), every rational number is $p/k$ with $p \in \mathbb{Z}$ and $k \in \mathbb{N}$, and every such quotient is rational. So
$$
\mathbb{Q} = \bigcup_{k \in \mathbb{N}} A_k, \qquad A_k = \{p/k : p \in \mathbb{Z}\}.
$$
Each $A_k$ is given with the enumeration $n \mapsto z_n / k$, where $(z_n)$ is the enumeration of $\mathbb{Z}$ from 10.1: every $z_n/k$ lies in $A_k$ because $z_n \in \mathbb{Z}$, and every $p/k$ with $p \in \mathbb{Z}$ equals $z_n/k$ for some $n$, since $p = z_n$ for some $n$ (10.1). The index set $\mathbb{N}$ is countable. The theorem on countable unions gives the result. ∎

Unwinding the proof gives an explicit enumeration: $c_m = z_n / k$ where $p_m = (k, n)$. Its first ten terms, from the table in 10.3, are
$$
0,\ 0,\ 1,\ 0,\ \tfrac{1}{2},\ -1,\ 0,\ \tfrac{1}{3},\ -\tfrac{1}{2},\ 2 .
$$
For example, $p_9 = (2, 3)$ gives $c_9 = z_3 / 2 = -1/2$.

The rationals are also spread through every interval. This needs two lemmas about integers.

**Lemma (integer steps).**
- (a) If $k \in \mathbb{Z}$, then $k + 1 \in \mathbb{Z}$.
- (b) If $j, k \in \mathbb{Z}$ and $j \lt k$, then $k - j \in \mathbb{N}$, and so $j + 1 \le k$.

*Proof.* (a) If $k \in \mathbb{N}$, then $k + 1 \in \mathbb{N}$ (Session 3). If $k = 0$, then $k + 1 = 1 \in \mathbb{N}$. If $k = -n$ with $n \in \mathbb{N}$, then $k + 1 = 0$ when $n = 1$, and otherwise $n - 1 \in \mathbb{N}$ (Session 3, Lemma 2) and $k + 1 = -(n - 1)$. In each case $k + 1 \in \mathbb{Z}$.

(b) By the definition of $\mathbb{Z}$, each of $j$ and $k$ lies in $\mathbb{N}$, is $0$, or is the negative of a natural number. Natural numbers are positive (Session 3, Lemma 1), so their negatives are negative. If $j$ is in $\mathbb{N}$ or is $0$, and $k$ is $0$ or negative, then $j \ge 0 \ge k$, against $j \lt k$. The remaining cases are these.
- $j, k \in \mathbb{N}$: $k - j \in \mathbb{N}$ by Session 3, Lemma 4(a).
- $j = 0$, $k \in \mathbb{N}$: $k - j = k$.
- $j = -a$ with $a \in \mathbb{N}$, and $k \in \mathbb{N}$: $k - j = k + a \in \mathbb{N}$ by Session 3, Lemma 3.
- $j = -a$ with $a \in \mathbb{N}$, and $k = 0$: $k - j = a$.
- $j = -a$ and $k = -b$ with $a, b \in \mathbb{N}$: $-a \lt -b$ gives $b \lt a$, so $a - b \in \mathbb{N}$ by Session 3, Lemma 4(a), and $k - j = a - b$.

In every case $k - j \in \mathbb{N}$, so $k - j \ge 1$ by Session 3, Lemma 1, and adding $j$ gives $j + 1 \le k$. ∎

**Lemma (integer part).** For every real $y$ there is exactly one integer $k$ with $k \le y \lt k + 1$, the **integer part** of $y$.

*Proof.* Existence. Let $S = \{j \in \mathbb{Z} : j \le y\}$. By the Archimedean property (Session 4) there is $n \in \mathbb{N}$ with $n \gt -y$, so $-n \lt y$ and $-n \in S$. So $S$ is nonempty, and $y$ is an upper bound for it. Let $s = \sup S$ (Session 4). Since $s - 1 \lt s$, the number $s - 1$ is not an upper bound of $S$, so some $k \in S$ has $k \gt s - 1$. Then $k + 1 \gt s$, so $k + 1 \notin S$. But $k + 1 \in \mathbb{Z}$ by the lemma on integer steps, so $k + 1 \le y$ fails, that is $k + 1 \gt y$. With $k \in S$, this is $k \le y \lt k+1$.

Uniqueness. Suppose $k$ and $k'$ both qualify. Then $k \le y \lt k' + 1$, so $k \lt k' + 1$. Here $k' + 1$ is an integer by part (a) of the lemma on integer steps, and part (b) gives $k + 1 \le k' + 1$, that is $k \le k'$. Exchanging the roles of $k$ and $k'$ gives $k' \le k$. So $k = k'$. ∎

**Definition.** Let $I$ be an interval and $A \subseteq I$. The set $A$ is **dense in** $I$ if for all $x \lt y$ in $I$ there is $a \in A$ with $x \lt a \lt y$.

**Lemma (density of the rationals).** If $x \lt y$ are real, there is a rational $q$ with $x \lt q \lt y$.

*Proof.* By the Archimedean property there is $n \in \mathbb{N}$ with $n \gt 1/(y - x)$, so $n(y - x) \gt 1$. Let $k$ be the integer part of $nx$ and $m = k + 1$, so $m - 1 \le nx \lt m$. Then $m \in \mathbb{Z}$ by the lemma on integer steps, so $m/n \in \mathbb{Q}$ (Session 4), and
$$
nx \lt m \le nx + 1 \lt nx + n(y - x) = ny .
$$
Dividing by $n \gt 0$ gives $x \lt m/n \lt y$. ∎

By the density lemma, $\mathbb{Q}$ is dense in $\mathbb{R}$.

## 10.5 Intervals are uncountable

An interval $I$ has at least two points (Session 7), so it contains two points $x \lt y$. Then $[x, y] \subseteq I$, since each $t \in [x, y]$ is $x$, is $y$, or lies strictly between them. So every interval contains an interval $[x, y]$ of length $y - x \gt 0$, and the words "of positive length" in the claim add no further condition.

**Lemma (nested intervals).** Let $a_n \lt b_n$ for every $n \in \mathbb{N}$, with $[a_{n+1}, b_{n+1}] \subseteq [a_n, b_n]$ for every $n$. Then some real $c$ lies in $[a_n, b_n]$ for every $n$.

*Proof.* The points $a_{n+1}$ and $b_{n+1}$ lie in $[a_{n+1}, b_{n+1}] \subseteq [a_n, b_n]$, so $a_n \le a_{n+1}$ and $b_{n+1} \le b_n$, that is $-b_n \le -b_{n+1}$. So $(a_n)$ and $(-b_n)$ are nondecreasing, and the comparison lemma of Session 6 gives, for $m \le n$, $a_m \le a_n$ and $-b_m \le -b_n$, that is $b_n \le b_m$. Hence $a_m \le b_n$ for all $m$ and $n$: if $m \le n$, then $a_m \le a_n \le b_n$; if $m \gt n$, then $a_m \le b_m \le b_n$.

So the set $\{a_m : m \in \mathbb{N}\}$ is nonempty, and each $b_n$ is an upper bound for it. Let $c$ be its least upper bound (Session 4). Then $a_n \le c$ because $c$ is an upper bound, and $c \le b_n$ because $c$ is the least one. ∎

**Theorem.** If $a \lt b$, the interval $[a, b]$ is uncountable.

*Proof.* The set $[a,b]$ is nonempty, so it is enough to show that no sequence of real numbers has range $[a,b]$. Let $(x_n)$ be any sequence of real numbers. We find a point of $[a, b]$ that is not a term of it. Define closed intervals $[a_n, b_n]$ for $n \ge 0$ by recursion (Session 3, Section 3.5), with values in the set of pairs $(a_n, b_n)$ of reals with $a_n \lt b_n$, starting from $[a_0, b_0] = [a, b]$.

Given $[a_{n-1}, b_{n-1}]$ with $\ell = b_{n-1} - a_{n-1} \gt 0$, form its left and right thirds
$$
K = [a_{n-1},\, a_{n-1} + \ell/3], \qquad K' = [b_{n-1} - \ell/3,\, b_{n-1}] .
$$
Since $0 \lt \ell/3 \lt \ell$, the endpoints of $K$ and $K'$ lie in $[a_{n-1}, b_{n-1}]$, so $K$ and $K'$ are contained in it. Every point of $K$ is at most $a_{n-1} + \ell/3$, and every point of $K'$ is at least $b_{n-1} - \ell/3$. Now $a_{n-1} + \ell/3 \lt b_{n-1} - \ell/3$, because this is equivalent to $2\ell/3 \lt \ell$, which holds since $\ell \gt 0$. So no point lies in both, and $x_n$ lies in at most one of them. If $x_n \notin K$, let $[a_n, b_n] = K$. If $x_n \in K$, let $[a_n, b_n] = K'$; then $x_n \notin K'$. In both cases
$$
[a_n, b_n] \subseteq [a_{n-1}, b_{n-1}], \qquad b_n - a_n = \ell/3 \gt 0, \qquad x_n \notin [a_n, b_n] .
$$
The nested-interval lemma, applied to $[a_n, b_n]$ for $n \in \mathbb{N}$, gives a real $c$ in every $[a_n, b_n]$. Then $c \in [a_1, b_1] \subseteq [a, b]$. For each $n$, $c \in [a_n, b_n]$ and $x_n \notin [a_n, b_n]$, so $c \ne x_n$. So $c$ is a point of $[a, b]$ outside the range of $(x_n)$. ∎

Thirds are used, not halves, because the two closed halves of an interval share their midpoint, and $x_n$ might be that midpoint.

**Corollary.** Every interval is uncountable. In particular $\mathbb{R}$ is uncountable, and $\mathbb{R} \setminus \mathbb{Q}$ is nonempty. A real number that is not rational is **irrational**.

*Proof.* An interval $I$ contains two points $x \lt y$. Then $[x, y] \subseteq I$, and $[x, y]$ is uncountable by the theorem, so $I$ is uncountable by 10.2. $\mathbb{R}$ is an interval (Session 7). If $\mathbb{R} \setminus \mathbb{Q}$ were empty, $\mathbb{R}$ would equal $\mathbb{Q}$, which is countable by 10.4. ∎

The theorem is due to G. Cantor, "Ueber eine Eigenschaft des Inbegriffes aller reellen algebraischen Zahlen", *J. reine angew. Math.* 77 (1874), 258-262, which also shows that the real algebraic numbers are countable.

**What fails without the least-upper-bound property.** The set $[0,1] \cap \mathbb{Q}$ contains $0$, and it is countable as a subset of $\mathbb{Q}$ (10.2, 10.4). Run the construction above on an enumeration $(x_n)$ of it. Every rational point of $[0,1]$ is some $x_n$ and lies outside $[a_n, b_n]$, and a rational number outside $[0,1]$ lies outside $[a_1, b_1] \subseteq [0,1]$, so no rational number lies in every interval. So the point $c$ of the nested-interval lemma, which lies in $[0,1]$, is irrational. It is supplied by the least-upper-bound property, the axiom that separates $\mathbb{R}$ from $\mathbb{Q}$ (Session 4).

## 10.6 Dense complements

**Theorem.** Let $I$ be an interval and $C$ a countable set. Then $I \setminus C$ is dense in $I$.

*Proof.* Let $x \lt y$ be points of $I$. The set $(x, y)$ is an interval (Session 7), so it is uncountable by the corollary of 10.5. If $(x, y)$ were contained in $C$, it would be countable by 10.2. So some $a$ with $x \lt a \lt y$ is not in $C$. Since $I$ is an interval, $a \in I$. So $a \in I \setminus C$. ∎

**Corollary.** $\mathbb{R} \setminus \mathbb{Q}$ is dense in $\mathbb{R}$: between any two reals there is an irrational number.

*Proof.* Take $I = \mathbb{R}$ and $C = \mathbb{Q}$, countable by 10.4. ∎

## 10.7 Monotone functions

Recall from Session 7 that a function $f$ on an interval $I$ is nondecreasing if $x \lt y$ in $I$ implies $f(x) \le f(y)$, nonincreasing if $x \lt y$ in $I$ implies $f(x) \ge f(y)$, and monotone if it is one of the two.

Let $f : I \to \mathbb{R}$ be nondecreasing and $x \in I$. Define two numbers.

- If some $t \in I$ has $t \lt x$, let $L(x) = \sup\{f(t) : t \in I,\ t \lt x\}$. The set is nonempty and bounded above by $f(x)$, since $t \lt x$ gives $f(t) \le f(x)$; so the supremum exists (Session 4). If no $t \in I$ has $t \lt x$, let $L(x) = f(x)$.
- If some $t \in I$ has $t \gt x$, let $R(x) = \inf\{f(t) : t \in I,\ t \gt x\}$. The set is nonempty and bounded below by $f(x)$, so the infimum exists (Session 4). If no $t \in I$ has $t \gt x$, let $R(x) = f(x)$.

When $L(x) \lt R(x)$, the open interval $(L(x), R(x))$ is the **jump** of $f$ at $x$.

**Lemma 1.** For every $x \in I$, $L(x) \le f(x) \le R(x)$. For $x \lt y$ in $I$, $R(x) \le L(y)$.

*Proof.* In the first case of the definition, $f(x)$ is an upper bound of the set whose least upper bound is $L(x)$, so $L(x) \le f(x)$; in the second case they are equal. The argument for $R(x)$ is the same with lower bounds.

Let $x \lt y$ in $I$, and $t = (x + y)/2$. Then $x \lt t \lt y$ (Session 4, 4.3(g)), and $t \in I$ because $I$ is an interval. Since $t \gt x$, the first case defines $R(x)$, and $R(x) \le f(t)$ because $R(x)$ is a lower bound of a set containing $f(t)$. Since $t \lt y$, the first case defines $L(y)$, and $f(t) \le L(y)$ because $L(y)$ is an upper bound of a set containing $f(t)$. So $R(x) \le f(t) \le L(y)$. ∎

**Lemma 2.** A nondecreasing $f : I \to \mathbb{R}$ is continuous at $x \in I$ if and only if $L(x) = R(x)$.

*Proof.* Suppose $L(x) = R(x)$. By Lemma 1 both equal $f(x)$. Let $\varepsilon \gt 0$.

- If some $t \in I$ has $t \lt x$: the number $f(x) - \varepsilon$ is less than $L(x) = f(x)$, so it is not an upper bound of $\{f(t) : t \lt x\}$, and some $t_1 \in I$ with $t_1 \lt x$ has $f(t_1) \gt f(x) - \varepsilon$. Put $\delta_1 = x - t_1$. Otherwise put $\delta_1 = 1$.
- If some $t \in I$ has $t \gt x$: in the same way some $t_2 \in I$ with $t_2 \gt x$ has $f(t_2) \lt f(x) + \varepsilon$. Put $\delta_2 = t_2 - x$. Otherwise put $\delta_2 = 1$.

Let $\delta = \min\{\delta_1, \delta_2\} \gt 0$ and let $y \in I$ with $\lvert y - x \rvert \lt \delta$. If $y \lt x$, then $y$ is a point of $I$ below $x$, so the first bullet applies and $t_1$ was defined; and $y \gt x - \delta_1 = t_1$, so $f(t_1) \le f(y) \le f(x)$, which gives $f(x) - \varepsilon \lt f(y) \le f(x)$. If $y \gt x$, then $y$ is a point of $I$ above $x$, so $t_2$ was defined, and in the same way $f(x) \le f(y) \le f(t_2) \lt f(x) + \varepsilon$. If $y = x$, then $f(y) - f(x) = 0$. In every case $\lvert f(y) - f(x) \rvert \lt \varepsilon$, so $f$ is continuous at $x$ (Session 7).

Conversely, suppose $L(x) \ne R(x)$. By Lemma 1, $L(x) \lt R(x)$, so $f(x) \lt R(x)$ or $L(x) \lt f(x)$. Take the first case. Then $R(x) \ne f(x)$, so $R(x)$ was defined by the first case of its definition, and some $t \in I$ has $t \gt x$. Let $\varepsilon = R(x) - f(x) \gt 0$. For any $\delta \gt 0$, put $y = \min\{x + \delta/2,\, t\}$. Then $x \lt y \le t$, and $y \in I$: if $y = t$ this is given, and otherwise $x \lt y \lt t$ and $I$ is an interval. Also $\lvert y - x \rvert \le \delta/2 \lt \delta$. Since $y \gt x$, $f(y) \ge R(x)$, so $\lvert f(y) - f(x) \rvert \ge R(x) - f(x) = \varepsilon$. So no $\delta$ serves this $\varepsilon$, and $f$ is not continuous at $x$. The second case is the same with some $t \lt x$ in $I$, $\varepsilon = f(x) - L(x) \gt 0$ and $y = \max\{x - \delta/2,\, t\}$, using $f(y) \le L(x)$ for $y \lt x$. ∎

**Theorem (discontinuities of monotone functions).** Let $I$ be an interval and $f : I \to \mathbb{R}$ monotone. The set $D$ of points of $I$ at which $f$ is not continuous is countable.

*Proof.* Suppose first that $f$ is nondecreasing. By Lemma 2, $f$ is not continuous at $x$ if and only if $L(x) \ne R(x)$, and since $L(x) \le R(x)$ (Lemma 1), $D = \{x \in I : L(x) \lt R(x)\}$. For each rational $q$ let
$$
D_q = \{x \in D : L(x) \lt q \lt R(x)\},
$$
the set of points whose jump contains $q$.

*Each $D_q$ has at most one element.* If $x \lt y$ both lay in $D_q$, Lemma 1 would give $q \lt R(x) \le L(y) \lt q$, which is false.

*The $D_q$ cover $D$.* If $x \in D$, then $L(x) \lt R(x)$, and the density lemma of 10.4 gives a rational $q$ with $L(x) \lt q \lt R(x)$, so $x \in D_q$.

So $D = \bigcup_{q \in \mathbb{Q}} D_q$. The index set $\mathbb{Q}$ is countable (10.4). Each nonempty $D_q$ is $\{x_q\}$ for exactly one point $x_q$, and it is given with the enumeration $n \mapsto x_q$; no choice is made, since $x_q$ is the only element. By the theorem on countable unions (10.3), $D$ is countable.

If $f$ is nonincreasing, $g = -f$ is nondecreasing, and $\lvert g(y) - g(x) \rvert = \lvert -(f(y) - f(x)) \rvert = \lvert f(y) - f(x) \rvert$ (Session 5) for all $x, y$, so $g$ is continuous exactly where $f$ is. The first part applies to $g$. ∎

This is the sense of "each jump contains its own rational": distinct points have disjoint jumps (Lemma 1), so a rational lies in the jump of at most one point. The result usually appears without a name. It is sometimes called Froda's theorem, after A. Froda's 1929 thesis, which states it as already well known.

## 10.8 Worked example

On $I = [0, 1]$ define $f(0) = 0$ and, for $0 \lt x \le 1$, $f(x) = 1/n$, where $n$ is the integer part of $1/x$ (10.4). Here $n \in \mathbb{N}$, for the following reason. Since $0 \lt x \le 1$, $1/x \ge 1$ (Session 4). An integer that is not in $\mathbb{N}$ is $0$ or the negative of a natural number, so it is at most $0$ (Session 4; Session 3, Lemma 1). If $n \le 0$, then $1/x \lt n + 1 \le 1$, which is false. For $x \gt 0$ and $n \in \mathbb{N}$,
$$
n \le 1/x \lt n+1 \quad \text{if and only if} \quad \frac{1}{n+1} \lt x \le \frac{1}{n},
$$
by multiplying through by $x \gt 0$ and dividing by $n$ and by $n+1$. So $f = 1/n$ on the piece $(1/(n+1), 1/n]$: $f = 1$ on $(1/2, 1]$, $f = 1/2$ on $(1/3, 1/2]$, $f = 1/3$ on $(1/4, 1/3]$, and so on.

*$f$ is nondecreasing.* Let $0 \lt x \le y \le 1$, with $n$ the integer part of $1/x$ and $m$ that of $1/y$. Then $m \le 1/y \le 1/x \lt n + 1$, so $m \lt n + 1$, and the lemma on integer steps (10.4) gives $m + 1 \le n + 1$, that is $m \le n$. So $f(x) = 1/n \le 1/m = f(y)$. If $x = 0$, then $f(x) = 0 \le f(y)$, since every value of $f$ is $0$ or positive.

Now compute $L$ and $R$ at each point.

1. *At $x = 0$.* No point of $I$ is below $0$, so $L(0) = f(0) = 0$. Every $f(t)$ with $t \gt 0$ is positive, so $0$ is a lower bound of $\{f(t) : 0 \lt t \le 1\}$, and $R(0) \ge 0$ because $R(0)$ is the greatest lower bound. For any $\varepsilon \gt 0$, Session 4 (Corollary (a) of the Archimedean property) gives $n \in \mathbb{N}$ with $1/n \lt \varepsilon$, and $f(1/n) = 1/n \lt \varepsilon$; so no positive number is a lower bound, and $R(0)$, which is one, is not positive. Hence $R(0) = 0 = L(0)$, and $f$ is continuous at $0$ by Lemma 2.
2. *Inside a piece,* $1/(n+1) \lt x \lt 1/n$ with $n \in \mathbb{N}$. Every $t \lt x$ has $f(t) \le f(x) = 1/n$, and the points of $(1/(n+1), x)$ give the value $1/n$, so $L(x) = 1/n$. Every $t \gt x$ has $f(t) \ge 1/n$, and the points of $(x, 1/n]$ give $1/n$, so $R(x) = 1/n$. Continuous.
3. *At $x = 1$.* No point of $I$ is above $1$, so $R(1) = f(1) = 1$. The points of $(1/2, 1)$ give the value $1$, and every $f(t) \le f(1) = 1$, so $L(1) = 1$. Continuous.
4. *At $x = 1/n$ with $n \ge 2$.* The points of $(1/(n+1), 1/n)$ give the value $1/n = f(1/n)$, and every $f(t)$ with $t \lt 1/n$ is at most $f(1/n)$, so $L(1/n) = 1/n$. For $t \gt 1/n$, the integer part $m$ of $1/t$ satisfies $m \le 1/t \lt n$, so $m + 1 \le n$ by the lemma on integer steps, that is $m \le n - 1$, and $f(t) = 1/m \ge 1/(n-1)$; the point $t = 1/(n-1)$ gives exactly $1/(n-1)$. So $R(1/n) = 1/(n-1)$. Since $1/n \lt 1/(n-1)$, $f$ is not continuous at $1/n$ (Lemma 2).

Every point of $[0,1]$ falls under one of the four cases. The points $0$ and $1$ are cases 1 and 3. If $0 \lt x \lt 1$, let $n$ be the integer part of $1/x$, so $1/(n+1) \lt x \le 1/n$ by the equivalence above. If $x \lt 1/n$, this is case 2. If $x = 1/n$, then $n \ne 1$ because $x \lt 1$, so $n \gt 1$ (Session 3, Lemma 1) and $n \ge 2$ (Session 3, Lemma 4(a)); this is case 4. So
$$
D = \{1/2,\ 1/3,\ 1/4,\ \dots\} = \{1/(n+1) : n \in \mathbb{N}\},
$$
countable as the range of the sequence $n \mapsto 1/(n+1)$. Its points are all different: $n \lt n'$ gives $n + 1 \lt n' + 1$, so $1/(n'+1) \lt 1/(n+1)$ (Session 4). The jumps are $(1/2, 1)$, $(1/3, 1/2)$, $(1/4, 1/3)$, ..., pairwise disjoint as Lemma 1 requires. The jump at $1/n$ contains its midpoint (Session 4, 4.3(g))
$$
\frac{1}{2}\Bigl(\frac{1}{n} + \frac{1}{n-1}\Bigr) = \frac{2n - 1}{2n(n-1)},
$$
which is $3/4$ for $n = 2$ and $5/12$ for $n = 3$. So $D_{3/4} = \{1/2\}$ and $D_{5/12} = \{1/3\}$. For every $\varepsilon \gt 0$ some point of $D$ lies in $(0, \varepsilon)$ (case 1 gives $n$ with $1/n \lt \varepsilon$, and $1/(n+1) \lt 1/n$), yet $f$ is continuous at $0$.

## 10.9 What fails without monotonicity

Define $f : [0, 1] \to \mathbb{R}$ by $f(x) = 1$ if $x$ is rational and $f(x) = 0$ otherwise. This is the **Dirichlet function**, which appears at the end of P. G. L. Dirichlet, "Sur la convergence des séries trigonométriques qui servent à représenter une fonction arbitraire entre des limites données", *J. reine angew. Math.* 4 (1829), 157-169.

It is not monotone. By the corollary of 10.6 there is an irrational $s$ with $0 \lt s \lt 1$. Then $0 \lt s$ but $f(0) = 1 \gt 0 = f(s)$, so $f$ is not nondecreasing; and $s \lt 1$ but $f(s) = 0 \lt 1 = f(1)$, so $f$ is not nonincreasing.

It is continuous at no point. Let $x \in [0, 1]$, take $\varepsilon = 1/2$, and let $\delta \gt 0$. If $x \lt 1$, put $u = x$ and $v = \min\{x + \delta/2,\, 1\}$; if $x = 1$, put $u = \max\{1 - \delta/2,\, 0\}$ and $v = 1$. In both cases $u \lt v$, both lie in $[0,1]$, and every point between them is within $\delta/2$ of $x$. By the density lemma of 10.4 there is a rational $r$ with $u \lt r \lt v$, and by the corollary of 10.6 an irrational $s$ with $u \lt s \lt v$. Both lie in $[0, 1]$ and within $\delta$ of $x$, and $f(r) = 1$, $f(s) = 0$. They cannot both be within $1/2$ of $f(x)$, because then the triangle inequality (Session 5) would give
$$
1 = \lvert f(r) - f(s) \rvert \le \lvert f(r) - f(x) \rvert + \lvert f(x) - f(s) \rvert \lt \tfrac12 + \tfrac12 = 1 .
$$
So no $\delta$ serves $\varepsilon = 1/2$. The set of discontinuities is all of $[0,1]$, which is uncountable by 10.5.

## Exercises

*Check*

1. (a) Continue the table of 10.3: find $p_{11}, \dots, p_{15}$. (b) Find the $m$ with $p_m = (3, 4)$. (c) Find the terms $c_{11}, \dots, c_{15}$ of the enumeration of $\mathbb{Q}$ in 10.4.
2. Run the construction in the proof of 10.5 on $[a, b] = [0, 1]$ with $x_1 = 0$, $x_2 = 3/4$, $x_3 = 9/10$ and $x_n = 0$ for every $n \ge 4$. Find $[a_n, b_n]$ for $n = 1, 2, 3$ and for every $n \ge 4$, and find the point $c$ of the nested-interval lemma. Check that $c$ differs from every $x_n$.
3. On $I = [0, 3]$ let $f(x) = x$ for $0 \le x \lt 1$, $f(1) = 2$, $f(x) = x + 1$ for $1 \lt x \le 2$ and $f(x) = 5$ for $2 \lt x \le 3$. Show that $f$ is nondecreasing, find $L(x)$ and $R(x)$ at every $x \in I$, find the set $D$ of points where $f$ is not continuous, and give a rational in each jump.

*Prove*

4. Let $(a_n)$ enumerate $A$ and $(b_n)$ enumerate $B$. Without the theorem on countable unions, show that the sequence $c_{2n-1} = a_n$, $c_{2n} = b_n$ enumerates $A \cup B$.
5. Show that if $A$ and $B$ are countable, then $A \times B$ is countable. Deduce that $\mathbb{Q} \times \mathbb{Q}$ is countable.
6. Let $a \lt b$ and let $f : [a, b] \to \mathbb{R}$ be nondecreasing. Suppose that for every $w$ with $f(a) \lt w \lt f(b)$ there is $t \in [a, b]$ with $f(t) = w$. Show that $f$ is continuous at every point of $[a, b]$. (This is a converse, for monotone functions, of the intermediate value theorem of Session 7.)

*Extend*

7. Let $I$ be an interval, $C$ a nonempty countable set of real numbers with a fixed enumeration $(c_k)$, and $x \in I$. Show that there is a sequence $(y_n)$ in $I \setminus C$ with $y_n \to x$ (Session 5), given by an explicit rule for each $n$, so that no choice is needed for infinitely many $n$ at once (10.3). (Hint: use the proof of 10.5 as a rule that turns an interval $[u, v]$ with $u \lt v$ into a point of $[u, v]$ outside $C$.)
8. (Cantor's diagonal argument.) Let $S$ be the set of all sequences $(s_k)$ with every $s_k \in \{0, 1\}$. (a) Given any sequence $n \mapsto s^{(n)}$ of elements of $S$, define $d_k = 1 - s^{(k)}_k$. Show that $d \in S$ and $d \ne s^{(n)}$ for every $n$, and conclude that $S$ is uncountable. (b) Deduce that the set of all subsets of $\mathbb{N}$ is uncountable. (Compare Session 2, Exercise 7.) The argument is from G. Cantor, "Ueber eine elementare Frage der Mannigfaltigkeitslehre", *Jahresbericht der Deutschen Mathematiker-Vereinigung* 1 (1890-91), 75-78.

Solutions: [solutions/010-countable-sets.md](../solutions/010-countable-sets.md).
