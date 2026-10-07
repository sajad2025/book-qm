# Solutions to Session 4. The real numbers and the least-upper-bound property

References such as 4.2(d) and 4.3(b) are to the field rules (Section 4.2) and order rules (Section 4.3) of Session 4. "The approximation property" is the lemma of Section 4.5, and "Corollary (a)" is part (a) of the corollary in Section 4.7.

## Check

**1.** Let $S = \{1 - \frac1n : n \in \mathbb{N}\}$.

*$0$ is the minimum.* Let $n \in \mathbb{N}$. By 4.6(b), $n \ge 1$. Note $\frac11 = 1$, since $1 \cdot 1 = 1$ and the reciprocal is unique by 4.2(e). If $n = 1$, then $\frac1n = 1$. If $n \gt 1$, then $0 \lt 1 \lt n$ and 4.3(e) gives $\frac1n \lt \frac11 = 1$. In both cases $\frac1n \le 1$, and 4.3(a), in its $\le$ form, gives $0 \le 1 - \frac1n$. So $0$ is a lower bound of $S$. Taking $n = 1$ gives $1 - 1 = 0 \in S$. So $0$ is an element of $S$ and a lower bound of $S$, that is, $\min S = 0$.

*$\sup S = 1$.* For every $n \in \mathbb{N}$, $n \gt 0$ by 4.6(b), so $\frac1n \gt 0$ by 4.3(e), so $-\frac1n \lt 0$ by 4.3(a), and adding $1$ by (O3) gives $1 - \frac1n \lt 1$. So $1$ is an upper bound of $S$. Let $\varepsilon \gt 0$. By Corollary (a) there exists $n \in \mathbb{N}$ with $\frac1n \lt \varepsilon$. By 4.3(a), $-\varepsilon \lt -\frac1n$, and adding $1$ by (O3) gives $1 - \varepsilon \lt 1 - \frac1n$. So the element $1 - \frac1n$ of $S$ exceeds $1 - \varepsilon$. The set $S$ is nonempty, so the approximation property gives $\sup S = 1$.

*No maximum.* A maximum would equal $\sup S = 1$ (Section 4.4), so it would give some $n$ with $1 - \frac1n = 1$. Adding $\frac1n - 1$ to both sides gives $0 = \frac1n$, which contradicts $\frac1n \gt 0$. So $S$ has no maximum.

**2.** Let $S = \{x \in \mathbb{R} : x^2 \lt x\}$. By (D) and 4.2(d), $x(x - 1) = x^2 - x$, and, adding $-x$ to both sides by (O3), and $x$ for the converse, $x^2 \lt x$ holds if and only if $x^2 - x \lt 0$, using (A1)-(A4). So $x \in S$ if and only if $x(x - 1) \lt 0$.

*$(0, 1) \subseteq S$.* Let $0 \lt x \lt 1$. Adding $-1$ to both sides of $x \lt 1$ by (O3) gives $x - 1 \lt 0$, using (A4). Multiplying by $x \gt 0$ with 4.3(b) gives $(x - 1)x \lt 0 \cdot x = 0$, using 4.2(c) and (M1). So $x(x - 1) \lt 0$ and $x \in S$.

*$S \subseteq (0, 1)$.* Let $x \in S$. By (O1), $x \lt 0$, $x = 0$ or $x \gt 0$.
- If $x \lt 0$: adding $x$ to $-1 \lt 0$ (which holds by 4.3(a) and 4.3(d)) gives $x - 1 \lt x$, so $x - 1 \lt 0$ by (O2). Then $-x \gt 0$ and $-(x - 1) \gt 0$ by 4.3(a), and $x(x - 1) = (-x)(-(x - 1)) \gt 0$ by 4.2(d) and (O4). This contradicts $x(x - 1) \lt 0$.
- If $x = 0$: $x(x - 1) = 0$ by 4.2(c), and $0 \lt 0$ is false by (O1). This contradicts $x \in S$.

