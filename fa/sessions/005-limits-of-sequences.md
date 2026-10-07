# ۱.۵. حد دنباله‌های حقیقی

*قضیه. بر پایهٔ جلسه‌های ۳ و ۴.*

**ادعا.** قدر مطلق در نابرابری مثلث صدق می‌کند. یک دنبالهٔ حقیقی حداکثر یک حد دارد، دنباله‌های همگرا کران‌دارند، حد با مجموع، حاصل‌ضرب، خارج‌قسمت و نابرابری‌های نااکید (non-strict inequalities) سازگار است، قاعدهٔ ساندویچ (squeeze rule) برقرار است، و وقتی $\lvert r \rvert \lt 1$، داریم $r^n \to 0$.

## ۵.۱ یادآوری

اثبات‌ها از موارد زیر استفاده می‌کنند، و نه از هیچ چیز دیگر.

از جلسهٔ ۲: توابع، نقیض گزاره‌های سوردار، و برهان خلف و اثبات با عکس نقیض.

از جلسهٔ ۳:
- استقرا، همچنین به صورتی که از $0$ آغاز می‌شود. گزاره‌ای دربارهٔ «$k \ge 0$» به $k = 0$ و هر $k \in \mathbb{N}$ مربوط است.
- هر $n \in \mathbb{N}$ در $n \ge 1$ صدق می‌کند، پس $n \gt 0$. اگر $n \in \mathbb{N}$ و $n \ne 1$، آنگاه $n - 1 \in \mathbb{N}$. اگر $m, n \in \mathbb{N}$، آنگاه $m + n \in \mathbb{N}$؛ اگر افزون بر این $m \lt n$، آنگاه $n - m \in \mathbb{N}$ و $m + 1 \le n$. اگر $k, n \in \mathbb{N}$ و $k \le n + 1$، آنگاه $k \le n$ یا $k = n + 1$.
- به‌ازای $x$ و $y$ حقیقی و $m, n \ge 0$: $x^0 = 1$، $x^{n+1} = x^n x$، $x^{m+n} = x^m x^n$ و $(xy)^n = x^n y^n$؛ اگر $x \gt 0$ آنگاه $x^n \gt 0$؛ و $1^n = 1$.
- مجموع‌های متناهی $\sum_{k=1}^{n} x_k$، که به‌صورت بازگشتی تعریف شده‌اند، با $\sum_{k=1}^{n+1} x_k = \sum_{k=1}^{n} x_k + x_{n+1}$ (قاعدهٔ (R)).
- *نابرابری برنولی* (Bernoulli): به‌ازای هر $x \ge -1$ و هر $n \ge 0$، $(1 + x)^n \ge 1 + nx$.

از جلسهٔ ۴، به‌ازای اعداد حقیقی $x$، $y$، $z$، $w$:
- قاعده‌های میدان، که با ۴.۲(الف) تا ۴.۲(ح) به آن‌ها ارجاع می‌شود. از جملهٔ آن‌ها $(-x)y = -(xy)$، $(-1)y = -y$ و $(-x)(-y) = xy$، پس $(-1)(-1) = 1$.
- دقیقاً یکی از $x \lt y$، $x = y$، $x \gt y$ برقرار است (*سه‌گانگی* (trichotomy))، پس «نه $x \lt y$» یعنی $y \le x$. هر دو رابطهٔ $\lt$ و $\le$ متعدی‌اند.
- از $x \lt y$ نتیجه می‌شود $x + z \lt y + z$. از $x \lt y$ همراه با $z \le w$ نتیجه می‌شود $x + z \lt y + w$، و از $x \le y$ همراه با $z \le w$ نتیجه می‌شود $x + z \le y + w$.
- از $x \lt y$ همراه با $z \gt 0$ نتیجه می‌شود $xz \lt yz$، و از $x \lt y$ همراه با $z \lt 0$ نتیجه می‌شود $xz \gt yz$. از $x \le y$ همراه با $z \ge 0$ نتیجه می‌شود $xz \le yz$: برای $z \gt 0$ این همان ۴.۳(ب) با $\le$ است، و برای $z = 0$ بنا بر ۴.۲(پ) هر دو طرف برابر $0$ هستند. به‌ویژه حاصل‌ضرب دو عدد $\ge 0$ خود $\ge 0$ است.
- از $x \gt 0$ و $y \gt 0$ نتیجه می‌شود $xy \gt 0$، و از $x \ne 0$ نتیجه می‌شود $x^2 \gt 0$، پس $1 \gt 0$.
- از $x \gt 0$ نتیجه می‌شود $1/x \gt 0$. از $0 \lt x \lt y$ نتیجه می‌شود $0 \lt 1/y \lt 1/x$، و از $0 \lt x \le y$ نتیجه می‌شود $1/y \le 1/x$ (*قاعدهٔ وارون‌ها* (rule for reciprocals)).
- داریم $0 \lt 1 \lt 2$ و $0 \lt \tfrac12$؛ و از $x \lt y$ نتیجه می‌شود $x \lt \tfrac{x + y}{2} \lt y$ (۴.۳(چ)). پس به‌ازای $\varepsilon \gt 0$، $0 \lt \varepsilon/2 \lt \varepsilon$، و $\varepsilon/2 + \varepsilon/2 = \varepsilon$.
- *خاصیت ارشمیدسی*: به‌ازای هر $x$ حقیقی، یک $n \in \mathbb{N}$ وجود دارد که $n \gt x$.

## ۵.۲ قدر مطلق

حد بیان می‌کند که عددها به هم نزدیک می‌شوند. نزدیکی با قدر مطلق سنجیده می‌شود.

**تعریف.** **قدر مطلق** عدد حقیقی $x$ عبارت است از

$$
\lvert x \rvert = \begin{cases} x & \text{اگر } x \ge 0, \\ -x & \text{اگر } x \lt 0. \end{cases}
$$

**فاصلهٔ** میان $x$ و $y$ عدد $\lvert x - y \rvert$ است. به‌ازای اعداد حقیقی $s$ و $t$، اگر $s \le t$ آنگاه $\max\{s, t\}$ برابر $t$ است، و در غیر این صورت برابر $s$ است. این عدد دست‌کم برابر $s$ و دست‌کم برابر $t$ است: در حالت دوم، بنا بر سه‌گانگی، $t \lt s$. برای سه عدد، $\max\{s, t, u\} = \max\{s, \max\{t, u\}\}$، که دست‌کم برابر هر یک از $s$، $t$، $u$ است.

