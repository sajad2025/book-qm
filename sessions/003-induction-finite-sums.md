# 1.3. Mathematical induction and finite sums

*Theorem. Builds on Session 2.*

**Claim.** The principle of induction proves statements for all natural numbers, and with it the rules for manipulating finite sums and products, including the binomial theorem and Bernoulli's inequality $(1 + x)^n \ge 1 + nx$ for every $x \ge -1$ and every natural number $n$.

The session first says what the natural numbers are and proves the principle of induction from that description. It then proves the few facts about natural numbers that later sessions cite, shows that induction can define things as well as prove them, and uses it to define sums, products, powers and factorials. The rules for computing with them follow, and the session ends with the binomial theorem and Bernoulli's inequality.

## 3.1 What this session uses

**Recall (Session 2).** A set is determined by its elements, and two sets are equal when each is a subset of the other. A function $f : A \to B$ assigns to each element of $A$ one element of $B$. The negation of "for every $x$, $P(x)$" is "there exists $x$ such that not $P(x)$". A statement can be proved by contradiction: assume its negation and derive a statement together with its negation.

In this session a **number** means a real number, and the set of numbers is written $\mathbb{R}$. The axioms of the real numbers are stated in the next session, which checks that every rule listed below is one of those axioms or follows from them in a few lines. Here the rules are taken as given, and nothing else about numbers is used. In particular, no general fact about the natural numbers is assumed: each one used is proved below.

**Rules of arithmetic.** For all numbers $x$, $y$, $z$:
- $x + y = y + x$, $xy = yx$, $(x + y) + z = x + (y + z)$, $(xy)z = x(yz)$ and $x(y + z) = xy + xz$;
- $x + 0 = x$, $x \cdot 1 = x$, and $0 \ne 1$;
- there is a number $-x$ with $x + (-x) = 0$, and if $x \ne 0$ there is a number $1/x$ with $x \cdot (1/x) = 1$; $y - x$ means $y + (-x)$, and $y/x$ means $y \cdot (1/x)$;
- $x \cdot 0 = 0$, $(-x)y = -(xy)$, $(-x)(-y) = xy$, $-(-x) = x$ and $-(x + y) = (-x) + (-y)$; if $y - x = 0$ then $y = x$; if $xy = 0$ then $x = 0$ or $y = 0$;
- if $x, y \ne 0$ then $1/(1/x) = x$ and $1/(xy) = (1/x)(1/y)$; fractions with nonzero denominators add and multiply by the rules $a/b + c/d = (ad + bc)/(bd)$ and $(a/b)(c/d) = (ac)/(bd)$, and $(ac)/(bc) = a/b$ when $b, c \ne 0$, since $(ac)/(bc) = (a/b)(c/c) = (a/b) \cdot 1$.

**Rules of order.** Here $x \le y$ means "$x \lt y$ or $x = y$", and $y \gt x$ and $y \ge x$ mean $x \lt y$ and $x \le y$. For all numbers $x$, $y$, $z$, $u$, $v$:
- exactly one of $x \lt y$, $x = y$, $y \lt x$ holds;
- if $x \lt y$ and $y \lt z$ then $x \lt z$; if $x \le y$ and $y \lt z$, or $x \lt y$ and $y \le z$, then $x \lt z$; if $x \le y$ and $y \le z$ then $x \le z$; if $x \le y$ and $y \le x$ then $x = y$;
- if $x \lt y$ then $x + z \lt y + z$; if $x \le y$ and $u \le v$ then $x + u \le y + v$;
- if $x \lt y$ and $0 \lt z$ then $xz \lt yz$; if $x \le y$ and $z \ge 0$ then $xz \le yz$;
- if $x \lt y$ then $-y \lt -x$, and if $x \le y$ then $-y \le -x$;
- $0 \lt 1$; $x^2 = x \cdot x \ge 0$, with $x^2 \gt 0$ when $x \ne 0$; if $0 \lt x$ then $0 \lt 1/x$.

## 3.2 The natural numbers and the principle of induction

The natural numbers are meant to be $1$, $1 + 1$, $1 + 1 + 1$, and so on. The words "and so on" are not a definition. The following definition captures them: the natural numbers are the numbers that every set containing $1$ and closed under adding $1$ must contain.

**Definition.** A set $S$ of numbers is **inductive** if $1 \in S$, and $x + 1 \in S$ whenever $x \in S$.

The set of all numbers is inductive. So is the set of numbers $x$ with $x \ge 1$, as Lemma 1 below shows.

**Definition.** The set of **natural numbers** $\mathbb{N}$ is the set of numbers $x$ such that $x \in S$ for every inductive set $S$.

**Lemma ($\mathbb{N}$ is inductive).** $\mathbb{N}$ is inductive, and $\mathbb{N} \subseteq S$ for every inductive set $S$.

*Proof.* The second statement is the definition of $\mathbb{N}$. For the first: $1$ lies in every inductive set, so $1 \in \mathbb{N}$. Let $n \in \mathbb{N}$ and let $S$ be any inductive set. Then $n \in S$, so $n + 1 \in S$ because $S$ is inductive. Since $S$ was any inductive set, $n + 1 \in \mathbb{N}$. ∎

**Numerals.** Particular natural numbers are named as usual: $2 = 1 + 1$, $3 = 2 + 1$, $4 = 3 + 1$, and each further numeral, written with the digits $0$ to $9$ in the usual way, names the number obtained by adding $1$ to the number before it. Each lies in $\mathbb{N}$ by the lemma. A computation with particular numerals, such as $2 + 2 = 2 + (1 + 1) = (2 + 1) + 1 = 3 + 1 = 4$ or $2 \cdot 3 = 2 \cdot 2 + 2 = 4 + 2 = 6$, is a finite chain of the rules of Section 3.1, and in examples it is written without comment.

**Theorem (principle of induction).** Let $S \subseteq \mathbb{N}$. If $1 \in S$, and $n + 1 \in S$ whenever $n \in S$, then $S = \mathbb{N}$.

*Proof.* The hypotheses say that $S$ is inductive. By the definition of $\mathbb{N}$, every element of $\mathbb{N}$ lies in $S$, so $\mathbb{N} \subseteq S$. Together with $S \subseteq \mathbb{N}$ this gives $S = \mathbb{N}$ (Session 2). ∎

The theorem is used in the following form. Let $P(n)$ be a statement about a natural number $n$. Suppose that

- (**base case**) $P(1)$ is true, and
- (**inductive step**) for every $n \in \mathbb{N}$, if $P(n)$ is true then $P(n + 1)$ is true.

Then $P(n)$ is true for every $n \in \mathbb{N}$. To see this, apply the theorem to $S = \{n \in \mathbb{N} : P(n)\}$. In the inductive step, the assumption "$P(n)$ is true" is the **induction hypothesis**.

**Example.** For every $n \in \mathbb{N}$, $1 + 2 + \dots + n = n(n+1)/2$. The sum on the left is defined precisely in Section 3.6. Here $1 + 2 + \dots + (n+1)$ means the number obtained by adding $n + 1$ to $1 + 2 + \dots + n$, and for $n = 1$ the sum is $1$. Let $P(n)$ be the statement. The right side divides by $2$, and $2 \ne 0$: adding $1$ to both sides of $0 \lt 1$ gives $1 \lt 2$, so $0 \lt 2$. Base case: the left side of $P(1)$ is $1$, and the right side is $1 \cdot 2/2 = 2 \cdot (1/2) = 1$. Inductive step: assume $P(n)$. Write $n + 1 = (n + 1) \cdot 2 \cdot (1/2) = \frac{2(n+1)}{2}$. Fractions with the same denominator add by the distributive law: $a/d + b/d = a \cdot (1/d) + b \cdot (1/d) = (a + b)/d$. So