So $x \gt 0$. Suppose $x \ge 1$. Then $x - 1 \ge 0$ by 4.3(a). If $x - 1 = 0$, then $x(x - 1) = 0$ by 4.2(c); if $x - 1 \gt 0$, then $x(x - 1) \gt 0$ by (O4). Either way $x(x - 1) \lt 0$ fails. So $x \lt 1$, and $x \in (0, 1)$. Hence $S = (0, 1)$.

*A point of $S$.* By 4.3(g) applied to $0 \lt 1$, $0 \lt \frac{0 + 1}{2} = \frac12 \lt 1$, so $\frac12 \in S$.

*$\sup S = 1$.* Every $x \in S$ satisfies $x \lt 1$, so $1$ is an upper bound. Let $b$ be an upper bound, and suppose $b \lt 1$. Since $\frac12 \in S$, $b \ge \frac12 \gt 0$. By 4.3(g), $b \lt \frac{b + 1}{2} \lt 1$, and $\frac{b + 1}{2} \gt b \gt 0$, so $\frac{b + 1}{2} \in S$. It exceeds the upper bound $b$, a contradiction. So $1 \le b$ for every upper bound $b$, and $\sup S = 1$.

*$\inf S = 0$.* Every $x \in S$ satisfies $x \gt 0$, so $0$ is a lower bound. Let $c$ be a lower bound, and suppose $c \gt 0$. Since $\frac12 \in S$, $c \le \frac12 \lt 1$. By 4.3(g) applied to $0 \lt c$, $0 \lt \frac{c}{2} \lt c$. Then $0 \lt \frac{c}{2} \lt 1$, by (O2) through $c \lt 1$, so $\frac{c}{2} \in S$, and $\frac{c}{2} \lt c$ contradicts that $c$ is a lower bound. So $c \le 0$ for every lower bound $c$, and $\inf S = 0$.

Neither bound belongs to $S$, so $S$ has neither a maximum nor a minimum.

**3.** *The difference of squares.* Each step names its rule:

$$
\begin{aligned}
(x + y)(x - y) &= (x + y)x + (x + y)(-y) && \text{(D)} \\
&= x^2 + yx + x(-y) + y(-y) && \text{mirror form of (D)} \\
&= x^2 + xy + (-(xy)) + (-(y^2)) && \text{(M1), 4.2(d)} \\
&= x^2 + 0 - y^2 && \text{(A4)} \\
&= x^2 - y^2 && \text{(A3)}.
\end{aligned}
$$

The regrouping of the four terms in the second and fourth lines uses (A1) and (A2).

*Equality of fractions.* Let $b \ne 0$ and $d \ne 0$. By (M1), (M2), (M4) and (M3),

$$
\frac{a}{b}\,(bd) = a\,(b^{-1} b)\,d = ad, \qquad \frac{c}{d}\,(bd) = c\,(d^{-1} d)\,b = bc.
$$

If $\frac{a}{b} = \frac{c}{d}$, multiplying both sides by $bd$ and using these two lines gives $ad = bc$. Conversely, suppose $ad = bc$. Multiply both sides by $b^{-1} d^{-1}$. The left side becomes $a (b^{-1}) (d d^{-1}) = \frac{a}{b}$, and the right side becomes $c (d^{-1}) (b b^{-1}) = \frac{c}{d}$, by (M1), (M2), (M4) and (M3). So $\frac{a}{b} = \frac{c}{d}$.

## Prove

**4.** Let $T = \{x \in \mathbb{R} : x \ge 0 \text{ and } x^2 \lt 3\}$. The identities $(a + b)^2 = a^2 + 2ab + b^2$ and $(a - b)^2 = a^2 - 2ab + b^2$ are those of Section 4.8. Recall $2 = 1 + 1$, $3 = 2 + 1$, $4 = 3 + 1$; by (O3) applied to $0 \lt 1$, $1 \lt 2 \lt 3 \lt 4$.

