# Farsi edition: conventions and glossary

The Farsi edition is a translation of the English text, sentence by sentence. It adds nothing, drops nothing and moves nothing: every step, citation, example and exercise of the English stays, in the same place. The voice is the English voice in Farsi: calm, exact, plain and formal written Persian (نثر علمی معیار), in short declarative sentences, with no hype. Use the standard words of Iranian university mathematics textbooks.

## Files

- Session n in Farsi is `fa/sessions/NNN-slug.md`; its solutions are `fa/solutions/NNN-slug.md`. The English file is the source.
- The solutions link at the end of a session reads `حل‌ها: [solutions/NNN-slug.md](../solutions/NNN-slug.md).` (the same relative path as in English; it resolves inside `fa/`).
- Run `python3 plan/check_fa.py N` from the book folder; it must report 0 errors.
- The Farsi title and claim of every session, the Part titles and goals, and the gap notes are in `plan/fa.json` (`sessions.<slug>.title`, `.claim`, `.gap`; `parts.<id>`). A new translation adds its session's entry there; the heading of the Farsi file must use the same title.

## Mathematics

- **Every formula is copied exactly** from the English: each `$...$` and each `$$` block, character for character. Do not change symbols, letters, spacing or line breaks inside them. The only exception: the words inside `\text{...}` may be translated into Farsi (for example `\text{for every } n` becomes `\text{به‌ازای هر } n`). The checker compares the formulas after removing `\text{...}`.
- Inline order may change with Farsi word order, but no formula is added, removed or split.
- `$$` stands on a line of its own, as in English.

## Digits and numbering

- In prose, use Persian digits (۰۱۲۳۴۵۶۷۸۹): «جلسهٔ ۵»، «بند ۵.۲»، «تمرین ۷». Inside formulas the digits stay as they are.
- Session heading: `# ۱.۵. حد دنباله‌های حقیقی` (Part.Session in Persian digits, then the title from `plan/fa.json`).
- Section headings: `## ۵.۲ قدر مطلق` (same numbers as English, Persian digits, Latin full stop between them).
- Markdown list markers stay ASCII (`1.`, `2.`), because Markdown needs them; the reader shows them in Persian digits.
- Lemma numbers, parts of results and exercise numbers in prose: Persian digits («لم ۴(الف)» for "Lemma 4(a)"; parts (a), (b), (c) become (الف)، (ب)، (پ), and (d), (e), (f) become (ت)، (ث)، (ج)).
- Labels in parentheses such as (S1), (P2), (R), (O1), (M3), (Q1) stay in Latin as they are, because formulas and other sessions cite them.

## References to other sessions

The reader turns these into links, so write them exactly in these forms:
- one session: «جلسهٔ ۷»
- several: «جلسه‌های ۳ و ۴»، «جلسه‌های ۳، ۴ و ۵»، «جلسه‌های ۳ تا ۵»
- a section: «بند ۵.۲» or «جلسهٔ ۵، بند ۵.۲»
- the syllabus: «جلسهٔ ۰» or «برنامهٔ درس»
- a Part: «بخش ۱۹» (Parts 1 to 26)

## Fixed phrases of the layout

| English | Farsi |
|---|---|
| Session | جلسه |
| Part | بخش |
| Section (5.2) | بند |
| *Theorem. Builds on Sessions 3 and 4.* | *قضیه. بر پایهٔ جلسه‌های ۳ و ۴.* |
| *Definition. Builds on Session 2.* | *تعریف. بر پایهٔ جلسهٔ ۲.* |
| *Survey. Builds on nothing earlier.* | *مرور. بر پایهٔ هیچ جلسهٔ پیشین.* |
| **Claim.** | **ادعا.** |
| **Recall.** / Recall (Session 2) | **یادآوری.** / یادآوری (جلسهٔ ۲) |
| **Definition.** | **تعریف.** |
| **Theorem (name).** | **قضیه (نام).** |
| **Lemma.** | **لم.** |
| **Corollary.** | **نتیجه.** |
| **Example.** | **مثال.** |
| **Notation.** | **نمادگذاری.** |
| *Proof.* ... ∎ | *اثبات.* ... ∎ |
| *Step 1:* | *گام ۱:* |
| Base case / Inductive step | حالت پایه / گام استقرا |
| What fails without ... / What fails | آنچه بدون ... برقرار نمی‌ماند / آنچه برقرار نمی‌ماند |
| Worked example | مثال حل‌شده |
| > **Gap.** Omitted: ... Why: ... Where: ... | > **شکاف.** حذف‌شده: ... چرا: ... کجا: ... |
| ## Exercises | ## تمرین‌ها |
| *Check* / *Prove* / *Extend* | *بررسی* / *اثبات* / *فراتر* |
| ## Problems | ## مسئله‌ها |
| Solutions: [link] | حل‌ها: [link] |
| # Solutions to 1.5. Title | # حل تمرین‌های ۱.۵. عنوان |
| ## Check / ## Prove / ## Extend (solutions) | ## بررسی / ## اثبات / ## فراتر |
| (Hint: ...) | (راهنمایی: ...) |

