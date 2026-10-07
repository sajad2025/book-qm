# Session 4. The real numbers and the least-upper-bound property

*Definition. Builds on Sessions 2 and 3.*

**Claim.** The real numbers form an ordered field in which every nonempty set bounded above has a least upper bound, and this property implies the Archimedean property.

School mathematics treats a real number as a point on a line or as an infinite decimal, and uses its rules of arithmetic without proof. From this session on, the real numbers are described by a short list of axioms, and every property of them that the book uses is derived from that list. The list has three groups. The field axioms (Section 4.2) govern addition and multiplication. The order axioms (Section 4.3) govern the inequality $x \lt y$. The least-upper-bound property (Section 4.4) is a single further axiom, and it is the one that distinguishes the real numbers from the rational numbers. Section 4.7 derives the Archimedean property from it.

## 4.1 Recall

Session 2 (Theorem (negations of the quantifiers), Section 2.4) fixed the negation of quantified statements. The negation of "for every $x \in S$, $P(x)$" is "there exists $x \in S$ such that not $P(x)$", and the negation of "there exists $x \in S$ such that $P(x)$" is "for every $x \in S$, not $P(x)$". It also established (Section 2.5) that a proof by contradiction is valid: to prove a statement, assume its negation and derive a statement together with its negation. Both are used repeatedly below.

## 4.2 Fields

**Definition.** A **field** is a set $F$ with two operations, **addition** $(x, y) \mapsto x + y$ and **multiplication** $(x, y) \mapsto xy$, each taking two elements of $F$ to an element of $F$, such that the following axioms hold for all $x, y, z \in F$.

- (A1) $x + y = y + x$.
- (A2) $(x + y) + z = x + (y + z)$.
- (A3) There is an element $0 \in F$ with $x + 0 = x$ for every $x \in F$.
- (A4) For each $x \in F$ there is an element $-x \in F$ with $x + (-x) = 0$.
- (M1) $xy = yx$.
- (M2) $(xy)z = x(yz)$.
- (M3) There is an element $1 \in F$ with $1 \ne 0$ and $x \cdot 1 = x$ for every $x \in F$.
- (M4) For each $x \in F$ with $x \ne 0$ there is an element $x^{-1} \in F$ with $x x^{-1} = 1$.
- (D) $x(y + z) = xy + xz$.

The element $-x$ is the **negative** of $x$, and $x^{-1}$ is the **reciprocal** of $x$. The product $xy$ is also written $x \cdot y$. We write $x - y$ for $x + (-y)$, and write $\frac{x}{y}$ or $x/y$ for $x y^{-1}$ when $y \ne 0$, so that $1/y = 1 \cdot y^{-1} = y^{-1}$ by (M1) and (M3). We write $x^2$ for $xx$, read $-x^2$ as $-(x^2)$, and write $2 = 1 + 1$, $3 = 2 + 1$, $4 = 3 + 1$.

Two remarks on bookkeeping. First, (A2) and (M2) say that the grouping of three terms does not matter, so we write $x + y + z$ and $xyz$ without brackets; with (A1) and (M1), a step that reorders or regroups three or four terms is an application of these four axioms, and we name them when the step is the point of the argument. Second, (D) has a mirror form: $(y + z)x = x(y + z) = xy + xz = yx + zx$, by (M1), (D) and (M1) again.

**Lemma (field rules).** In a field, for all elements $x, y, z, a, b, c, d$:

- (a) If $x + y = x + z$, then $y = z$. In particular the element $0$ of (A3) is the only element with that property, and $-x$ is the only element whose sum with $x$ is $0$.
- (b) $-(-x) = x$.
- (c) $0x = 0$.
- (d) $(-x)y = -(xy)$, and $(-x)(-y) = xy$. In particular $(-1)x = -x$. Also $-(x - y) = y - x$.
- (e) If $x \ne 0$ and $xy = xz$, then $y = z$. In particular $x^{-1} \ne 0$, $x^{-1}$ is the only element whose product with $x$ is $1$, and $(x^{-1})^{-1} = x$.
- (f) If $xy = 0$, then $x = 0$ or $y = 0$.
- (g) If $x \ne 0$ and $y \ne 0$, then $xy \ne 0$ and $(xy)^{-1} = x^{-1} y^{-1}$.
- (h) If $b \ne 0$ and $d \ne 0$, then $\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}$ and $\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$.

*Proof.* (a) Add $-x$ on the left of both sides: $(-x) + (x + y) = (-x) + (x + z)$. By (A2), $((-x) + x) + y = ((-x) + x) + z$. By (A1) and (A4), $(-x) + x = x + (-x) = 0$, so $0 + y = 0 + z$. By (A1) and (A3), $0 + y = y$ and $0 + z = z$, so $y = z$. If $0'$ also satisfies $x + 0' = x$ for every $x$, then $x + 0' = x + 0$ for any $x$, and cancellation gives $0' = 0$. If $x + y = 0$, then $x + y = x + (-x)$, and cancellation gives $y = -x$.

(b) By (A1) and (A4), $(-x) + x = 0$. So $x$ is an element whose sum with $-x$ is $0$. By the uniqueness in (a), applied to the element $-x$, $x = -(-x)$.

