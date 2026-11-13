# Continue PHYS 200 Quiz 1 prep

**Learner**

lets walk through Q2 together, develop a systematic method

**Tutor**

Yes. A systematic method is to **express the same event’s position in the ground frame using each moving frame, then equate the expressions.**

For either frame:
\[
\text{ground position}
=
\text{ground position of its origin}
+
\text{signed displacement from that origin}.
\]
The displacement’s sign depends on which way that frame’s positive axis points.

We’ll build this one step at a time.

A starts at \(x=80\,\mathrm m\) and moves left at \(6\,\mathrm{m/s}\). B starts at \(x=-20\,\mathrm m\) and moves right at \(4\,\mathrm{m/s}\).

**Write the ground positions of their origins at time \(t\):**
\[
x_A(t)=\,?
\qquad
x_B(t)=\,?
\]

---

**Learner**

first of all how do i systematically draw it

**Tutor**

Draw a **snapshot at \(t=0\)** first. Use three stacked axes, all aligned to the same physical left–right direction:

```text
Ground S:   ←───────●────────●───────────────●──────→ +x
                 −20        0              80
                  B                         A

Frame B:           O″────────────────────────────→ +x″
                   → 4 m/s

Frame A:    +x′ ←───────────────────────────O′
                                            ← 6 m/s
```

Systematically:

1. **Choose the ground direction:** right is \(+x\).
2. **Place the origins using ground coordinates:** B at \(-20\,\mathrm m\), A at \(80\,\mathrm m\).
3. **Draw each positive axis separately:** B’s points right; A’s points left.
4. **Add velocity arrows:** these show where the origins move, independently of their axis directions.

The stacked lines are just for readability—all three describe the same line in space.

**Draw this initial snapshot first.** Then we’ll draw it at a general time \(t\) and place an arbitrary event on it.

---

**Learner**

lets do variations of 2, using where the starting L is 0. lets do a couple of those first

**Tutor**

We’ll start with both origins at the ground origin at \(t=0\), so there’s no initial offset. I’ll keep the original Q2 marked unfinished while we practise these two variations.

---

**Learner**

i never used A and B

**Tutor**