## Glossary

Use these words, the same everywhere. A term not listed: use the standard term of Iranian university textbooks.

**English glosses.** A technical term that has no well-established Persian word in the Persian literature gets its English in parentheses on its first use in each session (and in each solutions file), with a space before the parenthesis: «میدان مرتب کامل (complete ordered field)»، «پیش‌نگاره (preimage)»، «برآمد (outcome)». Terms that every Persian textbook uses (حد، دنباله، تابع، مشتق، پیوسته، مجموعه) get no gloss. Later uses in the same session carry no gloss.

**Logic and proof.** statement گزاره · truth value ارزش درستی · true / false درست / نادرست · negation نقیض · conjunction عطف · disjunction فصل · implication استلزام (گزارهٔ شرطی) · biconditional دوشرطی · hypothesis / conclusion (of an implication) مقدم / تالی · hypothesis (of a theorem) فرض · conclusion (of a theorem) حکم · vacuously true به‌طور تهی درست · logically equivalent هم‌ارز منطقی · truth table جدول درستی · connective رابط · compound statement گزارهٔ مرکب · contrapositive عکس نقیض · converse عکس · direct proof اثبات مستقیم · proof by contraposition اثبات با عکس نقیض · proof by contradiction برهان خلف · proof by cases اثبات به‌روش حالت‌ها · quantifier سور · for every به‌ازای هر · there exists وجود دارد · if and only if اگر و تنها اگر · De Morgan's laws قوانین دمورگان · counterexample مثال نقض · without loss of generality بدون کاستن از کلیت.

**Sets and functions.** set مجموعه · element عضو · subset زیرمجموعه · empty set مجموعهٔ تهی · union اجتماع · intersection اشتراک · difference تفاضل · complement متمم · ordered pair زوج مرتب · Cartesian product ضرب دکارتی · function تابع · domain دامنه · codomain هم‌دامنه · range برد · image تصویر · preimage پیش‌نگاره · graph نمودار · injective یک‌به‌یک · surjective پوشا · bijection دوسویی · inverse وارون · composition ترکیب · identity function تابع همانی · restriction تحدید · set-builder notation نماد مجموعه‌ساز · finite / infinite متناهی / نامتناهی.

**Numbers.** number عدد · natural numbers اعداد طبیعی · integers اعداد صحیح · rational numbers اعداد گویا · real numbers اعداد حقیقی · numeral رقم‌نویسی (نام عدد) · inductive set مجموعهٔ استقرایی · principle of induction اصل استقرا · induction hypothesis فرض استقرا · definition by recursion تعریف بازگشتی · recursion theorem قضیهٔ تعریف بازگشتی · well-ordering خوش‌ترتیبی · least element کوچک‌ترین عضو · parity زوجیت · even / odd زوج / فرد · sum مجموع · product حاصل‌ضرب · empty sum / empty product مجموع تهی / حاصل‌ضرب تهی · telescoping تلسکوپی · power توان · factorial فاکتوریل · binomial coefficient ضریب دوجمله‌ای · binomial theorem قضیهٔ دوجمله‌ای · Pascal's rule قاعدهٔ پاسکال · Pascal's triangle مثلث پاسکال · Bernoulli's inequality نابرابری برنولی · geometric sum مجموع هندسی · difference of powers تفاضل توان‌ها · integer part جزء صحیح · decimal عدد اعشاری.