(c) By (A3), $0 + 0 = 0$, so $0x = (0 + 0)x = 0x + 0x$ by the mirror form of (D). Also $0x = 0x + 0$ by (A3). So $0x + 0x = 0x + 0$, and (a) gives $0x = 0$.

(d) By the mirror form of (D), (A4) and (c), $xy + (-x)y = (x + (-x))y = 0y = 0$. By the uniqueness in (a), $(-x)y = -(xy)$. Applying this twice, with (M1) between, $(-x)(-y) = -(x(-y)) = -((-y)x) = -(-(yx)) = yx = xy$, where the last two steps use (b) and (M1). The first statement, with $1$ and $x$ in place of $x$ and $y$, gives $(-1)x = -(1x) = -x$, by (M1) and (M3). Finally, $(x - y) + (y - x) = x + ((-y) + y) + (-x) = x + 0 + (-x) = 0$ by (A1)-(A4), so $-(x - y) = y - x$ by the uniqueness in (a).

(e) Multiply both sides of $xy = xz$ on the left by $x^{-1}$: $x^{-1}(xy) = x^{-1}(xz)$. Now $x^{-1}(xy) = (x^{-1}x)y$ by (M2), $= 1y$ by (M1) and (M4), $= y$ by (M1) and (M3). In the same way $x^{-1}(xz) = z$. So $y = z$. If $xy = 1$, then $xy = x x^{-1}$, so $y = x^{-1}$. Next, $x^{-1} \ne 0$, so that $(x^{-1})^{-1}$ is defined: if $x^{-1} = 0$, then $1 = x x^{-1} = x \cdot 0 = 0 \cdot x = 0$ by (M4), (M1) and (c), against (M3). Finally $x^{-1} x = 1$ by (M1) and (M4), so $x$ is the element whose product with $x^{-1}$ is $1$, that is, $(x^{-1})^{-1} = x$.

(f) Suppose $xy = 0$ and $x \ne 0$. Then $xy = 0 = x0$ by (c) and (M1), and (e) gives $y = 0$. So $x = 0$ or $y = 0$.

(g) If $xy = 0$, then (f) gives $x = 0$ or $y = 0$, which is false. So $xy \ne 0$. By (M1) and (M2), $(xy)(x^{-1}y^{-1}) = (x x^{-1})(y y^{-1}) = 1 \cdot 1 = 1$. By the uniqueness in (e), $(xy)^{-1} = x^{-1}y^{-1}$.

(h) By (g), $bd \ne 0$ and $(bd)^{-1} = b^{-1}d^{-1}$. Then $\frac{ac}{bd} = ac\, b^{-1} d^{-1} = (a b^{-1})(c d^{-1}) = \frac{a}{b}\cdot\frac{c}{d}$, by (M1) and (M2). For the sum, by (D) and its mirror form,

$$
\frac{ad + bc}{bd} = (ad + bc)\, b^{-1} d^{-1} = a b^{-1} (d d^{-1}) + c d^{-1} (b b^{-1}) = a b^{-1} + c d^{-1} = \frac{a}{b} + \frac{c}{d},
$$

where the middle steps regroup with (M1) and (M2) and then use (M4) and (M3). ∎

We cite these rules as 4.2(a), 4.2(b) and so on. From here on, a computation with $+$, $-$, $\cdot$ and $/$ uses only the field axioms and these rules, and each step of it is one of them, applied as many times as the line shows.

## 4.3 Ordered fields

**Definition.** An **ordered field** is a field $F$ with a relation $x \lt y$ ("$x$ is less than $y$") between elements of $F$, such that for all $x, y, z \in F$:

- (O1) exactly one of $x \lt y$, $x = y$, $y \lt x$ holds;
- (O2) if $x \lt y$ and $y \lt z$, then $x \lt z$;
- (O3) if $x \lt y$, then $x + z \lt y + z$;
- (O4) if $0 \lt x$ and $0 \lt y$, then $0 \lt xy$.

We write $y \gt x$ for $x \lt y$, and $x \le y$ for "$x \lt y$ or $x = y$". An element $x$ is **positive** if $x \gt 0$ and **negative** if $x \lt 0$. A statement $x \lt y \lt z$ means $x \lt y$ and $y \lt z$.

Axiom (O1) is called **trichotomy**. By (O1), "not $x \lt y$" is the same as $y \le x$. This is how a negated inequality is turned into an inequality throughout the session. The relation $\le$ is transitive: if $x \le y$ and $y \le z$, then either one of the two is an equality, and substituting it gives $x \le z$, or both are strict and (O2) gives $x \lt z$. In the same way, if $x \le y$ and $y \lt z$, or $x \lt y$ and $y \le z$, then $x \lt z$: in the case of equality substitute, and otherwise apply (O2). If $x \le y$ and $y \le x$, then $x = y$, since otherwise $x \lt y$ and $y \lt x$ would both hold, against (O1).

**Lemma (order rules).** In an ordered field, for all $x, y, z, u, v$:

