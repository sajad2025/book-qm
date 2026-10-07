# Solutions to Session 2. Sets, functions and the forms of proof

## Check

**1.** Compute $Q \Rightarrow R$ first, then $P \Rightarrow (Q \Rightarrow R)$ from the columns $P$ and $Q \Rightarrow R$; separately compute $P \wedge Q$, then $(P \wedge Q) \Rightarrow R$ from the columns $P \wedge Q$ and $R$. Each entry uses the table of Section 2.1 once.

| $P$ | $Q$ | $R$ | $Q \Rightarrow R$ | $P \Rightarrow (Q \Rightarrow R)$ | $P \wedge Q$ | $(P \wedge Q) \Rightarrow R$ |
|---|---|---|---|---|---|---|
| T | T | T | T | T | T | T |
| T | T | F | F | F | T | F |
| T | F | T | T | T | F | T |
| T | F | F | T | T | F | T |
| F | T | T | T | T | F | T |
| F | T | F | F | T | F | T |
| F | F | T | T | T | F | T |
| F | F | F | T | T | F | T |

For instance, in the sixth row $Q$ is T and $R$ is F, so $Q \Rightarrow R$ is F; but $P$ is F, so $P \Rightarrow (Q \Rightarrow R)$ is T. In the same row $P \wedge Q$ is F, so $(P \wedge Q) \Rightarrow R$ is T.

The fifth and seventh columns agree in all eight rows: both are F in the second row only. So the two statements are logically equivalent. This is why a proof of "if $P$ and $Q$, then $R$" may begin "assume $P$; assume $Q$".

**2.** By the definition of $\exists!$ (Section 2.4), with $P(a)$ the open statement "$f(a) = b$", the statement reads

$$
\forall b \in B,\ \Bigl[\bigl(\exists a \in A,\ f(a) = b\bigr) \wedge \bigl(\forall a \in A\ \forall a' \in A,\ (f(a) = b \wedge f(a') = b) \Rightarrow a = a'\bigr)\Bigr].
$$

Negate step by step.

$$
\begin{aligned}
&\neg\forall b \in B,\ [X(b) \wedge Y(b)] \\
&\equiv \exists b \in B,\ \neg[X(b) \wedge Y(b)] && \text{negation of } \forall \\
&\equiv \exists b \in B,\ [\neg X(b) \vee \neg Y(b)] && \text{De Morgan, Rule 2},
\end{aligned}
$$

where $X(b)$ is $\exists a \in A,\ f(a) = b$ and $Y(b)$ is the second bracket. Next,

$$
\neg X(b) \equiv \forall a \in A,\ f(a) \ne b
$$

by the negation of $\exists$, and

$$
\begin{aligned}
\neg Y(b)
&\equiv \exists a \in A,\ \neg\bigl(\forall a' \in A,\ (f(a) = b \wedge f(a') = b) \Rightarrow a = a'\bigr) \\
&\equiv \exists a \in A\ \exists a' \in A,\ \neg\bigl((f(a) = b \wedge f(a') = b) \Rightarrow a = a'\bigr) \\
&\equiv \exists a \in A\ \exists a' \in A,\ \bigl((f(a) = b \wedge f(a') = b) \wedge a \ne a'\bigr),
\end{aligned}
$$

using the negation of $\forall$ twice and then Rule 4, $\neg(P \Rightarrow Q) \equiv P \wedge \neg Q$, with $a \ne a'$ meaning $\neg(a = a')$. Putting the parts together, the negation is

$$
\exists b \in B,\ \Bigl[\bigl(\forall a \in A,\ f(a) \ne b\bigr) \vee \bigl(\exists a \in A\ \exists a' \in A,\ (f(a) = b \wedge f(a') = b) \wedge a \ne a'\bigr)\Bigr].
$$

In words: some element of $B$ is either the value of no element of $A$, or the value of two distinct elements of $A$.

**3.** The values are $f(1) = p$, $f(2) = p$, $f(3) = q$, $f(4) = q$.