**لم (ویژگی‌های قدر مطلق).** به‌ازای همهٔ اعداد حقیقی $x$، $y$، $z$، $w$ و $r$، و هر $n \in \mathbb{N}$:
1. $\lvert x \rvert \ge 0$، $\lvert 0 \rvert = 0$، و اگر $x \ne 0$ آنگاه $\lvert x \rvert \gt 0$؛
2. $\lvert -x \rvert = \lvert x \rvert$ و $-\lvert x \rvert \le x \le \lvert x \rvert$؛
3. اگر $z \ge 0$ و $z = w$ یا $z = -w$، آنگاه $z = \lvert w \rvert$؛
4. $\lvert xy \rvert = \lvert x \rvert \lvert y \rvert$، و اگر $x \ne 0$ آنگاه $\lvert 1/x \rvert = 1/\lvert x \rvert$؛
5. $\lvert x \rvert \lt r$ اگر و تنها اگر $-r \lt x \lt r$، و $\lvert x \rvert \le r$ اگر و تنها اگر $-r \le x \le r$؛
6. $\lvert x + y \rvert \le \lvert x \rvert + \lvert y \rvert$ (**نابرابری مثلث**)؛
7. $\bigl\lvert \lvert x \rvert - \lvert y \rvert \bigr\rvert \le \lvert x - y \rvert$ (**نابرابری مثلث وارون** (reverse triangle inequality))؛
8. $\lvert x^n \rvert = \lvert x \rvert^n$؛
9. به‌ازای همهٔ اعداد حقیقی $x_1, \dots, x_n$، $\bigl\lvert \sum_{k=1}^{n} x_k \bigr\rvert \le \sum_{k=1}^{n} \lvert x_k \rvert$ (نابرابری مثلث برای مجموع‌های متناهی).

*اثبات.* قسمت ۱. اگر $x \ge 0$ آنگاه $\lvert x \rvert = x \ge 0$، به‌ویژه $\lvert 0 \rvert = 0$، و اگر $x \gt 0$ آنگاه $\lvert x \rvert \gt 0$. اگر $x \lt 0$، افزودن $-x$ به دو طرف نتیجه می‌دهد $0 \lt -x = \lvert x \rvert$. پس همواره $\lvert x \rvert \ge 0$، و هرگاه $x \ne 0$، $\lvert x \rvert \gt 0$.

قسمت ۲. اگر $x \gt 0$ آنگاه $-x \lt 0$، پس $\lvert -x \rvert = -(-x) = x = \lvert x \rvert$. اگر $x = 0$ هر دو طرف برابر $0$ هستند. اگر $x \lt 0$ آنگاه $-x \gt 0$، پس $\lvert -x \rvert = -x = \lvert x \rvert$. برای نابرابری‌ها: اگر $x \ge 0$ آنگاه $x = \lvert x \rvert$ و $-\lvert x \rvert = -x \le 0 \le x$. اگر $x \lt 0$ آنگاه $-\lvert x \rvert = x$، و $x \lt 0 \lt -x = \lvert x \rvert$.

قسمت ۳. اگر $z = w$، آنگاه $w \ge 0$ و $\lvert w \rvert = w = z$. اگر $z = -w$، آنگاه $w = -z \le 0$؛ وقتی $w \lt 0$، $\lvert w \rvert = -w = z$، و وقتی $w = 0$، $z = 0 = \lvert w \rvert$.

قسمت ۴. بنا بر تعریف، با استفاده از $-x = (-1)x$ (جلسهٔ ۴)، $\lvert x \rvert = sx$ و $\lvert y \rvert = ty$، که در آن هر یک از $s, t$ برابر $1$ یا $-1$ است. آنگاه $\lvert x \rvert \lvert y \rvert = (st)(xy)$، که در آن $st$ برابر $1$ یا $-1$ است، زیرا $(-1)(-1) = 1$ (جلسهٔ ۴). همچنین $\lvert x \rvert \lvert y \rvert \ge 0$، چون حاصل‌ضرب دو عدد است که بنا بر قسمت ۱ هر دو $\ge 0$ هستند. قسمت ۳ با $z = \lvert x \rvert \lvert y \rvert$ و $w = xy$ نتیجه می‌دهد $\lvert x \rvert \lvert y \rvert = \lvert xy \rvert$. اگر $x \ne 0$، آنگاه $\lvert x \rvert \, \lvert 1/x \rvert = \lvert x \cdot (1/x) \rvert = \lvert 1 \rvert = 1$، و بنا بر قسمت ۱، $\lvert x \rvert \ne 0$، پس بنا بر ۴.۲(ث)، $\lvert 1/x \rvert = 1/\lvert x \rvert$.

قسمت ۵. فرض کنید $\lvert x \rvert \lt r$. بنا بر قسمت ۲، $x \le \lvert x \rvert \lt r$، و $-x \le \lvert -x \rvert = \lvert x \rvert \lt r$؛ افزودن $x - r$ به دو طرف $-x \lt r$ نتیجه می‌دهد $-r \lt x$. برعکس، فرض کنید $-r \lt x \lt r$. اگر $x \ge 0$ آنگاه $\lvert x \rvert = x \lt r$. اگر $x \lt 0$، افزودن $r - x$ به دو طرف $-r \lt x$ نتیجه می‌دهد $-x \lt r$، یعنی $\lvert x \rvert \lt r$. همین استدلال، با $\le$ در همه‌جا، گزارهٔ دوم را ثابت می‌کند.

قسمت ۶. بنا بر قسمت ۲، $-\lvert x \rvert \le x \le \lvert x \rvert$ و $-\lvert y \rvert \le y \le \lvert y \rvert$. جمع کردن این دو نتیجه می‌دهد $-(\lvert x \rvert + \lvert y \rvert) \le x + y \le \lvert x \rvert + \lvert y \rvert$، و قسمت ۵ با $r = \lvert x \rvert + \lvert y \rvert$ نتیجه می‌دهد $\lvert x + y \rvert \le \lvert x \rvert + \lvert y \rvert$.

قسمت ۷. چون $x = (x - y) + y$، قسمت ۶ نتیجه می‌دهد $\lvert x \rvert \le \lvert x - y \rvert + \lvert y \rvert$، پس $\lvert x \rvert - \lvert y \rvert \le \lvert x - y \rvert$. با جابه‌جا کردن $x$ و $y$ به دست می‌آید $\lvert y \rvert - \lvert x \rvert \le \lvert y - x \rvert$، و بنا بر قسمت ۲، $\lvert y - x \rvert = \lvert -(x - y) \rvert = \lvert x - y \rvert$. بنا بر ۴.۳(الف) و ۴.۲(ت)، $-\lvert x - y \rvert \le -(\lvert y \rvert - \lvert x \rvert) = \lvert x \rvert - \lvert y \rvert$. پس $-\lvert x - y \rvert \le \lvert x \rvert - \lvert y \rvert \le \lvert x - y \rvert$، و قسمت ۵ با $r = \lvert x - y \rvert$ اثبات را کامل می‌کند.

قسمت ۸. استقرا روی $n$ (جلسهٔ ۳). برای $n = 1$ هر دو طرف برابر $\lvert x \rvert$ هستند. اگر $\lvert x^n \rvert = \lvert x \rvert^n$، آنگاه قسمت ۴ نتیجه می‌دهد $\lvert x^{n+1} \rvert = \lvert x^n x \rvert = \lvert x^n \rvert \, \lvert x \rvert = \lvert x \rvert^n \lvert x \rvert = \lvert x \rvert^{n+1}$.

قسمت ۹. استقرا روی $n$ (جلسهٔ ۳). برای $n = 1$ هر دو طرف برابر $\lvert x_1 \rvert$ هستند. اگر نابرابری برای $n$ برقرار باشد، آنگاه قاعدهٔ (R)، قسمت ۶ و فرض استقرا نتیجه می‌دهند

$$
\Bigl\lvert \sum_{k=1}^{n+1} x_k \Bigr\rvert = \Bigl\lvert \sum_{k=1}^{n} x_k + x_{n+1} \Bigr\rvert \le \Bigl\lvert \sum_{k=1}^{n} x_k \Bigr\rvert + \lvert x_{n+1} \rvert \le \sum_{k=1}^{n} \lvert x_k \rvert + \lvert x_{n+1} \rvert = \sum_{k=1}^{n+1} \lvert x_k \rvert .
$$