- (a) $x \lt y$ if and only if $0 \lt y - x$. In particular $x \gt 0$ if and only if $-x \lt 0$, $x \lt 0$ if and only if $-x \gt 0$, and $x \lt y$ if and only if $-y \lt -x$.
- (b) If $x \lt y$ and $z \gt 0$, then $xz \lt yz$.
- (c) If $x \lt y$ and $z \lt 0$, then $xz \gt yz$.
- (d) If $x \ne 0$, then $x^2 \gt 0$. In particular $1 \gt 0$.
- (e) If $x \gt 0$, then $1/x \gt 0$. If $0 \lt x \lt y$, then $0 \lt 1/y \lt 1/x$.
- (f) If $x \lt y$ and $u \le v$, then $x + u \lt y + v$. If $x \le y$ and $u \le v$, then $x + u \le y + v$.
- (g) $0 \lt 1 \lt 2$, and $\frac12 + \frac12 = 1$. If $x \lt y$, then $x \lt \frac{x + y}{2} \lt y$.
- (h) If $0 \le x \lt y$, then $x^2 \lt y^2$.

*Proof.* (a) If $x \lt y$, add $-x$ to both sides by (O3): $x + (-x) \lt y + (-x)$, that is, $0 \lt y - x$. If $0 \lt y - x$, add $x$: $0 + x \lt (y - x) + x$, that is, $x \lt y$, by (A1)-(A4). For the second statement, add $-x$ to both sides of $0 \lt x$ by (O3): $0 + (-x) \lt x + (-x)$, that is, $-x \lt 0$. Conversely, add $x$ to both sides of $-x \lt 0$: $(-x) + x \lt 0 + x$, that is, $0 \lt x$. With $y = 0$ the first statement reads: $x \lt 0$ if and only if $0 \lt 0 - x = -x$, by (A1) and (A3). Finally, $-y \lt -x$ holds if and only if $0 \lt -x - (-y) = y - x$, by the first statement and 4.2(b), and that holds if and only if $x \lt y$.

(b) By (a), $y - x \gt 0$. By (O4), $(y - x)z \gt 0$. By the mirror form of (D) and 4.2(d), $(y - x)z = yz + (-x)z = yz - xz$. So $yz - xz \gt 0$, and (a) gives $xz \lt yz$.

(c) By (a), $-z \gt 0$, since $z \lt 0$. By (b), $x(-z) \lt y(-z)$. By 4.2(d) and (M1), $x(-z) = -(xz)$ and $y(-z) = -(yz)$. So $-(xz) \lt -(yz)$, and the last statement of (a), with 4.2(b), gives $yz \lt xz$.

(d) If $x \gt 0$, then $x^2 = xx \gt 0$ by (O4). If $x \lt 0$, then $-x \gt 0$ by (a), and $x^2 = (-x)(-x) \gt 0$ by 4.2(d) and (O4). By (O1) these are the only cases when $x \ne 0$. Since $1 \ne 0$ by (M3) and $1 = 1 \cdot 1 = 1^2$, we get $1 \gt 0$.

(e) Let $x \gt 0$. First, $1/x = x^{-1} \ne 0$, by 4.2(e). Suppose $1/x \lt 0$. Multiplying by $x \gt 0$ with (b) gives $(1/x)x \lt 0 \cdot x$, that is, $1 \lt 0$ by (M1), (M4) and 4.2(c). This contradicts $1 \gt 0$ and (O1). So, by (O1), $1/x \gt 0$. Now let $0 \lt x \lt y$. Then $y \gt 0$ by (O2), so $1/x \gt 0$ and $1/y \gt 0$, and $(1/x)(1/y) \gt 0$ by (O4). Multiply $x \lt y$ by $(1/x)(1/y)$ with (b): $x \cdot \frac1x \cdot \frac1y \lt y \cdot \frac1x \cdot \frac1y$. Regrouping with (M1), (M2) and (M4), the left side is $\frac1y$ and the right side is $\frac1x$.

(f) By (O3), $x + u \lt y + u$. If $u = v$, this is the claim. If $u \lt v$, then (O3) and (A1) give $y + u \lt y + v$, and (O2) gives $x + u \lt y + v$. For the second statement, if $x = y$ then $x + u \le x + v = y + v$ by (O3) or equality, and if $x \lt y$ the first statement applies.

(g) By (d), $0 \lt 1$. Adding $1$ by (O3) gives $1 \lt 1 + 1 = 2$, so $0 \lt 2$ by (O2), and $2 \ne 0$. By the mirror form of (D), (M1) and (M3), $\frac12 + \frac12 = (1 + 1)\cdot\frac12 = 2 \cdot \frac12 = 1$, the last step by (M4). Now let $x \lt y$. By (O3), $x + x \lt x + y$, and $x + x = (1 + 1)x = 2x$ by the mirror form of (D) and (M3). By (e), $\frac12 \gt 0$, so (b) gives $\frac12 \cdot 2x \lt \frac12 (x + y)$, that is, $x \lt \frac{x + y}{2}$. In the same way, adding $y$ to $x \lt y$ gives $x + y \lt 2y$, and multiplying by $\frac12$ gives $\frac{x + y}{2} \lt y$.

(h) If $x = 0$, then $x^2 = 0 \cdot 0 = 0$ by 4.2(c), and $0 \lt y^2$ by (d), since $y \gt 0$. If $x \gt 0$, then (b) with $z = x$ gives $x^2 \lt yx$, and (b) with $z = y$, which is positive by (O2), gives $xy \lt y^2$. Since $yx = xy$, (O2) gives $x^2 \lt y^2$. ∎

