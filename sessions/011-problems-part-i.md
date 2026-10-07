# Session 11. Problems for Part I

*Problems. Builds on Sessions 3, 9 and 10.*

**Claim.** These are integrated problems on induction, limits, continuity, countable sets and the mean value theorem. Each one combines results from several sessions of Part I. Nothing later depends on them, and every problem is solved in full in the solutions volume.

## 11.1 What the problems use

The problems use only the results of Sessions 2 to 10. The results most often needed are these.

- **Induction and finite sums (Session 3).** Proof by induction; the rules (S1) to (S7) for finite sums, including telescoping, (S5): $\sum_{k=1}^{n} (a_{k+1} - a_k) = a_{n+1} - a_1$; the rules (P1) to (P3) for finite products; the laws of powers, including (e): if $0 \le s \lt t$ and $k \in \mathbb{N}$, then $s^k \lt t^k$; the geometric sum $\sum_{i=0}^{m} x^i = (1 - x^{m+1})/(1 - x)$ for $x \neq 1$; the difference of powers $u^k - v^k = (u - v) \sum_{j=0}^{k-1} u^{k-1-j} v^j$ for $k \in \mathbb{N}$ (Section 3.7); the binomial theorem; Bernoulli's inequality $(1+x)^n \ge 1 + nx$ for every $x \ge -1$ and $n \ge 0$.
- **The real numbers (Session 4).** The ordered-field rules, and the Archimedean property: for every real $x$ there is $N \in \mathbb{N}$ with $N \gt x$.
- **Limits of sequences (Session 5).** The absolute value and the triangle inequality $\lvert a + b \rvert \le \lvert a \rvert + \lvert b \rvert$ (Section 5.2); $1/n \to 0$, and the lemma on tails: $a_n \to L$ if and only if $a_{n+k} \to L$ (Section 5.3); a limit is unique; a convergent sequence is bounded; limits respect sums, products, quotients (with a nonzero limit in the denominator), powers ($a_n \to a$ gives $a_n^k \to a^k$, Section 5.6) and non-strict inequalities; the squeeze rule.
- **Monotone and Cauchy sequences (Session 6).** If $(a_n)$ is nondecreasing, then $a_m \le a_n$ whenever $m \le n$, and if it is nonincreasing, then $a_m \ge a_n$ whenever $m \le n$ (comparison of terms). A nondecreasing sequence that is bounded above converges, and its limit $L$ satisfies $a_n \le L$ for every $n$ (monotone convergence). A nonincreasing sequence that is bounded below converges, and its limit $L$ satisfies $L \le a_n$ for every $n$ (corollary, nonincreasing case). A sequence converges if and only if it is Cauchy.
- **Continuity (Session 7).** A function on an interval is continuous at $x$ if and only if $f(x_n) \to f(x)$ for every sequence $x_n \to x$ in the interval; polynomials and rational functions are continuous (Section 7.4); a continuous function on $[a,b]$ attains its maximum and minimum; the intermediate value theorem; every $a \ge 0$ has a unique $a^{1/n} \ge 0$ with $(a^{1/n})^n = a$, written $\sqrt{a}$ when $n = 2$. For $u, v \ge 0$ and $k \in \mathbb{N}$, $u^k \le v^k$ implies $u \le v$ (Section 7.8). So $u^k \lt v^k$ implies $u \lt v$, since $u = v$ would give $u^k = v^k$.
- **Limits of functions (Session 8).** $\lim_{y \to x} f(y) = L$ if and only if $f(y_n) \to L$ for every sequence $y_n \to x$ with $y_n \neq x$.
- **Derivatives (Session 9).** A function differentiable at $x$ is continuous at $x$ (Lemma 1). The restriction of a function to a smaller interval keeps its continuity and its derivative at each point of that interval (Lemma 2, part 1). The sum, product and quotient rules. The function $x \mapsto x^k$ has derivative $k x^{k-1}$, and every polynomial is differentiable on $\mathbb{R}$ (Corollary 1). Rolle's theorem. The mean value theorem: if $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then $f(b) - f(a) = f'(\xi)(b - a)$ for some $\xi \in (a,b)$.
- **Countable sets (Session 10).** A set is countable if it is empty or the range of a sequence. A subset of a countable set is countable (Section 10.2), so a set that contains an uncountable subset is uncountable. The set $\mathbb{Q}$ is countable (Section 10.4). If $a \lt b$, the interval $[a,b]$ is uncountable (Section 10.5).

