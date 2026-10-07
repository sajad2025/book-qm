# Session 2. Sets, functions and the forms of proof

*Definition. Builds on Session 1.*

**Claim.** Statements built from "and", "or", "not", "implies", "for all" and "there exists" have fixed negations; direct proof, contraposition and contradiction are valid methods; and a function is a bijection if and only if it has an inverse.

Session 1 named the three questions the book is aimed at and the Parts each one needs. Every result on the way rests on proofs: chains of statements, each of which follows from earlier ones. This session fixes what a statement is, how to negate one, which chains of reasoning are valid, and the language of sets and functions in which every later session is written.

**Numbers in this session.** The real numbers are defined by axioms later in Part I. Until then, some examples use integers and fractions with their school arithmetic: sums, products, and comparison by size, including the facts that "not $x \lt y$" means $x \ge y$ and "not $x \le y$" means $x \gt y$ (so, by Rule 1 of Section 2.2, "not $x \ge y$" means $x \lt y$ and "not $x \gt y$" means $x \le y$). These examples only illustrate the logic. No theorem of this session uses them, and no later proof cites them.

## 2.1 Statements and connectives

**Definition.** A **statement** is a sentence that is either true or false, and not both. Whether it is true or false is its **truth value**, written T or F.

"$7 \gt 3$" is a statement, and it is true. "$2 + 2 = 5$" is a statement, and it is false. "$x \gt 3$" is not a statement, because its truth value depends on what $x$ is. Sentences of that kind are treated in Section 2.3.

From a statement $P$ one new statement is formed, and from two statements $P$ and $Q$ four more. The truth value of each is fixed by the truth values of $P$ and $Q$, as follows.

**Definition.**
- The **negation** "not $P$", written $\neg P$, is true when $P$ is false, and false when $P$ is true.
- The **conjunction** "$P$ and $Q$", written $P \wedge Q$, is true when $P$ and $Q$ are both true, and false otherwise.
- The **disjunction** "$P$ or $Q$", written $P \vee Q$, is true when at least one of $P$ and $Q$ is true, and false when both are false. The word "or" is inclusive: $P \vee Q$ is true when both are true.
- The **implication** "$P$ implies $Q$", or "if $P$ then $Q$", written $P \Rightarrow Q$, is false when $P$ is true and $Q$ is false, and true in the other three cases. $P$ is its **hypothesis** and $Q$ its **conclusion**.
- The **biconditional** "$P$ if and only if $Q$", written $P \Leftrightarrow Q$, is true when $P$ and $Q$ have the same truth value, and false otherwise.

The words "not", "and", "or", "implies" and "if and only if" are the **connectives**. The definition is summarised in a **truth table**, whose four rows list every possible pair of truth values for $P$ and $Q$:

| $P$ | $Q$ | $\neg P$ | $P \wedge Q$ | $P \vee Q$ | $P \Rightarrow Q$ | $P \Leftrightarrow Q$ |
|---|---|---|---|---|---|---|
| T | T | F | T | T | T | T |
| T | F | F | F | T | F | F |
| F | T | T | F | T | T | F |
| F | F | T | F | F | T | T |

The implication needs a comment. $P \Rightarrow Q$ makes a claim only about the case in which $P$ is true: in that case $Q$ is true. When $P$ is false it claims nothing, and so it is not false. It is then said to be **vacuously true**. For example, "if $2 + 2 = 5$ then $7 \gt 3$" and "if $2 + 2 = 5$ then $7 \lt 3$" are both true. The reason for this choice: the sentence "for every natural number $n$, if $n \gt 5$ then $n \gt 3$" ought to be true (statements with "for every" are defined in Section 2.4), so the implication must be true for $n = 1$, where hypothesis and conclusion are both false, and for $n = 4$, where the hypothesis is false and the conclusion true.

Several phrases mean $P \Rightarrow Q$: "$Q$ if $P$", "$P$ only if $Q$", "$P$ is sufficient for $Q$" and "$Q$ is necessary for $P$".

Connectives can be applied again to the statements they produce, giving statements such as $\neg(P \wedge Q)$ or $P \Rightarrow (Q \vee R)$. The truth value of such a **compound statement** is computed from the inside out, one connective at a time, using the table above.

In a compound statement the letters $P, Q, R, \dots$ may stand for any statements. Its truth value then depends only on the truth values of the letters, and each row of a truth table is one possible assignment of T or F to them.

**Definition.** Two compound statements built from the same letters $P, Q, \dots$ are **logically equivalent**, written with the sign $\equiv$, if they have the same truth value for every assignment of truth values to the letters.

Logically equivalent statements are true in exactly the same cases. So in any argument one may be replaced by the other. The same holds for a part of a compound statement: the truth value of the whole is computed from the truth values of its parts, so replacing a part by a logically equivalent statement does not change the truth value of the whole.

## 2.2 Negations of compound statements

**Theorem (negations of the connectives).** For all statements $P$ and $Q$:

1. $\neg(\neg P) \equiv P$;
2. $\neg(P \wedge Q) \equiv \neg P \vee \neg Q$;
3. $\neg(P \vee Q) \equiv \neg P \wedge \neg Q$;
4. $\neg(P \Rightarrow Q) \equiv P \wedge \neg Q$.

Rules 2 and 3 are **De Morgan's laws** (A. De Morgan, *Formal Logic*, 1847).

*Proof.* Rule 1. If $P$ is true, then $\neg P$ is false, so $\neg(\neg P)$ is true. If $P$ is false, then $\neg P$ is true, so $\neg(\neg P)$ is false. In both cases $\neg(\neg P)$ has the truth value of $P$.

Rules 2-4. Compute both sides in each of the four rows. Each entry is computed from the values of $P$ and $Q$ by applying the connectives one at a time, from the inside out, with the table of Section 2.1. For example, in the second row $P$ is T and $Q$ is F, so $P \wedge Q$ is F and $\neg(P \wedge Q)$ is T; also $\neg P$ is F and $\neg Q$ is T, so $\neg P \vee \neg Q$ is T.

| $P$ | $Q$ | $\neg(P \wedge Q)$ | $\neg P \vee \neg Q$ | $\neg(P \vee Q)$ | $\neg P \wedge \neg Q$ | $\neg(P \Rightarrow Q)$ | $P \wedge \neg Q$ |
|---|---|---|---|---|---|---|---|
| T | T | F | F | F | F | F | F |
| T | F | T | T | F | F | T | T |
| F | T | T | T | F | F | F | F |
| F | F | T | T | T | T | F | F |