**Non-strict forms.** In (O3), and in (a), (b), (c), (e) and (h), if the hypothesis $x \lt y$ is weakened to $x \le y$, the conclusion holds with $\le$ in place of $\lt$ (with $\ge$ in place of $\gt$ in (c)), because the extra case $x = y$ gives equality. For (a) this uses that $x = y$ if and only if $y - x = 0$, by (A4), 4.2(a) and 4.2(b), and if and only if $-y = -x$, by 4.2(b). In particular $x \le y$ if and only if $0 \le y - x$, and if and only if $-y \le -x$. Since $0 + 0 = 0$ by (A3), the uniqueness in 4.2(a) gives $-0 = 0$; so also $x \ge 0$ if and only if $-x \le 0$, and $x \le 0$ if and only if $-x \ge 0$. In (b) the factor may also be $z = 0$: then $xz = 0 = yz$ by (M1) and 4.2(c). So $x \le y$ and $z \ge 0$ give $xz \le yz$. Taking $x = 0$, a product of two elements that are $\ge 0$ is $\ge 0$.

We cite these rules as 4.3(a), 4.3(b) and so on, the non-strict forms included. Two consequences of (g) are used constantly in later sessions: if $\varepsilon \gt 0$, then $\frac{\varepsilon}{2} \gt 0$ by (e) and (O4), and $\frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$ by (D).

## 4.4 Upper bounds and the least-upper-bound property

The rational numbers (defined in Section 4.6) also satisfy the field and order axioms, granted fact (i) of Section 4.9. The axiom that separates the real numbers from the rational numbers concerns upper bounds.

**Definition.** Let $F$ be an ordered field and $S \subseteq F$.

- An element $b \in F$ is an **upper bound** of $S$ if $x \le b$ for every $x \in S$. The set $S$ is **bounded above** if it has an upper bound.
- An element $s \in F$ is a **least upper bound**, or **supremum**, of $S$ if $s$ is an upper bound of $S$ and $s \le b$ for every upper bound $b$ of $S$.
- An element $a \in F$ is a **lower bound** of $S$ if $a \le x$ for every $x \in S$. The set $S$ is **bounded below** if it has a lower bound, and **bounded** if it is bounded above and bounded below.
- An element $m \in F$ is a **greatest lower bound**, or **infimum**, of $S$ if $m$ is a lower bound of $S$ and $a \le m$ for every lower bound $a$ of $S$.
- A **maximum** of $S$ is an element of $S$ that is an upper bound of $S$. A **minimum** of $S$ is an element of $S$ that is a lower bound of $S$.

A set has at most one least upper bound. If $s$ and $s'$ are both least upper bounds of $S$, then $s'$ is an upper bound, so $s \le s'$; and $s$ is an upper bound, so $s' \le s$. By Section 4.3, $s = s'$. The same argument shows that a set has at most one greatest lower bound, at most one maximum and at most one minimum. When they exist they are written $\sup S$, $\inf S$, $\max S$ and $\min S$.

A maximum, when it exists, is the least upper bound. If $m = \max S$, then $m$ is an upper bound; and if $b$ is any upper bound, then $m \le b$ because $m \in S$. So $\sup S = \max S$. In the same way $\inf S = \min S$ when $S$ has a minimum. The converse fails: a set can have a least upper bound that does not belong to it, and then it has no maximum. The example below shows this.

**Definition.** For $a \lt b$ in an ordered field, the **intervals** with **endpoints** $a$ and $b$ are

$$
[a, b] = \{x \in F : a \le x \le b\}, \quad (a, b) = \{x \in F : a \lt x \lt b\}, \quad [a, b) = \{x \in F : a \le x \lt b\}, \quad (a, b] = \{x \in F : a \lt x \le b\}.
$$

Each of them has **length** $b - a$.

**Example.** In an ordered field, the interval $S = [0, 1)$ has $\sup S = 1$ and has no maximum.

*Proof.* Every $x \in S$ satisfies $x \lt 1$, so $1$ is an upper bound. Let $b$ be an upper bound of $S$; we show $1 \le b$. Suppose instead $b \lt 1$. Since $0 \le 0 \lt 1$ by 4.3(d), $0 \in S$, so $0 \le b$. By 4.3(g), $b \lt \frac{b + 1}{2} \lt 1$. Then $0 \le b \lt \frac{b + 1}{2}$, so $\frac{b + 1}{2} \in S$, and $\frac{b + 1}{2} \gt b$ contradicts that $b$ is an upper bound. So $1 \le b$ for every upper bound $b$, and $\sup S = 1$. If $S$ had a maximum, it would equal $\sup S = 1$, but $1 \notin S$ because $1 \lt 1$ is false by (O1). ∎

**Definition (the least-upper-bound property).** An ordered field $F$ has the **least-upper-bound property** if every nonempty subset of $F$ that is bounded above has a least upper bound in $F$.

**Definition (the real numbers).** Fix an ordered field with the least-upper-bound property. It is called the **real numbers** and written $\mathbb{R}$, and its elements are called real numbers.