You’re right—let’s use your \(x'\) and \(x''\) labels.

In your formula,
\[
L=\text{initial position of the }x'\text{ origin}
-\text{initial position of the }x''\text{ origin},
\]
measured positive to the right.

So:

- \(x'\) origin starts **right of** \(x''\) origin → \(L>0\).
- \(x'\) origin starts **left of** \(x''\) origin → \(L<0\).

And \(V\) is the signed velocity of the **\(x''\) origin relative to the \(x'\) origin**, positive rightward.

---

**Learner**

simple example using our decision tree, you demonstrate, using my 1 2 3 step by step

**Tutor**

Suppose initially the **\(x'\) origin is 20 m right of the \(x''\) origin**. The \(x'\)-axis points **left**, the \(x''\)-axis points **right**, and the \(x''\) origin moves **left at \(3\,\mathrm{m/s}\) relative to the \(x'\) origin**.

Start with your template:
\[
x''=x'-Vt+L.
\]

**① Axis directions:** \(x'\) points left, so replace \(x'\) with \(-x'\). \(x''\) points right, so keep it:
\[
x''=-x'-Vt+L.
\]

**② Relative motion:** the \(x''\) origin moves left, so \(V=-3\,\mathrm{m/s}\):
\[
x''=-x'-(-3\,\mathrm{m/s})t+L.
\]

**③ Starting offset:** the \(x'\) origin starts 20 m right of the \(x''\) origin, so \(L=+20\,\mathrm m\):
\[
\boxed{x''=-x'+(3\,\mathrm{m/s})t+20\,\mathrm m.}
\]

---

**Learner**

it doesn't matter what sign x is? (units to the right=+L), (units to the left=-L). ok lets start independent practice now. one at a time, short and mixed.

**Tutor**

Yes—**for your decision tree, the offset uses physical right as positive**, regardless of either axis direction. Measure it from the \(x''\) origin **to the \(x'\) origin**: right gives \(+L\), left gives \(-L\).

**Generated**

At \(t=0\), the \(x'\) origin is **12 m left of** the \(x''\) origin.

- \(x'\) points right; \(x''\) points left.
- The \(x''\) origin moves **right at \(2\,\mathrm{m/s}\)** relative to the \(x'\) origin.

Find \(x''\) in terms of \(x'\) and \(t\).

---

**Learner**

for the previous question how do i use the shortcut method?

**Tutor**

Use **length contraction, then track the light and the moving ends** in the ground frame.

The train’s ground-frame length is
\[
L=300\sqrt{1-0.6^2}=240\,\mathrm m.
\]
At emission, each end is therefore **120 m from the lamp**.

**Front:** the light moves right at \(c\), while the front moves right at \(0.6c\):
\[
ct_{\mathrm F}=120\,\mathrm m+0.6ct_{\mathrm F}
\quad\Rightarrow\quad
t_{\mathrm F}=\frac{120\,\mathrm m}{0.4c}=10^{-6}\,\mathrm s.
\]

**Rear:** the light moves left at \(c\), while the rear moves right toward it:
\[
ct_{\mathrm R}=120\,\mathrm m-0.6ct_{\mathrm R}
\quad\Rightarrow\quad
t_{\mathrm R}=\frac{120\,\mathrm m}{1.6c}=2.5\times10^{-7}\,\mathrm s.
\]

Here \(c-0.6c\) and \(c+0.6c\) are **gap-closing rates measured in the ground frame**. Both light pulses still travel at speed \(c\).

---

**Learner**

ok. for these problems since we're preparing for quiz1, we want to use both if convienient, shortcut+ spacetime plot if inconvenient.&#x20;

lets keep going

**Tutor**

Got it—for Quiz 1, we’ll compare the shortcut and Lorentz methods when convenient; otherwise, use the shortcut with a spacetime plot.

**Continue — Generated**

A spaceship travels around a circle at constant **speed** relative to an inertial frame. Its captain says:

> “Our speed is constant, so our frame is inertial. A released, force-free object will remain stationary relative to the cabin.”

Is either claim correct? Explain briefly.

---

**Learner**

no, there is a perpendicular acceleration so velocity is not constant.&#x20;

and also no, in the ship things will accelerate to the edge

**Tutor**

Both conclusions are right. I’ll log this as a successful review of circular motion and inertial frames, with one clarification about the object’s path.

---

**Learner**

we should be emphasizing course questions at this point, no? how come you use so many generated problems

**Tutor**

Yes. I let the generated practice continue too long after the targeted Galilean drills. Your guidelines prioritize course questions at this stage. I’ll replace the unattempted particle question with an in-scope course question now.

---

**Learner**

i dont understand how this is wrong, in earth's frame people age 25 years, in her frame she ages 15 years

**Tutor**

**Yes—between 2075 and 2100, people on Earth age 25 years and Fran ages 15 years. That part is correct.**

But your diagram’s top event is **her return to Earth**, which might happen **before 2100**.

For example, suppose she returns in 2095:

| Interval | Earth aging | Fran aging |
|---|---:|---:|
| Trips, 2075–2095 | 20 years | 10 years |
| Back on Earth, 2095–2100 | 5 years | 5 years |
| **Total** | **25 years** | **15 years** |

These are illustrative numbers, but they show the distinction: **15 years of total aging doesn’t mean 15 years aboard the ship.**

You can label the final event with **25 and 15** if it represents **2100**—but then your diagram needs a stay-on-Earth segment after her return. The moving-trip equation applies only up to her return.

---

**Learner**

give the question again, and get ready to handhold me throughout this question

**Tutor**

**Course**

In 2075, Fran is **28 years old**. She wants to join a mission in **2100**, but would ordinarily be too old to qualify. She signs up for **two round trips to Alpha Centauri**, which is **4.36 light-years from Earth**.

Assuming a constant travel speed:

1. What fraction of \(c\) must the ship travel at for Fran to be **10 years younger in 2100 than she otherwise would be**?
2. Will she return in time for the mission?

We’ll work through it **one step at a time**, checking each step before continuing.

**First step only:** Two round trips consist of how many one-way legs, and what total distance does Fran travel in Earth’s frame?

---

**Learner**

Let's first check if my space-time is correctly labeled. So she takes four trips. She starts in 2075, and she ends up In 2100. In Earth, ten years younger than she would otherwise be. So she would age 25 years if she were at Earth, and she only ages 15 years when she's back on Earth.

**Tutor**

**Your four-leg path is correct.** The distinction is between **returning to Earth** and **reaching the year 2100**.

- **At 2100:** Earth has aged 25 years, and Fran must have aged 15 years.
- **At her return:** we don’t yet know either elapsed time.

So if the top of your zigzag is **her return**, label Earth’s elapsed time there **\(T\)**, not 25 years. You can then extend her worldline **vertically along Earth’s position** from her return to 2100.

Your statement becomes correct with one change: **“She has aged 15 years by 2100,”** rather than necessarily **“when she gets back.”**

For now, just relabel the zigzag’s top as **return, \(t=T\)**.

---

**Learner**

ok lets keep going on with this proposal, using my equations, what's the step at which i should look and go oh shit soemthing is wrong

**Tutor**

**Right after you obtain \(\beta=0.758\)**—that’s where you check whether your result fits your proposed **25-year Earth duration**.

Using your speed, the four legs take
\[
T=\frac{4L}{\beta c}
=\frac{4(4.36\,\mathrm{ly})}{0.758c}
\approx23.0\,\mathrm{yr}.
\]

**“Wait—I labelled the arrival as 25 years, but my calculated speed gets her home in 23 years.”**

Your equation used **her 15 years** and **the total distance \(4L\)**. It never enforced your other label, **Earth’s 25 years**. This check exposes the incompatibility.

So your algebra is fine; **the two arrival-time labels cannot both hold for this journey.**

---

**Learner**

no but from her perspective she is not travelling that much, maybe that why for her she can return having aged only 15 years

**Tutor**

**Yes—she measures a shorter travel distance, and your equation already accounts for that.** At your speed \(0.758c\), she really can complete the trips while aging only **15 years**.

The **23 years** we calculated uses Earth’s distance and Earth’s speed, so it is **Earth’s elapsed time**. These describe the same return event:

- Earth: **23 years elapsed** → return in **2098**.
- Fran: **15 years aged** → she is **43** at return.

So your calculation is physically consistent. The mismatch is only with the question: she then ages another **2 years on Earth**, making her **45 in 2100**, rather than the required **43**.

**Length contraction explains how she ages 15 years during the trips. It doesn’t make her return happen in Earth’s year 2100.**

---

**Learner**

according to the wording, i would either arrive at 2100 being 10 years younger exactly, or arrive BEFORE 2100, being 10 years younger

**Tutor**

**Yes—exactly. Either would satisfy the wording:**

- Arrive **in 2100**, having aged 10 years less than if she had stayed on Earth.
- Arrive **before 2100**, already having aged 10 years less; that difference persists while she waits on Earth.

So **your interpretation is right**. We just cannot choose “exactly in 2100” in advance—the fixed travel distance and required 10-year aging difference determine her return time. Then we check whether it is **at or before 2100**.

---

**Learner**

maybe i should do shortcut method, the algebra is still quite messy

**Tutor**

**Yes—the shortcut makes the algebra cleaner here.** Keep your diagram and corrected time labels.

Equal speeds on all four legs let us write
\[
T-10\,\mathrm{yr}=T\sqrt{1-\beta^2}.
\]
Since \(\beta=4L/(cT)\), and \(4L/c=17.44\,\mathrm{yr}\),
\[
T-10\,\mathrm{yr}
=T\sqrt{1-\frac{(17.44\,\mathrm{yr})^2}{T^2}}.
\]

**Next step only: square both sides.** The outside \(T^2\) will cancel the denominator inside.

---

**Learner**

which week is this q from?

**Tutor**

**Week 2, PS2** — “Staying young,” on page 3 of the course’s *Relativity practice problems*.

---

**Learner**

are questions from the lorentz transformations sections easier on the algebra? cuz this is quite a bit of algebra

**Tutor**

**Often, yes—when the speed and event coordinates are given.** Those Lorentz questions can be straightforward substitution into two equations.

This question is harder algebraically because **both the speed and travel time are unknown**, and the speed also appears inside \(\gamma\). Using Lorentz transformations doesn’t remove that difficulty.

The shortcut here is shorter than it looks: **square once, and the \(T^2\) terms cancel**, leaving a linear equation in \(T\).

So a question from a later Lorentz section can absolutely be easier than this Week 2 question. **Week order isn’t difficulty order.**

---

**Learner**

go have a look

**Tutor**

I’ll compare the actual Lorentz-section questions with this one and check how much algebra they require.

---

**Learner**

how could have known that the algebra was so shitty that its best to go straight to shortcut method? which method should i pick?&#x20;

**Tutor**

**You weren’t expected to predict the algebra. I should have helped you choose sooner.** The clue is what the question asks you to calculate.

For Quiz 1, use this order:

| What you need | First method to try |
|---|---|
| Aging or elapsed time on a travelling clock | **Time dilation** |
| Length or separation measured in another frame | **Length contraction** |
| When light meets a moving endpoint | **Length contraction + motion equations**, with a spacetime sketch |
| Coordinates of an event in another frame, or which separated events are simultaneous | **Lorentz transformations**, if useful |

**For Fran:** the requested age saving compares accumulated clock times. That points directly to time dilation. Equal speed magnitudes on all four legs let you combine them:
\[
\tau=T/\gamma,\qquad T-\tau=10\,\mathrm{yr}.
\]
Then distance supplies \(vT=4L\).

Your equivalent straight-trip construction is valid, but it introduces event coordinates and a transformation just to recover that same clock relationship.

**Practical switching rule:** if you’re inventing an equivalent journey or tracking coordinate offsets merely to find someone’s aging, pause and try time dilation first. If a shortcut leaves you unsure which events it connects, draw the events before calculating.

These “shortcuts” are exact under the problem’s assumptions—they’re the natural first methods for this quiz.

---

**Learner**

for this coming quiz, though, should i be exclusively practising shortcut method + spacetime diagram for clarity?

**Tutor**

**Yes—as your default through Friday.** Given your stated quiz scope, focus on **course questions using time dilation, length contraction, and ordinary motion equations**, with spacetime diagrams when they clarify events.

For now:

- **Make your first attempt without Lorentz transformations.**
- **Use diagrams purposefully**, especially for separated events, light signals, or changing direction; simple questions don’t need one.
- **Pause the routine “solve it both ways” comparisons.** Use Lorentz only if it quickly resolves a specific confusion.

The priority is independently choosing the right events, frame, and clock—not practising extra transformation algebra. For Fran, keep your diagram and finish with time dilation.

---

**Learner**

the reason why i learned lorentz early is because i was having trouble figuring out multiply or divide for gamma. now that i have lorentz plot and i can always figure out what the rest frame is it makes more sense to use shortcut method.&#x20;

lets keep practicing

**Tutor**

That makes sense—Lorentz helped you identify the rest frame and the relevant events. Now you can use that understanding to choose the time-dilation or length-contraction relation directly.

**Continue Fran, using time dilation.** Let \(T\) be Earth’s total travel time. Fran’s travel time is \(T-10\,\mathrm{yr}\), so
\[
T-10\,\mathrm{yr}
=T\sqrt{1-\frac{(17.44\,\mathrm{yr})^2}{T^2}}.
\]

**Next step: square both sides and expand the left.** Keep \(17.44^2\) unevaluated for now.

---

**Learner**

4L+6)/root3 C?

**Tutor**

Do you mean \(\displaystyle \frac{4L+6}{\sqrt3\,c}\)? I’m not sure what the “6” represents.

From your diagram, use the **gap between the right ends**, \(2L-\frac L2\), divided by their relative speed. The clock reading should be **negative**, because they lined up before \(t'=0\).

---

**Learner**

give the question again, all parts until the current part

**Tutor**

**Course — Two rulers**

Two parallel rulers lie along the direction of motion. The **lower ruler is stationary**, while the **upper ruler moves right** at
\[
v=\frac{\sqrt3}{2}c.
\]
In the lower ruler’s rest frame, **both rulers measure length \(L\)**.

**(a)** What is the proper length of the upper ruler?

**(b)** What is the measured length of the lower ruler in the upper ruler’s rest frame?

**(c)** Draw both rulers in the upper ruler’s rest frame **when their left ends line up**. Label their lengths and indicate their velocities.

**(d) — Current part:** Clocks at the ends of each ruler are synchronized in that ruler’s own rest frame. Both left-end clocks read zero when the left ends line up.

**What does the upper ruler’s right-end clock read when the right ends line up? Is this reading positive or negative?**

---

**Learner**

wait even though my plot was wrong, if i didn't make the mistake in my algebra i would have gotten the right answer?

**Tutor**

**Yes.** Your sketch’s tilted spatial axis was misplaced, but the event coordinates you used—\(x=2L\), \(x'=L\)—and your equation
\[
L=\gamma(2L+\beta ct)
\]
were correct.

You therefore correctly reached
\[
ct=\frac{L}{\beta}\left(\frac1\gamma-2\right).
\]
That already gives the requested upper-clock reading, \(t=-\sqrt3L/c\).

**The inaccurate line in the sketch never entered your calculation.** The later error came from dropping a factor, not from the plot.

---

**Learner**

i just didn't use the fact that t' was 0

**Tutor**

**Exactly.** You used the position transformation to find \(t\), so you didn’t need to use \(t'=0\) explicitly.

The fact that \(t'=0\) was still true—it could serve as a **check** afterward. Your correct event positions and transformation already contained enough information to solve the question.

---

**Learner**

ok: now the shortcut method, i have no intuition about the shortcut method

**Tutor**

Start with **your ruler drawing**, in the upper ruler’s rest frame:

- Upper ruler: stationary, right end at \(2L\).
- Lower ruler: moving left, right end at \(L/2\) when \(t=0\).

**Imagine a video paused at \(t=0\).** Play it forward: the lower ruler moves left, so the right ends separate further. Rewind it: the lower ruler moves right until their right ends meet.

The shortcut is simply **how far you must rewind ÷ speed**. No additional time dilation is needed—we’re already working in the frame of the clock being asked about.

**First step only:** how far must the lower ruler move right from your drawing for its right end to reach the upper ruler’s right end?

---

**Learner**

3/2 L

3/2 L/root3/2C gives the answer

**Tutor**

**Yes—that gives the time interval’s magnitude:**
\[
\frac{3L/2}{(\sqrt3/2)c}=\frac{\sqrt3L}{c}.
\]

Because we **rewound from zero**, the clock reading is
\[
\boxed{t=-\frac{\sqrt3L}{c}}.
\]

That’s the whole shortcut: **gap ÷ speed, with a negative sign because the alignment happened earlier.**

---

**Learner**

bruh i feel retarded

**Tutor**

You’re not stupid. You just correctly found the gap and divided by the speed yourself. The missing piece was realizing that the question asks about an event **before** the snapshot.

I also made this harder by letting us switch frame labels and spend too long on Lorentz algebra. That confusion wasn’t all yours.

We’ll keep the next question’s frame labels fixed and start with the physical picture.

---

**Learner**

front

**Tutor**

The **rear** fires first. Its light chases the target moving away, taking \(4500\,\mathrm m/c\); the front pulse meets the approaching target in \(1000\,\mathrm m/c\).

Since they arrive together, the pulse with the **longer travel time must leave earlier**—the rear pulse, by \(3500\,\mathrm m/c\).