$$
1 + 2 + \dots + n + (n+1) = \frac{n(n+1)}{2} + \frac{2(n+1)}{2} = \frac{n(n+1) + 2(n+1)}{2} = \frac{(n+1)(n+2)}{2},
$$

where the last step is the distributive law. This is $P(n+1)$. By induction, $P(n)$ holds for every $n \in \mathbb{N}$.

**What fails without the base case.** Let $P(n)$ be the statement $n + 1 \le n$. If $P(n)$ is true, adding $1$ to both sides gives $n + 2 \le n + 1$, which is $P(n+1)$. So the inductive step holds for every $n$. But $P(1)$ says $2 \le 1$, which is false, and in fact $P(n)$ is false for every $n$, since $n \lt n + 1$ by $0 \lt 1$. The inductive step only carries truth forward; the base case supplies it.

## 3.3 First facts about the natural numbers

Each fact below is proved from the definition of $\mathbb{N}$, the principle of induction and the rules of Section 3.1.

**Lemma 1.** Every $n \in \mathbb{N}$ satisfies $n \ge 1$. In particular $0 \notin \mathbb{N}$.

*Proof.* Let $T$ be the set of numbers $x$ with $x \ge 1$. Then $1 \in T$. If $x \in T$, then $x \lt x + 1$ (add $x$ to both sides of $0 \lt 1$), and $1 \le x$, so $1 \lt x + 1$ and $x + 1 \in T$. Thus $T$ is inductive, and $\mathbb{N} \subseteq T$ by the definition of $\mathbb{N}$. Since $0 \lt 1$, the number $0$ is not in $T$, so it is not in $\mathbb{N}$. ∎

**Lemma 2.** If $n \in \mathbb{N}$ and $n \ne 1$, then $n - 1 \in \mathbb{N}$.

*Proof.* Let $S$ be the set of $n \in \mathbb{N}$ such that $n = 1$ or $n - 1 \in \mathbb{N}$. Then $1 \in S$. Let $n \in S$. Then $n + 1 \in \mathbb{N}$, and $(n + 1) - 1 = n \in \mathbb{N}$, so $n + 1 \in S$. By the principle of induction $S = \mathbb{N}$, which is the claim. ∎

**Lemma 3.** If $m, n \in \mathbb{N}$, then $m + n \in \mathbb{N}$ and $mn \in \mathbb{N}$.

*Proof.* Fix $m \in \mathbb{N}$. Let $S$ be the set of $n \in \mathbb{N}$ with $m + n \in \mathbb{N}$. Then $1 \in S$ because $\mathbb{N}$ is inductive. If $n \in S$, then $m + (n + 1) = (m + n) + 1 \in \mathbb{N}$, so $n + 1 \in S$. Hence $S = \mathbb{N}$.

Now let $S'$ be the set of $n \in \mathbb{N}$ with $mn \in \mathbb{N}$. Then $m \cdot 1 = m \in \mathbb{N}$, so $1 \in S'$. If $n \in S'$, then $m(n + 1) = mn + m$, a sum of two natural numbers, which lies in $\mathbb{N}$ by the first part. So $n + 1 \in S'$, and $S' = \mathbb{N}$. ∎

**Lemma 4.** Let $m, n \in \mathbb{N}$.
- (a) If $m \lt n$, then $n - m \in \mathbb{N}$, and $m + 1 \le n$.
- (b) If $k \in \mathbb{N}$ and $k \le n + 1$, then $k \le n$ or $k = n + 1$.

So no natural number lies strictly between $n$ and $n + 1$.

*Proof.* (a) Fix $n \in \mathbb{N}$, and let $S$ be the set of $m \in \mathbb{N}$ such that, if $m \lt n$, then $n - m \in \mathbb{N}$. We show $S = \mathbb{N}$ by induction.

Base case. If $1 \lt n$, then $n \ne 1$, so $n - 1 \in \mathbb{N}$ by Lemma 2. Hence $1 \in S$.

Inductive step. Let $m \in S$, and suppose $m + 1 \lt n$. Then $m \lt m + 1 \lt n$, so $n - m \in \mathbb{N}$ because $m \in S$. Subtracting $m$ from $m + 1 \lt n$ gives $1 \lt n - m$, so $n - m \ne 1$ and $(n - m) - 1 \in \mathbb{N}$ by Lemma 2. Since $(n - m) - 1 = n - (m + 1)$ by the rules of Section 3.1, $m + 1 \in S$.

So $S = \mathbb{N}$. Now if $m \lt n$, then $m \in S$ gives $n - m \in \mathbb{N}$, so $n - m \ge 1$ by Lemma 1. Adding $m$ to both sides gives $n \ge m + 1$.

(b) Suppose $k \ne n + 1$. Then $k \lt n + 1$, so $k + 1 \le n + 1$ by (a). Subtracting $1$ gives $k \le n$. ∎

**Lemma (parity).** Every $n \in \mathbb{N}$ equals $2k$ or $2k - 1$ for some $k \in \mathbb{N}$, and not both. The number $k$ is unique. In the first case $n$ is **even**, and in the second it is **odd**.

*Proof.* Existence, by induction on $n$. For $n = 1$: $1 = 2 \cdot 1 - 1$. If $n = 2k - 1$, then $n + 1 = 2k$. If $n = 2k$, then $n + 1 = 2(k + 1) - 1$, and $k + 1 \in \mathbb{N}$.

Not both. Suppose $2k = 2j - 1$ with $j, k \in \mathbb{N}$. Adding $1 - 2k$ to both sides gives $2(j - k) = 1$. If $j \le k$, then $j - k \le 0$, and multiplying by $2 \gt 0$ (Section 3.2) gives $2(j - k) \le 0 \lt 1$. If $j \gt k$, then $j - k \in \mathbb{N}$ by Lemma 4(a), so $j - k \ge 1$ by Lemma 1, and multiplying by $2$ gives $2(j - k) \ge 2 \gt 1$. Either way $2(j - k) \ne 1$.

Uniqueness of $k$. By what was just shown, $n$ has only one of the two forms. If $2k = 2k'$, multiplying by $1/2$ gives $k = k'$. If $2k - 1 = 2k' - 1$, adding $1$ and multiplying by $1/2$ gives $k = k'$. ∎

**Notation.** For $n = 0$ or $n \in \mathbb{N}$, write $\{1, \dots, n\}$ for the set of $k \in \mathbb{N}$ with $k \le n$. By Lemma 1, $\{1, \dots, 0\}$ is empty and $\{1, \dots, 1\} = \{1\}$. By Lemma 4(b), $\{1, \dots, n+1\}$ is $\{1, \dots, n\}$ together with the one further element $n + 1$.

When the letters $j$, $k$, $m$, $n$ and $n_0$ index sums, products, powers or sequences (defined in Sections 3.5 and 3.6), they stand for natural numbers or zero, and for them "$n \ge 0$" means that $n = 0$ or $n \in \mathbb{N}$. Such an $n$ also satisfies $n \ge 0$ in the order of numbers: $n = 0$, or $n \ge 1 \gt 0$ by Lemma 1. For any other letter, $x \ge 0$ is the inequality of Section 3.1. A chain $0 \le k \le n$ means $k \ge 0$ and $k \le n$.