The least-upper-bound property is also called the **completeness axiom**, and $\mathbb{R}$ a **complete ordered field**. This is the form in which Rudin, *Principles of Mathematical Analysis*, Ch. 1, states the axioms. The definition says what properties $\mathbb{R}$ has; that a field with these properties exists is proved by constructing one, which this book omits (the gap at the end of the session). Every later session uses $\mathbb{R}$ only through the field axioms, the order axioms and the least-upper-bound property. So no result of the book depends on which such field is fixed.

## 4.5 Working with suprema

The definition of the least upper bound quantifies over all upper bounds. The following lemma replaces that by a test that involves only the elements of $S$, and it is the form in which the supremum is used in later sessions.

**Lemma (approximation property).** Let $S \subseteq \mathbb{R}$ be nonempty, and let $s$ be an upper bound of $S$. Then $s = \sup S$ if and only if for every $\varepsilon \gt 0$ there exists $x \in S$ with $x \gt s - \varepsilon$.

*Proof.* Suppose $s = \sup S$, and let $\varepsilon \gt 0$. Adding $s - \varepsilon$ to both sides of $0 \lt \varepsilon$ by (O3) gives $s - \varepsilon \lt (s - \varepsilon) + \varepsilon = s$, using (A1)-(A4). If $s - \varepsilon$ were an upper bound of $S$, then $s \le s - \varepsilon$, because $s$ is the least upper bound; together with $s - \varepsilon \lt s$ this contradicts (O1). So $s - \varepsilon$ is not an upper bound. By the negations of the quantifiers (Session 2, Section 2.4), there exists $x \in S$ such that $x \le s - \varepsilon$ is false, and by (O1) this means $x \gt s - \varepsilon$.

Conversely, suppose the condition holds, and let $b$ be an upper bound of $S$. We show $s \le b$. Suppose instead $b \lt s$. Then $\varepsilon = s - b \gt 0$ by 4.3(a), so there exists $x \in S$ with $x \gt s - \varepsilon = s + (b - s) = b$, by 4.2(d) and (A1)-(A4). This contradicts that $b$ is an upper bound. So $s \le b$, and $s$ is the least upper bound. ∎

For a set $S \subseteq \mathbb{R}$ write $-S = \{-x : x \in S\}$.

**Theorem (greatest lower bounds).** Every nonempty subset $S$ of $\mathbb{R}$ that is bounded below has a greatest lower bound, and

$$
\inf S = -\sup(-S).
$$

*Proof.* Let $a$ be a lower bound of $S$. Every element of $-S$ has the form $-x$ with $x \in S$, and $a \le x$ gives $-x \le -a$ by 4.3(a). So $-a$ is an upper bound of $-S$. The set $-S$ is nonempty because $S$ is. By the least-upper-bound property, $s = \sup(-S)$ exists.

We show that $-s$ is a lower bound of $S$. Let $x \in S$. Then $-x \in -S$, so $-x \le s$, and 4.3(a) with 4.2(b) gives $-s \le x$.

We show that $-s$ is the greatest lower bound. Let $c$ be any lower bound of $S$. The argument of the first paragraph, with $c$ in place of $a$, shows that $-c$ is an upper bound of $-S$. Since $s$ is the least upper bound, $s \le -c$, and 4.3(a) with 4.2(b) gives $c \le -s$. ∎

So $\mathbb{R}$ has the **greatest-lower-bound property**: every nonempty subset that is bounded below has a greatest lower bound. It is a consequence of the least-upper-bound property, not a further axiom.

## 4.6 The natural numbers inside the real numbers

The natural numbers $1$, $2 = 1 + 1$, $3 = 2 + 1$, and so on, are elements of $\mathbb{R}$. Session 3 defined the set they form, and proved its first properties, taking the rules of arithmetic and order listed in its Section 3.1 as given. Each of those rules is now an axiom, a rule proved above, or a one-line consequence. The rules of arithmetic are (A1)-(A4), (M1)-(M4) and (D), with $1/x = x^{-1}$ (Section 4.2), and 4.2(b)-(h), with (M1) for $x \cdot 0 = 0$. The rules of order are (O1)-(O3), the transitivity rules before the lemma of Section 4.3, and 4.3(a), (b), (d), (e) and (f) with their non-strict forms. Three need a line. The rule "if $y - x = 0$ then $y = x$" is in the paragraph on non-strict forms. The rule $x^2 \ge 0$ at $x = 0$ holds because $0 \cdot 0 = 0$ by 4.2(c). Finally, $-(x + y) = (-x) + (-y)$, because $(x + y) + \bigl((-x) + (-y)\bigr) = 0$ by (A1)-(A4) and the negative is unique by 4.2(a). So every result of Session 3 holds in $\mathbb{R}$.

**Recall (Session 3).** A set $S$ of real numbers is inductive if $1 \in S$, and $x + 1 \in S$ whenever $x \in S$. The set $\mathbb{N}$ of natural numbers is the set of real numbers that lie in every inductive set. Two facts proved in Session 3 are recalled here, and cited below as 4.6(a) and 4.6(b).

- (a) $\mathbb{N}$ is inductive (the lemma "$\mathbb{N}$ is inductive", Session 3, Section 3.2). In particular $1 \in \mathbb{N}$, so $\mathbb{N}$ is nonempty, and $n + 1 \in \mathbb{N}$ for every $n \in \mathbb{N}$.
- (b) $n \ge 1$ for every $n \in \mathbb{N}$ (Session 3, Section 3.3, Lemma 1). Since $1 \gt 0$ by 4.3(d), every natural number is positive.