∎

برای مثال، بنا بر قسمت ۲، $\lvert -1 \rvert = 1$، پس قسمت ۸ و $1^n = 1$ (جلسهٔ ۳) نتیجه می‌دهند که به‌ازای هر $n \in \mathbb{N}$، $\lvert (-1)^n \rvert = 1^n = 1$.

دو پیامد تقریباً در همهٔ اثبات‌های زیر به کار می‌روند. نخست، به‌ازای همهٔ اعداد حقیقی $a$، $b$، $c$، قسمت ۶ با $x = a - b$ و $y = b - c$ نتیجه می‌دهد

$$
\lvert a - c \rvert \le \lvert a - b \rvert + \lvert b - c \rvert .
$$

دوم، به‌ازای همهٔ اعداد حقیقی $x$، $c$ و $r$، $\lvert x - c \rvert \lt r$ برقرار است اگر و تنها اگر $c - r \lt x \lt c + r$. در واقع، قسمت ۵ می‌گوید $\lvert x - c \rvert \lt r$ برقرار است اگر و تنها اگر $-r \lt x - c \lt r$، و افزودن $c$ به هر یک از سه عبارت، یا افزودن $-c$ برای بازگشت، این را به $c - r \lt x \lt c + r$ تبدیل می‌کند. همین حکم با $\le$ به‌جای $\lt$ نیز برقرار است.

## ۵.۳ دنباله‌ها و حدهای آن‌ها

دنبالهٔ حقیقی تابعی است $a : \mathbb{N} \to \mathbb{R}$ (جلسهٔ ۳، بند ۳.۵). مقدار آن در $n$، یعنی $a_n$، **جملهٔ** $n$ام آن نامیده می‌شود، و دنباله را با $(a_n)$ نشان می‌دهند.

**تعریف.** فرض کنید $(a_n)$ یک دنبالهٔ حقیقی و $a$ یک عدد حقیقی باشد. می‌گوییم دنباله **به $a$ همگراست** اگر به‌ازای هر $\varepsilon \gt 0$ یک $N \in \mathbb{N}$ وجود داشته باشد به‌طوری که

$$
\lvert a_n - a \rvert \lt \varepsilon \quad \text{به‌ازای هر } n \ge N .
$$

در این صورت $a$ یک **حد** $(a_n)$ است، و می‌نویسیم $a_n \to a$. دنباله **همگرا** است اگر به عددی حقیقی همگرا باشد، و در غیر این صورت **واگرا** است.

عدد $N$ ممکن است به $\varepsilon$ وابسته باشد: $\varepsilon$ کوچک‌تر معمولاً $N$ بزرگ‌تری لازم دارد. اگر یک $N$ برای $\varepsilon$ معینی مناسب باشد، آنگاه هر $N' \ge N$ نیز مناسب است، زیرا از $n \ge N'$ نتیجه می‌شود $n \ge N$. بنا بر قاعده‌های نقیض در جلسهٔ ۲، $(a_n)$ به $a$ همگرا نیست دقیقاً وقتی که

$$
\exists \varepsilon \gt 0 \;\; \forall N \in \mathbb{N} \;\; \exists n \ge N : \; \lvert a_n - a \rvert \ge \varepsilon .
$$

**مثال (دنباله‌های ثابت).** فرض کنید به‌ازای هر $n$، $a_n = c$. به‌ازای هر $\varepsilon \gt 0$، $N = 1$ را بگیرید. آنگاه به‌ازای هر $n \ge 1$، $\lvert a_n - c \rvert = 0 \lt \varepsilon$. پس $a_n \to c$: دنبالهٔ ثابت $(c)$ به $c$ همگراست.

**مثال ($1/n \to 0$).** فرض کنید $\varepsilon \gt 0$. بنا بر خاصیت ارشمیدسی (جلسهٔ ۴) یک $N \in \mathbb{N}$ با $N \gt 1/\varepsilon$ وجود دارد. به‌ازای $n \ge N$ داریم $n \ge N \gt 1/\varepsilon \gt 0$، پس قاعدهٔ وارون‌ها نتیجه می‌دهد $1/n \lt 1/(1/\varepsilon)$، و بنا بر ۴.۲(ث)، $1/(1/\varepsilon) = \varepsilon$. چون $n \gt 0$، داریم $1/n \gt 0$، پس $\lvert 1/n - 0 \rvert = 1/n \lt \varepsilon$. بنابراین $1/n \to 0$.

دو لم اثبات‌های بعدی را کوتاه می‌کنند. لم نخست اجازه می‌دهد که اثبات با کران $C\varepsilon$ به‌جای $\varepsilon$ پایان یابد.

**لم ($C\varepsilon$ کافی است).** فرض کنید $C \gt 0$ ثابت باشد. فرض کنید به‌ازای هر $\varepsilon \gt 0$ یک $N \in \mathbb{N}$ وجود داشته باشد که به‌ازای هر $n \ge N$، $\lvert a_n - a \rvert \le C\varepsilon$. آنگاه $a_n \to a$.

*اثبات.* فرض کنید $\varepsilon \gt 0$. چون $2 \gt 0$ و $C \gt 0$، داریم $2C \gt 0$ و $1/(2C) \gt 0$، پس $\varepsilon' = \varepsilon / (2C) \gt 0$. اعمال فرض بر $\varepsilon'$ عددی مانند $N$ به دست می‌دهد که به‌ازای هر $n \ge N$، $\lvert a_n - a \rvert \le C \varepsilon' = \varepsilon/2$. چون $\varepsilon/2 \lt \varepsilon$ (بند ۵.۱)، به‌ازای هر $n \ge N$، $\lvert a_n - a \rvert \lt \varepsilon$. ∎

لم دوم می‌گوید که همگرایی تنها به جمله‌های از جایی به بعد بستگی دارد.

**لم (دم‌ها (tails)).** فرض کنید $k \ge 0$ و به‌ازای هر $n \in \mathbb{N}$، $b_n = a_{n+k}$. آنگاه $a_n \to a$ اگر و تنها اگر $b_n \to a$.

در اینجا $n + k \in \mathbb{N}$: اگر $k = 0$ این عدد برابر $n$ است، و در غیر این صورت مجموع دو عدد طبیعی است (جلسهٔ ۳). پس $(b_n)$ یک دنبالهٔ حقیقی است.

*اثبات.* فرض کنید $a_n \to a$، و فرض کنید $\varepsilon \gt 0$. $N$ را چنان بگیرید که به‌ازای هر $n \ge N$، $\lvert a_n - a \rvert \lt \varepsilon$. به‌ازای $n \ge N$ داریم $n + k \ge n \ge N$، پس $\lvert b_n - a \rvert = \lvert a_{n+k} - a \rvert \lt \varepsilon$.