The third and fourth columns agree in every row, which is Rule 2. The fifth and sixth agree, which is Rule 3. The seventh and eighth agree, which is Rule 4. ∎

In words: "$P$ and $Q$" fails when at least one of them fails; "$P$ or $Q$" fails when both fail; and an implication fails exactly when its hypothesis holds and its conclusion does not. In particular, the negation of $P \Rightarrow Q$ is not $P \Rightarrow \neg Q$: when $P$ is false, $P \Rightarrow Q$ and $P \Rightarrow \neg Q$ are both true (third and fourth rows of the table in Section 2.1), so one cannot be the negation of the other.

**Definition.** The **contrapositive** of $P \Rightarrow Q$ is $\neg Q \Rightarrow \neg P$. Its **converse** is $Q \Rightarrow P$.

**Theorem (contrapositive and biconditional).** For all statements $P$ and $Q$:

1. $P \Rightarrow Q \equiv \neg Q \Rightarrow \neg P$;
2. $P \Leftrightarrow Q \equiv (P \Rightarrow Q) \wedge (Q \Rightarrow P)$.

*Proof.* In the table, the column $\neg Q \Rightarrow \neg P$ is computed from the columns $\neg Q$ and $\neg P$ by the rule for implication. For example, in the second row $\neg Q$ is T and $\neg P$ is F, so $\neg Q \Rightarrow \neg P$ is F.

| $P$ | $Q$ | $P \Rightarrow Q$ | $\neg Q$ | $\neg P$ | $\neg Q \Rightarrow \neg P$ | $Q \Rightarrow P$ | $(P \Rightarrow Q) \wedge (Q \Rightarrow P)$ | $P \Leftrightarrow Q$ |
|---|---|---|---|---|---|---|---|---|
| T | T | T | F | F | T | T | T | T |
| T | F | F | T | F | F | T | F | F |
| F | T | T | F | T | T | F | F | F |
| F | F | T | T | T | T | T | T | T |

The third and sixth columns agree in every row, which is statement 1. The eighth and ninth agree, which is statement 2. ∎

The table also shows that the converse is not equivalent to the implication: the columns $P \Rightarrow Q$ and $Q \Rightarrow P$ differ in the second and third rows. Section 2.10 gives an instance.

## 2.3 Sets

**Definition.** A **set** is a collection of objects, called its **elements**. "$x \in A$" means that $x$ is an element of $A$, and "$x \notin A$" means $\neg(x \in A)$. Two sets $A$ and $B$ are **equal**, written $A = B$, if every element of $A$ is an element of $B$ and every element of $B$ is an element of $A$.

So a set is determined by its elements and by nothing else. A set may be given by listing its elements between braces. Then $\{1, 2, 3\} = \{3, 1, 2\} = \{1, 1, 2, 3\}$, since each of these has exactly the elements 1, 2 and 3: order and repetition in a list do not matter. The sets of numbers used in the book are $\mathbb{N} = \{1, 2, 3, \dots\}$, the integers $\mathbb{Z}$, the rationals $\mathbb{Q}$ and the reals $\mathbb{R}$.

The book uses sets in this descriptive sense. Axiomatic set theory states precisely which collections count as sets, and every set built in this book is of a kind those axioms allow. The axioms themselves are not used, except the axiom of countable choice, which is stated where it is first used.

**Definition.** A set $A$ is a **subset** of a set $B$, written $A \subseteq B$, if every element of $A$ is an element of $B$. The **empty set** $\emptyset$ is the set with no elements. (Section 2.5 shows that there is only one set with no elements.)

By the two definitions, $A = B$ holds exactly when $A \subseteq B$ and $B \subseteq A$. A proof that two sets are equal therefore usually has two halves, one for each inclusion. This is called **double inclusion**.

**Definition.** Let $S$ be a set. An **open statement** on $S$ is a sentence $P(x)$, containing a variable $x$, that becomes a statement whenever $x$ is replaced by an element of $S$. The set of elements of $S$ for which $P(x)$ is true is written

$$
\{x \in S : P(x)\}.
$$

This is **set-builder notation**. Open statements are also called **predicates**. For example, "$x \gt 3$" is an open statement on $\mathbb{N}$, and $\{x \in \mathbb{N} : x \gt 3\} = \{4, 5, 6, \dots\}$. An open statement may contain several variables, as "$x \lt y$" does. It becomes a statement when every variable is replaced by an element.

**Definition.** Let $A$ and $B$ be sets.
- The **intersection** $A \cap B$ is the set whose elements are the $x$ with $x \in A$ and $x \in B$.
- The **union** $A \cup B$ is the set whose elements are the $x$ with $x \in A$ or $x \in B$.
- The **difference** $A \setminus B = \{x \in A : x \notin B\}$. When $B \subseteq A$ it is also called the **complement** of $B$ in $A$.
- $A$ and $B$ are **disjoint** if $A \cap B = \emptyset$.

**Definition.** For objects $a$ and $b$, the **ordered pair** $(a, b)$ is an object determined by $a$ and $b$ in that order, with the rule that $(a, b) = (c, d)$ if and only if $a = c$ and $b = d$. The **Cartesian product** $A \times B$ is the set of all ordered pairs $(a, b)$ with $a \in A$ and $b \in B$.

Here $a \ne b$ means $\neg(a = b)$. The statement $(a, b) = (c, d)$ has the same truth value as "$a = c$ and $b = d$", so their negations have the same truth value, and by De Morgan's law (Rule 2), $(a, b) \ne (c, d)$ exactly when $a \ne c$ or $b \ne d$. An ordered pair therefore differs from a two-element set: $\{1, 2\} = \{2, 1\}$, but $(1, 2) \ne (2, 1)$, because $1 \ne 2$.

## 2.4 Quantifiers