The **integers** and **rational numbers** are the subsets

$$
\mathbb{Z} = \mathbb{N} \cup \{0\} \cup \{-n : n \in \mathbb{N}\}, \qquad \mathbb{Q} = \Bigl\{\frac{p}{q} : p \in \mathbb{Z},\ q \in \mathbb{N}\Bigr\}
$$

of $\mathbb{R}$. Each $q \in \mathbb{N}$ is positive by 4.6(b), so $q \ne 0$ by (O1), and $\frac{p}{q}$ is defined. Sums and products of natural numbers are natural numbers (Session 3, Section 3.3, Lemma 3). The corresponding facts for $\mathbb{Z}$ and $\mathbb{Q}$ are not proved in Part I; Section 4.9 states the one it assumes.

## 4.7 The Archimedean property

**Theorem (Archimedean property).** For every $x \in \mathbb{R}$ there exists $n \in \mathbb{N}$ with $n \gt x$.

*Proof.* Suppose the statement is false. By the negations of the quantifiers (Session 2, Section 2.4), there is an $x \in \mathbb{R}$ such that for every $n \in \mathbb{N}$, $n \gt x$ is false; by (O1), $n \le x$ for every $n \in \mathbb{N}$. Then $x$ is an upper bound of $\mathbb{N}$. The set $\mathbb{N}$ is nonempty by 4.6(a). By the least-upper-bound property, $s = \sup \mathbb{N}$ exists.

Apply the approximation property (Section 4.5) with $\varepsilon = 1$, which is positive by 4.3(d). There exists $n \in \mathbb{N}$ with $n \gt s - 1$. Adding $1$ by (O3) gives $n + 1 \gt s$. But $n + 1 \in \mathbb{N}$ by 4.6(a), and $s$ is an upper bound of $\mathbb{N}$, so $n + 1 \le s$. This contradicts (O1). So the statement is true. ∎

The property is named after Archimedes, who assumed it for magnitudes such as lengths in *On the Sphere and Cylinder*, Book I; the name "Archimedean axiom" is due to O. Stolz, *Mathematische Annalen* 22, 504-519 (1883). In this book it is a theorem: it follows from the least-upper-bound property.

**Corollary.**

- (a) For every $\varepsilon \gt 0$ there exists $n \in \mathbb{N}$ with $\frac1n \lt \varepsilon$.
- (b) For every $x \gt 0$ and every $y \in \mathbb{R}$ there exists $n \in \mathbb{N}$ with $nx \gt y$.
- (c) If $a \in \mathbb{R}$ satisfies $a \le \frac1n$ for every $n \in \mathbb{N}$, then $a \le 0$.

*Proof.* (a) By 4.3(e), $\frac1\varepsilon \gt 0$. By the Archimedean property there exists $n \in \mathbb{N}$ with $n \gt \frac1\varepsilon$. Then $0 \lt \frac1\varepsilon \lt n$, and 4.3(e) gives $\frac1n \lt \frac{1}{1/\varepsilon} = \varepsilon$, the last step by 4.2(e).

(b) By the Archimedean property there exists $n \in \mathbb{N}$ with $n \gt \frac{y}{x}$. Multiplying by $x \gt 0$ with 4.3(b) gives $nx \gt \frac{y}{x} \cdot x = y \cdot x^{-1} x = y$, by (M2), (M1), (M4) and (M3).

(c) Suppose $a \gt 0$. By (a) with $\varepsilon = a$ there exists $n \in \mathbb{N}$ with $\frac1n \lt a$, which contradicts $a \le \frac1n$ by (O1). So $a \le 0$ by (O1). ∎

**Example.** Let $S = \{\frac1n : n \in \mathbb{N}\}$. Then $\inf S = 0$, and $S$ has no minimum.

*Proof.* Each $n \in \mathbb{N}$ is positive by 4.6(b), so $\frac1n \gt 0$ by 4.3(e). So $0$ is a lower bound of $S$. Let $c$ be any lower bound of $S$. Then $c \le \frac1n$ for every $n \in \mathbb{N}$, and Corollary (c) gives $c \le 0$. So $0$ is a lower bound that is greater than or equal to every lower bound, that is, $\inf S = 0$. If $S$ had a minimum, it would equal $\inf S = 0$; but $0 \notin S$, since every element of $S$ is positive. ∎

## 4.8 Worked example: a real number whose square is 2

The least-upper-bound property produces numbers that the field and order axioms alone do not. This example uses it to produce a positive real number $s$ with $s^2 = 2$.

One identity is used twice. For all real $a$ and $b$,

$$
(a + b)^2 = (a + b)a + (a + b)b = a^2 + ba + ab + b^2 = a^2 + ab + ab + b^2 = a^2 + 2ab + b^2,
$$

by (D), the mirror form of (D), (M1), and $ab + ab = (1 + 1)ab = 2ab$. With $-b$ in place of $b$, and $2a(-b) = -2ab$ and $(-b)^2 = b^2$ by 4.2(d), it gives $(a - b)^2 = a^2 - 2ab + b^2$.

Let

