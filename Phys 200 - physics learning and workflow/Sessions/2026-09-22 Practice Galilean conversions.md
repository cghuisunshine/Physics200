# Practice Galilean conversions

**Learner**

x' has to add d+L,

**Tutor**

Yes—add \(d+L\) to the right-hand side of your equation for \(x'\). That accounts for the initial separation.

---

**Learner**

i want to do it both ways, and get the same equation. A relative to be and B relative to A. you see i wrote two equations?

**Tutor**

Yes—I see your two equations. I moved on too quickly. **Both approaches are valid**, and both need the initial offset.

**A relative to B**, using your first equation:
\[
x'=-x''-(u+v)t+(d+L).
\]
Rearrange:
\[
\boxed{x''=-x'-(u+v)t+(d+L)}.
\]

**B relative to A**, using your second equation:
\[
-x''=x'+(u+v)t-(d+L).
\]
Multiply by \(-1\):
\[
\boxed{x''=-x'-(u+v)t+(d+L)}.
\]

The offset is **positive in your first equation and negative in your second** because the second has \(-x''\) on the left. Both give exactly the same transformation.

---

**Learner**

so we will do course questions and questions that you generate first, covering all these topics. 3 questions a set, otherwise follow the practice instructions.&#x20;

if we have time we'll do varations of the homework. lets start

**Tutor**

We’ll do sets of three, one question at a time, mixing course questions with generated ones and covering all six quiz topics across the sets. Homework variations will come afterward if there’s time.

---

**Learner**

give it to me 3 at a time to mimick a qui

**Tutor**

Yes—**three at once, with feedback after you submit the set.** No hints or solutions beforehand.

**Set 1 · Question 1 — Course**

Maggie is **11 years old**, and her brother Jacob is **1 year old**. She travels from Earth to Barnard’s Star, **5.96 light-years away**, and returns.

The ship travels at the same constant speed on both legs, with negligible turnaround time. On returning, Maggie is biologically **one year younger than Jacob**.

**How old is Jacob when she returns?**

---

**Question 2 — Generated**

In an inertial ground frame \(S\), right is positive.

- A’s origin starts at \(x=80\,\mathrm m\), moves **left at \(6\,\mathrm{m/s}\)**, and its \(x'\)-axis points **left**.
- B’s origin starts at \(x=-20\,\mathrm m\), moves **right at \(4\,\mathrm{m/s}\)**, and its \(x''\)-axis points **right**.

Both use the same time \(t\). Use Galilean physics.

**(a)** Find \(x''\) in terms of \(x'\) and \(t\). Derive it both ways: considering A relative to B, then B relative to A.

**(b)** Are both moving frames inertial? Explain briefly. Would B remain inertial if it began slowing down?

---

**Question 3 — Generated**

A train has **rest length \(300\,\mathrm m\)** and travels right at **\(0.60c\)** relative to the ground. A lamp at its midpoint emits two light pulses simultaneously, one toward each end.

Set \(t=t'=0\) at emission. Use \(c=3.00\times10^8\,\mathrm{m/s}\).

**(a)** In the train frame, when does each pulse reach its respective end?

**(b)** In the ground frame, when does each pulse reach its respective end?

**(c)** Are the two arrival events simultaneous in both frames? Explain how your answer is consistent with the speed of light being \(c\) in both frames.

**Show your setups; use no Lorentz transformations.**

---

**Learner**

it will not be on the long quiz but i can still use lorentz plots and transformation to help me

**Tutor**

Yes—you can use **Lorentz transformations and spacetime diagrams** to help solve these practice questions. “Not tested” doesn’t mean “forbidden”; my restriction was unnecessary.

The three questions stay the same. Use whichever valid method you prefer—just use **Galilean transformations for Question 2**, since it explicitly assumes Galilean physics.

---

**Learner**

now its on the same axis, i wrote those two as equivalent because they have the same slope and comes back the same. same time dilation

**Tutor**

**Yes—you’re right.** The legs have equal speed magnitudes and equal Earth-frame durations, so they have the **same time-dilation factor**. You can combine them:
\[
\Delta t_{\text{Earth,total}}=\gamma\,\Delta\tau_{\text{Maggie,total}}.
\]

I was too restrictive earlier: you don’t need to calculate the legs separately when using this symmetry.

If \(x\) is Jacob’s final age, your corrected equation is therefore
\[
\boxed{x-1=\gamma(x-12)}.
\]

Your original contradiction came from **reversing which elapsed time gets multiplied by \(\gamma\)**, along with using \(x\) instead of \(x-1\) for Earth’s elapsed time.

---

**Learner**

is this question much worse as a lorentz' question than a shortcut questions

**Tutor**

**Yes—this question is considerably more cumbersome with full Lorentz transformations.** You need separate frames for the two legs and must track coordinate origins and clock offsets.

Time dilation fits directly: Maggie travels at the same speed magnitude throughout, so
\[
x=\gamma y,\qquad y=x-11.
\]
Then connect Earth’s elapsed time \(x\) to the round-trip distance and speed.

That’s an exact method under the problem’s assumptions, not an approximation. **For this question, I’d use time dilation.** Your Lorentz approach is valid, but it adds bookkeeping that obscures the simple relationship—and I should have made that distinction clearer earlier.

---

**Learner**

but delta x is the unprime position. and the unprime you star and end up unchanged

**Tutor**

**Yes—for the actual round trip, you’re right:**
\[
\Delta X=0-0=0.
\]

I wasn’t clear enough: **extending the return line changes the starting event.**

- **Actual departure → reunion:** \(\Delta X=0\), but one moving inertial frame doesn’t follow Maggie throughout. Its elapsed coordinate time \(\Delta t'\) therefore **isn’t Maggie’s total aging**.
- **Dashed-line start → reunion:** \(\Delta X=0-2L=-2L\). This hypothetical traveller moves at constant velocity throughout and ages by the same total amount as Maggie.

So you can use either pair of events, but you **cannot combine the actual trip’s \(\Delta X=0\) with the hypothetical traveller’s \(\Delta t'=T-11\)**. That mixing is exactly what produced the contradiction.

---

**Learner**

ok, guide me through this question, slow WAY down

**Tutor**

Let’s keep your Lorentz approach and work with **only the outward leg** first.

Call departure **A** and arrival at Barnard’s Star **B**. Use Earth’s frame, with Earth at position \(X=0\) and departure at time \(t=0\). The star is at \(X=L\), where \(L=5.96\) light-years.

If Maggie’s speed is \(v\), **what are the Earth-frame coordinates \((X_B,t_B)\) of event B?**

Just that step for now.

---

**Learner**

yes

**Tutor**

Good. For this left-moving frame,
\[
c\Delta t'=\gamma\left(c\Delta t+\beta\Delta X\right),
\qquad \beta=\frac vc>0.
\]

**Substitute the three differences from your diagram into this equation.** Just the substitution—no algebra yet.

---

**Learner**

do all observers always agree what beta is?

**Tutor**

**For the same two inertial frames, they agree on the magnitude of their relative velocity**, so they agree on \(\beta=v/c\) when \(v\) means speed.

Earth says the ship moves left at \(-v\); the ship says Earth moves right at \(+v\), assuming aligned axes. **Same speed, opposite signed velocities.**

A third observer can measure different speeds for Earth and the ship, so there isn’t one universal \(\beta\).

Here, our \(\beta>0\) means **the ship–Earth relative speed divided by \(c\)**. We already accounted for its leftward direction through the \(+\beta\Delta X\) sign.