**Definition.** Let $P(x)$ be an open statement on a set $S$.
- "For every $x \in S$, $P(x)$", written $\forall x \in S,\ P(x)$, is the statement that is true when $P(x)$ is true for every element $x$ of $S$, and false when there is at least one element $x$ of $S$ for which $P(x)$ is false. The sign $\forall$ is the **universal quantifier**.
- "There exists $x \in S$ such that $P(x)$", written $\exists x \in S,\ P(x)$, is the statement that is true when $P(x)$ is true for at least one element $x$ of $S$, and false when $P(x)$ is false for every element $x$ of $S$. The sign $\exists$ is the **existential quantifier**.
- "There exists exactly one $x \in S$ such that $P(x)$", written $\exists!\, x \in S,\ P(x)$, means: there exists $x \in S$ with $P(x)$, and for all $x, y \in S$, if $P(x)$ and $P(y)$ then $x = y$.

For example, $A \subseteq B$ is the statement "for every $x \in A$, $x \in B$". If $S = \emptyset$, then "for every $x \in S$, $P(x)$" is true, because there is no element of $S$ for which $P(x)$ is false. It is vacuously true. In the same case "there exists $x \in S$ such that $P(x)$" is false.

A quantifier is often restricted by a condition. "For every $x \in S$ with $Q(x)$, $P(x)$" means $\forall x \in S,\ (Q(x) \Rightarrow P(x))$. "There exists $x \in S$ with $Q(x)$ such that $P(x)$" means $\exists x \in S,\ (Q(x) \wedge P(x))$.

**Theorem (negations of the quantifiers).** For every set $S$ and every open statement $P(x)$ on $S$,

$$
\neg\bigl(\forall x \in S,\ P(x)\bigr) \equiv \exists x \in S,\ \neg P(x),
\qquad
\neg\bigl(\exists x \in S,\ P(x)\bigr) \equiv \forall x \in S,\ \neg P(x).
$$

Here $\equiv$ means that the two sides have the same truth value for every $S$ and every $P$.

*Proof.* First rule. By the definition of $\forall$, the statement $\forall x \in S,\ P(x)$ is false exactly when there is at least one $x \in S$ for which $P(x)$ is false. So its negation is true exactly when there is at least one $x \in S$ for which $P(x)$ is false, that is, for which $\neg P(x)$ is true. By the definition of $\exists$, this is exactly when $\exists x \in S,\ \neg P(x)$ is true. The two sides are true in the same cases, so they are also false in the same cases.

Second rule. By the definition of $\exists$, the statement $\exists x \in S,\ P(x)$ is false exactly when $P(x)$ is false for every $x \in S$. So its negation is true exactly when $\neg P(x)$ is true for every $x \in S$, which by the definition of $\forall$ is exactly when $\forall x \in S,\ \neg P(x)$ is true. ∎

Combining this with Section 2.2 gives the negations of restricted quantifiers. By Rule 4 of the negations of the connectives,

$$
\neg\bigl(\forall x \in S,\ (Q(x) \Rightarrow P(x))\bigr) \equiv \exists x \in S,\ \neg(Q(x) \Rightarrow P(x)) \equiv \exists x \in S,\ (Q(x) \wedge \neg P(x)).
$$

An element $x$ with $Q(x)$ true and $P(x)$ false is a **counterexample** to the statement being negated. Likewise, by De Morgan's law (Rule 2),

$$
\neg\bigl(\exists x \in S,\ (Q(x) \wedge P(x))\bigr) \equiv \forall x \in S,\ \neg(Q(x) \wedge P(x)) \equiv \forall x \in S,\ (\neg Q(x) \vee \neg P(x)),
$$

and $\neg Q(x) \vee \neg P(x) \equiv Q(x) \Rightarrow \neg P(x)$. The last equivalence is an instance of $\neg U \vee V \equiv U \Rightarrow V$, with $U = Q(x)$ and $V = \neg P(x)$: by the table in Section 2.1, $U \Rightarrow V$ is false only when $U$ is T and $V$ is F, and $\neg U \vee V$ is false only when $\neg U$ and $V$ are both F, that is, again only when $U$ is T and $V$ is F. So the restriction stays in place, and only the quantifier and the final clause change. In each step above, a statement inside a quantifier was replaced by a logically equivalent one. This does not change the truth value of the whole, since for each $x$ the two inner statements have the same truth value.

**Nested quantifiers.** Let $P(x, y)$ be an open statement in two variables, $x$ from a set $S$ and $y$ from a set $T$. For each fixed $x$, "there exists $y \in T$ such that $P(x, y)$" is an open statement in $x$ alone, and the universal quantifier can be applied to it. Applying the theorem twice, first to the outer quantifier and then, for each $x$, to the inner one:

$$
\neg\bigl(\forall x \in S\ \exists y \in T,\ P(x, y)\bigr) \equiv \exists x \in S,\ \neg\bigl(\exists y \in T,\ P(x, y)\bigr) \equiv \exists x \in S\ \forall y \in T,\ \neg P(x, y).
$$

The rule is mechanical: the negation sign moves from left to right, each quantifier it passes changes from $\forall$ to $\exists$ or back, and when it reaches the end the negations of the connectives apply.

**The order of quantifiers matters.** Compare, for natural numbers,

$$
\text{(i)}\ \ \forall n \in \mathbb{N}\ \exists m \in \mathbb{N},\ m \gt n,
\qquad
\text{(ii)}\ \ \exists m \in \mathbb{N}\ \forall n \in \mathbb{N},\ m \gt n.
$$

Statement (i) is true: given $n$, the number $m = n + 1$ is in $\mathbb{N}$ and $n + 1 \gt n$. Statement (ii) is false. Its negation is

$$
\forall m \in \mathbb{N}\ \exists n \in \mathbb{N},\ m \le n,
$$

and this is true: given $m$, take $n = m$. In (i) the number $m$ may depend on $n$. In (ii) one $m$ must serve for every $n$ at once. Exchanging two quantifiers of different kinds is not a valid step.

## 2.5 The forms of proof

A **proof** of a statement is a finite chain of statements that ends with it. Each statement in the chain is an axiom, a definition, a result proved earlier, an assumption made by one of the methods below (such as the hypothesis $P$ in a direct proof of $P \Rightarrow Q$), or follows from statements earlier in the chain by a valid rule. A rule is **valid** if it never leads from true statements to a false one. The basic rule is the following.

**Theorem (modus ponens).** If $P$ is true and $P \Rightarrow Q$ is true, then $Q$ is true.

*Proof.* In the table of Section 2.1, the only row in which $P$ is T and $P \Rightarrow Q$ is T is the first, and there $Q$ is T. ∎

The methods below are the forms that proofs in this book take.