**Order and the reals.** field میدان · ordered field میدان مرتب · axiom اصل موضوع · trichotomy سه‌گانگی · upper / lower bound کران بالا / کران پایین · bounded above / below از بالا / از پایین کران‌دار · least upper bound کوچک‌ترین کران بالا · greatest lower bound بزرگ‌ترین کران پایین · supremum / infimum سوپریمم / اینفیمم · maximum / minimum بیشینه / کمینه · least-upper-bound property خاصیت کوچک‌ترین کران بالا · Archimedean property خاصیت ارشمیدسی · approximation property خاصیت تقریب · interval بازه · closed / open interval بازهٔ بسته / بازهٔ باز · endpoint نقطهٔ انتهایی · half-line نیم‌خط · length طول · dense چگال · absolute value قدر مطلق · triangle inequality نابرابری مثلث · reverse triangle inequality نابرابری مثلث وارون · rule for reciprocals قاعدهٔ وارون‌ها.

**Sequences and limits.** sequence دنباله · real sequence دنبالهٔ حقیقی · term جمله · converges to همگراست به · convergent / divergent همگرا / واگرا · limit حد · bounded / unbounded کران‌دار / بی‌کران · tail دم · squeeze rule قاعدهٔ ساندویچ (فشردگی is compactness) · monotone یکنوا · nondecreasing / nonincreasing نانزولی / ناصعودی · strictly increasing اکیداً صعودی · subsequence زیردنباله · Cauchy sequence دنبالهٔ کوشی · monotone convergence theorem قضیهٔ همگرایی یکنوا · Bolzano-Weierstrass theorem قضیهٔ بولتسانو-وایرشتراس · peak قله · geometric sequence دنبالهٔ هندسی · contractive sequence دنبالهٔ انقباضی.

**Functions of a real variable.** continuous پیوسته · continuity پیوستگی · continuous at a point پیوسته در یک نقطه · sequential characterisation توصیف دنباله‌ای · bounded function تابع کران‌دار · extreme value theorem قضیهٔ مقدار فرین · intermediate value theorem قضیهٔ مقدار میانی · n-th root ریشهٔ nام · polynomial چندجمله‌ای · coefficient ضریب · zero (of a function) صفر (تابع) · rational function تابع گویا · accumulation point نقطهٔ انباشتگی · limit of a function حد تابع · derivative مشتق · differentiable مشتق‌پذیر · sum, product, quotient and chain rules قاعده‌های جمع، حاصل‌ضرب، خارج‌قسمت و زنجیره‌ای · interior point نقطهٔ درونی · extremum فرین · local maximum / minimum بیشینهٔ موضعی / کمینهٔ موضعی · Rolle's theorem قضیهٔ رل · mean value theorem قضیهٔ مقدار میانگین · constant function تابع ثابت.

**Countable sets.** countable شمارا · uncountable ناشمارا · enumeration شمارش · countable union اجتماع شمارا · axiom of countable choice اصل انتخاب شمارا · nested intervals بازه‌های تودرتو · jump جهش.

**Physics words in Session 1.** observation مشاهده · action کنش · measurement اندازه‌گیری · system سیستم · apparatus دستگاه · formalism صورت‌بندی · state حالت · observable مشاهده‌پذیر · instrument (quantum) ابزار اندازه‌گیری (instrument) · channel کانال · Born rule قاعدهٔ بورن · realism واقع‌گرایی · local realism واقع‌گرایی موضعی · locality موضعیت · local causality علیت موضعی · ontic state حالت هستی‌شناختی · ontological model مدل هستی‌شناختی · measurement independence استقلال اندازه‌گیری · verify / verifying بررسی کردن · unverifiable (Q3) تحقیق‌ناپذیر (unverifiable) · trade-off بده‌بستان (in Session 1 said in plain words) · informal غیرصوری (informal) · singlet حالت تکتایه (singlet) · contextuality زمینه‌مندی · macrorealism ماکرو-واقع‌گرایی · Heisenberg cut برش هایزنبرگ · decoherence ناهمدوسی · entanglement درهم‌تنیدگی · composite system سیستم مرکب · local friendliness دوستی موضعی (local friendliness) · quantum reference frame چارچوب مرجع کوانتومی · interpretation تعبیر.

## Names and references