## 11.2 A worked problem

Problems 5 and 6 concern sequences defined by a recursion. For such a sequence there is a four-step pattern. First, bound the terms by induction. Second, show that the sequence is monotone, by an identity. Third, conclude from Session 6 that it converges. Fourth, identify the limit by passing to the limit in the recursion with the rules of Session 5. Problem 5 follows the pattern; Problem 6 shows what to do when the second step fails. In Problems 5 and 6 the formula for the next term is not defined at every number: $c/a_n$ needs $a_n \neq 0$, and $1/(2 + x_n)$ needs $x_n \neq -2$. As in Session 6, Section 6.6, give the formula the value $0$ there, so that the recursion theorem (Session 3, Section 3.5) applies; part (a) of each problem shows that this value is never used. Here is the pattern on one case.

**Problem.** Let $a_1 = 0$ and $a_{n+1} = (1 + a_n^2)/2$ for $n \ge 1$. Show that $a_n \to 1$.

*Solution.* The first terms are

$$
a_1 = 0, \qquad a_2 = \tfrac{1}{2}, \qquad a_3 = \tfrac{1}{2}\bigl(1 + \tfrac{1}{4}\bigr) = \tfrac{5}{8}, \qquad a_4 = \tfrac{1}{2}\bigl(1 + \tfrac{25}{64}\bigr) = \tfrac{89}{128}, \qquad a_5 = \tfrac{1}{2}\bigl(1 + \tfrac{7921}{16384}\bigr) = \tfrac{24305}{32768}.
$$

They increase, slowly: $a_5 = 24305/32768$ is still below $3/4 = 24576/32768$.

*Step 1: bounds.* We show $0 \le a_n \le 1$ for every $n$, by induction (Session 3). For $n = 1$, $a_1 = 0$. Suppose $0 \le a_n \le 1$. Multiplying $a_n \le 1$ by $a_n \ge 0$ gives $a_n^2 \le a_n \le 1$, and $a_n^2 \ge 0$. So $1 \le 1 + a_n^2 \le 2$, and dividing by $2$ gives $\tfrac{1}{2} \le a_{n+1} \le 1$. Since $0 \lt \tfrac{1}{2}$, this gives $0 \le a_{n+1} \le 1$, which is the statement for $n + 1$.

*Step 2: monotonicity.* For every $n$,

$$
a_{n+1} - a_n = \frac{1 + a_n^2}{2} - \frac{2 a_n}{2} = \frac{1 - 2a_n + a_n^2}{2} = \frac{(1 - a_n)^2}{2} \ge 0 .
$$

So $(a_n)$ is nondecreasing.

*Step 3: convergence.* The sequence is nondecreasing and bounded above by $1$, so it converges (Session 6). Call its limit $L$.

*Step 4: the limit.* By Session 5 (Lemma (tails), with $k = 1$), $a_{n+1} \to L$. By the product rule (Session 5), $a_n^2 \to L^2$, and by the sum rule and the product rule with a constant, $(1 + a_n^2)/2 \to (1 + L^2)/2$. The sequences $(a_{n+1})$ and $((1 + a_n^2)/2)$ are the same sequence, and a limit is unique (Session 5), so

$$
L = \frac{1 + L^2}{2}, \qquad \text{that is,} \qquad L^2 - 2L + 1 = (L - 1)^2 = 0 .
$$

If $L - 1 \neq 0$, multiplying $(L-1)^2 = 0$ by $(L-1)^{-1}$ gives $L - 1 = 0$, a contradiction. So $L = 1$. ∎

## 11.3 What fails: passing to the limit before convergence is known

Step 4 used Step 3. The equation $L = (1 + L^2)/2$ says what the limit must be *if* there is one. It does not say that there is one. The same recursion started elsewhere shows the difference.