*Step 1: $T$ is nonempty.* $1 \ge 0$, and $1^2 = 1 \lt 3$. So $1 \in T$.

*Step 2: $2$ is an upper bound.* Let $x \in T$ and suppose $x \ge 2$. Then $0 \le 2 \le x$, and 4.3(h) in its $\le$ form gives $x^2 \ge 2^2 = 4$ (computed in Section 4.8). Since $4 \gt 3$, $x^2 \gt 3$, which contradicts $x \in T$. So $x \lt 2$.

*Step 3: the supremum.* By Steps 1 and 2 and the least-upper-bound property, $t = \sup T$ exists. Since $1 \in T$, $t \ge 1 \gt 0$.

*Step 4: $t^2 \lt 3$ is impossible.* Suppose $t^2 \lt 3$ and let $d = 3 - t^2 \gt 0$. From $0 \le 1 \le t$, 4.3(h) gives $t^2 \ge 1$, so $-t^2 \le -1$ by 4.3(a) and $d \le 3 - 1 = 2$ by (O3), since $3 = 2 + 1$ and (A2)-(A4). From $1 \le t$, 4.3(b) with the positive factor $2$ gives $2 \le 2t$, using (M1) and (M3). Adding $2t$ to $0 \lt 1$ by (O3) gives $2t \lt 2t + 1$, using (A1) and (A3). So $d \le 2 \le 2t \lt 2t + 1$, and $d \lt 2t + 1$ by the transitivity rules of Section 4.3. Since $d \gt 0$, (O2) gives $2t + 1 \gt 0$. Let $h = \frac{d}{2t + 1}$. Then $h \gt 0$ by 4.3(e) and (O4); multiplying $d \lt 2t + 1$ by $\frac{1}{2t + 1} \gt 0$ gives $h \lt 1$; and multiplying $h \lt 1$ by $h \gt 0$ gives $h^2 \lt h$. Hence

$$
(t + h)^2 = t^2 + 2th + h^2 \lt t^2 + 2th + h = t^2 + (2t + 1)h = t^2 + d = 3.
$$

Since $t + h \gt t \gt 0$, $t + h \in T$, and $t + h \gt t$ contradicts that $t$ is an upper bound of $T$.

*Step 5: $t^2 \gt 3$ is impossible.* Suppose $t^2 \gt 3$ and let $h = \frac{t^2 - 3}{2t}$. Then $t^2 - 3 \gt 0$ by 4.3(a) and $2t \gt 0$ by (O4), so $h \gt 0$ by 4.3(e) and (O4), and $2th = t^2 - 3$. By (D) and 4.2(d), $2t(t - h) = 2t^2 - 2th = 2t^2 - (t^2 - 3) = 2t^2 + (3 - t^2)$, and $2t^2 = t^2 + t^2$ by the mirror form of (D) and (M3), so by (A1)-(A4) this is $t^2 + 3$. Since $t^2 \gt 0$ by 4.3(d) and $3 \gt 0$ (from $0 \lt 1 \lt 3$ and (O2)), 4.3(f) and (A3) give $t^2 + 3 \gt 0$. If $t - h \le 0$, then 4.3(b) with the positive factor $2t$ would give $2t(t - h) \le 0$, so $t - h \gt 0$. Next, $(t - h)^2 = t^2 - 2th + h^2 = t^2 + (3 - t^2) + h^2 = 3 + h^2$ by 4.2(d) and (A1)-(A4), and $3 + h^2 \gt 3 + 0 = 3$ by (O3) and (A3), since $h^2 \gt 0$ by 4.3(d). Now let $x \in T$ and suppose $x \gt t - h$. Then $0 \lt t - h \lt x$, so $x^2 \gt (t - h)^2 \gt 3$ by 4.3(h) and (O2), which contradicts $x \in T$. So $t - h$ is an upper bound of $T$, and $t \le t - h$ because $t$ is the least upper bound. But $-h \lt 0$ by 4.3(a), and adding $t$ by (O3) gives $t - h \lt t$, using (A1) and (A3). This contradicts (O1).