**Theorem (validity of the forms of proof).** Each method below, when carried out, proves the statement it names.

*Proof.* The argument is given method by method, in the paragraph headed *Validity* after each one. The last of these paragraphs ends the proof.

**Direct proof of $P \Rightarrow Q$.** Assume that $P$ is true, and derive $Q$ by valid steps.

*Validity.* If $P$ is false, then $P \Rightarrow Q$ is true by the definition of implication (third and fourth rows). If $P$ is true, the derivation shows that $Q$ is true, and $P \Rightarrow Q$ is true (first row). In both cases $P \Rightarrow Q$ is true.

**Proof of "for every $x \in S$, $P(x)$".** Let $x$ be an arbitrary element of $S$, which means that no property of $x$ is used except $x \in S$, and derive $P(x)$.

*Validity.* The derivation uses nothing about $x$ beyond $x \in S$, so it applies to each element of $S$. So $P(x)$ is true for every element of $S$, which is the definition of the universal statement. A statement "for every $x \in S$, if $Q(x)$ then $P(x)$" is proved by letting $x \in S$ be arbitrary, assuming $Q(x)$ and deriving $P(x)$, which is a direct proof inside a universal one.

**Proof of "there exists $x \in S$ such that $P(x)$".** Name a particular element $s$ of $S$ and show that $P(s)$ is true.

*Validity.* This is the definition of the existential statement.

**Disproof by counterexample.** To show that "for every $x \in S$, $P(x)$" is false, name an element $s \in S$ for which $P(s)$ is false.

*Validity.* This proves "there exists $x \in S$ such that $\neg P(x)$", which is the negation of the universal statement by the negations of the quantifiers (Section 2.4).

**Proof by contraposition.** To prove $P \Rightarrow Q$, prove $\neg Q \Rightarrow \neg P$, usually by a direct proof.

*Validity.* The two statements are logically equivalent (Section 2.2), so they have the same truth value.

**Proof by contradiction.** To prove $P$, assume $\neg P$ and derive some statement $R$ together with its negation $\neg R$.

*Validity.* The argument shows that $\neg P \Rightarrow (R \wedge \neg R)$ is true. Compute its truth table:

| $P$ | $R$ | $\neg P$ | $\neg R$ | $R \wedge \neg R$ | $\neg P \Rightarrow (R \wedge \neg R)$ |
|---|---|---|---|---|---|
| T | T | F | F | F | T |
| T | F | F | T | F | T |
| F | T | T | F | F | F |
| F | F | T | T | F | F |

The last column is T only in the first two rows, and in both of them $P$ is T. So whenever $\neg P \Rightarrow (R \wedge \neg R)$ is true, $P$ is true.

To prove an implication $P \Rightarrow Q$ by contradiction, apply the method to the statement $\neg(P \wedge \neg Q)$. Its negation $\neg(\neg(P \wedge \neg Q))$ is equivalent to $P \wedge \neg Q$ by Rule 1, and assuming $P \wedge \neg Q$ is assuming $P$ and assuming $\neg Q$. So deriving $R$ and $\neg R$ from $P$ and $\neg Q$ proves $\neg(P \wedge \neg Q)$. Finally, $P \wedge \neg Q \equiv \neg(P \Rightarrow Q)$ by Rule 4, so $\neg(P \wedge \neg Q) \equiv \neg(\neg(P \Rightarrow Q)) \equiv P \Rightarrow Q$ by Rule 1.

**Proof of $P \Leftrightarrow Q$.** Prove $P \Rightarrow Q$ and prove $Q \Rightarrow P$.

*Validity.* $P \Leftrightarrow Q \equiv (P \Rightarrow Q) \wedge (Q \Rightarrow P)$ (Section 2.2), and a conjunction is true when both its parts are.

**Proof by cases.** To prove $(P \vee Q) \Rightarrow R$, prove $P \Rightarrow R$ and prove $Q \Rightarrow R$.

*Validity.* The truth table over the eight assignments of truth values to $P$, $Q$ and $R$ shows that $(P \Rightarrow R) \wedge (Q \Rightarrow R) \equiv (P \vee Q) \Rightarrow R$:

| $P$ | $Q$ | $R$ | $P \Rightarrow R$ | $Q \Rightarrow R$ | $(P \Rightarrow R) \wedge (Q \Rightarrow R)$ | $P \vee Q$ | $(P \vee Q) \Rightarrow R$ |
|---|---|---|---|---|---|---|---|
| T | T | T | T | T | T | T | T |
| T | T | F | F | F | F | T | F |
| T | F | T | T | T | T | T | T |
| T | F | F | F | T | F | T | F |
| F | T | T | T | T | T | T | T |
| F | T | F | T | F | F | T | F |
| F | F | T | T | T | T | F | T |
| F | F | F | T | T | T | F | T |

The sixth and eighth columns agree in every row. So proving $P \Rightarrow R$ and $Q \Rightarrow R$ makes their conjunction true, and hence $(P \vee Q) \Rightarrow R$ true. When $P \vee Q$ is known to be true, modus ponens then gives $R$. A common case is $Q = \neg P$: the statement $P \vee \neg P$ is always true, since if $P$ is T it is T $\vee$ F, and if $P$ is F it is F $\vee$ T. So any proof may split into the cases $P$ and $\neg P$.

**Proof of uniqueness.** To prove that there is at most one $x \in S$ with $P(x)$, let $x, y \in S$, assume $P(x)$ and $P(y)$, and derive $x = y$.

*Validity.* This is a direct proof of the second half of the definition of $\exists!$ in Section 2.4. ∎

**Examples.** A direct proof. *For all sets $A$, $B$ and $C$, if $A \subseteq B$ and $B \subseteq C$, then $A \subseteq C$.* Assume $A \subseteq B$ and $B \subseteq C$. Let $x \in A$ be arbitrary. Since $A \subseteq B$, $x \in B$. Since $B \subseteq C$, $x \in C$. So every element of $A$ is an element of $C$, which is the statement $A \subseteq C$.

A uniqueness proof, with a vacuous step. *There is only one empty set.* Let $E$ and $E'$ be sets with no elements. The statement "every element of $E$ is an element of $E'$" is true vacuously, because $E$ has no elements; so $E \subseteq E'$. In the same way $E' \subseteq E$. So $E = E'$ by double inclusion. The same vacuous argument shows $\emptyset \subseteq A$ for every set $A$.

