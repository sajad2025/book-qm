# Solutions to Session 1. What this book builds, and the three questions it is aimed at

## Check

**1.** The list has three terms, so there are two comparisons to make: the second term with the first, and the third with the second.

Under meaning A, the first comparison asks whether $2 \gt 2$. It does not hold, because the two numbers are equal. One failed comparison is enough: the list is not increasing under meaning A.

Under meaning B, the first comparison asks whether $2 \ge 2$. It holds, because $2 = 2$. The second comparison is again $2 \ge 2$, and it holds for the same reason. Both comparisons hold, so the list is increasing under meaning B.

The two meanings give different answers, so the question has no answer until "increasing" is defined.

## Prove

**2.1.** Let $x$ be between 0 and 1 under meaning A, so $0 \lt x$ and $x \lt 1$. Since $0 \lt x$ holds, the statement "$0 \lt x$ or $0 = x$" holds, and this is $0 \le x$. In the same way, $x \lt 1$ gives "$x \lt 1$ or $x = 1$", which is $x \le 1$. So $0 \le x \le 1$, and $x$ is between 0 and 1 under meaning B. ∎

**2.2.** By 2.1, meaning A cannot give the answer yes while meaning B gives no. So the two meanings give different answers for $x$ exactly when meaning B gives yes and meaning A gives no. We show that this happens if and only if $x = 0$ or $x = 1$.

*Only if.* Suppose $0 \le x \le 1$ holds and $0 \lt x \lt 1$ fails. Since $0 \lt x \lt 1$ means "$0 \lt x$ and $x \lt 1$", its failure means that $0 \lt x$ fails or $x \lt 1$ fails.

- If $0 \lt x$ fails: $0 \le x$ means "$0 \lt x$ or $0 = x$", and the first part fails, so $0 = x$.
- If $x \lt 1$ fails: $x \le 1$ means "$x \lt 1$ or $x = 1$", and the first part fails, so $x = 1$.

In either case $x = 0$ or $x = 1$.

*If.* Take $x = 0$. Meaning B: $0 \le 0$ holds because $0 = 0$, and $0 \le 1$ holds because $0 \lt 1$. Meaning A: $0 \lt 0$ would need to hold. With $a = b = 0$, the statement $a = b$ holds, so by the fact that exactly one of the three holds, $0 \lt 0$ fails. So meaning B gives yes and meaning A gives no.

Take $x = 1$. Meaning B: $0 \le 1$ holds because $0 \lt 1$, and $1 \le 1$ holds because $1 = 1$. Meaning A: $1 \lt 1$ would need to hold, and it fails because $1 = 1$ holds and only one of the three can hold. So meaning B gives yes and meaning A gives no. ∎

## Extend

**3.1.** The difference of the two times is $3040 - 3000 = 40$ ms.

Under meaning (a), the times are not equal, since their difference 40 is not 0. So the observation and the action were not simultaneous.

Under meaning (b), $40 \lt 100$, so they were simultaneous.

**3.2.** The differences are:

- second minus first: $3060 - 3000 = 60$, and $60 \lt 100$, so the first and second are simultaneous under (b);
- third minus second: $3120 - 3060 = 60$, and $60 \lt 100$, so the second and third are simultaneous under (b);
- third minus first: $3120 - 3000 = 120$, and $120 \lt 100$ fails, so the first and third are not simultaneous under (b).

Under meaning (a) this cannot happen. If the first time equals the second and the second equals the third, then the first equals the third, by substituting the second time for the first in "the second equals the third". So meaning (b) gives "simultaneous" a property that meaning (a) does not: a chain of simultaneous pairs need not end in a simultaneous pair. Choosing a definition decides properties like this one as well as single answers.