*Step 6.* By (O1), $t^2 = 3$.

**5.** *(a)* Both suprema exist by the least-upper-bound property. Let $a \in A$. Then $a \in B$, so $a \le \sup B$, because $\sup B$ is an upper bound of $B$. So $\sup B$ is an upper bound of $A$, and $\sup A \le \sup B$ because $\sup A$ is the least upper bound of $A$.

*(b)* Let $\alpha = \sup A$ and $\beta = \sup B$. The set $A + B$ is nonempty: if $a \in A$ and $b \in B$, then $a + b \in A + B$.

*Upper bound.* Every element of $A + B$ is $a + b$ with $a \in A$ and $b \in B$. Then $a \le \alpha$ and $b \le \beta$, and 4.3(f) gives $a + b \le \alpha + \beta$.

*Approximation.* Let $\varepsilon \gt 0$. Then $\frac{\varepsilon}{2} \gt 0$ (Section 4.3). By the approximation property for $A$, there is $a \in A$ with $a \gt \alpha - \frac{\varepsilon}{2}$, and for $B$, there is $b \in B$ with $b \gt \beta - \frac{\varepsilon}{2}$. By 4.3(f),

$$
a + b \gt \Bigl(\alpha - \frac{\varepsilon}{2}\Bigr) + \Bigl(\beta - \frac{\varepsilon}{2}\Bigr) = \alpha + \beta - \Bigl(\frac{\varepsilon}{2} + \frac{\varepsilon}{2}\Bigr) = \alpha + \beta - \varepsilon,
$$

using $\frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$ (Section 4.3) and $-(u + v) = (-u) + (-v)$ (Section 4.6) to collect the negatives. So the element $a + b$ of $A + B$ exceeds $(\alpha + \beta) - \varepsilon$. By the approximation property, $\sup(A + B) = \alpha + \beta$.

**6.** Let $S$ be nonempty and $m$ a lower bound of $S$.

Suppose $m = \inf S$, and let $\varepsilon \gt 0$. Adding $m$ to both sides of $0 \lt \varepsilon$ by (O3) gives $0 + m \lt \varepsilon + m$, that is, $m \lt m + \varepsilon$ by (A1) and (A3). If $m + \varepsilon$ were a lower bound of $S$, then $m + \varepsilon \le m$, because $m$ is the greatest lower bound; together with $m \lt m + \varepsilon$ this contradicts (O1). So $m + \varepsilon$ is not a lower bound. By the negations of the quantifiers (Session 2, Section 2.4), there exists $x \in S$ for which $m + \varepsilon \le x$ is false, and by (O1) this means $x \lt m + \varepsilon$.

Conversely, suppose the condition holds, and let $a$ be a lower bound of $S$. Suppose $a \gt m$. Then $\varepsilon = a - m \gt 0$ by 4.3(a), so there is $x \in S$ with $x \lt m + \varepsilon = m + (a - m) = a$, by (A1)-(A4). This contradicts that $a$ is a lower bound. So $a \le m$ by (O1), and $m$ is the greatest lower bound.

**7.** Let $F$ be an ordered field in which every nonempty set bounded below has a greatest lower bound. The rules 4.2 and 4.3 were proved from the field and order axioms alone, so they hold in $F$. Let $S \subseteq F$ be nonempty and bounded above, with upper bound $b$, and let $-S = \{-x : x \in S\}$.

*$-S$ is nonempty and bounded below.* It is nonempty because $S$ is. Every element of $-S$ is $-x$ with $x \in S$; then $x \le b$, so $-b \le -x$ by 4.3(a). So $-b$ is a lower bound of $-S$.

By the hypothesis on $F$, $m = \inf(-S)$ exists. We show that $-m = \sup S$.