برعکس، فرض کنید $b_n \to a$، و فرض کنید $\varepsilon \gt 0$. $N$ را چنان بگیرید که به‌ازای هر $n \ge N$، $\lvert b_n - a \rvert \lt \varepsilon$، و قرار دهید $N' = N + k$، که مانند بالا عددی طبیعی است. فرض کنید $n \ge N'$، و قرار دهید $m = n - k$. اگر $k = 0$، آنگاه $m = n \in \mathbb{N}$. اگر $k \in \mathbb{N}$، آنگاه چون $N \gt 0$، داریم $n \ge N + k \gt k$، پس $m \in \mathbb{N}$ (جلسهٔ ۳). در هر دو حالت، کم کردن $k$ از $n \ge N + k$ نتیجه می‌دهد $m \ge N$، پس $\lvert a_n - a \rvert = \lvert b_m - a \rvert \lt \varepsilon$. ∎

اکنون فرض کنید دو دنباله از اندیسی مانند $K \in \mathbb{N}$ به بعد برابر باشند: به‌ازای هر $n \ge K$، $a'_n = a_n$. قرار دهید $k = K - 1$، که اگر $K = 1$ برابر $0$ است و در غیر این صورت در $\mathbb{N}$ قرار دارد (جلسهٔ ۳). به‌ازای هر $n \in \mathbb{N}$، $n + k \ge 1 + k = K$، پس هر دو دنباله دم یکسان $b_n = a_{n+k} = a'_{n+k}$ را دارند. دو بار به‌کار بستن لم نتیجه می‌دهد $a_n \to a$ اگر و تنها اگر $b_n \to a$، اگر و تنها اگر $a'_n \to a$. پس تغییر دادن تعداد متناهی جمله نه همگرا بودن دنباله را تغییر می‌دهد و نه حد آن را.

## ۵.۴ یک دنباله حداکثر یک حد دارد

**قضیه (یکتایی حد).** اگر $a_n \to a$ و $a_n \to b$، آنگاه $a = b$.

*اثبات.* با برهان خلف استدلال می‌کنیم (جلسهٔ ۲). فرض کنید $a \ne b$. آنگاه $a - b \ne 0$، زیرا از $a - b = 0$ با افزودن $b$ نتیجه می‌شد $a = b$. پس بنا بر بند ۵.۲، قسمت ۱، $\lvert a - b \rvert \gt 0$، و $\varepsilon = \lvert a - b \rvert / 2 \gt 0$، با $\varepsilon + \varepsilon = \lvert a - b \rvert$ (بند ۵.۱). $N_1$ را چنان بگیرید که به‌ازای هر $n \ge N_1$، $\lvert a_n - a \rvert \lt \varepsilon$، و $N_2$ را چنان که به‌ازای هر $n \ge N_2$، $\lvert a_n - b \rvert \lt \varepsilon$. قرار دهید $n = \max\{N_1, N_2\}$. آنگاه

$$
\lvert a - b \rvert \le \lvert a - a_n \rvert + \lvert a_n - b \rvert \lt \varepsilon + \varepsilon = \lvert a - b \rvert ,
$$

که در آن گام نخست همان پیامد نخست در بند ۵.۲ است، و بنا بر بند ۵.۲، قسمت ۲، $\lvert a - a_n \rvert = \lvert a_n - a \rvert$. پس $\lvert a - b \rvert \lt \lvert a - b \rvert$، که سه‌گانگی آن را ناممکن می‌کند. بنابراین $a = b$. ∎

این قضیه سخن گفتن از *حد* یک دنبالهٔ همگرا را موجه می‌کند، که با $\lim_{n \to \infty} a_n$ نوشته می‌شود.

## ۵.۵ دنباله‌های همگرا کران‌دارند

**تعریف.** دنبالهٔ حقیقی $(a_n)$ **کران‌دار** است اگر عددی حقیقی مانند $M$ وجود داشته باشد که به‌ازای هر $n \in \mathbb{N}$، $\lvert a_n \rvert \le M$. دنباله **بی‌کران** است اگر کران‌دار نباشد: به‌ازای هر $M$ حقیقی، یک $n$ وجود دارد که $\lvert a_n \rvert \gt M$.

جمله‌های آغازین هر دنباله کران‌دارند.

**لم (تعداد متناهی جمله).** به‌ازای هر دنبالهٔ حقیقی $(a_n)$ و هر $m \in \mathbb{N}$، یک $B \ge 0$ وجود دارد که به‌ازای هر $k \in \mathbb{N}$ با $k \le m$، $\lvert a_k \rvert \le B$.

*اثبات.* استقرا روی $m$ (جلسهٔ ۳). برای $m = 1$، $B = \lvert a_1 \rvert$ را بگیرید، که بنا بر بند ۵.۲، قسمت ۱، $\ge 0$ است؛ عدد طبیعی $k \le 1$ برابر $1$ است، زیرا $k \ge 1$ (جلسهٔ ۳). فرض کنید $B$ برای $m$ مناسب باشد، و قرار دهید $B' = \max\{B, \lvert a_{m+1} \rvert\} \ge B \ge 0$. فرض کنید $k \in \mathbb{N}$ و $k \le m + 1$. بنا بر جلسهٔ ۳، $k \le m$ یا $k = m + 1$. در حالت نخست $\lvert a_k \rvert \le B \le B'$؛ در حالت دوم $\lvert a_k \rvert = \lvert a_{m+1} \rvert \le B'$. ∎

**قضیه (همگرایی کران‌داری را نتیجه می‌دهد).** اگر $a_n \to a$، یک $M \gt 0$ وجود دارد که به‌ازای هر $n$، $\lvert a_n \rvert \le M$.

*اثبات.* تعریف همگرایی را با $\varepsilon = 1$ به کار ببرید: یک $N$ وجود دارد که به‌ازای هر $n \ge N$، $\lvert a_n - a \rvert \lt 1$. برای چنین مقادیری از $n$، نابرابری مثلث نتیجه می‌دهد

$$
\lvert a_n \rvert = \lvert (a_n - a) + a \rvert \le \lvert a_n - a \rvert + \lvert a \rvert \lt 1 + \lvert a \rvert .
$$

اگر $N = 1$، قرار دهید $M = 1 + \lvert a \rvert$؛ هر $n$ در $n \ge 1 = N$ صدق می‌کند. اگر $N \ne 1$، آنگاه $N - 1 \in \mathbb{N}$ (جلسهٔ ۳). $B$ را مانند لم با $m = N - 1$ بگیرید، و قرار دهید $M = \max\{B, 1 + \lvert a \rvert\}$. فرض کنید $n \in \mathbb{N}$. اگر $n \ge N$، آنگاه $\lvert a_n \rvert \lt 1 + \lvert a \rvert \le M$. در غیر این صورت بنا بر سه‌گانگی $n \lt N$، پس $n + 1 \le N$ (جلسهٔ ۳) و $n \le N - 1$، و $\lvert a_n \rvert \le B \le M$. در هر دو حالت $M \ge 1 + \lvert a \rvert \ge 1 \gt 0$، زیرا $\lvert a \rvert \ge 0$. ∎

**آنچه برقرار نمی‌ماند: عکس قضیه.** یک دنبالهٔ کران‌دار لزوماً همگرا نیست. فرض کنید $a_n = (-1)^n$. بنا بر بند ۵.۲، به‌ازای هر $n$، $\lvert a_n \rvert = 1$، پس دنباله با $M = 1$ کران‌دار است. فرض کنید $a_n \to a$. $N$ را چنان بگیرید که به‌ازای هر $n \ge N$، $\lvert a_n - a \rvert \lt 1$. چون $a_{N+1} = (-1)^N (-1) = -a_N$ (جلسه‌های ۳ و ۴)، بنا بر بند ۵.۲، قسمت ۴ و $\lvert 2 \rvert = 2$ داریم $\lvert a_N - a_{N+1} \rvert = \lvert 2 a_N \rvert = \lvert 2 \rvert \, \lvert a_N \rvert = 2$. ولی