$$
S = \{x \in \mathbb{R} : x \ge 0 \text{ and } x^2 \lt 2\}.
$$

**Step 1: $S$ is nonempty.** By 4.3(d), $1 \ge 0$, and $1^2 = 1 \lt 2$ by 4.3(g). So $1 \in S$.

**Step 2: $2$ is an upper bound of $S$.** First, $2 \cdot 2 = 2(1 + 1) = 2 + 2$ by (D) and (M3), and $2 + 2 = 2 + 1 + 1 = 3 + 1 = 4$. Since $0 \lt 2$, (O3) gives $2 = 0 + 2 \lt 2 + 2 = 4$. Now let $x \in S$, and suppose $x \ge 2$. Then $0 \le 2 \le x$, and 4.3(h), in its $\le$ form, gives $4 = 2^2 \le x^2$. So $x^2 \ge 4 \gt 2$, which contradicts $x^2 \lt 2$ by (O1). So $x \lt 2$ for every $x \in S$.

**Step 3: the supremum.** By Steps 1 and 2 and the least-upper-bound property, $s = \sup S$ exists. Since $1 \in S$, $1 \le s$; since $0 \lt 1$ by 4.3(d), $s \gt 0$. This is the only step that uses the least-upper-bound property.

**Step 4: $s^2 \lt 2$ is impossible.** Suppose $s^2 \lt 2$, and let $d = 2 - s^2$, which is positive by 4.3(a). We find $h \gt 0$ with $s + h \in S$.

- From $0 \le 1 \le s$, 4.3(h) gives $1 \le s^2$. Then $-s^2 \le -1$ by 4.3(a), and adding $2$ by (O3) gives $d = 2 - s^2 \le 2 - 1 = 1$, the last step by (A2)-(A4) since $2 = 1 + 1$.
- By 4.3(g) and Step 3, $2 \gt 0$ and $s \gt 0$, so $2s \gt 0$ by (O4). Adding $1$ to $0 \lt 2s$ by (O3) gives $1 \lt 2s + 1$, using (A1) and (A3). With $d \le 1$, this gives $d \lt 2s + 1$. Since $d \gt 0$, (O2) gives $2s + 1 \gt 0$.
- Let $h = \frac{d}{2s + 1}$. It is positive by 4.3(e) and (O4). Multiplying $d \lt 2s + 1$ by $\frac{1}{2s + 1} \gt 0$ gives $h \lt 1$. Multiplying $h \lt 1$ by $h \gt 0$ gives $h^2 \lt h$.

Then, by the identity, 4.3(f), (D) and the definition of $h$,

$$
(s + h)^2 = s^2 + 2sh + h^2 \lt s^2 + 2sh + h = s^2 + (2s + 1)h = s^2 + d = 2.
$$

Also $s + h \gt s \gt 0$ by (O3). So $s + h \in S$ and $s + h \gt s$, which contradicts that $s$ is an upper bound of $S$.

**Step 5: $s^2 \gt 2$ is impossible.** Suppose $s^2 \gt 2$. Let $h = \frac{s^2 - 2}{2s}$. Here $s^2 - 2 \gt 0$ by 4.3(a) and $2s \gt 0$ by (O4), so $h \gt 0$ by 4.3(e) and (O4), and $2sh = s^2 - 2$.

- $s - h$ is positive. By (D) and 4.2(d), $2s(s - h) = 2s^2 - 2sh = 2s^2 - (s^2 - 2) = 2s^2 + (2 - s^2)$. By the mirror form of (D) and (M3), $2s^2 = (1 + 1)s^2 = s^2 + s^2$, so by (A1)-(A4) this is $s^2 + 2$. It is positive: $s^2 \gt 0$ by 4.3(d) and $2 \gt 0$ by 4.3(g), so $s^2 + 2 \gt 0 + 0 = 0$ by 4.3(f) and (A3). If $s - h \le 0$, then 4.3(b), in its $\le$ form with $z = 2s \gt 0$, would give $2s(s - h) \le 0$. So $s - h \gt 0$ by (O1).
- $(s - h)^2 \gt 2$. By the identity, $(s - h)^2 = s^2 - 2sh + h^2 = s^2 + (2 - s^2) + h^2 = 2 + h^2$, by 4.2(d) and (A1)-(A4), and $h^2 \gt 0$ by 4.3(d), so $(s - h)^2 \gt 2$ by (O3).
- $s - h$ is an upper bound of $S$. Let $x \in S$, and suppose $x \gt s - h$. Then $0 \lt s - h \lt x$, and 4.3(h) gives $(s - h)^2 \lt x^2$, so $x^2 \gt 2$ by (O2), which contradicts $x \in S$. So $x \le s - h$ for every $x \in S$.

Since $s$ is the least upper bound, $s \le s - h$. But $-h \lt 0$ by 4.3(a), and adding $s$ by (O3) gives $s - h \lt s$, using (A1) and (A3). This contradicts (O1).

**Step 6: conclusion.** By (O1) and Steps 4 and 5, $s^2 = 2$. So $s$ is a positive real number whose square is $2$. It is the only one: if $t \gt 0$ and $t \ne s$, then $t \lt s$ or $s \lt t$, and 4.3(h) gives $t^2 \lt s^2 = 2$ or $t^2 \gt 2$, so $t^2 \ne 2$. This number is written $\sqrt2$.