A proof by contraposition, using arithmetic as an illustration. *For numbers $x$ and $y$, if $x + y \ge 2$ then $x \ge 1$ or $y \ge 1$.* The contrapositive is "if not ($x \ge 1$ or $y \ge 1$), then not ($x + y \ge 2$)". By De Morgan's law (Rule 3), the hypothesis is "$x \lt 1$ and $y \lt 1$", and the conclusion reads $x + y \lt 2$. Proof of the contrapositive: assume $x \lt 1$ and $y \lt 1$. Adding the two inequalities gives $x + y \lt 1 + 1 = 2$.

A proof by contradiction, again with arithmetic as an illustration. *There is no largest natural number*, that is, $\neg\bigl(\exists m \in \mathbb{N}\ \forall n \in \mathbb{N},\ n \le m\bigr)$. Assume the opposite: there is $m \in \mathbb{N}$ with $n \le m$ for every $n \in \mathbb{N}$. Then $m + 1 \in \mathbb{N}$, so $m + 1 \le m$. This is the statement $R$. But $m \lt m + 1$, which is $\neg R$. The assumption has led to $R$ and $\neg R$, so it is false.

## 2.6 Families of sets and De Morgan's laws for sets

**Definition.** Let $I$ be a set, and for each $i \in I$ let $A_i$ be a set. The collection $(A_i)_{i \in I}$ is a **family of sets** indexed by $I$. Its **union** $\bigcup_{i \in I} A_i$ is the set of all $x$ such that $x \in A_i$ for at least one $i \in I$. When $I$ is nonempty, its **intersection** $\bigcap_{i \in I} A_i$ is the set of all $x$ such that $x \in A_i$ for every $i \in I$.

For $I = \{1, 2\}$, "$x \in A_i$ for at least one $i \in \{1, 2\}$" says $x \in A_1$ or $x \in A_2$, and "$x \in A_i$ for every $i \in \{1, 2\}$" says $x \in A_1$ and $x \in A_2$. So the union and intersection of the family are $A_1 \cup A_2$ and $A_1 \cap A_2$.

**Theorem (De Morgan's laws for sets).** Let $X$ be a set and $(A_i)_{i \in I}$ a family of sets with $I$ nonempty. Then

$$
X \setminus \bigcup_{i \in I} A_i = \bigcap_{i \in I} (X \setminus A_i),
\qquad
X \setminus \bigcap_{i \in I} A_i = \bigcup_{i \in I} (X \setminus A_i).
$$

In particular $X \setminus (A \cup B) = (X \setminus A) \cap (X \setminus B)$ and $X \setminus (A \cap B) = (X \setminus A) \cup (X \setminus B)$.

*Proof.* First law. Fix an object $x$. The following statements are each logically equivalent to the next.

1. $x \in X \setminus \bigcup_{i \in I} A_i$.
2. $x \in X$, and not ($x \in A_i$ for at least one $i \in I$). This is the definition of difference and union.
3. $x \in X$, and $x \notin A_i$ for every $i \in I$. This is the negation of the existential quantifier (Section 2.4).
4. For every $i \in I$: $x \in X$ and $x \notin A_i$.
5. For every $i \in I$, $x \in X \setminus A_i$. This is the definition of difference.
6. $x \in \bigcap_{i \in I} (X \setminus A_i)$. This is the definition of intersection.

The step from 3 to 4 needs an argument. If 3 holds, then for each $i \in I$ both $x \in X$ and $x \notin A_i$ hold, which is 4. If 4 holds, then since $I$ is nonempty there is some $i_0 \in I$, and 4 for $i_0$ gives $x \in X$; also 4 gives $x \notin A_i$ for every $i$; together these are 3. So 1 is true exactly when 6 is. Applied to each $x$, this gives both inclusions, and the sets are equal.

Second law. In the same way:

1. $x \in X \setminus \bigcap_{i \in I} A_i$.
2. $x \in X$, and not ($x \in A_i$ for every $i \in I$). This is the definition of difference and intersection.
3. $x \in X$, and $x \notin A_i$ for at least one $i \in I$, by the negation of the universal quantifier.
4. For at least one $i \in I$: $x \in X$ and $x \notin A_i$.
5. $x \in \bigcup_{i \in I} (X \setminus A_i)$. This is the definition of difference and union.

From 3 to 4: if $x \in X$ and $x \notin A_{i_0}$ for some $i_0$, then that $i_0$ satisfies 4. If some $i_0$ satisfies 4, then $x \in X$, and $i_0$ witnesses the second half of 3. The two-set forms are the case $I = \{1, 2\}$, $A_1 = A$, $A_2 = B$. ∎

Inside the proof, the hypothesis that $I$ is nonempty was used once, in the step from 4 to 3 of the first law. When $I$ is empty, statement 4 is vacuously true (Section 2.4) for every $x$, including every $x \notin X$, and that step fails. The definition of the intersection excludes an empty $I$ for a related reason. When $I$ is empty, the condition "$x \in A_i$ for every $i \in I$" is vacuously true of every object $x$ whatsoever, so an intersection over $I$ would contain every object. The axioms of set theory do not allow such a collection as a set.

## 2.7 Functions

**Definition.** Let $A$ and $B$ be sets. A **function** $f$ from $A$ to $B$, written $f : A \to B$, is given by the set $A$, the set $B$, and a subset $\Gamma_f$ of $A \times B$ with the property that for every $a \in A$ there exists exactly one $b \in B$ with $(a, b) \in \Gamma_f$. This $b$ is written $f(a)$ and called the **value** of $f$ at $a$. $A$ is the **domain** of $f$, $B$ its **codomain**, and $\Gamma_f$ its **graph**. The words **map** and **mapping** mean the same as function.

In practice a function is given by a rule $x \mapsto f(x)$, together with its domain and codomain. The definition says what a rule must do: assign to each element of $A$ one element of $B$, no fewer and no more. Its graph is then $\Gamma_f = \{(a, b) \in A \times B : b = f(a)\}$, the set of all pairs $(a, f(a))$ with $a \in A$.

For example, with $A = \{1, 2, 3\}$ and $B = \{p, q\}$, where $p \ne q$, the set $\{(1, p), (2, q), (3, p)\}$ is the graph of a function $f : A \to B$ with $f(1) = p$, $f(2) = q$, $f(3) = p$. The set $\{(1, p), (1, q), (2, p), (3, q)\}$ is not the graph of a function from $A$ to $B$, because 1 is paired with two elements. The set $\{(1, p), (2, q)\}$ is not either, because 3 is paired with none.

**Definition.** Two functions $f : A \to B$ and $g : C \to D$ are **equal** if $A = C$, $B = D$, and $f(a) = g(a)$ for every $a \in A$.

Equal functions have the same graph, since each graph is the set of pairs $(a, f(a))$. Functions with the same rule but different codomains are different functions; Section 2.8 shows why this matters.

**Definition.** The **identity** on a set $A$ is $\mathrm{id}_A : A \to A$, $\mathrm{id}_A(a) = a$.

**Definition.** Let $f : A \to B$.
- For $C \subseteq A$, the **image** of $C$ is $f(C) = \{b \in B : \text{there exists } c \in C \text{ with } f(c) = b\}$, also written $\{f(c) : c \in C\}$. The set $f(A)$ is the **range** of $f$.
- For $D \subseteq B$, the **preimage** of $D$ is $f^{-1}(D) = \{a \in A : f(a) \in D\}$.

The preimage is defined for every function. Section 2.8 defines a second object written $f^{-1}$, the inverse of a function, and shows that the two meanings of $f^{-1}(D)$ agree when both apply.

**Definition.** Let $f : A \to B$ and $g : B \to C$. The **composition** $g \circ f : A \to C$ is $(g \circ f)(a) = g(f(a))$.

This is a function: for each $a \in A$, $f(a)$ is one element of $B$, and $g$ assigns to it one element $g(f(a))$ of $C$.

**Lemma (composition).** Let $f : A \to B$, $g : B \to C$ and $h : C \to D$. Then

$$
h \circ (g \circ f) = (h \circ g) \circ f,
\qquad
f \circ \mathrm{id}_A = f = \mathrm{id}_B \circ f.
$$

*Proof.* Both sides of the first equation are functions from $A$ to $D$. For every $a \in A$,

$$
\bigl(h \circ (g \circ f)\bigr)(a) = h\bigl((g \circ f)(a)\bigr) = h\bigl(g(f(a))\bigr),
\qquad
\bigl((h \circ g) \circ f\bigr)(a) = (h \circ g)\bigl(f(a)\bigr) = h\bigl(g(f(a))\bigr),
$$

so the values agree. All three functions in the second equation go from $A$ to $B$, and for every $a \in A$, $f(\mathrm{id}_A(a)) = f(a)$ and $\mathrm{id}_B(f(a)) = f(a)$. ∎

Because of the first equation, brackets in a composition of three functions may be omitted, and $h \circ g \circ f$ has one meaning.

## 2.8 Injections, surjections, bijections and inverses

**Definition.** A function $f : A \to B$ is
- **injective**, or an **injection**, if for all $a, a' \in A$, $f(a) = f(a')$ implies $a = a'$;
- **surjective**, or a **surjection**, if for every $b \in B$ there exists $a \in A$ with $f(a) = b$;
- **bijective**, or a **bijection**, if it is injective and surjective.