**Corollary (induction from 0).** Let $P(n)$ be a statement about $n \ge 0$. If $P(0)$ is true, and $P(n)$ implies $P(n+1)$ for every $n \ge 0$, then $P(n)$ is true for every $n \ge 0$.

*Proof.* $P(0)$ and the step at $n = 0$ give $P(1)$. The steps at $n \in \mathbb{N}$ then give $P(n)$ for every $n \in \mathbb{N}$ by the principle of induction. ∎

**Corollary (induction from $n_0$).** Let $n_0 \in \mathbb{N}$, and let $P(n)$ be a statement about $n \in \mathbb{N}$. If $P(n_0)$ is true, and $P(n)$ implies $P(n+1)$ for every $n \in \mathbb{N}$ with $n \ge n_0$, then $P(n)$ is true for every $n \in \mathbb{N}$ with $n \ge n_0$.

*Proof.* Let $Q(n)$ be the statement "if $n \ge n_0$ then $P(n)$", and prove $Q(n)$ for every $n \in \mathbb{N}$ by induction. Base case: if $1 \ge n_0$, then $n_0 = 1$ by Lemma 1, and $P(1) = P(n_0)$ is true. Inductive step: assume $Q(n)$, and let $n + 1 \ge n_0$. If $n + 1 = n_0$, then $P(n+1)$ is true. Otherwise $n_0 \lt n + 1$, so $n_0 \le n$ by Lemma 4(b); then $P(n)$ holds by $Q(n)$, and $P(n+1)$ holds by the step. ∎

## 3.4 The least element

**Definition.** Let $A$ be a set of numbers. An element $a \in A$ is a **least element** of $A$ if $a \le b$ for every $b \in A$. A set has at most one least element: if $a$ and $a'$ are both least elements, then $a \le a'$ and $a' \le a$, so $a = a'$ (Section 3.1).

**Theorem (well-ordering of $\mathbb{N}$).** Every nonempty subset $A$ of $\mathbb{N}$ has a least element.

*Proof.* Suppose, for a contradiction, that $A$ is nonempty and has no least element. Let $S$ be the set of $n \in \mathbb{N}$ such that no $k \in \mathbb{N}$ with $k \le n$ lies in $A$.

Base case. If $1 \in A$, then $1$ is a least element of $A$, because every element of $A$ is at least $1$ by Lemma 1. So $1 \notin A$. A natural number $k$ with $k \le 1$ equals $1$ by Lemma 1. Hence $1 \in S$.

Inductive step. Let $n \in S$. Every $b \in A$ satisfies $b \gt n$: otherwise $b \le n$, and $n \in S$ would give $b \notin A$. By Lemma 4(a), every $b \in A$ then satisfies $b \ge n + 1$. So if $n + 1 \in A$, it is a least element of $A$; there is none, so $n + 1 \notin A$. Now let $k \in \mathbb{N}$ with $k \le n + 1$. By Lemma 4(b), $k \le n$, in which case $k \notin A$ because $n \in S$, or $k = n + 1$, in which case $k \notin A$ by what was just shown. Hence $n + 1 \in S$.

By induction $S = \mathbb{N}$. Let $a \in A$. Then $a \in S$, and $a \le a$, so $a \notin A$. This contradicts $a \in A$. ∎

Section 3.5 uses the theorem to turn the choice of a natural number into a function.

## 3.5 Definition by recursion

A **sequence** in a set $X$ is a function $\mathbb{N} \to X$. Its value at $n$ is written $a_n$, and the sequence is written $(a_n)$. A sequence of numbers, or **real sequence**, is a sequence in $\mathbb{R}$. A sequence **indexed from 0** is a function on the set of $n \ge 0$, written in the same way.

Sums, products and powers are defined by recursion: the first value is given, and each later value is given in terms of the one before. The next theorem shows that such a description defines exactly one sequence.

**Theorem (definition by recursion).** Let $X$ be a set, $c \in X$, and for each $n \in \mathbb{N}$ let $g_n : X \to X$. There is exactly one sequence $(s_n)$ in $X$ with

$$
s_1 = c, \qquad s_{n+1} = g_n(s_n) \quad \text{for every } n \in \mathbb{N}.
$$

*Proof.* For $n \in \mathbb{N}$, call a function $t : \{1, \dots, n\} \to X$ an **$n$-step solution** if $t(1) = c$ and $t(k+1) = g_k(t(k))$ for every $k \in \mathbb{N}$ with $k + 1 \le n$ (then $k \lt k + 1 \le n$, so $t(k)$ is defined).

If $t : \{1, \dots, n+1\} \to X$, its **restriction** to $\{1, \dots, n\}$ is the function $\{1, \dots, n\} \to X$, $k \mapsto t(k)$; each such $k$ is in the domain of $t$, since $k \le n \lt n + 1$. If $t$ is an $(n+1)$-step solution, its restriction is an $n$-step solution: it takes the value $c$ at $1$, and if $k + 1 \le n$ then also $k + 1 \le n + 1$, so $t(k+1) = g_k(t(k))$.

*Step 1: for every $n \in \mathbb{N}$ there is exactly one $n$-step solution.* By induction on $n$. For $n = 1$, the domain is $\{1\}$. The condition on $k$ is never in force, since $k + 1 \ge 2 \gt 1$ for $k \in \mathbb{N}$. So the $1$-step solutions are the functions with $t(1) = c$, and there is exactly one.

Assume there is exactly one $n$-step solution $t$. Define $u$ on $\{1, \dots, n+1\}$ by $u(k) = t(k)$ for $k \le n$ and $u(n+1) = g_n(t(n))$. By Section 3.3, $\{1, \dots, n+1\}$ consists of $\{1, \dots, n\}$ and $n + 1$, and $n + 1 \notin \{1, \dots, n\}$ since $n \lt n + 1$, so this assigns exactly one value to each element. Then $u(1) = t(1) = c$. Let $k \in \mathbb{N}$ with $k + 1 \le n + 1$, so $k \le n$. If $k + 1 \le n$, then $u(k+1) = t(k+1) = g_k(t(k)) = g_k(u(k))$. Otherwise $k + 1 = n + 1$ by Lemma 4(b), so $k = n$ and $u(n+1) = g_n(t(n)) = g_n(u(n))$. So $u$ is an $(n+1)$-step solution. If $v$ is another, its restriction to $\{1, \dots, n\}$ is an $n$-step solution (by the remark before Step 1), so it equals $t$; and $v(n+1) = g_n(v(n)) = g_n(t(n)) = u(n+1)$. So $v = u$.

*Step 2: existence.* Let $t_n$ be the $n$-step solution and set $s_n = t_n(n)$. Then $s_1 = t_1(1) = c$. The restriction of $t_{n+1}$ to $\{1, \dots, n\}$ is an $n$-step solution (by the remark before Step 1), so it is $t_n$ by Step 1. Hence

$$
s_{n+1} = t_{n+1}(n+1) = g_n(t_{n+1}(n)) = g_n(t_n(n)) = g_n(s_n).
$$