## 4.9 What fails without each hypothesis

The least-upper-bound property has two hypotheses on the set, and, granted two facts of integer arithmetic, the axiom itself is not a consequence of the others.

**A nonempty set.** Every real number $b$ is an upper bound of $\emptyset$. The statement "for every $x \in \emptyset$, $x \le b$" has the negation "there exists $x \in \emptyset$ with $x \gt b$" (Session 2), which is false because $\emptyset$ has no elements; so the statement is true. If $\emptyset$ had a least upper bound $s$, then $s - 1$ would be an upper bound too, so $s \le s - 1$; but $-1 \lt 0$ by 4.3(d) and 4.3(a), and adding $s$ by (O3) gives $s - 1 \lt s$. So $\emptyset$ is bounded above and has no least upper bound.

**A set bounded above.** The set $\mathbb{N}$ is nonempty and has no least upper bound, because by the Archimedean property it has no upper bound at all, and a least upper bound is an upper bound.

**The axiom itself.** Assume two facts proved from integer arithmetic: (i) sums, differences, products and quotients (by nonzero elements) of rational numbers are rational, so that $\mathbb{Q}$ with the operations and order of $\mathbb{R}$ is an ordered field; (ii) no rational number has square $2$. Let $S_{\mathbb{Q}} = \{x \in \mathbb{Q} : x \ge 0 \text{ and } x^2 \lt 2\}$. Steps 1 and 2 of Section 4.8 hold in $\mathbb{Q}$, since $1 = \frac11$ and $2 = \frac21$ are rational, by 4.6(a) and because $1^{-1} = 1$ by (M3) and 4.2(e): $S_{\mathbb{Q}}$ is nonempty and bounded above in $\mathbb{Q}$. Suppose $S_{\mathbb{Q}}$ had a least upper bound $s$ in $\mathbb{Q}$. Then $1 \le s$, as in Step 3, and Steps 4 to 6 run unchanged in $\mathbb{Q}$: they use only the field and order axioms and the fact that $s$ is a least upper bound, and the numbers $h$, $s + h$ and $s - h$ they form are rational by (i). They give $s^2 = 2$, against (ii). So $\mathbb{Q}$ is an ordered field without the least-upper-bound property, and the property is not a consequence of the field and order axioms. Exercise 8 gives a second proof, with an explicit construction.

> **Gap.** Omitted: the construction of R from Q (by Dedekind cuts or Cauchy sequences) and the proof that it satisfies the axioms. Why: it is long, and nothing later depends on the construction, only on the axioms. Where: W. Rudin, Principles of Mathematical Analysis, 3rd ed., Ch. 1 appendix.

## Exercises

*Check*

1. Let $S = \{1 - \frac1n : n \in \mathbb{N}\}$. Show that $\min S = 0$, that $\sup S = 1$, and that $S$ has no maximum.
2. Let $S = \{x \in \mathbb{R} : x^2 \lt x\}$. Show that $S = (0, 1)$, and find $\sup S$ and $\inf S$ with proof.
3. Using only the field axioms and the rules 4.2, prove that $(x + y)(x - y) = x^2 - y^2$ for all real $x, y$, and that for $b \ne 0$ and $d \ne 0$, $\frac{a}{b} = \frac{c}{d}$ if and only if $ad = bc$.

*Prove*

4. Let $T = \{x \in \mathbb{R} : x \ge 0 \text{ and } x^2 \lt 3\}$. Rerun the argument of Section 4.8 to show that $t = \sup T$ exists and satisfies $t^2 = 3$.
5. Let $A$ and $B$ be nonempty subsets of $\mathbb{R}$ that are bounded above.
   - (a) If $A \subseteq B$, show that $\sup A \le \sup B$.
   - (b) Let $A + B = \{a + b : a \in A,\ b \in B\}$. Show that $\sup(A + B) = \sup A + \sup B$.
6. Prove the approximation property for infima: if $S \subseteq \mathbb{R}$ is nonempty and $m$ is a lower bound of $S$, then $m = \inf S$ if and only if for every $\varepsilon \gt 0$ there exists $x \in S$ with $x \lt m + \varepsilon$.
7. Let $F$ be an ordered field in which every nonempty set that is bounded below has a greatest lower bound. Prove that $F$ has the least-upper-bound property. The theorem of Section 4.5 on greatest lower bounds is proved from the field and order axioms and the least-upper-bound property alone, so it holds in any ordered field that has the least-upper-bound property; together with it, this shows that the two properties are equivalent for an ordered field.

*Extend*

8. Assume the two facts (i) and (ii) of Section 4.9. Let $A = \{p \in \mathbb{Q} : p \gt 0,\ p^2 \lt 2\}$. Show that $A$ is nonempty and has an upper bound in $\mathbb{Q}$, but that no element of $\mathbb{Q}$ is an upper bound of $A$ that is less than or equal to every upper bound of $A$ in $\mathbb{Q}$. Instead of Steps 4 to 6 of Section 4.8, construct the competing rational numbers explicitly. (Hint: for rational $p \gt 0$ consider $q = \frac{2p + 2}{p + 2}$.)

Solutions: [solutions/004-real-numbers-lub.md](../solutions/004-real-numbers-lub.md).