By the contrapositive (Section 2.2), $f$ is injective if and only if for all $a, a' \in A$, $a \ne a'$ implies $f(a) \ne f(a')$: distinct elements have distinct values. Since $f(A) \subseteq B$ always holds, $f$ is surjective if and only if $B \subseteq f(A)$, that is, if and only if $f(A) = B$. Surjectivity depends on the codomain, which is why the codomain is part of a function.

With quantifiers, $f$ is injective when $\forall a \in A\ \forall a' \in A,\ (f(a) = f(a') \Rightarrow a = a')$, and surjective when $\forall b \in B\ \exists a \in A,\ f(a) = b$. Moving the negation sign to the right (Section 2.4), with Rule 4 of Section 2.2 for the implication:

$$
f \text{ is not injective} \equiv \exists a \in A\ \exists a' \in A,\ \bigl(f(a) = f(a') \wedge a \ne a'\bigr),
$$

$$
f \text{ is not surjective} \equiv \exists b \in B\ \forall a \in A,\ f(a) \ne b.
$$

**Definition.** Let $f : A \to B$ and $g : B \to A$.
- $g$ is a **left inverse** of $f$ if $g \circ f = \mathrm{id}_A$, that is, $g(f(a)) = a$ for every $a \in A$.
- $g$ is a **right inverse** of $f$ if $f \circ g = \mathrm{id}_B$, that is, $f(g(b)) = b$ for every $b \in B$.
- $g$ is an **inverse** of $f$ if it is both a left inverse and a right inverse.

**Lemma (one-sided inverses).** Let $f : A \to B$.
1. If $f$ has a left inverse, then $f$ is injective.
2. If $f$ has a right inverse, then $f$ is surjective.