$$
2 = \lvert a_N - a_{N+1} \rvert \le \lvert a_N - a \rvert + \lvert a - a_{N+1} \rvert \lt 1 + 1 = 2 ,
$$

که در آن گام نخست همان پیامد نخست در بند ۵.۲ است، و چون $N + 1 \ge N$، بنا بر بند ۵.۲، قسمت ۲، $\lvert a - a_{N+1} \rvert = \lvert a_{N+1} - a \rvert \lt 1$. این یک تناقض است. پس $((-1)^n)$ واگراست. بنا بر عکس نقیض (جلسهٔ ۲)، قضیه همچنین می‌گوید که یک دنبالهٔ بی‌کران واگراست.

## ۵.۶ مجموع‌ها و حاصل‌ضرب‌ها

**قضیه (قاعده‌های جمع و حاصل‌ضرب).** فرض کنید $a_n \to a$ و $b_n \to b$، و $c$ عددی حقیقی باشد. آنگاه
1. $a_n + b_n \to a + b$؛
2. $a_n b_n \to ab$؛
3. $c a_n \to ca$ و $a_n - b_n \to a - b$.

*اثبات.* قسمت ۱. فرض کنید $\varepsilon \gt 0$. $N_1$ را چنان بگیرید که به‌ازای هر $n \ge N_1$، $\lvert a_n - a \rvert \lt \varepsilon$، و $N_2$ را چنان که به‌ازای هر $n \ge N_2$، $\lvert b_n - b \rvert \lt \varepsilon$. قرار دهید $N = \max\{N_1, N_2\}$. به‌ازای هر $n \ge N$، نابرابری مثلث نتیجه می‌دهد

$$
\lvert (a_n + b_n) - (a + b) \rvert = \lvert (a_n - a) + (b_n - b) \rvert \le \lvert a_n - a \rvert + \lvert b_n - b \rvert \lt 2\varepsilon .
$$

لم «$C\varepsilon$ کافی است» (بند ۵.۳) با $C = 2$ نتیجه می‌دهد $a_n + b_n \to a + b$.

قسمت ۲. بنا بر بند ۵.۵، یک $M \gt 0$ وجود دارد که به‌ازای هر $n$، $\lvert a_n \rvert \le M$. با افزودن و کم کردن $a_n b$،

$$
a_n b_n - ab = a_n (b_n - b) + b (a_n - a) .
$$

فرض کنید $\varepsilon \gt 0$، و $N_1$، $N_2$ و $N = \max\{N_1, N_2\}$ را مانند قسمت ۱ بگیرید. به‌ازای هر $n \ge N$، نابرابری مثلث و بند ۵.۲، قسمت ۴ نتیجه می‌دهند

$$
\lvert a_n b_n - ab \rvert \le \lvert a_n \rvert \, \lvert b_n - b \rvert + \lvert b \rvert \, \lvert a_n - a \rvert \le M\varepsilon + \lvert b \rvert \varepsilon = (M + \lvert b \rvert)\,\varepsilon .
$$

گام دوم برای هر جمله کرانی به دست می‌دهد. ضرب کردن $\lvert a_n \rvert \le M$ در $\lvert b_n - b \rvert \ge 0$، و سپس ضرب کردن $\lvert b_n - b \rvert \lt \varepsilon$ در $M \gt 0$، نتیجه می‌دهد $\lvert a_n \rvert \, \lvert b_n - b \rvert \le M \lvert b_n - b \rvert \le M\varepsilon$. ضرب کردن $\lvert a_n - a \rvert \le \varepsilon$ در $\lvert b \rvert \ge 0$ نتیجه می‌دهد $\lvert b \rvert \, \lvert a_n - a \rvert \le \lvert b \rvert \varepsilon$. در اینجا $M + \lvert b \rvert \gt 0$، پس لم «$C\varepsilon$ کافی است» با $C = M + \lvert b \rvert$ نتیجه می‌دهد $a_n b_n \to ab$.

قسمت ۳. دنبالهٔ ثابت $(c)$ به $c$ همگراست (بند ۵.۳)، پس قسمت ۲ نتیجه می‌دهد $c a_n \to ca$. با $c = -1$، $-b_n \to -b$، و قسمت ۱ نتیجه می‌دهد $a_n - b_n = a_n + (-b_n) \to a - b$. ∎

استقرا قاعده‌های جمع و حاصل‌ضرب را به توان‌ها و چندجمله‌ای‌ها گسترش می‌دهد. **چندجمله‌ای** با **ضرایب** حقیقی $c_0, \dots, c_m$، که در آن $m \ge 0$، تابع $p : \mathbb{R} \to \mathbb{R}$ با $p(x) = \sum_{k=0}^{m} c_k x^k = c_0 + c_1 x + \dots + c_m x^m$ است (مجموع‌هایی که از $0$ آغاز می‌شوند، جلسهٔ ۳، بند ۳.۶).

**نتیجه (توان‌ها و چندجمله‌ای‌ها).** اگر $a_n \to a$، آنگاه به‌ازای هر $k \in \mathbb{N}$، $a_n^k \to a^k$. اگر $p$ یک چندجمله‌ای با ضرایب حقیقی باشد، آنگاه $p(a_n) \to p(a)$.

*اثبات.* استقرا روی $k$ (جلسهٔ ۳). برای $k = 1$ گزاره همان فرض است. اگر $a_n^k \to a^k$، آنگاه بنا بر قاعدهٔ حاصل‌ضرب $a_n^{k+1} = a_n^k a_n \to a^k a = a^{k+1}$. برای چندجمله‌ای، استقرا روی $m$ از $0$ (جلسهٔ ۳). برای $m = 0$، $p(x) = c_0 x^0 = c_0$، پس $p(a_n) = c_0$ یک دنبالهٔ ثابت است و به $c_0 = p(a)$ همگراست. فرض کنید گزاره برای هر چندجمله‌ای با ضرایب $c_0, \dots, c_m$ برقرار باشد، و فرض کنید $p$ ضرایب $c_0, \dots, c_{m+1}$ را داشته باشد. بنا بر (R0) (جلسهٔ ۳)، $p(x) = q(x) + c_{m+1} x^{m+1}$، که در آن $q$ چندجمله‌ای با ضرایب $c_0, \dots, c_m$ است. آنگاه بنا بر فرض استقرا $q(a_n) \to q(a)$، بنا بر گزارهٔ نخست و قسمت ۳، $c_{m+1} a_n^{m+1} \to c_{m+1} a^{m+1}$، و قاعدهٔ جمع نتیجه می‌دهد $p(a_n) \to p(a)$. ∎

## ۵.۷ خارج‌قسمت‌ها

خارج‌قسمت $a_n / b_n$ به $b_n \ne 0$ نیاز دارد. لم نخست نشان می‌دهد که دنباله‌ای با حد ناصفر از جایی به بعد از صفر دور می‌ماند.