- $f(\{1, 3\}) = \{f(1), f(3)\} = \{p, q\}$.
- $f^{-1}(\{p\}) = \{a \in \{1, 2, 3, 4\} : f(a) \in \{p\}\}$. Going through the four elements, $f(1) = p$ and $f(2) = p$ are in $\{p\}$, while $f(3) = q$ and $f(4) = q$ are not. So $f^{-1}(\{p\}) = \{1, 2\}$.
- $f^{-1}(\{r\})$: none of the four values is $r$, so $f^{-1}(\{r\}) = \emptyset$.
- $f^{-1}(\{p, r\})$: the elements with value $p$ or $r$ are 1 and 2, so it is $\{1, 2\}$. Then $f(\{1, 2\}) = \{f(1), f(2)\} = \{p\}$. So $f(f^{-1}(\{p, r\})) = \{p\}$, which is not $\{p, r\}$.
- $f(\{1\}) = \{p\}$, and $f^{-1}(\{p\}) = \{1, 2\}$ from above. So $f^{-1}(f(\{1\})) = \{1, 2\}$, which is not $\{1\}$.

$f$ is not injective: $f(1) = f(2)$ while $1 \ne 2$. $f$ is not surjective: $r$ is not a value, as the computation of $f^{-1}(\{r\})$ showed.

## Prove

**4.** *First inclusion.* Let $x \in A \cap (B \cup C)$. Then $x \in A$, and $x \in B$ or $x \in C$. Proceed by cases on the disjunction.
- Case $x \in B$. With $x \in A$ this gives $x \in A \cap B$, and so $x \in (A \cap B) \cup (A \cap C)$, by the definition of union.
- Case $x \in C$. With $x \in A$ this gives $x \in A \cap C$, and so $x \in (A \cap B) \cup (A \cap C)$.

By proof by cases (Section 2.5), $x \in (A \cap B) \cup (A \cap C)$. So $A \cap (B \cup C) \subseteq (A \cap B) \cup (A \cap C)$.

*Second inclusion.* Let $x \in (A \cap B) \cup (A \cap C)$. Then $x \in A \cap B$ or $x \in A \cap C$.
- Case $x \in A \cap B$. Then $x \in A$ and $x \in B$. From $x \in B$, $x \in B \cup C$. So $x \in A \cap (B \cup C)$.
- Case $x \in A \cap C$. Then $x \in A$ and $x \in C$. From $x \in C$, $x \in B \cup C$. So $x \in A \cap (B \cup C)$.

So $(A \cap B) \cup (A \cap C) \subseteq A \cap (B \cup C)$. By double inclusion the two sets are equal.

**5.** (a) Assume $f$ and $g$ are injective. Let $a, a' \in A$ with $(g \circ f)(a) = (g \circ f)(a')$, that is, $g(f(a)) = g(f(a'))$. Since $g$ is injective and $f(a), f(a')$ are elements of $B$ with equal values under $g$, $f(a) = f(a')$. Since $f$ is injective, $a = a'$. So $g \circ f$ is injective.

(b) The contrapositive is: if $f$ is not injective, then $g \circ f$ is not injective. Assume $f$ is not injective. By the negation in Section 2.8 there are $a, a' \in A$ with $f(a) = f(a')$ and $a \ne a'$. Applying $g$ to the equal elements $f(a)$ and $f(a')$ gives $g(f(a)) = g(f(a'))$, that is, $(g \circ f)(a) = (g \circ f)(a')$, with $a \ne a'$. By the same negation, $g \circ f$ is not injective. This proves the contrapositive, and so the statement.

(c) Assume $g \circ f$ is surjective. Let $c \in C$. There is $a \in A$ with $(g \circ f)(a) = c$, that is, $g(f(a)) = c$. Put $b = f(a)$, an element of $B$. Then $g(b) = c$. So every $c \in C$ is a value of $g$, and $g$ is surjective.

**6.** We prove "if $f$ is not surjective, then $g$ is not injective" by contradiction: assume $f$ is not surjective and $g$ is injective (by Rule 1 of Section 2.2, this is the negation of "$g$ is not injective"), and derive a statement together with its negation.

Since $f$ is not surjective, by the negation in Section 2.8 there is $b \in B$ with $f(a) \ne b$ for every $a \in A$. Put $a_0 = g(b)$, an element of $A$. Since $g \circ f = \mathrm{id}_A$,

$$
g(f(a_0)) = a_0 = g(b).
$$

So the elements $f(a_0)$ and $b$ of $B$ have the same value under $g$. Since $g$ is injective, $f(a_0) = b$. Call this statement $R$. But $f(a) \ne b$ for every $a \in A$, and in particular for $a = a_0$; this is $\neg R$. The assumptions have led to $R$ and $\neg R$, so they cannot both hold. Hence if $f$ is not surjective, $g$ is not injective.

## Extend

**7.** Let $f : A \to \mathcal{P}(A)$ be any function. Each $f(a)$ is a subset of $A$, so "$a \notin f(a)$" is an open statement on $A$, and

$$
D = \{a \in A : a \notin f(a)\}
$$

is a subset of $A$, that is, $D \in \mathcal{P}(A)$.

Suppose, for a contradiction, that $f$ is surjective. Then there is $d \in A$ with $f(d) = D$. Let $P$ be the statement "$d \in D$". By the definition of $D$, $d \in D$ holds exactly when $d \notin f(d)$, and since $f(d) = D$, this is exactly when $d \notin D$. So $P \Rightarrow \neg P$ and $\neg P \Rightarrow P$ are both true.

Now $P \vee \neg P$ is true (Section 2.5, proof by cases). Proceed by cases.
- Case $P$. From $P$ and $P \Rightarrow \neg P$, modus ponens gives $\neg P$. So $P$ and $\neg P$ both hold.
- Case $\neg P$. From $\neg P$ and $\neg P \Rightarrow P$, modus ponens gives $P$. So again $P$ and $\neg P$ both hold.

By proof by cases and modus ponens (Section 2.5), the assumption that $f$ is surjective has led to a statement and its negation. So $f$ is not surjective. Since $f$ was an arbitrary function from $A$ to $\mathcal{P}(A)$, no such function is surjective.

**8.** *Injective.* Let $n, n' \in \mathbb{N}$ with $t(n) = t(n')$, that is, $n + 1 = n' + 1$. Subtracting 1 from both sides gives $n = n'$.