*Proof.* 1. Let $g$ be a left inverse. Let $a, a' \in A$ with $f(a) = f(a')$. Applying $g$ to both sides gives $g(f(a)) = g(f(a'))$. Since $g \circ f = \mathrm{id}_A$, the left side is $a$ and the right side is $a'$. So $a = a'$.

2. Let $g$ be a right inverse. Let $b \in B$, and put $a = g(b)$, an element of $A$. Then $f(a) = f(g(b)) = b$, since $f \circ g = \mathrm{id}_B$. So $b$ is a value of $f$. ∎

**Theorem (bijections and inverses).** A function $f : A \to B$ is a bijection if and only if it has an inverse. The inverse is then unique. It is written $f^{-1} : B \to A$, it is itself a bijection, and its inverse is $f$.

*Proof.* Suppose first that $f$ has an inverse $g$. Then $g$ is a left inverse, so $f$ is injective, and a right inverse, so $f$ is surjective, by the lemma on one-sided inverses. So $f$ is a bijection.

Conversely, suppose $f$ is a bijection. Let $b \in B$. Since $f$ is surjective, there is $a \in A$ with $f(a) = b$. Since $f$ is injective, there is at most one: if $f(a) = b$ and $f(a') = b$, then $f(a) = f(a')$, so $a = a'$. So there is exactly one $a \in A$ with $f(a) = b$. Define $g(b)$ to be this element. Then $g : B \to A$ is a function: its graph is $\{(b, a) \in B \times A : f(a) = b\}$, and we have just shown that for every $b \in B$ there is exactly one $a$ with $(b, a)$ in this set. It remains to check the two equations.
- For every $b \in B$, $g(b)$ is an element whose value under $f$ is $b$. So $f(g(b)) = b$, and $f \circ g = \mathrm{id}_B$.
- Let $a \in A$ and put $b = f(a)$. By definition, $g(b)$ is the only element of $A$ whose value under $f$ is $b$. The element $a$ has this property. So $g(b) = a$, that is, $g(f(a)) = a$, and $g \circ f = \mathrm{id}_A$.

So $g$ is an inverse of $f$.

Uniqueness. Let $g$ and $h$ be inverses of $f$. By the composition lemma (Section 2.7), and the equations $f \circ h = \mathrm{id}_B$ and $g \circ f = \mathrm{id}_A$,

$$
g = g \circ \mathrm{id}_B = g \circ (f \circ h) = (g \circ f) \circ h = \mathrm{id}_A \circ h = h.
$$

Finally, the equations $f^{-1} \circ f = \mathrm{id}_A$ and $f \circ f^{-1} = \mathrm{id}_B$ say, read the other way round, that $f$ is a left and a right inverse of $f^{-1} : B \to A$. So $f$ is an inverse of $f^{-1}$. By the first part of the proof, applied to $f^{-1}$, the function $f^{-1}$ is a bijection, and by uniqueness its inverse is $f$. ∎

The uniqueness argument used only that $g$ is a left inverse and $h$ a right inverse. So if a function has a left inverse and a right inverse, they are equal, and the function is a bijection by the lemma on one-sided inverses.

**Lemma (the two meanings of $f^{-1}$).** Let $f : A \to B$ be a bijection and $D \subseteq B$. The preimage of $D$ under $f$ equals the image of $D$ under $f^{-1}$.

*Proof.* Both are subsets of $A$. Let $a \in A$. If $a$ is in the preimage, then $f(a) \in D$; put $d = f(a)$. Then $f^{-1}(d) = f^{-1}(f(a)) = a$, so $a$ is the value of $f^{-1}$ at an element of $D$, and $a$ is in the image. Conversely, if $a$ is in the image, then $a = f^{-1}(d)$ for some $d \in D$, and $f(a) = f(f^{-1}(d)) = d \in D$, so $a$ is in the preimage. By double inclusion the two sets are equal. ∎

So the notation $f^{-1}(D)$ has one meaning whenever both readings are defined.

**Corollary (composition of bijections).** If $f : A \to B$ and $g : B \to C$ are bijections, then $g \circ f : A \to C$ is a bijection, and $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$.

*Proof.* By the composition lemma, used to move brackets, and the defining equations of $f^{-1}$ and $g^{-1}$,

$$
(f^{-1} \circ g^{-1}) \circ (g \circ f) = f^{-1} \circ \bigl(g^{-1} \circ (g \circ f)\bigr) = f^{-1} \circ \bigl((g^{-1} \circ g) \circ f\bigr) = f^{-1} \circ (\mathrm{id}_B \circ f) = f^{-1} \circ f = \mathrm{id}_A,
$$

$$
(g \circ f) \circ (f^{-1} \circ g^{-1}) = g \circ \bigl(f \circ (f^{-1} \circ g^{-1})\bigr) = g \circ \bigl((f \circ f^{-1}) \circ g^{-1}\bigr) = g \circ (\mathrm{id}_B \circ g^{-1}) = g \circ g^{-1} = \mathrm{id}_C.
$$

So $f^{-1} \circ g^{-1}$ is an inverse of $g \circ f$. By the theorem, $g \circ f$ is a bijection and this is its unique inverse. ∎

## 2.9 Worked examples

**Negating a statement with three quantifiers.** Let $a : \mathbb{N} \to \mathbb{Q}$ be a function, and write $a_n$ for $a(n)$. Consider the statement

$$
L:\quad \forall \varepsilon \in \mathbb{Q} \text{ with } \varepsilon \gt 0\ \ \exists N \in \mathbb{N}\ \ \forall n \in \mathbb{N} \text{ with } n \ge N,\ \ \bigl(-\varepsilon \lt a_n \wedge a_n \lt \varepsilon\bigr).
$$

Statements of this shape define limits later in Part I. The negation sign moves from left to right, one quantifier at a time. Restrictions stay in place (Section 2.4). In the display, $\forall n \ge N$ abbreviates "for every $n \in \mathbb{N}$ with $n \ge N$", and from the second line on $\exists \varepsilon \gt 0$ abbreviates "there exists $\varepsilon \in \mathbb{Q}$ with $\varepsilon \gt 0$".

$$
\begin{aligned}
\neg L
&\equiv \exists \varepsilon \in \mathbb{Q} \text{ with } \varepsilon \gt 0,\ \ \neg\bigl(\exists N \in \mathbb{N}\ \forall n \ge N,\ (-\varepsilon \lt a_n \wedge a_n \lt \varepsilon)\bigr) \\
&\equiv \exists \varepsilon \gt 0\ \ \forall N \in \mathbb{N},\ \ \neg\bigl(\forall n \ge N,\ (-\varepsilon \lt a_n \wedge a_n \lt \varepsilon)\bigr) \\
&\equiv \exists \varepsilon \gt 0\ \ \forall N \in \mathbb{N}\ \ \exists n \ge N,\ \ \neg(-\varepsilon \lt a_n \wedge a_n \lt \varepsilon) \\
&\equiv \exists \varepsilon \gt 0\ \ \forall N \in \mathbb{N}\ \ \exists n \ge N,\ \ \bigl(\neg(-\varepsilon \lt a_n) \vee \neg(a_n \lt \varepsilon)\bigr) \\
&\equiv \exists \varepsilon \gt 0\ \ \forall N \in \mathbb{N}\ \ \exists n \ge N,\ \ \bigl(a_n \le -\varepsilon \vee a_n \ge \varepsilon\bigr).
\end{aligned}
$$

The first three lines use the negations of the quantifiers, the fourth uses De Morgan's law (Rule 2), and the fifth uses the arithmetic of order: "not $x \lt y$" means $x \ge y$. In words: there is a positive $\varepsilon$ such that, however large $N$ is taken, some $a_n$ with $n \ge N$ satisfies $a_n \le -\varepsilon$ or $a_n \ge \varepsilon$.

Now take the function with $a_n = 1$ for every $n$, and check $\neg L$ for it by the form of proof that each quantifier demands. The existential $\varepsilon$ is exhibited: $\varepsilon = \tfrac{1}{2}$. The universal $N$ is arbitrary: let $N \in \mathbb{N}$. The existential $n$ is exhibited: $n = N$, which satisfies $n \ge N$. Then $a_n = 1 \ge \tfrac{1}{2} = \varepsilon$, so the disjunction in the last line is true, through its second part. So $\neg L$ is true for this function, and $L$ is false.

**A bijection and its inverse.** Let $A = \{1, 2, 3\}$, $B = \{p, q, r\}$ with $p$, $q$, $r$ distinct, and $f : A \to B$ with

$$
f(1) = q, \qquad f(2) = r, \qquad f(3) = p.
$$

*Injective.* The three pairs of distinct elements of $A$ are $\{1, 2\}$, $\{1, 3\}$ and $\{2, 3\}$. Their values are $q \ne r$, $q \ne p$ and $r \ne p$. So distinct elements have distinct values.

*Surjective.* $p = f(3)$, $q = f(1)$ and $r = f(2)$, so every element of $B$ is a value.

*The inverse, built as in the proof.* For each $b \in B$, $g(b)$ is the one element of $A$ with value $b$:

$$
g(p) = 3, \qquad g(q) = 1, \qquad g(r) = 2.
$$

*Check of $g \circ f = \mathrm{id}_A$.* $g(f(1)) = g(q) = 1$, $g(f(2)) = g(r) = 2$ and $g(f(3)) = g(p) = 3$.

*Check of $f \circ g = \mathrm{id}_B$.* $f(g(p)) = f(3) = p$, $f(g(q)) = f(1) = q$ and $f(g(r)) = f(2) = r$.

So $g = f^{-1}$. Its graph $\{(q, 1), (r, 2), (p, 3)\}$ is the graph of $f$ with each pair reversed.

## 2.10 What fails

**The converse is a different statement.** For a number $x$, the implication "if $x = 1$ then $x^2 = 1$" is true: if $x = 1$, then $x^2 = 1 \cdot 1 = 1$. Its converse "if $x^2 = 1$ then $x = 1$" is false, and $x = -1$ is a counterexample: $(-1)^2 = (-1)(-1) = 1$, so the hypothesis is true, while the conclusion $-1 = 1$ is false. With $P$ the statement $x = 1$ and $Q$ the statement $x^2 = 1$, the case $x = -1$ is the third row of the second table in Section 2.2: $P$ is false and $Q$ is true, so $P \Rightarrow Q$ is true and $Q \Rightarrow P$ is false. So a proof of $P \Rightarrow Q$ is not a proof of its converse $Q \Rightarrow P$.

**One equation does not make an inverse.** The definition of an inverse asks for both $g \circ f = \mathrm{id}_A$ and $f \circ g = \mathrm{id}_B$. One alone is not enough. Let $A = \{1, 2\}$ and $B = \{p, q, r\}$ with $p$, $q$, $r$ distinct, and define

$$
f : A \to B,\quad f(1) = p,\ f(2) = q;
\qquad
g : B \to A,\quad g(p) = 1,\ g(q) = 2,\ g(r) = 1.
$$

Then $g(f(1)) = g(p) = 1$ and $g(f(2)) = g(q) = 2$, so $g \circ f = \mathrm{id}_A$, and $g$ is a left inverse of $f$. But $f(g(r)) = f(1) = p \ne r$, so $f \circ g \ne \mathrm{id}_B$. Neither function is a bijection: $f$ is not surjective, since $r$ is not a value of $f$, and $g$ is not injective, since $g(p) = g(r)$ with $p \ne r$. In agreement with the lemma on one-sided inverses, $f$ is injective and $g$ is surjective.

## Exercises

*Check*

1. Use a truth table with eight rows to decide whether $P \Rightarrow (Q \Rightarrow R)$ and $(P \wedge Q) \Rightarrow R$ are logically equivalent.

2. Let $f : A \to B$. Write the statement "for every $b \in B$ there exists exactly one $a \in A$ with $f(a) = b$" with quantifiers, using the definition of $\exists!$, and negate it, moving the negation sign all the way to the right.

3. Let $p$, $q$, $r$ be distinct, and let $f : \{1, 2, 3, 4\} \to \{p, q, r\}$ be given by $f(1) = f(2) = p$ and $f(3) = f(4) = q$. Compute $f(\{1, 3\})$, $f^{-1}(\{p\})$, $f^{-1}(\{r\})$, $f(f^{-1}(\{p, r\}))$ and $f^{-1}(f(\{1\}))$. Is $f$ injective? Is it surjective?

*Prove*

4. Prove that $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ for all sets $A$, $B$, $C$, by double inclusion, using proofs by cases.

5. Let $f : A \to B$ and $g : B \to C$. Prove:
   - (a) if $f$ and $g$ are injective, then $g \circ f$ is injective (direct proof);
   - (b) if $g \circ f$ is injective, then $f$ is injective (by contraposition);
   - (c) if $g \circ f$ is surjective, then $g$ is surjective.

6. Let $f : A \to B$ and $g : B \to A$ with $g \circ f = \mathrm{id}_A$. Prove by contradiction that if $f$ is not surjective, then $g$ is not injective.

*Extend*

7. For a set $A$, the **power set** $\mathcal{P}(A)$ is the set whose elements are the subsets of $A$. Prove that no function $f : A \to \mathcal{P}(A)$ is surjective. (Consider $D = \{a \in A : a \notin f(a)\}$.) This is Cantor's theorem. Cantor's paper gives the argument with two-valued functions in place of subsets, and the set $D$ is its standard modern form (G. Cantor, "Ueber eine elementare Frage der Mannigfaltigkeitslehre", *Jahresbericht der Deutschen Mathematiker-Vereinigung* 1 (1890-91), 75-78).

8. Let $t : \mathbb{N} \to \mathbb{N}$, $t(n) = n + 1$, using the arithmetic of natural numbers as an illustration. Show that $t$ is injective and not surjective, find a left inverse of $t$, and show that $t$ has no right inverse. Then show that $t$, with its codomain replaced by $\mathbb{N} \setminus \{1\}$, is a bijection, and find its inverse.

Solutions: [solutions/002-sets-functions-logic.md](../solutions/002-sets-functions-logic.md).