*Upper bound.* Let $x \in S$. Then $-x \in -S$, so $m \le -x$, and 4.3(a) with 4.2(b) gives $x \le -m$.

*Least.* Let $c$ be an upper bound of $S$. The argument above, with $c$ in place of $b$, shows that $-c$ is a lower bound of $-S$. Since $m$ is the greatest lower bound, $-c \le m$, and 4.3(a) with 4.2(b) gives $-m \le c$.

So $S$ has the least upper bound $-m$, and $F$ has the least-upper-bound property. The theorem of Section 4.5 proves the reverse implication, and its proof uses only the field and order axioms and the least-upper-bound property, so it holds in any ordered field that has the least-upper-bound property. The two properties are therefore equivalent for an ordered field.

## Extend

**8.** Throughout, (i) and (ii) are the facts of Section 4.9. Three rules are used.

- *Sign rules.* If $u \gt 0$ and $v \gt 0$, then $\frac{u}{v} \gt 0$, by 4.3(e) and (O4). If $u \lt 0$ and $v \gt 0$, then $\frac{u}{v} \lt 0$, by 4.3(e) and 4.3(b) applied to $u \lt 0$ with the positive factor $\frac1v$, together with 4.2(c).
- *Same denominator.* If $b \ne 0$, then $\frac{u}{b} - \frac{v}{b} = u b^{-1} + (-v) b^{-1} = (u - v) b^{-1}$, by 4.2(d) and the mirror form of (D).
- *Numerals.* By Step 2 of Section 4.8, $2 \cdot 2 = 2 + 2 = 4$. Also $4 + 4 = 8$, a computation with numerals as in Session 3, Section 3.2. Then $2 \cdot 4 = 4 \cdot 2 = 4(1 + 1) = 4 + 4 = 8$, by (M1), (D) and (M3).

*$A$ is nonempty and bounded above in $\mathbb{Q}$.* The numbers $1 = \frac11$ and $2 = \frac21$ are rational, as in Section 4.9. Since $1 \gt 0$ by 4.3(d) and $1^2 = 1 \lt 2$ by 4.3(g), $1 \in A$. If $p \in A$ and $p \ge 2$, then $p^2 \ge 4 \gt 2$ as in Step 2 of Section 4.8, which contradicts $p^2 \lt 2$; so $p \lt 2$ for every $p \in A$, and $2$ is a rational upper bound of $A$.

*The construction.* Let $p \in \mathbb{Q}$ with $p \gt 0$, and let

$$
q = \frac{2p + 2}{p + 2}.
$$

Adding $2$ to $0 \lt p$ by (O3) gives $2 \lt p + 2$, using (A1) and (A3); with $0 \lt 2$ from 4.3(g), (O2) gives $p + 2 \gt 0$. So the denominator is nonzero, and $q \in \mathbb{Q}$ by (i). Also $2p \gt 0$ by (O4), so $2p + 2 \gt 0$ by 4.3(f) and (A3), and $q \gt 0$ by the first sign rule. Two identities hold.

First, $p = p(p + 2)(p + 2)^{-1} = \frac{p^2 + 2p}{p + 2}$, by (M2), (M4), (M3), (D) and (M1). By the same-denominator rule,

$$
q - p = \frac{(2p + 2) - (p^2 + 2p)}{p + 2} = \frac{2 - p^2}{p + 2},
$$

where $-(p^2 + 2p) = (-1)(p^2 + 2p) = -p^2 - 2p$ by 4.2(d) and (D), and the terms $2p$ cancel by (A1)-(A4).

Second, $q^2 = \frac{(2p + 2)^2}{(p + 2)^2}$ by 4.2(h), and $2 = 2 (p + 2)^2 \bigl((p + 2)^2\bigr)^{-1} = \frac{2(p + 2)^2}{(p + 2)^2}$ by (M2), (M4) and (M3), where $(p + 2)^2 \ne 0$ by 4.2(g). By the identity of Section 4.8, with (M1), (M2) and the numerals,