- People: Persian spelling, with the Latin name in parentheses on first use in a session: «ددکیند (Dedekind)»، «پاسکال (Pascal)»، «برنولی (Bernoulli)»، «کانتور (Cantor)»، «رودین (Rudin)».
- Titles of books and papers stay in their original language and script.
- The names of the questions Q1, Q2, Q3 stay in Latin.

## Writing

- Use the zero-width non-joiner correctly: «می‌شود»، «دنباله‌ها»، «به‌ازای»، «بزرگ‌ترین».
- Persian punctuation: comma «،»، semicolon «؛»، question mark «؟»، quotation marks «».
- Never «بدیهی است»، «واضح است»، «به‌سادگی دیده می‌شود»، «به‌آسانی»، «می‌توان نشان داد» or the like, as the English never says "clearly" or "it can be shown".
- Bold marks a term where it is defined, as in English; italics mark the names of recalled results.

## Settled terms

Chosen after the first translations, to make the edition consistent. These override any other choice.

- **Parts of a result.** "Part 3" of a lemma or theorem, or "Section 5.2, Part 9": «قسمت ۳». Never «بخش» (a Part of the book) or «جزء» (a part of a composite system). "Part (a)" of an exercise: «قسمت (الف)».
- **Lettered labels.** (a) الف, (b) ب, (c) پ, (d) ت, (e) ث, (f) ج, (g) چ, (h) ح; so 4.2(d) is «۴.۲(ت)». Roman labels (i), (ii) and capital labels (A), (B), (D), (S1), (M3), (O1) stay in Latin.
- **Bare section numbers** in prose take «بند»: «بند ۱۰.۲». "§126" of an old book stays «§۱۲۶».
- **Recalled results, as cited:** «قوانین توان‌ها»، «قاعدهٔ ساندویچ» and «نتیجهٔ قاعدهٔ ساندویچ»، «نتیجهٔ مربوط به توان‌ها و چندجمله‌ای‌ها»، «لم دم‌ها»، «لم رشد اندیس‌ها»، «لم مقایسه»، «لم زوجیت»، «لم گام‌های صحیح»، «قضیهٔ تعریف بازگشتی»، «آزمون همگرایی»، «یکتایی حد»، «اصل موضوع کمال»، «میدان مرتب کامل».
- **Words.** criterion محک (sequential criterion محک دنباله‌ای, Cauchy criterion محک کوشی) · test آزمون · functions (plural) توابع · nonempty / nonzero / nonnegative ناتهی / ناصفر / نامنفی · strict / non-strict اکید / نااکید · uniqueness یکتایی · square root ریشهٔ دوم · numerator / denominator صورت / مخرج · identity (algebraic) اتحاد · exponent نما · disjoint جدا از هم · well defined خوش‌تعریف · outcome برآمد · setting تنظیم · feedback پس‌خورد · paragraph پاراگراف · compact / compactness فشرده / فشردگی · postulate اصل موضوع · Excursion گشت جانبی.
- **Later Parts.** self-adjoint خودالحاقی · orthonormal متعامدیکه · trace اثر · pure / mixed state حالت خالص / آمیخته · reduced state حالت کاهیده · separable جدایی‌پذیر · homomorphism همریختی · master equation معادلهٔ مادر · no-signalling عدم علامت‌دهی · no-cloning عدم همانندسازی · teleportation تله‌پورت کوانتومی · noncontextual / noncontextuality نازمینه‌مند / نازمینه‌مندی · psi-ontic / psi-epistemic psi-هستی‌شناختی / psi-معرفت‌شناختی · fine-tuning تنظیم ظریف · proper / improper mixture آمیزهٔ سره / ناسره · pointer عقربه · record ثبت · loophole روزنه.
- **Names.** Bolzano بولتسانو · Weierstrass وایرشتراس · Cauchy کوشی · Dedekind ددکیند · Cantor کانتور · Rudin رودین · Bernoulli برنولی · Pascal پاسکال · Archimedes ارشمیدس · Stolz اشتولتس · Rolle رل · Lagrange لاگرانژ · Fermat فرما · Kochen-Specker کوخن-اشپکر · Frauchiger فراوخیگر · Renner رنر · Brukner بروکنر · Breuer برویر · Leggett-Garg لگت-گارگ.