**لم (دوری از صفر).** اگر $b_n \to b$ و $b \ne 0$، یک $N_0$ وجود دارد که به‌ازای هر $n \ge N_0$، $\lvert b_n \rvert \gt \lvert b \rvert / 2$. به‌ویژه به‌ازای هر $n \ge N_0$، $b_n \ne 0$.

*اثبات.* در اینجا بنا بر بند ۵.۲، قسمت ۱، $\lvert b \rvert \gt 0$، پس $\lvert b \rvert / 2 \gt 0$. $N_0$ را چنان بگیرید که به‌ازای هر $n \ge N_0$، $\lvert b_n - b \rvert \lt \lvert b \rvert / 2$. برای چنین مقادیری از $n$،

$$
\lvert b \rvert = \lvert (b - b_n) + b_n \rvert \le \lvert b - b_n \rvert + \lvert b_n \rvert \lt \frac{\lvert b \rvert}{2} + \lvert b_n \rvert ,
$$

با استفاده از $\lvert b - b_n \rvert = \lvert b_n - b \rvert$ (بند ۵.۲، قسمت ۲). کم کردن $\lvert b \rvert / 2$ از دو طرف نتیجه می‌دهد $\lvert b_n \rvert \gt \lvert b \rvert / 2 \gt 0$. پس $b_n \ne 0$، زیرا از $b_n = 0$ نتیجه می‌شد $\lvert b_n \rvert = 0$ (بند ۵.۲، قسمت ۱). ∎

**قضیه (قاعدهٔ خارج‌قسمت).** فرض کنید $a_n \to a$ و $b_n \to b$، با $b \ne 0$ و به‌ازای هر $n$، $b_n \ne 0$. آنگاه $1/b_n \to 1/b$ و $a_n / b_n \to a/b$.

*اثبات.* $N_0$ را مانند لم بگیرید. به‌ازای $n \ge N_0$،

$$
\left\lvert \frac{1}{b_n} - \frac{1}{b} \right\rvert = \left\lvert \frac{b - b_n}{b_n b} \right\rvert = \frac{\lvert b_n - b \rvert}{\lvert b_n \rvert \, \lvert b \rvert} \le \frac{\lvert b_n - b \rvert}{(\lvert b \rvert / 2) \, \lvert b \rvert} = \frac{2}{\lvert b \rvert^2} \, \lvert b_n - b \rvert .
$$

گام نخست ۴.۲(ح) است. گام دوم از بند ۵.۲، قسمت‌های ۲ و ۴ استفاده می‌کند. برای گام سوم، ضرب کردن $\lvert b_n \rvert \gt \lvert b \rvert / 2$ در $\lvert b \rvert \gt 0$ نتیجه می‌دهد $\lvert b_n \rvert \, \lvert b \rvert \gt (\lvert b \rvert / 2) \lvert b \rvert \gt 0$؛ قاعدهٔ وارون‌ها نتیجه می‌دهد $1/(\lvert b_n \rvert \, \lvert b \rvert) \lt 1/((\lvert b \rvert / 2) \lvert b \rvert)$؛ و ضرب کردن در $\lvert b_n - b \rvert \ge 0$ گام سوم را به دست می‌دهد. فرض کنید $\varepsilon \gt 0$، و $N_1$ را چنان بگیرید که به‌ازای هر $n \ge N_1$، $\lvert b_n - b \rvert \lt \varepsilon$. به‌ازای $n \ge \max\{N_0, N_1\}$، با ضرب کردن در $2/\lvert b \rvert^2 \gt 0$،

$$
\left\lvert \frac{1}{b_n} - \frac{1}{b} \right\rvert \le \frac{2}{\lvert b \rvert^2} \, \varepsilon ,
$$

و لم «$C\varepsilon$ کافی است» با $C = 2/\lvert b \rvert^2$ نتیجه می‌دهد $1/b_n \to 1/b$. آنگاه بنا بر قاعدهٔ حاصل‌ضرب، $a_n / b_n = a_n \cdot (1/b_n) \to a \cdot (1/b) = a/b$. ∎

اگر $b \ne 0$ ولی برخی جمله‌های $b_n$ صفر شوند، لم نشان می‌دهد که برای همهٔ آن‌ها $n \lt N_0$. قرار دهید $k = N_0 - 1 \ge 0$. بنا بر لم دم‌ها (بند ۵.۳)، دنباله‌های $n \mapsto a_{n+k}$ و $n \mapsto b_{n+k}$ به $a$ و $b$ همگرایند، و به‌ازای هر $n$، $b_{n+k} \ne 0$، زیرا $n + k \ge N_0$. قضیه دربارهٔ آن‌ها به کار می‌رود.

**آنچه برقرار نمی‌ماند: حد صفر در مخرج.** فرض کنید $b_n = 1/n$، پس به‌ازای هر $n$، $b_n \ne 0$ و $b_n \to 0$. آنگاه $1/b_n = n$. به‌ازای هر $M$ حقیقی، خاصیت ارشمیدسی یک $n \in \mathbb{N}$ با $n \gt M$ به دست می‌دهد، و چون $n \gt 0$، $\lvert n \rvert = n$. پس $(n)$ بی‌کران است، و بنا بر بند ۵.۵ واگراست. فرض $b \ne 0$ را نمی‌توان کنار گذاشت.

## ۵.۸ حدها نابرابری‌های نااکید را حفظ می‌کنند

**قضیه (حد و $\le$).** فرض کنید $a_n \to a$ و $b_n \to b$، و یک $K \in \mathbb{N}$ وجود داشته باشد که به‌ازای هر $n \ge K$، $a_n \le b_n$. آنگاه $a \le b$.

*اثبات.* فرض کنید، برخلاف حکم، $a \gt b$. آنگاه $a - b \gt 0$ (جلسهٔ ۴)، پس $\varepsilon = (a - b)/2 \gt 0$، و

$$
a - \varepsilon = \frac{2a - (a - b)}{2} = \frac{a + b}{2} = \frac{2b + (a - b)}{2} = b + \varepsilon .
$$

$N_1$ را چنان بگیرید که به‌ازای هر $n \ge N_1$، $\lvert a_n - a \rvert \lt \varepsilon$؛ بنا بر پیامد دوم در بند ۵.۲، برای این مقادیر $n$ داریم $a_n \gt a - \varepsilon$. $N_2$ را چنان بگیرید که به‌ازای هر $n \ge N_2$، $\lvert b_n - b \rvert \lt \varepsilon$؛ آنگاه برای این مقادیر $n$ داریم $b_n \lt b + \varepsilon$. قرار دهید $n = \max\{K, N_1, N_2\}$. آنگاه

$$
b_n \lt b + \varepsilon = a - \varepsilon \lt a_n ,
$$

که بنا بر سه‌گانگی با $a_n \le b_n$ در تناقض است. پس $a \le b$. ∎

**نتیجه.** اگر $a_n \to a$، $K \in \mathbb{N}$ و به‌ازای هر $n \ge K$، $a_n \le c$، آنگاه $a \le c$. اگر به‌ازای هر $n \ge K$، $a_n \ge c$، آنگاه $a \ge c$.

*اثبات.* قضیه را با دنبالهٔ ثابت $(c)$، که به $c$ همگراست (بند ۵.۳)، در نقش $(b_n)$ در حالت نخست و در نقش $(a_n)$ در حالت دوم به کار ببرید. ∎