Let $b_1 = 2$ and $b_{n+1} = (1 + b_n^2)/2$. The identity of Step 2 holds for every real starting value, so $b_{n+1} - b_n = (1 - b_n)^2/2 \ge 0$ and $(b_n)$ is nondecreasing. So $b_n \ge b_1 = 2$ for every $n$ (Session 6, comparison of terms). Since $(1 - b_n)^2 = (b_n - 1)^2$ and $b_n - 1 \ge 1 \ge 0$, (P3) of Session 3 gives $(b_n - 1)^2 \ge 1^2 = 1$ (laws of powers (f)), and

$$
b_{n+1} - b_n = \frac{(b_n - 1)^2}{2} \ge \frac{1}{2} .
$$

For $n \ge 2$, adding these inequalities for $k = 1, \dots, n-1$ ((S3) of Session 3), telescoping the left side ((S5)) and summing the constant right side (Session 3, Corollary (sums of constants)) gives $b_n - b_1 \ge (n-1)/2$; for $n = 1$ both sides are $0$. So $b_n \ge 2 + (n-1)/2$ for every $n$. Given any $M$, the Archimedean property (Session 4) gives $n \in \mathbb{N}$ with $n \gt 2M + 1$; then $(n-1)/2 \gt M$, so $\lvert b_n \rvert \ge b_n \ge 2 + (n-1)/2 \gt (n-1)/2 \gt M$. The sequence is unbounded, so it has no limit (Session 5). Yet the equation $L = (1 + L^2)/2$ still has the solution $L = 1$. Solving the equation $L = (1 + L^2)/2$ identifies a limit only after a separate argument has shown that the limit exists.

## Problems

The problems are in three tiers. The *Check* problems are short and mostly computational; the *Prove* problems combine two or three results of Part I; the *Extend* problem is optional and goes a little further. A hint names a result only where finding it is not the point of the problem.

*Check*

1. **Sums of cubes.**
   (a) Prove by induction that $\sum_{k=1}^{n} k^3 = n^2(n+1)^2/4$ for every $n \in \mathbb{N}$.
   (b) Write $\frac{1}{n^4} \sum_{k=1}^{n} k^3$ as $\frac{1}{4} + \frac{1}{2n} + \frac{1}{4n^2}$, and deduce that it tends to $\frac{1}{4}$.
   (c) Compute both sides of (a) for $n = 10$, and check the value of $\frac{1}{n^4}\sum_{k=1}^{n} k^3$ for $n = 10$ against the expression in (b).

2. **Counting the zeros of a polynomial.** Let $p(x) = x^5 - 5x + 1$. A zero of $p$ is a number $c$ with $p(c) = 0$ (Session 7, Section 7.4).
   (a) Show that $p$ has a zero in each of the intervals $(-2,-1)$, $(0,1)$ and $(1,2)$.
   (b) Find the zeros of $p'$, and deduce from Rolle's theorem that $p$ has no other zero.
   (c) Find an interval of length $1/16$ that contains the zero in $(0,1)$.

*Prove*

3. **Roots tending to one.**
   (a) Let $c \gt 0$. Show that $c^{1/n} \to 1$. Treat $c \ge 1$ first, using Bernoulli's inequality, and reduce $0 \lt c \lt 1$ to it.
   (b) Show that $n^{1/n} \to 1$. Bernoulli's inequality is not strong enough here; use the binomial theorem.

4. **An increasing sequence and a decreasing one.** Let $a_n = (1 + 1/n)^n$ and $b_n = (1 + 1/n)^{n+1}$.
   (a) Show that $(a_n)$ is nondecreasing. Write $a_{n+1}/a_n$ as $\frac{n+1}{n}\bigl(1 - \frac{1}{(n+1)^2}\bigr)^{n+1}$ and apply Bernoulli's inequality.
   (b) Show that $(b_n)$ is nonincreasing. Bernoulli's inequality gives lower bounds, so bound $b_n/b_{n+1}$ from below: write it as $\bigl(1 + \frac{1}{n(n+2)}\bigr)^{n+1}\frac{n+1}{n+2}$ and show that it is at least $1$.
   (c) Show that $(a_n)$ and $(b_n)$ converge to the same limit $L$, and that $a_m \le L \le b_m$ for every $m$. Compute $a_5$ and $b_5$ as fractions and give the interval they place $L$ in.