$$
(2p + 2)^2 = (2p)^2 + 2(2p)2 + 2^2 = 4p^2 + 8p + 4, \qquad (p + 2)^2 = p^2 + 2p2 + 2^2 = p^2 + 4p + 4,
$$

and so $2(p + 2)^2 = 2p^2 + 8p + 8$ by (D). By the same-denominator rule,

$$
q^2 - 2 = \frac{(4p^2 + 8p + 4) - (2p^2 + 8p + 8)}{(p + 2)^2} = \frac{2p^2 - 4}{(p + 2)^2} = \frac{2(p^2 - 2)}{(p + 2)^2}.
$$

In the numerator, the negative of the bracket is $-2p^2 - 8p - 8$ by 4.2(d) and (D). The terms $8p$ cancel by (A1)-(A4). Also $4p^2 - 2p^2 = (2 + 2)p^2 - 2p^2 = 2p^2$ and $4 - 8 = 4 - (4 + 4) = -4$, by the mirror form of (D), 4.2(d) and (A1)-(A4). Finally $2p^2 - 4 = 2p^2 - 2 \cdot 2 = 2(p^2 - 2)$ by (D) and 4.2(d).

The denominators $p + 2$ and $(p + 2)^2$ are positive, by the above and 4.3(d). Now compare $p^2$ with $2$.

- If $p^2 \lt 2$: then $2 - p^2 \gt 0$ by 4.3(a), so $q - p \gt 0$ by the first sign rule, and $q \gt p$ by 4.3(a). Also $p^2 - 2 \lt 0$ by 4.3(a), so $2(p^2 - 2) \lt 2 \cdot 0 = 0$ by 4.3(b) with the positive factor $2$, (M1) and 4.2(c). So $q^2 - 2 \lt 0$ by the second sign rule, and $q^2 \lt 2$ by 4.3(a).
- If $p^2 \gt 2$: then $p^2 - 2 \gt 0$ by 4.3(a), so $2(p^2 - 2) \gt 0$ by (O4), $q^2 - 2 \gt 0$ by the first sign rule, and $q^2 \gt 2$ by 4.3(a). Also $2 - p^2 = -(p^2 - 2) \lt 0$ by 4.2(d) and 4.3(a), so $q - p \lt 0$ by the second sign rule. Then $p - q = -(q - p) \gt 0$ by 4.2(d) and 4.3(a), and $q \lt p$ by 4.3(a).

*No least upper bound in $\mathbb{Q}$.* Suppose $b \in \mathbb{Q}$ is an upper bound of $A$ with $b \le c$ for every rational upper bound $c$ of $A$. Since $1 \in A$, $1 \le b$, and $b \gt 0$ because $0 \lt 1$. By (ii), $b^2 \ne 2$, so by (O1) either $b^2 \lt 2$ or $b^2 \gt 2$. Let $q$ be the number constructed from $p = b$.

- If $b^2 \lt 2$: then $q \in \mathbb{Q}$, $q \gt 0$ and $q^2 \lt 2$, so $q \in A$. But $q \gt b$, which contradicts that $b$ is an upper bound of $A$.
- If $b^2 \gt 2$: then $q \in \mathbb{Q}$, $q \gt 0$ and $q^2 \gt 2$. We show $q$ is an upper bound of $A$. If $x \in A$ and $x \gt q$, then $0 \lt q \lt x$, so $x^2 \gt q^2 \gt 2$ by 4.3(h) and (O2), which contradicts $x \in A$. So $x \le q$ for every $x \in A$. Then $q$ is a rational upper bound with $q \lt b$, which contradicts $b \le q$.

Both cases are impossible, so $A$ has no least upper bound in $\mathbb{Q}$. Under (i) and (ii), $\mathbb{Q}$ is an ordered field without the least-upper-bound property.
