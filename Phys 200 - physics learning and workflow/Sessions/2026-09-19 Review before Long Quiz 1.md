# Review before Long Quiz 1

**Learner**

so its basically right but i just need to not flip gamma.

**Tutor**

Yes—your method and substitution were right. The algebra error was flipping \(\gamma\); the diagram also needs \(L/\beta\) as the height on a \(ct\) axis. I’ll log it as solved with those minor corrections.

---

**Learner**

for the previous one, is this a clean method or do i just multiply or divide by gamma right away? its a little hard to see that way

**Tutor**

Yes—**your Lorentz-transformation method is clean and valid**, especially if it makes the frame choices clearer. You don’t need to spot a shortcut immediately.

For the shortcut, identify the two events: **the particle’s creation and decay**.

- In the detector frame, the elapsed time is \(\Delta t=L/(\beta c)\).
- In the particle’s frame, both events happen at the same position, so its elapsed time is the **proper lifetime** \(\tau_0\).

Then use
\[
\Delta t=\gamma\tau_0
\quad\Longrightarrow\quad
\tau_0=\frac{\Delta t}{\gamma}
=\frac{L}{\beta c\,\gamma}.
\]

Rather than guessing “multiply or divide,” write **detector time \(=\gamma\times\) particle time**, then rearrange. The particle ages less between these events, so dividing by \(\gamma>1\) also makes sense.

Your full transformation reaches exactly the same result—it makes the reasoning explicit.

---

**Learner**

keep going

**Tutor**

**Helliwell**

A rogue planet passes Earth. Its diameter in its own rest frame is **9,000 km**, and it takes **0.040 s** to pass a single Earth clock.

How fast is the planet moving relative to Earth?

---

**Learner**

I thought this is comparing delta T

Let me redo it

**Tutor**

Yes, you’re comparing time intervals—the key is **which frame measures proper time for these particular events**.

Go ahead and redo it; I’ll wait.

---

**Learner**

is the 0.04 in earth or in planet's frame?

**Tutor**

**Earth’s frame.** The question says the \(0.040\,\text{s}\) is measured by a single Earth clock—from the planet’s front passing it to the planet’s back passing it.

---

**Learner**

Before I start, 400 meters per second is tiny compared to the speed of light. So I'm guessing that it should be very, very, very similar.

**Tutor**

Yes—the two elapsed times should be almost identical because \(v/c\) is tiny and \(\gamma\) is very close to \(1\). That’s a useful check on your eventual answer.

---

**Learner**

Is it true that for Lorentz transformations it usually doesn’t lead to clean symbolic transformation? And we should sub values quite early

**Tutor**

**Not generally—Lorentz transformations often give clean symbolic results.** The algebra gets longer when you must eliminate extra unknowns, as you did here.

A useful rule:

- **Set up symbolically first:** identify the events, frames, coordinates, and signs.
- **Substitute known dimensionless values early:** here, \(\beta=4/5\) and \(\gamma=5/3\).
- **Keep unknown lengths and times symbolic** until you isolate the requested quantity.

Use exact fractions where convenient, and postpone rounding.

So for this problem, **yes: substitute \(\beta\) and \(\gamma\) early**. Your transformation method was fine; carrying them symbolically added work without helping.

---

**Learner**

but i dont want to make ANY mistakes in these quizzes

**Tutor**

Then we should aim for **a method you can execute reliably under time pressure**, not automatically the shortest one. You don’t need to abandon Lorentz transformations.

On this problem, your event coordinates and physics were correct. The mistakes came during algebra. Use this brief check each time:

1. **Events and frames:** Are all coordinates for the same two events, with each quantity assigned to its frame?
2. **Units and \(\gamma\):** Is it \(t\) or \(ct\)? Is \(\gamma=1/\sqrt{1-\beta^2}\ge1\)?
3. **Algebra:** Substitute known \(\beta,\gamma\) early, keep exact fractions, and check your answer in the original equations.

No method guarantees zero mistakes. We can build reliability through repeated independent solutions, then timed mixed practice—tracking whether you needed help, not just whether we eventually reached the answer.

For you right now, **keep the clear event setup and practise making the algebra accurate and routine.** Shortcuts can come as they become equally dependable.

---

**Learner**

lets keep going. let me do it again without lorentz tranformations

**Tutor**

**Course — retry without Lorentz transformations**

Two trains, A and B, move toward each other at a relative speed of **\(0.8c\)**.

The interval from **their fronts lining up to their backs lining up** is **20% longer in A’s frame** than in B’s frame.

Find the ratio of their **rest lengths**, \(L_{A0}/L_{B0}\).

---

**Learner**

FUCK. yeah lets keep going.&#x20;

does lorentz transformations usually lead to shitty algebra like mine? why was mine so long

**Tutor**

**No—Lorentz transformations usually give manageable algebra.** Yours got long because you kept \(\beta\) and \(\gamma\) symbolic, introduced \(u\), and then had to eliminate it. Corrections added more lines. Your original event setup was good.

With the numbers inserted immediately, your entire calculation becomes
\[
1.2cu=\frac53(cu-0.8L_{B0})
\Rightarrow cu=\frac{20}{7}L_{B0},
\]
\[
-L_{A0}=\frac53(L_{B0}-0.8cu)
\Rightarrow \frac{L_{A0}}{L_{B0}}=\frac{15}{7}.
\]

**Keep the method; simplify the bookkeeping.** The shorter method also requires careful frame choices—it isn’t automatically safer.

**Course**

A spaceship flies horizontally at **\(0.6c\)**, **10 km** above flat ground. Its laser points straight downward **in the ship’s frame**.

It fires while directly above a person standing on the ground. The pulse hits a nearby tree.

**How far from the person is the tree?**

---

**Learner**

do i need two lorentz graph for this question? let me attempt it first. im guessing no because they're not moving relative to each other in 2D

**Tutor**

You don’t need two Lorentz diagrams. One ground-frame sketch showing horizontal and vertical motion is enough.

Small correction: the ship **does** move relative to the ground, along \(x\). There’s no relative motion along \(y\), but the light can have velocity components in both directions.

Go ahead—I’ll leave the setup to you.
