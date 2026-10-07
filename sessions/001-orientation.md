# 1.1. What this book builds, and the three questions it is aimed at

*Survey. Builds on nothing earlier.*

**Claim.** The book is aimed at three questions, stated here in ordinary words. None of them can be posed precisely until the formalism of quantum mechanics, its mathematical definitions of state, measurement and change in time, has been built, and this session names the Parts that each one needs.

## 1.1 The three questions

The three questions are these.

- **Q1.** Whether observation and action can be simultaneous.
- **Q2.** Whether measurement can be done from outside a system.
- **Q3.** Whether local realism could be true but unverifiable.

Their key words ("observation", "outside", "realism") have several possible meanings, and the answer depends on the meaning chosen.

**Example.** Take the question "Is 1 between 0 and 1?". If "$x$ is between 0 and 1" means $0 \lt x \lt 1$, the answer is no, because $1 \lt 1$ is false. If it means $0 \le x \le 1$, the answer is yes, because $0 \le 1$ and $1 \le 1$ are both true. The question has one answer only once "between" is defined. Q1, Q2 and Q3 are questions of this kind.

The book gives each key word a definition, so that each question becomes a list of statements, each of which can be proved or refuted. It then proves or refutes them.

## 1.2 Why the formalism comes first

The questions are taken in the order Q1, Q3, Q2, the order in which the book treats them, for the reasons given in Section 1.3.

This section names objects that later Parts define. They are names only: no later proof uses them as premises from this session, and the reader is not expected to know what they mean yet. Each name comes with the Part that defines it or with a short gloss.

**Q1.** To ask whether observation and action can be simultaneous, one must say what an observation does to the system observed and what counts as an action on it. In quantum mechanics both are described by one object, an instrument (Part 17), which assigns to each outcome a probability and a change of the state. Since one instrument produces both the outcome and the change of state, "observation and action are simultaneous" can be read as "a single instrument produces both the outcome wanted and the change wanted". Q1 then becomes a set of questions about instruments: what their outcomes can reveal, and what changes of state must come with them. These questions need not have the same answer:

- whether two given observables (measurable quantities, Part 7) can be measured jointly;
- how the error in measuring one quantity trades against the disturbance of another;
- how much information can be gained about a state for a given change of it (Part 18);
- whether a measurement can leave the measured quantity unchanged;
- what a conservation law forbids a measurement to do;
- what feedback, an action chosen according to an outcome, can achieve.

None of these can be asked before states and observables (Part 7), and instruments and channels (the most general changes of state, Part 17), have been defined.

**Q3.** "Local realism" joins two assumptions, and "unverifiable" needs a definition of its own.

*Realism.* In the form the literature uses, realism says that a system has a state, its ontic state, which together with the measurement chosen fixes the probabilities of the outcomes. Its precise form is an ontological model (Part 20).

*Locality.* Locality says that an outcome in one place does not depend on a setting chosen so far away that no signal could connect them. Bell's local causality (Part 20) turns this into a condition on probabilities. A local model, defined in Part 20, needs only the probability of Part 6; what needs the formalism is the question whether such a model can reproduce what quantum mechanics predicts.

*Unverifiable.* Verifying needs an experiment, a statistical test of its data, and a list of the assumptions under which the test is valid. If an assumption of the test cannot itself be tested, the data cannot rule out a local realist model that breaks it. Measurement independence (Part 20) is such an assumption. It says that the distribution of the ontic state does not depend on the settings, and a theorem of Part 21 shows that without it a local model can reproduce every observed correlation.

*Beyond locality.* Realism also raises questions that do not involve locality: whether an ontological model must let an outcome depend on which other quantities are measured with it (contextuality, the Kochen-Specker theorem), and whether its ontic state must determine the quantum state (the PBR theorem). Part 22 treats both, because a local model is one kind of ontological model, and these are further ways in which an ontological model can be ruled out. A third, macrorealism for a single system observed at several times, is the subject of the Leggett-Garg sessions in Part 19.

Each of these compares a class of models with the predictions of quantum mechanics, for single systems and for systems of several parts. So none can be posed before states, observables and the Born rule (Part 7) and composite systems (Part 13) have been built.