*Step 3: uniqueness.* If $(s_n)$ and $(s'_n)$ both satisfy the two conditions, let $S$ be the set of $n$ with $s_n = s'_n$. Then $1 \in S$ since both equal $c$, and if $n \in S$ then $s_{n+1} = g_n(s_n) = g_n(s'_n) = s'_{n+1}$. By induction $S = \mathbb{N}$. ∎

The theorem, and the idea of defining the natural numbers as the smallest set that contains $1$ and is closed under a successor step, are due to R. Dedekind, *Was sind und was sollen die Zahlen?* (Braunschweig, 1888); the theorem is his §126.

The same holds for a sequence indexed from 0, with $s_0 = c$ and $s_{n+1} = g_n(s_n)$ for every $n \ge 0$. For existence, let $(r_n)$ be the sequence with $r_1 = g_0(c)$ and $r_{n+1} = g_n(r_n)$ for $n \in \mathbb{N}$, and put $s_0 = c$ and $s_n = r_n$ for $n \in \mathbb{N}$. Then $s_1 = g_0(s_0)$, and $s_{n+1} = g_n(s_n)$ for $n \in \mathbb{N}$. Uniqueness is Step 3 with induction from 0.

**Choosing the least.** Sometimes the next value is the least natural number with a property that depends on the previous value. Precisely: let $X$ be a set with $\mathbb{N} \subseteq X$, and suppose that for each $n \in \mathbb{N}$ and each $x \in X$ the set $A_n(x)$ of natural numbers with the property is nonempty. By well-ordering (Section 3.4), $A_n(x)$ has exactly one least element; put $g_n(x)$ equal to it. Since $g_n(x) \in \mathbb{N} \subseteq X$, this defines a function $g_n : X \to X$, and the theorem applies.

## 3.6 Finite sums and products

**Definition.** Let $(a_k)$ be a sequence of numbers. The **sums** $\sum_{k=1}^{n} a_k$, for $n \in \mathbb{N}$, are the sequence given by recursion (Section 3.5) with $c = a_1$ and $g_n(x) = x + a_{n+1}$:

$$
\sum_{k=1}^{1} a_k = a_1, \qquad \sum_{k=1}^{n+1} a_k = \sum_{k=1}^{n} a_k + a_{n+1}.
$$

The **products** $\prod_{k=1}^{n} a_k$ are given in the same way with $g_n(x) = x \cdot a_{n+1}$. The **empty sum** $\sum_{k=1}^{0} a_k$ is $0$, and the **empty product** $\prod_{k=1}^{0} a_k$ is $1$. With these conventions, for every $n \ge 0$,

$$
\sum_{k=1}^{n+1} a_k = \sum_{k=1}^{n} a_k + a_{n+1}, \qquad \prod_{k=1}^{n+1} a_k = \Bigl(\prod_{k=1}^{n} a_k\Bigr) \cdot a_{n+1}. \tag{R}
$$

For $n = 0$ it reads $a_1 = 0 + a_1$ and $a_1 = 1 \cdot a_1$, which hold by the rules of Section 3.1; for $n \in \mathbb{N}$ it is the definition.

The letter $k$ is a dummy: $\sum_{k=1}^{n} a_k$ and $\sum_{j=1}^{n} a_j$ are the same number. When the terms are given by an expression, as in $\sum_{k=1}^{n} k$ or $\sum_{k=1}^{n} (a_{k+1} - a_k)$, the sum is that of the sequence whose $k$-th term is the expression. The expression need not contain $k$: $\prod_{k=1}^{n} x$ is the product of the constant sequence $k \mapsto x$. In this notation the example of Section 3.2 states $\sum_{k=1}^{n} k = n(n+1)/2$, and the first equality in its inductive step is (R).

**Finitely many terms.** If only $a_1, \dots, a_n$ are given, extend them to a sequence by putting $a_k = 0$ for $k \gt n$. The sums up to $n$ do not depend on the extension. Precisely: if $a_k = b_k$ for every $k \in \{1, \dots, n\}$, then $\sum_{k=1}^{m} a_k = \sum_{k=1}^{m} b_k$ for every $m \ge 0$ with $m \le n$. By induction on $m$ from 0: for $m = 0$ both sides are $0$; and if $m + 1 \le n$, then $m \le n$, so by (R) and the induction hypothesis $\sum_{k=1}^{m+1} a_k = \sum_{k=1}^{m} b_k + a_{m+1} = \sum_{k=1}^{m+1} b_k$, because $a_{m+1} = b_{m+1}$. The same argument applies to products.

**Other lower limits.** For a sequence $(a_k)$ indexed from 0 and $n \ge 0$, put $\sum_{k=0}^{n} a_k = a_0 + \sum_{k=1}^{n} a_k$ and $\prod_{k=0}^{n} a_k = a_0 \cdot \prod_{k=1}^{n} a_k$. If only $a_0, \dots, a_n$ are given, extend them by $a_k = 0$ for $k \gt n$. Since $\sum_{k=0}^{m} a_k = a_0 + \sum_{k=1}^{m} a_k$, the sums from 0 up to any $m \le n$ again do not depend on the extension. By (R) and the associative laws,

$$
\sum_{k=0}^{n+1} a_k = \sum_{k=0}^{n} a_k + a_{n+1}, \qquad \prod_{k=0}^{n+1} a_k = \Bigl(\prod_{k=0}^{n} a_k\Bigr) \cdot a_{n+1}. \tag{R0}
$$

For $m, n \ge 0$ put $\sum_{k=m+1}^{m+n} a_k = \sum_{j=1}^{n} a_{m+j}$ and $\prod_{k=m+1}^{m+n} a_k = \prod_{j=1}^{n} a_{m+j}$. The indices $m + j$ are natural numbers: they equal $j$ when $m = 0$, and lie in $\mathbb{N}$ by Lemma 3 otherwise.

**Definition.** For a number $x$ and $n \ge 0$, the **power** $x^n$ is $\prod_{k=1}^{n} x$, the product of $n$ factors all equal to $x$. The **factorial** $n!$ is $\prod_{k=1}^{n} k$.

So $x^0 = 1$ for every $x$, including $x = 0$, and $0! = 1$. By (R), $x^{n+1} = x^n \cdot x$ and $(n+1)! = n! \cdot (n+1)$ for every $n \ge 0$. In particular $x^1 = x$, $x^2 = x \cdot x$, $1! = 1$, $2! = 2$, $3! = 6$ and $4! = 24$.

**Theorem (rules for finite sums).** Let $(a_k)$ and $(b_k)$ be sequences of numbers, $c$ a number, $c_{jk}$ a number for each pair $j, k \in \mathbb{N}$, and $m, n \ge 0$.
- (S1) $\sum_{k=1}^{n} (a_k + b_k) = \sum_{k=1}^{n} a_k + \sum_{k=1}^{n} b_k$.
- (S2) $\sum_{k=1}^{n} c\, a_k = c \sum_{k=1}^{n} a_k$. In particular, with $c = 0$, a sum of zeros is $0$.
- (S3) If $a_k \le b_k$ for every $k \in \mathbb{N}$ with $k \le n$, then $\sum_{k=1}^{n} a_k \le \sum_{k=1}^{n} b_k$.
- (S4) (splitting) $\sum_{k=1}^{m+n} a_k = \sum_{k=1}^{m} a_k + \sum_{k=m+1}^{m+n} a_k$.
- (S5) (telescoping) $\sum_{k=1}^{n} (a_{k+1} - a_k) = a_{n+1} - a_1$.
- (S6) (shift) $\sum_{k=0}^{n} a_{k+1} = \sum_{k=1}^{n+1} a_k$.
- (S7) (double sums) $\sum_{j=1}^{m} \sum_{k=1}^{n} c_{jk} = \sum_{k=1}^{n} \sum_{j=1}^{m} c_{jk}$, and $\Bigl(\sum_{j=1}^{m} a_j\Bigr)\Bigl(\sum_{k=1}^{n} b_k\Bigr) = \sum_{j=1}^{m} \sum_{k=1}^{n} a_j b_k$.

*Proof.* Each, except the second statement of (S7), is proved by induction on $n$ from 0, with $m$ fixed. In each base case the sums over $k$ from $1$ to $0$ are $0$. Each inductive step applies (R) to the sum up to $n + 1$, then the induction hypothesis.

(S1) For $n = 0$: $0 = 0 + 0$. Step: by (R), the induction hypothesis, and the commutative and associative laws of addition,

$$
\sum_{k=1}^{n+1} (a_k + b_k) = \sum_{k=1}^{n} a_k + \sum_{k=1}^{n} b_k + a_{n+1} + b_{n+1} = \Bigl(\sum_{k=1}^{n} a_k + a_{n+1}\Bigr) + \Bigl(\sum_{k=1}^{n} b_k + b_{n+1}\Bigr) = \sum_{k=1}^{n+1} a_k + \sum_{k=1}^{n+1} b_k.
$$

(S2) For $n = 0$: $0 = c \cdot 0$. Step: $\sum_{k=1}^{n+1} c\, a_k = c \sum_{k=1}^{n} a_k + c\, a_{n+1} = c \bigl(\sum_{k=1}^{n} a_k + a_{n+1}\bigr) = c \sum_{k=1}^{n+1} a_k$, by the distributive law.

(S3) For $n = 0$: $0 \le 0$. Step: suppose $a_k \le b_k$ for every $k \le n + 1$. Then in particular $a_k \le b_k$ for every $k \le n$, so $\sum_{k=1}^{n} a_k \le \sum_{k=1}^{n} b_k$ by the induction hypothesis. Adding this to $a_{n+1} \le b_{n+1}$ gives $\sum_{k=1}^{n+1} a_k \le \sum_{k=1}^{n+1} b_k$.

(S4) For $n = 0$: the right side is $\sum_{k=1}^{m} a_k + 0$. Step: $m + n \ge 0$, so (R) applies at $m + n$, and also to the sequence $j \mapsto a_{m+j}$:

$$
\sum_{k=1}^{m+n+1} a_k = \sum_{k=1}^{m+n} a_k + a_{m+n+1} = \sum_{k=1}^{m} a_k + \sum_{j=1}^{n} a_{m+j} + a_{m+(n+1)} = \sum_{k=1}^{m} a_k + \sum_{j=1}^{n+1} a_{m+j}.
$$

(S5) For $n = 0$: $0 = a_1 - a_1$. Step: $\sum_{k=1}^{n+1} (a_{k+1} - a_k) = (a_{n+1} - a_1) + (a_{n+2} - a_{n+1}) = a_{n+2} - a_1$.

(S6) For $n = 0$: the left side is $a_1 + \sum_{k=1}^{0} a_{k+1} = a_1$, and the right side is $\sum_{k=1}^{1} a_k = a_1$. Step: by (R0) for the sequence $k \mapsto a_{k+1}$, the induction hypothesis, and (R),

$$
\sum_{k=0}^{n+1} a_{k+1} = \sum_{k=0}^{n} a_{k+1} + a_{n+2} = \sum_{k=1}^{n+1} a_k + a_{n+2} = \sum_{k=1}^{n+2} a_k.
$$

(S7) For $n = 0$: the left side is $\sum_{j=1}^{m} 0 = 0$ by (S2), and the right side is $0$. Step: by (R) inside, (S1), the induction hypothesis, and (R) for the sequence $k \mapsto \sum_{j=1}^{m} c_{jk}$,

$$
\sum_{j=1}^{m} \sum_{k=1}^{n+1} c_{jk} = \sum_{j=1}^{m} \Bigl(\sum_{k=1}^{n} c_{jk} + c_{j,n+1}\Bigr) = \sum_{j=1}^{m} \sum_{k=1}^{n} c_{jk} + \sum_{j=1}^{m} c_{j,n+1} = \sum_{k=1}^{n} \sum_{j=1}^{m} c_{jk} + \sum_{j=1}^{m} c_{j,n+1} = \sum_{k=1}^{n+1} \sum_{j=1}^{m} c_{jk}.
$$

For the product, write $B = \sum_{k=1}^{n} b_k$. By (S2) with $c = B$, and $B a_j = a_j B$, we get $\bigl(\sum_{j=1}^{m} a_j\bigr) B = \sum_{j=1}^{m} a_j B$. By (S2) with $c = a_j$, $a_j B = \sum_{k=1}^{n} a_j b_k$ for each $j$. Substituting gives the claim. ∎

(S1), (S2) and (S3) hold also for sums from 0: add the term with $k = 0$ to both sides. For (S2), $\sum_{k=0}^{n} c\, a_k = c\, a_0 + c \sum_{k=1}^{n} a_k = c \sum_{k=0}^{n} a_k$; for (S3), add $a_0 \le b_0$ to the inequality from 1.

**Corollary (sums of constants).** For every number $c$ and every $n \ge 0$, $\sum_{k=1}^{n} 1 = n$ and $\sum_{k=1}^{n} c = nc$.

*Proof.* By induction on $n$ from 0: the empty sum is $0$, and if $\sum_{k=1}^{n} 1 = n$ then $\sum_{k=1}^{n+1} 1 = n + 1$ by (R). By (S2) with every $a_k = 1$, $\sum_{k=1}^{n} c = \sum_{k=1}^{n} c \cdot 1 = c \sum_{k=1}^{n} 1 = cn = nc$. ∎

**Theorem (rules for finite products).** Let $(a_k)$ and $(b_k)$ be sequences of numbers and $m, n \ge 0$.
- (P1) $\prod_{k=1}^{n} (a_k b_k) = \prod_{k=1}^{n} a_k \cdot \prod_{k=1}^{n} b_k$.
- (P2) $\prod_{k=1}^{m+n} a_k = \prod_{k=1}^{m} a_k \cdot \prod_{k=m+1}^{m+n} a_k$.
- (P3) If $0 \le a_k \le b_k$ for every $k \in \mathbb{N}$ with $k \le n$, then $0 \le \prod_{k=1}^{n} a_k \le \prod_{k=1}^{n} b_k$. If $a_k \gt 0$ for every $k \in \mathbb{N}$ with $k \le n$, then $\prod_{k=1}^{n} a_k \gt 0$.

*Proof.* By induction on $n$ from 0, with $m$ fixed. The empty products are $1$.

(P1) For $n = 0$: $1 = 1 \cdot 1$. Step: by (R), the induction hypothesis, and the commutative and associative laws of multiplication, $\prod_{k=1}^{n+1} (a_k b_k) = \prod_{k=1}^{n} a_k \cdot \prod_{k=1}^{n} b_k \cdot a_{n+1} b_{n+1} = \bigl(\prod_{k=1}^{n} a_k \cdot a_{n+1}\bigr) \bigl(\prod_{k=1}^{n} b_k \cdot b_{n+1}\bigr)$, which is the right side for $n + 1$.

(P2) For $n = 0$: the right side is $\prod_{k=1}^{m} a_k \cdot 1$. Step:

$$
\prod_{k=1}^{m+n+1} a_k = \prod_{k=1}^{m+n} a_k \cdot a_{m+n+1} = \prod_{k=1}^{m} a_k \cdot \prod_{j=1}^{n} a_{m+j} \cdot a_{m+(n+1)} = \prod_{k=1}^{m} a_k \cdot \prod_{j=1}^{n+1} a_{m+j}.
$$

(P3) For $n = 0$: $0 \le 1 \le 1$ and $1 \gt 0$. Step: write $A = \prod_{k=1}^{n} a_k$ and $B = \prod_{k=1}^{n} b_k$. The hypothesis for $n + 1$ contains the hypothesis for $n$, so $0 \le A \le B$ by the induction hypothesis. Multiplying $0 \le A$ by $a_{n+1} \ge 0$ gives $0 \le A a_{n+1}$. Multiplying $a_{n+1} \le b_{n+1}$ by $A \ge 0$ gives $A a_{n+1} \le A b_{n+1}$, and multiplying $A \le B$ by $b_{n+1} \ge 0$ (since $0 \le a_{n+1} \le b_{n+1}$) gives $A b_{n+1} \le B b_{n+1}$. So $0 \le A a_{n+1} \le B b_{n+1}$, which is the claim for $n + 1$ by (R). For the second part, the hypothesis for $n + 1$ again contains that for $n$, so $A \gt 0$, and $a_{n+1} \gt 0$; multiplying $0 \lt A$ by $a_{n+1}$ gives $0 \lt A a_{n+1}$. ∎

**Corollary (laws of powers).** Let $x$, $y$ be numbers and $m, n \ge 0$.
- (a) $x^{m+n} = x^m x^n$.
- (b) $(xy)^n = x^n y^n$.
- (c) $(x^m)^n = x^{mn}$.
- (d) If $x \ge 0$ then $x^n \ge 0$, and if $x \gt 0$ then $x^n \gt 0$.
- (e) If $0 \le x \lt y$ and $n \in \mathbb{N}$, then $x^n \lt y^n$.
- (f) $1^n = 1$.

Also $n! \gt 0$ for every $n \ge 0$.

*Proof.* (a) is (P2) with every $a_k = x$, since then $\prod_{k=m+1}^{m+n} x = \prod_{j=1}^{n} x = x^n$. (b) is (P1) with $a_k = x$ and $b_k = y$. (d) is (P3) with $a_k = b_k = x$.

(c) By induction on $n$ from 0. For $n = 0$: $(x^m)^0 = 1 = x^0 = x^{m \cdot 0}$. Step: $mn$ is $0$ if $m = 0$ or $n = 0$, and lies in $\mathbb{N}$ otherwise by Lemma 3, so (a) applies, and $(x^m)^{n+1} = (x^m)^n \, x^m = x^{mn} x^m = x^{mn + m} = x^{m(n+1)}$.

(e) By induction on $n$. For $n = 1$: $x^1 = x \lt y = y^1$. Step: assume $x^n \lt y^n$. By (d), $x^n \ge 0$, and $y \gt 0$ because $y \gt x \ge 0$. Multiplying $x \le y$ by $x^n \ge 0$ gives $x^n x \le x^n y$, and multiplying $x^n \lt y^n$ by $y \gt 0$ gives $x^n y \lt y^n y$. So $x^{n+1} = x^n x \lt y^n y = y^{n+1}$ by (R).

(f) By induction on $n$ from 0: $1^0 = 1$, and if $1^n = 1$ then $1^{n+1} = 1^n \cdot 1 = 1$ by (R).

Finally, $n! = \prod_{k=1}^{n} k$ and every $k \in \mathbb{N}$ satisfies $k \ge 1 \gt 0$ by Lemma 1, so $n! \gt 0$ by (P3). ∎

## 3.7 The geometric sum

**Theorem (geometric sum).** Let $x \ne 1$ and $n \ge 0$. Then

$$
\sum_{k=0}^{n} x^k = \frac{1 - x^{n+1}}{1 - x}.
$$

*Proof.* By induction on $n$ from 0. Since $x \ne 1$, also $1 - x \ne 0$, for $1 - x = 0$ would give $1 = x$ (Section 3.1). For $n = 0$: the left side is $x^0 = 1$, and the right side is $(1 - x)/(1 - x) = 1$. Step: write

$$
x^{n+1} = \frac{x^{n+1}(1 - x)}{1 - x} = \frac{x^{n+1} - x^{n+2}}{1 - x},
$$

by the distributive law and $x^{n+1} \cdot x = x^{n+2}$. By (R0), the induction hypothesis, and the addition of fractions with the same denominator (Section 3.2),

$$
\sum_{k=0}^{n+1} x^k = \frac{1 - x^{n+1}}{1 - x} + \frac{x^{n+1} - x^{n+2}}{1 - x} = \frac{1 - x^{n+1} + x^{n+1} - x^{n+2}}{1 - x} = \frac{1 - x^{n+2}}{1 - x}.
$$

∎

For example, take $x = 1/2$ and $n = 3$. Here $(1/2)^k = 1/2^k$: by the laws of powers (b) and (f), $(1/2)^k \, 2^k = \bigl((1/2) \cdot 2\bigr)^k = 1^k = 1$, and $2^k \gt 0$ by (d), so multiplying by $1/2^k$ gives the claim. Also $1/(1/2) = 2$ by Section 3.1. The left side is $1 + 1/2 + 1/4 + 1/8 = 15/8$, and the right side is $(1 - 1/16)/(1/2) = (15/16) \cdot 2 = 15/8$.

Telescoping (S5) gives a factorisation that later sessions use.

**Corollary (difference of powers).** For all numbers $u$, $v$ and every $n \in \mathbb{N}$,

$$
u^n - v^n = (u - v) \sum_{j=0}^{n-1} u^{n-1-j} v^j .
$$

*Proof.* Since $n \in \mathbb{N}$, $n - 1 \ge 0$: it is $0$ if $n = 1$, and in $\mathbb{N}$ otherwise by Lemma 2. For $0 \le j \le n$ the exponent $n - j$ is $0$ or lies in $\mathbb{N}$ (Lemma 4(a)), so $c_j = u^{n-j} v^j$ is defined. Let $0 \le j \le n - 1$. Then $j + 1 \le n$, so $n - 1 - j = n - (j+1)$ is also $0$ or in $\mathbb{N}$, and $1 + (n - 1 - j) = n - j$. By the laws of powers (a), with $u^1 = u^0 u = u$ by (R), $u \cdot u^{n-1-j} v^j = u^{n-j} v^j = c_j$, and likewise with $v^1 = v$, $v \cdot u^{n-1-j} v^j = u^{n-(j+1)} v^{j+1} = c_{j+1}$. So (S2) for sums from 0, with $c = u$ and with $c = -v$, then (S1) for sums from 0, give

$$
(u - v) \sum_{j=0}^{n-1} u^{n-1-j} v^j = \sum_{j=0}^{n-1} c_j + \sum_{j=0}^{n-1} (-c_{j+1}) = \sum_{j=0}^{n-1} \bigl( c_{j} - c_{j+1} \bigr).
$$

Put $a_i = c_{i-1}$ for $1 \le i \le n + 1$, so that $c_j - c_{j+1} = a_{j+1} - a_{j+2}$. By (S6), then (S2) with the constant $-1$, then (S5),

$$
\sum_{j=0}^{n-1} \bigl( c_{j} - c_{j+1} \bigr) = \sum_{i=1}^{n} \bigl( a_i - a_{i+1} \bigr) = -\sum_{i=1}^{n} \bigl( a_{i+1} - a_i \bigr) = -(a_{n+1} - a_1) = c_0 - c_n = u^n - v^n .
$$

∎

For $n = 2$ it reads $u^2 - v^2 = (u - v)(u + v)$. For $n = 3$, $u = 2$ and $v = 1$: the left side is $8 - 1 = 7$, and the right side is $(2 - 1)(4 + 2 + 1) = 7$.

## 3.8 The binomial theorem

**Definition.** Let $n \ge 0$, and let $k$ satisfy $k \ge 0$ and $k \le n$. The **binomial coefficient** is

$$
\binom{n}{k} = \frac{n!}{k!\,(n-k)!}.
$$

The definition makes sense. First, $n - k \ge 0$: it is $0$ if $k = n$, it is $n$ if $k = 0$, and otherwise $k \in \mathbb{N}$ and $k \lt n$, so $n \gt k \ge 1$, $n \ne 0$ and $n \in \mathbb{N}$, and $n - k \in \mathbb{N}$ by Lemma 4(a). Second, the denominator is a product of two numbers $\gt 0$ (factorials are $\gt 0$, by the laws of powers in Section 3.6), so it is $\gt 0$ and in particular nonzero. For the same reason $\binom{n}{k} \gt 0$.

From the definition, $\binom{n}{0} = \frac{n!}{0!\,n!} = 1$ and $\binom{n}{n} = \frac{n!}{n!\,0!} = 1$. For $n \in \mathbb{N}$, $n - 1 \ge 0$ (Section 3.7). So $n! = (n-1)! \cdot n$ by (R), and $\binom{n}{1} = \frac{(n-1)! \cdot n}{1 \cdot (n-1)!} = n$.

**Lemma 5 (Pascal's rule).** Let $n \ge 0$ and $k \in \mathbb{N}$ with $k \le n$. Then

$$
\binom{n}{k-1} + \binom{n}{k} = \binom{n+1}{k}.
$$

*Proof.* Here $k - 1 \ge 0$ (it is $0$ if $k = 1$, and in $\mathbb{N}$ otherwise by Lemma 2) and $k - 1 \lt k \le n \lt n + 1$, so both sides are defined; and $n - k \ge 0$ as above. By (R), $k! = (k-1)! \cdot k$ and $(n - k + 1)! = (n-k)! \cdot (n - k + 1)$. Also $n - (k - 1) = n - k + 1$, and $n - k + 1 \ge 1$. A fraction is unchanged when its numerator and denominator are multiplied by the same nonzero number (Section 3.1). Multiplying by $k$ in the first fraction and by $n - k + 1$ in the second,

$$
\binom{n}{k-1} = \frac{n!}{(k-1)!\,(n-k+1)!} = \frac{n! \cdot k}{k!\,(n-k+1)!}, \qquad \binom{n}{k} = \frac{n!}{k!\,(n-k)!} = \frac{n! \cdot (n-k+1)}{k!\,(n-k+1)!}.
$$

The two fractions have the same denominator, so by Section 3.2 their sum is

$$
\frac{n! \cdot \bigl(k + (n - k + 1)\bigr)}{k!\,(n-k+1)!} = \frac{n! \cdot (n+1)}{k!\,(n+1-k)!} = \frac{(n+1)!}{k!\,\bigl((n+1)-k\bigr)!} = \binom{n+1}{k}.
$$

∎

The coefficients arranged in rows $n = 0, 1, 2, \dots$ form **Pascal's triangle**, in which by Lemma 5 each inner entry is the sum of the two entries above it. Pascal's rule is named after B. Pascal, *Traité du triangle arithmétique* (Paris, 1665).

**Theorem (binomial theorem).** For all numbers $a$, $b$ and every $n \ge 0$,

$$
(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k.
$$

*Proof.* By induction on $n$ from 0. The terms of the sum are defined for $0 \le k \le n$, which is all the sum uses (Section 3.6, other lower limits).

Base case. The left side is $(a+b)^0 = 1$. The right side is $\binom{0}{0} a^0 b^0 = 1$.

Inductive step. Assume the formula for $n$, and write $t_k = \binom{n}{k} a^{n-k} b^k$ for $0 \le k \le n$. By (R), the induction hypothesis, the distributive law and (S2) for sums from 0,

$$
(a+b)^{n+1} = (a+b)^n (a + b) = a \sum_{k=0}^{n} t_k + b \sum_{k=0}^{n} t_k = \sum_{k=0}^{n} a\, t_k + \sum_{k=0}^{n} b\, t_k.
$$

*The first sum.* Since $a^{n-k} \cdot a = a^{n-k+1}$ by (R), $a\, t_k = \binom{n}{k} a^{n+1-k} b^k$. The term with $k = 0$ is $1 \cdot a^{n+1} \cdot 1 = a^{n+1}$. By the definition of a sum from 0,

$$
\sum_{k=0}^{n} a\, t_k = a^{n+1} + \sum_{k=1}^{n} \binom{n}{k} a^{n+1-k} b^k.
$$

*The second sum.* For $1 \le k \le n + 1$ put $u_k = \binom{n}{k-1} a^{n+1-k} b^k$. For $0 \le k \le n$, $u_{k+1} = \binom{n}{k} a^{n-k} b^{k+1} = b\, t_k$, using $b^k \cdot b = b^{k+1}$. By (S6), then (R),

$$
\sum_{k=0}^{n} b\, t_k = \sum_{k=0}^{n} u_{k+1} = \sum_{k=1}^{n+1} u_k = \sum_{k=1}^{n} \binom{n}{k-1} a^{n+1-k} b^k + b^{n+1},
$$

since $u_{n+1} = \binom{n}{n} a^0 b^{n+1} = b^{n+1}$.

*Adding.* By (S1), the distributive law, and Lemma 5 for each $k \in \{1, \dots, n\}$,

$$
(a+b)^{n+1} = a^{n+1} + \sum_{k=1}^{n} \Bigl(\binom{n}{k} + \binom{n}{k-1}\Bigr) a^{n+1-k} b^k + b^{n+1} = a^{n+1} + \sum_{k=1}^{n} \binom{n+1}{k} a^{n+1-k} b^k + b^{n+1}.
$$

By the definition of a sum from 0 and (R), the right side of the formula for $n + 1$ is

$$
\sum_{k=0}^{n+1} \binom{n+1}{k} a^{n+1-k} b^k = \binom{n+1}{0} a^{n+1} + \sum_{k=1}^{n} \binom{n+1}{k} a^{n+1-k} b^k + \binom{n+1}{n+1} b^{n+1},
$$

which is the same number, since $\binom{n+1}{0} = \binom{n+1}{n+1} = 1$. For $n = 0$ the sums from $1$ to $n$ are empty, and every line above still holds. ∎

## 3.9 Bernoulli's inequality

**Theorem (Bernoulli's inequality).** Let $x \ge -1$. Then for every $n \ge 0$,

$$
(1 + x)^n \ge 1 + nx.
$$

*Proof.* By induction on $n$ from 0.

Base case. $(1+x)^0 = 1 = 1 + 0 \cdot x$.

Inductive step. Assume $(1 + x)^n \ge 1 + nx$. Adding $1$ to $x \ge -1$ gives $1 + x \ge 0$. Multiplying the induction hypothesis by $1 + x \ge 0$, and using (R),

$$
(1+x)^{n+1} = (1+x)^n (1+x) \ge (1 + nx)(1 + x) = 1 + x + nx + nx^2 = 1 + (n+1)x + nx^2.
$$

Now $x^2 \ge 0$, and $n \ge 0$ as a number (Section 3.3), so $nx^2 \ge 0$. Adding $1 + (n+1)x$ to both sides of $nx^2 \ge 0$ gives $1 + (n+1)x + nx^2 \ge 1 + (n+1)x$. Hence $(1+x)^{n+1} \ge 1 + (n+1)x$. ∎

The inequality is named after Jacob Bernoulli, who published it in *Positiones arithmeticae de seriebus infinitis* (Basel, 1689).

**Why induction and not the binomial theorem.** For $x \ge 0$ and $n \in \mathbb{N}$ the binomial theorem gives a second proof. With $a = 1$ and $b = x$, and $1^m = 1$ (laws of powers (f)), it gives $(1+x)^n = \sum_{k=0}^{n} t_k = 1 + \sum_{k=1}^{n} t_k$, where $t_k = \binom{n}{k} x^k$. Here $n - 1 \ge 0$ (Section 3.7), and $1 + (n - 1) = n$. By (S4) with $m = 1$ and $n - 1$ in place of $n$, $\sum_{k=1}^{n} t_k = t_1 + \sum_{j=1}^{n-1} t_{1+j}$, and $t_1 = nx$. Each $t_{1+j}$ is a product of $\binom{n}{1+j} \gt 0$ and $x^{1+j} \ge 0$ (laws of powers (d)), so it is $\ge 0$, and $\sum_{j=1}^{n-1} t_{1+j} \ge \sum_{j=1}^{n-1} 0 = 0$ by (S3) and (S2). This proves $(1+x)^n \ge 1 + nx$ for $x \ge 0$. For $-1 \le x \lt 0$ and $n \ge 3$ the term with $k = 3$ is $\lt 0$, since $\binom{n}{3} \gt 0$ and $x^3 = x^2 \cdot x$ with $x^2 \gt 0$ and $x \lt 0$, and this argument says nothing. The induction proof uses only $1 + x \ge 0$, and so covers the whole range.

**What fails without $x \ge -1$.** The inductive step multiplied an inequality by $1 + x$, which needs $1 + x \ge 0$. Without that hypothesis the conclusion can fail. Take $n = 3$ and $x = -4$. Then $(1 + x)^3 = (-3)^3 = 9 \cdot (-3) = -27$, while $1 + 3x = -11$, and $-27 \lt -11$.

## 3.10 Worked example

This example computes the binomial theorem for $n = 3$ and $n = 4$, and finds for those $n$ exactly which $x$ satisfy Bernoulli's inequality.

*Pascal's triangle up to $n = 4$.* Row $0$ is $\binom{0}{0} = 1$. Each row begins and ends with $1$, and by Lemma 5 each inner entry is the sum of the entries above it to the left and directly above:

| $n$ | $k=0$ | $k=1$ | $k=2$ | $k=3$ | $k=4$ |
|---|---|---|---|---|---|
| 0 | 1 | | | | |
| 1 | 1 | 1 | | | |
| 2 | 1 | 1 + 1 = 2 | 1 | | |
| 3 | 1 | 1 + 2 = 3 | 2 + 1 = 3 | 1 | |
| 4 | 1 | 1 + 3 = 4 | 3 + 3 = 6 | 3 + 1 = 4 | 1 |

As a check against the definition, $\binom{4}{2} = \frac{4!}{2!\,2!} = \frac{24}{2 \cdot 2} = 6$.

*The expansions.* With $a = 1$ and $b = x$, and $1^m = 1$, the binomial theorem gives

$$
(1+x)^3 = 1 + 3x + 3x^2 + x^3, \qquad (1+x)^4 = 1 + 4x + 6x^2 + 4x^3 + x^4.
$$

*Bernoulli for $n = 3$.* Subtracting $1 + 3x$,

$$
(1+x)^3 - (1 + 3x) = 3x^2 + x^3 = x^2 (x + 3).
$$

If $x = 0$ the difference is $0$. If $x \ne 0$ then $x^2 \gt 0$. Multiplying $x + 3 \ge 0$ by $x^2$ gives a difference $\ge 0$, and multiplying $x + 3 \lt 0$ by $x^2$ gives a difference $\lt 0$. Hence $(1+x)^3 \ge 1 + 3x$ holds exactly for $x \ge -3$. This contains the range $x \ge -1$ of the theorem, and it fails for every $x \lt -3$, as at $x = -4$ in Section 3.9, where the difference is $16 \cdot (-1) = -16 = -27 - (-11)$.

*Bernoulli for $n = 4$.* Subtracting $1 + 4x$,

$$
(1+x)^4 - (1 + 4x) = 6x^2 + 4x^3 + x^4 = x^2 (x^2 + 4x + 6) = x^2 \bigl((x + 2)^2 + 2\bigr),
$$

using $(x+2)^2 = x^2 + 4x + 4$ (the binomial theorem with $n = 2$). Since $x^2 \ge 0$, and $(x+2)^2 + 2 \ge 0 + 2 \gt 0$, the difference is a product of two numbers $\ge 0$, so it is $\ge 0$ for every number $x$.

So the hypothesis $x \ge -1$ is not the exact range for each $n$. It is a range that works for every $n$ at once, though not the largest one (Exercise 8(c)), and it is exactly what the inductive step uses.

*A number.* For $x = 1/10$ and $n = 4$, $(1/10)^k = 1/10^k$ as in Section 3.7, and the expansion gives, over the common denominator $10000$, $(10000 + 4000 + 600 + 40 + 1)/10000 = 14641/10000$, against $1 + 4x = 14000/10000$. Bernoulli's inequality keeps the first two terms and drops the rest, which here are all $\gt 0$.

## Exercises

*Check*

1. Use Pascal's rule and row 4 from Section 3.10 to compute row 5, $\binom{5}{k}$ for $0 \le k \le 5$. Write out $(a+b)^5$, and evaluate both sides at $a = b = 1$.
2. (a) Compute $\sum_{k=0}^{5} (1/2)^k$ from the geometric sum, and again by adding the six terms. (b) Show that $(1 + 1/n)^n \ge 2$ for every $n \in \mathbb{N}$.
3. Show that $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$ for $k \in \mathbb{N}$, and use telescoping (S5) to prove $\sum_{k=1}^{n} \frac{1}{k(k+1)} = \frac{n}{n+1}$ for every $n \in \mathbb{N}$. Check the case $n = 4$ by adding the four terms.
4. Prove that $\sum_{k=0}^{n} \binom{n}{k} = 2^n$ for every $n \ge 0$, and that $\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$ for every $n \in \mathbb{N}$. What is the second sum when $n = 0$?

*Prove*

5. Prove by induction that $\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$ for every $n \in \mathbb{N}$.
6. (Strict Bernoulli.) Let $x \ge -1$ with $x \ne 0$, and let $n \in \mathbb{N}$ with $n \ge 2$. Prove that $(1+x)^n \gt 1 + nx$.
7. Prove that $\binom{n}{k} \in \mathbb{N}$ for every $n \ge 0$ and every $k$ with $0 \le k \le n$. Use Pascal's rule, Lemma 3 and induction on $n$ from 0.

*Extend*

8. (Weierstrass product inequality.) Let $n \in \mathbb{N}$ and let $x_1, \dots, x_n$ be numbers with $0 \le x_k \le 1$ for every $k$.
   - (a) Prove that $\prod_{k=1}^{n} (1 - x_k) \ge 1 - \sum_{k=1}^{n} x_k$.
   - (b) Deduce Bernoulli's inequality for $-1 \le x \le 0$.
   - (c) Show that Bernoulli's inequality also holds for every $n \ge 0$ when $-2 \le x \lt -1$. (Hint: put $y = 1 + x$, so that $-1 \le y \lt 0$; show $-1 \le y^n \le 1$ for every $n \ge 0$ by induction from 0, and $1 + nx \le 1 - n$.)

Solutions: [solutions/003-induction-finite-sums.md](../solutions/003-induction-finite-sums.md).