**آنچه برقرار نمی‌ماند: نابرابری‌های اکید.** فرض کنید $a_n = 0$ و $b_n = 1/n$. آنگاه به‌ازای هر $n$، $a_n \lt b_n$، ولی هر دو حد برابر $0$ هستند (بند ۵.۳)، پس $\lim_{n \to \infty} a_n \lt \lim_{n \to \infty} b_n$ نادرست است. نابرابری اکید میان جمله‌ها تنها نابرابری نااکید میان حدها را نتیجه می‌دهد.

## ۵.۹ قاعدهٔ ساندویچ

**قضیه (قاعدهٔ ساندویچ).** فرض کنید $a_n \to L$ و $b_n \to L$، و یک $K \in \mathbb{N}$ وجود داشته باشد که به‌ازای هر $n \ge K$، $a_n \le c_n \le b_n$. آنگاه $c_n \to L$.

همگرایی دنبالهٔ $(c_n)$ فرض نشده است؛ قضیه آن را ثابت می‌کند.

*اثبات.* فرض کنید $\varepsilon \gt 0$. $N_1$ را چنان بگیرید که به‌ازای هر $n \ge N_1$، $\lvert a_n - L \rvert \lt \varepsilon$، و $N_2$ را چنان که به‌ازای هر $n \ge N_2$، $\lvert b_n - L \rvert \lt \varepsilon$. قرار دهید $N = \max\{K, N_1, N_2\}$. به‌ازای هر $n \ge N$، پیامد دوم در بند ۵.۲ نتیجه می‌دهد $L - \varepsilon \lt a_n$ و $b_n \lt L + \varepsilon$، پس

$$
L - \varepsilon \lt a_n \le c_n \le b_n \lt L + \varepsilon .
$$

باز بنا بر پیامد دوم در بند ۵.۲، به‌ازای هر $n \ge N$، $\lvert c_n - L \rvert \lt \varepsilon$. ∎

قاعدهٔ ساندویچ بیش از همه به صورت زیر به کار می‌رود.

**نتیجه.** اگر $d_n \to 0$، $K \in \mathbb{N}$ و به‌ازای هر $n \ge K$، $\lvert c_n - L \rvert \le d_n$، آنگاه $c_n \to L$.

*اثبات.* بنا بر پیامد دوم در بند ۵.۲، با $\le$، به‌ازای هر $n \ge K$، $L - d_n \le c_n \le L + d_n$. بنا بر قاعده‌های جمع (بند ۵.۶)، با دنبالهٔ ثابت $(L)$، $L - d_n \to L - 0 = L$ و $L + d_n \to L + 0 = L$. قاعدهٔ ساندویچ نتیجه می‌دهد $c_n \to L$. ∎

**آنچه برقرار نمی‌ماند: حدهای بیرونی متفاوت.** فرض کنید $a_n = -1$، $b_n = 1$ و $c_n = (-1)^n$. چون $\lvert c_n \rvert = 1$ (بند ۵.۲)، قسمت ۵ از لم آن بند نتیجه می‌دهد که به‌ازای هر $n$، $a_n \le c_n \le b_n$، و $(a_n)$ و $(b_n)$ همگرایند، به $-1$ و $1$. ولی $(c_n)$ واگراست (بند ۵.۵). دو دنبالهٔ بیرونی باید حد یکسانی داشته باشند.

## ۵.۱۰ دنبالهٔ هندسی

قاعدهٔ ساندویچ و نابرابری برنولی (جلسهٔ ۳) حدی را به دست می‌دهند که تمرین‌ها و جلسه‌های بعدی بارها از آن استفاده می‌کنند.

**قضیه (دنبالهٔ هندسی).** اگر $\lvert r \rvert \lt 1$، آنگاه $r^n \to 0$.

*اثبات.* اگر $r = 0$، آنگاه $r^1 = 0$، و از $r^n = 0$ نتیجه می‌شود $r^{n+1} = r^n \cdot 0 = 0$. بنا بر استقرا، $(r^n)$ همان دنبالهٔ ثابت $(0)$ است، که به $0$ همگراست. فرض کنید $r \ne 0$. آنگاه بنا بر بند ۵.۲، قسمت ۱، $0 \lt \lvert r \rvert \lt 1$، و قاعدهٔ وارون‌ها نتیجه می‌دهد $1/\lvert r \rvert \gt 1/1 = 1$. قرار دهید $h = 1/\lvert r \rvert - 1$، پس $h \gt 0$ و $1/\lvert r \rvert = 1 + h$. به‌ازای هر $n$، $nh \gt 0$، چون حاصل‌ضرب اعداد مثبت است، و افزودن $nh$ به $1 \gt 0$ نتیجه می‌دهد $1 + nh \gt nh$. افزودن $-1$ به $0 \lt 1$ نتیجه می‌دهد $-1 \lt 0 \lt h$، پس $h \ge -1$، و نابرابری برنولی (جلسهٔ ۳) نتیجه می‌دهد

$$
(1 + h)^n \ge 1 + nh \gt nh \gt 0 .
$$

بنا بر قاعدهٔ $(xy)^n = x^n y^n$ (جلسهٔ ۳)، $\lvert r \rvert^n (1 + h)^n = (\lvert r \rvert (1 + h))^n = 1^n = 1$، پس بنا بر ۴.۲(ث)، $\lvert r \rvert^n = 1/(1 + h)^n$. با بند ۵.۲، قسمت ۸ و قاعدهٔ وارون‌ها، که بر $0 \lt nh \lt (1 + h)^n$ اعمال می‌شود،

$$
\lvert r^n - 0 \rvert = \lvert r \rvert^n = \frac{1}{(1 + h)^n} \lt \frac{1}{nh} = \frac{1}{h} \cdot \frac{1}{n} .
$$

دنبالهٔ $(1/h)(1/n)$، بنا بر بند ۵.۳ و قاعدهٔ حاصل‌ضرب (بند ۵.۶)، به $(1/h) \cdot 0 = 0$ همگراست. نتیجهٔ قاعدهٔ ساندویچ (بند ۵.۹) با $d_n = (1/h)(1/n)$ حکم $r^n \to 0$ را به دست می‌دهد. ∎

برای $r = 1/2$، $h = 1$ و کران به صورت $(1/2)^n \lt 1/n$ درمی‌آید. در $n = 10$ کران برابر $1/10$ است، در حالی که $(1/2)^{10} = 1/2^{10} = 1/1024$ (جلسهٔ ۳، بند ۳.۷)، که از $1/1000$ کمتر است. این کران درشت است، ولی کرانی درشت که به $0$ میل کند تمام آن چیزی است که قاعدهٔ ساندویچ لازم دارد. برای $r = 1$ دنباله ثابت است و به $1$ همگراست؛ برای $r = -1$ دنباله همان $((-1)^n)$ است، که واگراست (بند ۵.۵)؛ تمرین ۶ به $\lvert r \rvert \gt 1$ می‌پردازد.

## ۵.۱۱ مثال حل‌شده

فرض کنید

$$
a_n = \frac{3n^2 + n}{2n^2 + 1} .
$$

