# Assess Quiz 2 practice

**Learner**

ac

**Tutor**

Neither A nor C is correct—the velocity signs are reversed. Frame \(A\) moves in the **positive** direction relative to \(B\).

Try again: which option matches that motion?

---

**Learner**

one moment, remember those gallelean trsnform qeustions? lets do some of those

**Tutor**

Yes—the ones with moving frames, reversed axes, and origins starting at different positions. We’ll pause the slides and do those one at a time.

---

**Learner**

thats good, how about the previous Q i missed?

**Tutor**

The lecture question—let’s return to it.

Frame \(A(x,y)\) moves at speed \(v\) in the **positive \(x\)-direction** relative to frame \(B(x',y')\). Both axes point right, and their origins coincide at \(t=0\).

Which statement is true?

A. The origin of \(A\) is at \(x=0\) and \(x'=-vt\).  
B. The origin of \(B\) is at \(x=0\) and \(x'=+vt\).  
C. The origin of \(B\) is at \(x'=0\) and \(x=+vt\).  
D. The origin of \(B\) is at \(x'=0\) and \(x=-vt\).  
E. The origin of \(A\) is at \(x'=0\) and \(x=+vt\).

Try your position-equation method, using **B as the reference frame**.

---

**Learner**

which lecture is this

**Tutor**

We’re now on **Week 2, Tuesday, September 15**—PDF page 3, slide 6, about a fixed point viewed from a moving frame.

The earlier frame-origin question was from **Week 1, slide 53**.

---

**Learner**

lets work on slides that cover THIS long quiz

**Tutor**

I’ll move to the slides on Lorentz transformations, velocity addition, spacetime diagrams, and intervals, starting with Week 3 Thursday.

---

**Learner**

D

**Tutor**

It accounts for **C: relativity of simultaneity**.

Compare two events using
\[
\Delta t'=\gamma\left(\Delta t-\frac{v\Delta x}{c^2}\right).
\]

If they happen **simultaneously in \(S\)**, then \(\Delta t=0\). But if they happen at different positions,
\[
\Delta t'=-\gamma\frac{v\Delta x}{c^2},
\]
which generally isn’t zero. **Same time in one frame need not mean same time in another.** The position term makes that possible.

For example: two lamps fixed in \(S\), one on the left and one on the right, flash simultaneously in \(S\). Frame \(S'\) moves right, so \(v>0\).

**In \(S'\), which lamp flashes first?**

---

**Learner**

i know how to answer this, i just use Spacetime diagram instead.

**Tutor**

That works—your spacetime diagram represents the same relationship.

A line of simultaneous events in \(S'\) has constant \(t'\), so
\[
t-\frac{vx}{c^2}=\text{constant}
\quad\Rightarrow\quad
ct=\frac vc\,x+\text{constant}.
\]

That’s the **tilted simultaneity line parallel to \(x'\)** in your diagram. The position term in the Lorentz transformation produces that tilt.

Go ahead and use your diagram: **which lamp flashes first in \(S'\)?**

---

**Learner**

B

**Tutor**

Correct—B. Swapping frames reverses \(v\), while \(\gamma\) stays the same because it depends on \(v^2\). I’ll check the setup for the next slide question.

---

**Learner**

I dont understand this Q

**Tutor**

It’s asking **where Anne should put her coordinate zero, and when she should call the time zero**.

These are two separate choices:

- \(x_A=0\): the location Anne uses as her spatial origin.
- \(t_A=0\): the clock reading Anne labels “zero seconds.” Her clock can display 12:00 while her coordinate time is \(0\).

Bart has already chosen both. **The event “Bart passes Anne at 12:00” has coordinates \((x_B,t_B)=(0,0)\).**

The question asks which choice for Anne makes the ordinary Lorentz equations work without extra position or time offsets.

Try substituting \(x_B=0,\ t_B=0\) into
\[
t_A=\gamma\left(t_B+\frac{v x_B}{c^2}\right),
\qquad
x_A=\gamma(x_B+vt_B).
\]

**What coordinates must Anne assign to that same passing event?**

---

**Learner**

0,0 right? but if we use deltas then it doesn't matter

**Tutor**

**Exactly—both points are right.** The passing event must be \((0,0)\) in Anne’s coordinates, so **B** answers the question *as written*.

With differences,
\[
\Delta t_A=\gamma\left(\Delta t_B+\frac{v\Delta x_B}{c^2}\right),\qquad
\Delta x_A=\gamma(\Delta x_B+v\Delta t_B),
\]
constant position and time offsets cancel. **The origins need not coincide when using these difference equations**, provided both frames describe the same pair of events.

Your distinction is precisely the subtlety the question is testing.

---

**Learner**

keep going

**Tutor**

I’ll continue with the slides’ Anne-and-Bart example, one event at a time.

---

**Learner**

7

**Tutor**

\(7\,\mathrm s\) isn’t correct. Show me the equation you used so we can locate the error.

---

**Learner**

I thought the plus sign alredy accounted for it?

**Tutor**

The **plus sign accounts for the frame’s leftward velocity**. The sign of \(\Delta x\) separately describes **where the second event occurs relative to the first**.

Start with the signed-velocity formula:
\[
c\Delta t'=\gamma(c\Delta t-\beta\Delta x).
\]

Bart moves left, so \(\beta=-\sqrt3/2\). Substituting that gives
\[
c\Delta t'=\gamma\left(c\Delta t+\frac{\sqrt3}{2}\Delta x\right).
\]

That explains your plus sign. But **\(\Delta x\) is still a signed displacement**, not a distance. The encounter with AF happens to the left of the starting event, so \(\Delta x<0\).

You aren’t counting the direction twice: one sign belongs to **the frame velocity**, and the other belongs to **the separation between the events**.

---

**Learner**

the plus sign accounts for the beta instead, but not the delta x?

**Tutor**

**Exactly.** The plus sign comes from substituting the negative \(\beta\):
\[
-\beta\Delta x=-\left(-\frac{\sqrt3}{2}\right)\Delta x
=+\frac{\sqrt3}{2}\Delta x.
\]

You still substitute **\(\Delta x<0\)** separately, so this term ultimately subtracts from \(c\Delta t\).

---

**Learner**

so mentally: always have a unprimed upright frame

and have everything signed

**Tutor**

**Yes—for your usual spacetime diagram:** draw the unprimed \(x,ct\) axes horizontal and vertical, then draw the primed axes tilted relative to them. That’s a drawing convention, not an absolute rest frame.

**Keep everything signed:**

- \(\beta=v/c\): primed frame’s velocity measured in the unprimed frame.
- \(\Delta x=x_2-x_1\), and likewise for \(\Delta x'\) and time differences—always using the same event order.

Then keep the formulas fixed:
\[
c\Delta t'=\gamma(c\Delta t-\beta\Delta x),
\qquad
c\Delta t=\gamma(c\Delta t'+\beta\Delta x').
\]

**Let the signed substitutions handle direction.**

---

**Learner**

ok nexy

**Tutor**

We’ll move to the next lecture event. I’ll keep the sign convention flagged for later review.

---

**Learner**

whats a more consistent way to do this

**Tutor**

**Write the event coordinates first, then choose the equation.** Keep \(\beta\) signed, and never change a formula’s signs mentally.

For this problem, keep Anne unprimed, Bart primed, and right positive:
\[
\beta=-\frac{\sqrt3}{2}.
\]

Then list only what you know:

| Event | Anne’s \(t\) | Anne’s \(x\) |
|---|---:|---:|
| \(E_1\): Bart passes Anne | \(0\) | \(0\) |
| \(E_2\): Bart passes AF | \(2\,\mathrm s\) | unknown |
| \(E_3\): BF passes Anne | \(2\,\mathrm s\) | \(0\) |

The requested length uses **\(E_2\) and \(E_3\)**: the positions of Bart and BF at the same Anne-frame time.

Bart’s position follows directly from his motion:
\[
x_2=v t_2
=\left(-\frac{\sqrt3}{2}c\right)(2\,\mathrm s)
=-\sqrt3\,c\,\mathrm s.
\]

Therefore,
\[
L=x_3-x_2=0-(-\sqrt3\,c\,\mathrm s)
=\sqrt3\,c\,\mathrm s.
\]

Your \(E_4\) method was valid, but introduced another event and more transformations.

The consistent sequence is **frame labels → event coordinates → required event pair → equation → signed substitution**. Use a Lorentz transformation when you need to connect measurements between frames; here, the table shows that the length can be found entirely in Anne’s frame.

---

**Learner**

uh, whats wron with 2 root 3/2?

**Tutor**

Nothing—that’s correct **if you mean**
\[
L=(2\,\mathrm s)\left(\frac{\sqrt3}{2}c\right)
=\sqrt3\,c\,\mathrm s.
\]

That’s **\(\sqrt3\) light-seconds**. You’ve used speed × time; just include the units.

---

**Learner**

was this the question i was doing?

**Tutor**

**Yes—the same question:** the distance between Bart and BF measured in Anne’s frame.

Before lunch, you were using a spacetime diagram and Lorentz transformations. Your latest approach—speed × \(2\,\mathrm s\)—finds that same distance directly.

---

**Learner**

that was SO unecessarY wtf was i thinking

**Tutor**

You reached for Lorentz transformations because we were practising them. Your method was valid—it just did more work than needed.

The useful check is: **are the speed, time, and requested distance all in the same frame?** Here, yes, so \(L=|v|\Delta t\) was enough.

---

**Learner**

are we far along the lecture content

**Tutor**

**We’re partway through the first relevant lecture, still early in the full Quiz 2 review.**

In **Week 3 Thursday**, we’ve reached slide **55–56 of 67**. We’ve covered:

- Lorentz transformations and their inverse
- The simultaneity term
- Coordinate origins versus event differences
- Anne/Bart clock comparisons and length measurement

**Next is velocity addition**, which finishes this lecture. Then we still need the later slides on **spacetime diagrams and intervals**.

So we’ve worked through much of this lecture’s Lorentz section, but haven’t yet reviewed all four main Quiz 2 topics through the slides.

---

**Learner**

B

**Tutor**

Correct—B: the ball’s travel time minus the light’s travel time.

---

**Learner**

is the slide here trying to derive it?

**Tutor**

**Yes—this sequence is deriving the velocity-addition formula.**

It builds up by:

1. Finding the arrival-time difference in the ship frame—you just did this.
2. Relating that interval to the ground-frame interval—the current question.
3. Calculating the ground-frame interval directly using the ball’s unknown ground speed.
4. Equating the two expressions and solving for that speed.

So this question is one step in the derivation.

---

**Learner**

lets skip the derivation

**Tutor**

We’ll skip to the slide that applies the velocity-addition formula.

---

**Learner**

give c, what is it trying to say

**Tutor**

**Yes, \(u'=c\).** It shows that velocity addition preserves the speed of light:

\[
u'=\frac{c+v}{1+v/c}
=\frac{c+v}{(c+v)/c}
=c.
\]

If a spaceship emits light forward, **both the ship and the planet measure that light travelling at \(c\)**, regardless of the ship’s speed. Unlike an ordinary ball, light doesn’t gain speed from its moving source.

---

**Learner**

next

**Tutor**

That finishes the lecture’s velocity questions. I’ll cover its closing distinction, then move to the next lecture’s question.

---

**Learner**

its the domain of general relativity to turn around

**Tutor**

**The turnaround breaks the symmetry, yes—but general relativity isn’t required.** The slide is misleading on that point.

The travelling twin changes inertial frames between the outbound and inbound legs; the Earth twin stays in one. Special relativity can calculate the elapsed proper time along both journeys, including an accelerated turnaround.

**The travelling twin is younger when they reunite.** Acceleration marks the asymmetry; the age difference isn’t simply accumulated during the turn.

---

**Learner**

i also know this, skip

**Tutor**

We’ll move on to spacetime intervals.

---

**Learner**

E

**Tutor**

Correct—E. The event pair stays fixed; changing frames leaves its interval unchanged.

---

**Learner**

A

**Tutor**

The sign is incorrect. Our convention is
\[
s^2=(\text{spatial separation})^2-(c\Delta t)^2.
\]

The events are simultaneous in A, so the time term is zero. Try again.