**Q2.** "Outside a system" presupposes a boundary between the system and the rest of the world. In the formalism, a measurement is an interaction between the system and an apparatus (Part 19), and the apparatus can itself be described as a quantum system. The boundary between what is described as a quantum system and what is treated as the observer is the Heisenberg cut, defined in Part 23. Part 23 shows that, in a chain of devices each of which records the outcome of the one before, the cut can be placed after any completed record without changing the predicted state of the chain. Q2 then asks what can be known when the observer, too, is placed inside the description. Its precise forms are the movability of the cut (Part 23) and the questions answered in Part 24 by Breuer's theorem on measurement from inside, by the arguments of Frauchiger and Renner and of Brukner about observers modelled as quantum systems, by local friendliness, and by the dependence of a state on the quantum reference frame chosen. These need composite systems, the state of one part of a composite system (Part 14), decoherence (Part 23), and the Bell scenarios of Part 20, in which two distant parties each choose a setting.

## 1.3 Which Parts each question needs

| Question | Main Parts | Where it is restated precisely |
|---|---|---|
| Q1 | 19 | at the end of Part 19 |
| Q3 | 20, 21 and 22 | at the end of Part 22 |
| Q2 | 23 and 24 | at the end of Part 24 |
| all three | 26 | in Part 26, each informal word matched to a defined object |

Q1 comes first because it can be posed for a single system and the device that measures it, with no question of distance between systems. Q3 comes next because its central case, Bell's, needs two or more separated systems and the assumptions of an ontological model. Q2 comes last because some of its precise forms, such as local friendliness, are compared directly with the locality conditions of Q3.

Each restatement is a list of precise statements, each with its assumptions.

Parts 1 to 18 build the formalism these Parts use; the question Parts also build on one another, and Q2 uses the Bell scenarios of Part 20. Parts 1 to 6 are mathematics: limits, complex numbers and groups, linear algebra through the spectral theorem, and finite probability. The physics begins in Part 7 with the postulates for a single system. After that, Parts of mathematics (8, 10, 11, 12 and 16) come between Parts of physics, each placed before the first physics that uses it. The Parts of physics add dynamics, composite systems, entanglement, entropy, measurements and channels. Part 25 sets out the main interpretations.

## 1.4 How to use the book

- **The syllabus** is the book's zeroth session. It lists every session with the one claim it establishes and the earlier sessions it builds on, and it lists every labelled gap.
- **A session** opens with its kind (definition, theorem, construction, calculation, example, experiment, survey or problems), the sessions it builds on, and its one claim, which the rest of the session earns. It uses only results established in earlier sessions. A survey, such as this one, may name objects defined later, but it uses none of them as a premise.
- **Gaps.** Where a proof is omitted, a box headed **Gap** says what is omitted, why, and where a complete proof can be found.
- **A Part** opens with a page that lists every result from an earlier Part that its sessions use, each with its session number and statement. A reader who knows a topic can skip its Part and use that page to check what is assumed.
- **Exercises** come in three tiers, *Check*, *Prove* and *Extend*, with full solutions in a separate volume. Those for this session are below.

The next session begins the mathematics of Part 1 with sets, functions and the forms of proof.

## Exercises

*Check*

1. Take the question "Is the list 2, 2, 2 increasing?". Under meaning A, a list is increasing if each term after the first is greater than the one before it. Under meaning B, it is increasing if each term after the first is at least the one before it. Answer the question under each meaning, giving the comparisons that decide it.

*Prove*

2. Take the two meanings of "$x$ is between 0 and 1" from the example in Section 1.1: meaning A is $0 \lt x \lt 1$, and meaning B is $0 \le x \le 1$. Use only these facts about real numbers $a$ and $b$: exactly one of $a \lt b$, $a = b$ and $b \lt a$ holds; $a \le b$ means "$a \lt b$ or $a = b$"; and $0 \lt 1$.
   1. Show that every $x$ that is between 0 and 1 under meaning A is between 0 and 1 under meaning B.
   2. Show that the two meanings give different answers for a real number $x$ if and only if $x = 0$ or $x = 1$.

*Extend*

3. A reference clock times an observation at 3000 ms and an action at 3040 ms (1 ms is a thousandth of a second). Take two meanings of "simultaneous": (a) the two times are equal; (b) the two times differ by less than 100 ms, the smallest difference a second, coarser clock can detect.
   1. Answer "Were the observation and the action simultaneous?" under each meaning.
   2. Three events are timed at 3000 ms, 3060 ms and 3120 ms. Show that under meaning (b) the first is simultaneous with the second and the second with the third, but the first is not simultaneous with the third. Under meaning (a), can this happen?

Solutions: [solutions/001-orientation.md](../solutions/001-orientation.md).