مخرج در $2n^2 + 1 \ge 1 \gt 0$ صدق می‌کند، پس همهٔ جمله‌ها تعریف شده‌اند. جمله‌های نخست عبارت‌اند از $a_1 = 4/3$، $a_2 = 14/9$، $a_{10} = 310/201$ و $a_{100} = 30100/20001$. فاصله‌های آن‌ها تا $3/2$ برابر $1/6$، $1/18$، $17/402$ و $197/40002$ است، و این مقادیر حد $3/2$ را پیشنهاد می‌کنند. این را دو بار ثابت می‌کنیم: یک بار با قاعده‌ها، یک بار از روی تعریف.

**با قاعده‌ها.** صورت و مخرج را بر $n^2 \ne 0$ تقسیم کنید:

$$
a_n = \frac{3 + 1/n}{2 + 1/n^2} .
$$

1. $1/n \to 0$ (بند ۵.۳)، پس بنا بر قاعدهٔ جمع (بند ۵.۶)، $3 + 1/n \to 3 + 0 = 3$.
2. بنا بر قاعدهٔ حاصل‌ضرب، $1/n^2 = (1/n)(1/n) \to 0 \cdot 0 = 0$، پس بنا بر قاعدهٔ جمع، $2 + 1/n^2 \to 2$.
3. به‌ازای هر $n$، $2 + 1/n^2 \gt 0$، و حد $2$ برابر $0$ نیست. قاعدهٔ خارج‌قسمت (بند ۵.۷) نتیجه می‌دهد $a_n \to 3/2$.

**از روی تعریف.** نخست فاصله تا $3/2$ را دقیقاً محاسبه کنید:

$$
a_n - \frac{3}{2} = \frac{2(3n^2 + n) - 3(2n^2 + 1)}{2(2n^2 + 1)} = \frac{6n^2 + 2n - 6n^2 - 3}{4n^2 + 2} = \frac{2n - 3}{4n^2 + 2} .
$$

به‌ازای $n \ge 2$، $2n - 3 \ge 4 - 3 = 1 \gt 0$، پس $\lvert a_n - 3/2 \rvert = (2n - 3)/(4n^2 + 2)$. همچنین $2n - 3 \lt 2n$، و $4n^2 + 2 \gt 4n^2 \gt 0$. با ضرب کردن $2n - 3 \lt 2n$ در $1/(4n^2 + 2) \gt 0$، و سپس ضرب کردن $1/(4n^2 + 2) \lt 1/(4n^2)$، که از قاعدهٔ وارون‌ها به دست می‌آید، در $2n \gt 0$،

$$
\left\lvert a_n - \frac{3}{2} \right\rvert = \frac{2n - 3}{4n^2 + 2} \lt \frac{2n}{4n^2 + 2} \lt \frac{2n}{4n^2} = \frac{1}{2n} \qquad (n \ge 2) .
$$

اکنون فرض کنید $\varepsilon \gt 0$. هر $N \in \mathbb{N}$ با $N \ge 2$ و $N \ge 1/(2\varepsilon)$ مناسب است. در واقع، از $N \ge 1/(2\varepsilon)$ نتیجه می‌شود $2N \ge 1/\varepsilon \gt 0$، پس بنا بر قاعدهٔ وارون‌ها $1/(2N) \le \varepsilon$. به‌ازای $n \ge N$، از $0 \lt 2N \le 2n$ به همین ترتیب نتیجه می‌شود $1/(2n) \le 1/(2N)$، پس $\lvert a_n - 3/2 \rvert \lt 1/(2n) \le \varepsilon$. یک $N$ با این ویژگی وجود دارد: خاصیت ارشمیدسی یک $N_1 \in \mathbb{N}$ با $N_1 \gt 1/(2\varepsilon)$ به دست می‌دهد، و $N = \max\{2, N_1\}$ مناسب است.

برای $\varepsilon = 1/100$ شرط به صورت $N \ge 50$ است، و $N = 50$ مناسب است، زیرا $1/(2 \cdot 50) = 1/100$. بررسی در $n = 50$: $a_{50} = 7550/5001$، و $\lvert a_{50} - 3/2 \rvert = (2 \cdot 50 - 3)/(4 \cdot 2500 + 2) = 97/10002$، که از $1/100$ کمتر است، زیرا $100 \cdot 97 = 9700 \lt 10002$. همین فرمول در $n = 10$ مقدار $17/402$ را می‌دهد، که با $a_{10} - 3/2 = 310/201 - 3/2 = (620 - 603)/402$ سازگار است.

دو اثبات با هم سازگارند، همان‌گونه که بند ۵.۴ می‌گوید باید باشند. قاعده‌ها حد را به‌سرعت به دست می‌دهند. تعریف بیشتر به دست می‌دهد: یک $N$ صریح برای هر $\varepsilon$.

## تمرین‌ها

*بررسی*

1. فرض کنید $a_n = \dfrac{2n + 1}{n + 3}$. از روی تعریف نشان دهید که $a_n \to 2$. برای $\varepsilon = 1/10$، کوچک‌ترین $N$ را بیابید که به‌ازای هر $n \ge N$، $\lvert a_n - 2 \rvert \lt 1/10$.
2. با قاعده‌های بندهای ۵.۳، ۵.۶ و ۵.۷، $\lim_{n \to \infty} \dfrac{n^3 - 2n}{4n^3 + n^2 + 1}$ را بیابید و هر گام را توجیه کنید.
3. با بند ۵.۱۰ و قاعده‌ها، $\lim_{n \to \infty} \dfrac{1 + (1/2)^n}{3 - (2/3)^n}$ را بیابید. نخست بررسی کنید که مخرج هرگز صفر نمی‌شود.

*اثبات*

4. ثابت کنید اگر $a_n \to a$ آنگاه $\lvert a_n \rvert \to \lvert a \rvert$. با یک مثال نشان دهید که $\lvert a_n \rvert$ ممکن است همگرا باشد در حالی که $(a_n)$ واگراست، و ثابت کنید $a_n \to 0$ اگر و تنها اگر $\lvert a_n \rvert \to 0$.
5. ثابت کنید اگر $a_n \to 0$ و $(b_n)$ کران‌دار باشد، آنگاه $a_n b_n \to 0$، حتی وقتی $(b_n)$ واگرا باشد. این را دربارهٔ $(-1)^n / n$ به کار ببرید. توضیح دهید چرا قاعدهٔ حاصل‌ضرب بند ۵.۶ این را به دست نمی‌دهد.
6. ثابت کنید اگر $\lvert r \rvert \gt 1$، آنگاه $(r^n)$ بی‌کران است و بنابراین واگراست.

*فراتر*

7. (میانگین‌ها.) فرض کنید $a_n \to a$، و $s_n = (a_1 + a_2 + \dots + a_n)/n$. ثابت کنید $s_n \to a$. سپس نشان دهید که برای $a_n = (-1)^n$ میانگین‌های $s_n$ همگرایند، هرچند $(a_n)$ همگرا نیست.
8. (نسبت‌ها.) فرض کنید به‌ازای هر $n$، $a_n \gt 0$ و $a_{n+1}/a_n \to L$ با $L \lt 1$. ثابت کنید $a_n \to 0$. با استفاده از این، نشان دهید $n/2^n \to 0$. سپس دو دنباله با جمله‌های مثبت و $a_{n+1}/a_n \to 1$ ارائه کنید، که یکی به $0$ همگرا باشد و دیگری نباشد.

حل‌ها: [solutions/005-limits-of-sequences.md](../solutions/005-limits-of-sequences.md).