5. **The Babylonian square root.** Let $c \gt 0$, let $a_1 \gt 0$, and let $a_{n+1} = \frac{1}{2}\bigl(a_n + c/a_n\bigr)$ for $n \ge 1$. Write $r = \sqrt{c}$.
   (a) Show that $a_n \gt 0$ for every $n$, and that $a_{n+1} - r = (a_n - r)^2/(2a_n)$.
   (b) Show that $a_n \to r$.
   (c) Take $c = 2$ and $a_1 = 1$. Compute $a_2$, $a_3$ and $a_4$ as fractions. Show $4/3 \lt r$ by comparing squares, and then use (a) and (b) to show $0 \le a_4 - r \le 1/24576$.

6. **A sequence that converges without being monotone.** Let $x_1 = 0$ and $x_{n+1} = 1/(2 + x_n)$.
   (a) Compute $x_2, \dots, x_5$, and show that the sequence is not monotone. Show that $0 \le x_n \le \frac{1}{2}$ for every $n$.
   (b) Let $g(t) = 1/(2 + t)$. Use the mean value theorem to show $\lvert g(s) - g(t) \rvert \le \frac{1}{4}\lvert s - t \rvert$ for all $s, t \ge 0$.
   (c) Show that $\lvert x_{n+1} - x_n \rvert \le \frac{1}{2}(\frac{1}{4})^{n-1}$ for every $n$. Deduce, with the geometric sum, that $\lvert x_m - x_n \rvert \le \frac{2}{3}(\frac{1}{4})^{n-1} \le \frac{2}{3n}$ whenever $m \gt n$, and that $(x_n)$ converges.
   (d) Show that the limit is $\sqrt{2} - 1$.
   (e) What fails: show that $c_n = \sqrt{n}$ satisfies $c_{n+1} - c_n \to 0$ but does not converge. So consecutive differences that tend to zero do not make a sequence Cauchy; part (c) used the faster, geometric decay.

7. **The $k$-th root near a positive point and at zero.** Let $k \ge 2$ be an integer and $r(x) = x^{1/k}$ for $x \ge 0$.
   (a) Show that $\lvert r(x) - r(y) \rvert \le \lvert x - y \rvert / r(y)^{k-1}$ for every $x \ge 0$ and $y \gt 0$. Deduce that $r$ is continuous at every $y \gt 0$.
   (b) What fails at $0$: show that the difference quotient $(r(h) - r(0))/h$ is unbounded along $h_n = 1/n^k$, so it has no limit at $0$, and $r$ is not differentiable at $0$ (Session 9, Section 9.2).

8. **Continuous functions with few values.**
   (a) Let $a \lt b$ and let $f : [a,b] \to \mathbb{R}$ be continuous. Show that if $f(u) \neq f(v)$ for some $u, v \in [a,b]$, then $f([a,b])$ contains a closed interval $[\alpha, \beta]$ with $\alpha \lt \beta$, and so is uncountable.
   (b) Deduce that a continuous function on $[a,b]$ whose set of values is countable is constant. In particular, a continuous function on $[a,b]$ that takes only rational values is constant.
   (c) What fails: let $D = [0,1] \cup [2,3]$, which is not an interval, and let $g(x) = 0$ for $x \in [0,1]$ and $g(x) = 1$ for $x \in [2,3]$. Show that $g$ is continuous at every point of $D$, in the sense of Session 7 for a function on a set $D$, and takes exactly two values. Say which step of (a) fails.

*Extend*

9. **Sums of powers without a formula.** Let $p \in \mathbb{N}$ and $S_p(n) = \sum_{k=1}^{n} k^p$.
   (a) Use the mean value theorem to show that for $0 \le a \lt b$,
   $$
   (p+1)\, a^p (b - a) \le b^{p+1} - a^{p+1} \le (p+1)\, b^p (b - a) .
   $$
   (b) Deduce, by telescoping, that $\frac{n^{p+1}}{p+1} \le S_p(n) \le \frac{(n+1)^{p+1} - 1}{p+1}$.
   (c) Deduce that $S_p(n)/n^{p+1} \to 1/(p+1)$.
   (d) Check (b) against the formula of Problem 1 for $p = 3$, both for $n = 10$ and for every $n$.

Solutions: [solutions/011-problems-part-i.md](../solutions/011-problems-part-i.md).