*Not surjective.* For every $n \in \mathbb{N}$, $n \ge 1$, so $t(n) = n + 1 \ge 2 \gt 1$, and $t(n) \ne 1$. So $1 \in \mathbb{N}$ is not a value of $t$, which is the negation of surjectivity in Section 2.8.

*A left inverse.* Define $u : \mathbb{N} \to \mathbb{N}$ by $u(1) = 1$ and $u(m) = m - 1$ for $m \ge 2$. For $m \ge 2$, $m - 1 \ge 1$, so $m - 1 \in \mathbb{N}$ and $u$ is a function into $\mathbb{N}$. For every $n \in \mathbb{N}$, $t(n) = n + 1 \ge 2$, so $u(t(n)) = (n + 1) - 1 = n$. So $u \circ t = \mathrm{id}_{\mathbb{N}}$. (The check never used $u(1)$, since $t(n) \ne 1$ for every $n$. So any natural number would serve as $u(1)$, and $t$ has more than one left inverse.)

*No right inverse.* If $t$ had a right inverse, then $t$ would be surjective, by the lemma on one-sided inverses (Section 2.8). It is not, so it has none. Directly: for every function $v : \mathbb{N} \to \mathbb{N}$, $t(v(1)) = v(1) + 1 \ge 2$, so $t(v(1)) \ne 1$ and $t \circ v \ne \mathrm{id}_{\mathbb{N}}$.

*A bijection onto $\mathbb{N} \setminus \{1\}$.* Let $t' : \mathbb{N} \to \mathbb{N} \setminus \{1\}$, $t'(n) = n + 1$. This is a function into $\mathbb{N} \setminus \{1\}$, since $n + 1 \in \mathbb{N}$ and $n + 1 \ge 2$, so $n + 1 \ne 1$. It is injective by the same argument as for $t$. It is surjective: let $m \in \mathbb{N} \setminus \{1\}$; then $m \ge 2$, so $n = m - 1 \in \mathbb{N}$, and $t'(n) = m$. So $t'$ is a bijection. Its inverse is $s : \mathbb{N} \setminus \{1\} \to \mathbb{N}$, $s(m) = m - 1$: for every $n \in \mathbb{N}$, $s(t'(n)) = (n + 1) - 1 = n$, and for every $m \in \mathbb{N} \setminus \{1\}$, $t'(s(m)) = (m - 1) + 1 = m$.

The functions $t$ and $t'$ have the same rule and the same graph, and differ only in their codomains. One is a bijection and the other is not. The example also shows that $\mathbb{N}$ is in bijection with a subset of itself that is not all of $\mathbb{N}$.
