# Practice Lorentz transformations

**Learner**

is ct a distance plot or a time axis?

**Tutor**

**\(ct\) is the time axis, expressed in distance units.** Multiplying time by the constant \(c\) changes its units, not what it represents.

For example:
\[
t=5\,\mathrm{s}\quad\Longleftrightarrow\quad ct=5\,\text{light-seconds}.
\]

So on the diagram:

- **\(x\):** where the event happens.
- **\(ct\):** when the event happens.

Using \(ct\) lets both axes have the same units. With equal scales, light follows \(x=\pm ct\), giving **45° lines**. It does **not** mean the object has travelled a distance \(ct\).

---

**Learner**

introduce it very slowly, only a few things at a time

**Tutor**

We’ll go slowly.

A spacetime diagram records **where and when an event happens**. An event could be a lamp flashing.

- **Horizontal axis \(x\):** where it flashes.
- **Vertical axis \(ct\):** when it flashes, with time multiplied by \(c\).

For now, just use this conversion: **a time of 2 seconds corresponds to a height of 2 light-seconds.**

If a lamp flashes at \(x=3\) light-seconds and \(t=2\) seconds, where would you place its dot on the diagram?

---

**Learner**

x=ct here?

**Tutor**

**Not generally.** Having the same units doesn’t mean they have the same value.

In our example:
\[
x=3\,\text{light-seconds},\qquad ct=2\,\text{light-seconds},
\]
so \(x\ne ct\).

The line **\(x=ct\)** specifically describes light travelling in the positive \(x\)-direction from \(x=0\) at \(t=0\).

---

**Learner**

how does length axis denote time?

**Tutor**

Because \(c\) is a **fixed conversion factor**, every value of \(ct\) corresponds to exactly one time:
\[
t=\frac{ct}{c}.
\]

For example, a height of **3 light-seconds** means:
\[
t=\frac{3\text{ light-seconds}}{1\text{ light-second per second}}
=3\text{ seconds}.
\]

We could label that same height **“3 seconds”** on a \(t\)-axis or **“3 light-seconds”** on a \(ct\)-axis. It represents the same moment.

---

**Learner**

do i need to know why t is expressed with c and not alone?

**Tutor**

**For now, you only need the practical reason:** using \(ct\) gives both axes the same units, so we can draw space and time on a common scale.

You **can** use \(t\) alone. Using \(ct\) is convenient because, with equal axis scales, light’s path is a 45° line.

There’s no further derivation you need before we continue.

---

**Learner**

Next.

**Tutor**

Next: **one dot represents one event**—something happening at a particular place and time.

A lamp flashes at \(x=3\) light-seconds and \(t=2\) seconds. Its dot goes:

- **3 units right**, for \(x=3\).
- **2 units up**, for \(ct=2\).

If the same lamp stays there and flashes again at \(t=4\) seconds, where would the second dot go?

---

**Learner**

How does C t equal two if t equals two?

**Tutor**

I left out the units—that made it confusing. **\(ct\) doesn’t equal the number 2; it equals 2 light-seconds.**

Since
\[
c=1\ \frac{\text{light-second}}{\text{second}},
\]
when \(t=2\) seconds:
\[
ct=\left(1\ \frac{\text{light-second}}{\text{second}}\right)(2\ \text{seconds})
=2\ \text{light-seconds}.
\]

In metres, that same \(ct\) would be approximately **600 million metres**.

---

**Learner**

Also, three units to the right, two units up, you would end up with a larger x and a smaller ct, which means that it's faster than the speed of light. That's not right.

**Tutor**

**That would imply faster-than-light travel if an object travelled from the origin \((0,0)\) to that dot.** It would cover 3 light-seconds in 2 seconds: \(1.5c\).

But the dot alone says only:

> A flash happens at position \(x=3\) light-seconds, at time \(t=2\) seconds.

The lamp was **already at that position**. Nothing had to travel there from the origin.

**A point specifies an event. To describe motion, we need a line connecting events along an object’s path.**

---

**Learner**

Light starting at origin reaches the lamp at 3s between two flashes of lamp

**Tutor**

**Correct.** Light leaves the origin at \(t=0\) and reaches the lamp at \(t=3\,\mathrm{s}\), between its flashes at \(2\) and \(4\,\mathrm{s}\).

Next, consider a moving object: it starts at the origin and travels right at \(v=0.5c\).

At \(t=2\,\mathrm{s}\), what are its \(x\) and \(ct\) coordinates?

---

**Learner**

ye

**Tutor**

Now just the **time** of that same event.

The two frames assign it different times:

- \(S\): \(t=2\,\mathrm{s}\).
- \(S'\): \(t'\approx1.73\,\mathrm{s}\), from the Lorentz transformation.

So your **same dot** is labelled \(ct=2\) using the vertical axis and \(ct'=1.73\) using the tilted axis, both in light-seconds.

Tilting the axis doesn’t move the event—it changes how we assign its coordinates.

---

**Learner**

Yes keep going

**Tutor**

Next we need the **\(x'\)-axis**.

Your horizontal \(x\)-axis contains all events with **\(t=0\)**. Similarly, the \(x'\)-axis must contain all events with **\(t'=0\)**.

Using our transformation,
\[
ct'=\gamma(ct-0.5x),
\]
setting \(ct'=0\) gives
\[
ct=0.5x.
\]

Draw a line through the origin and the point **\(x=2\,\mathrm{ls},\ ct=1\,\mathrm{ls}\)**. Label it \(x'\).

It lies between the horizontal axis and the light line. **Every event on it has time \(t'=0\) in the moving frame.**

---

**Learner**

Not understanding it.

**Tutor**

Let’s pause before drawing \(x'\).

Look only at your **horizontal \(x\)-axis**. Every point on it has height \(ct=0\), so every point represents an event at **\(t=0\)**.

For example, \((x,ct)=(1,0)\) and \((3,0)\) are **different places at the same time**.

Does that part make sense?

---

**Learner**

Yes.

**Tutor**

The **\(x'\)-axis has the same job for the moving frame**: every point on it has \(t'=0\).

But events that happen at the same time in \(S'\) need not happen at the same time in \(S\). **This is why the \(x'\)-axis can be tilted** instead of horizontal.

A point on that tilted axis can have:
\[
t'=0,\qquad t\ne0.
\]

That means the frames assign different times to the same event—not that the event happens twice.

---

**Learner**

I noticed that there's a good chunk of this that's faster than speed of light, if something were happened inside of it.

**Tutor**

**Yes—if an object travelled from the origin to a point between the light line and the \(x\)-axis, it would have to travel faster than light.**

But **an event can happen there** without anything travelling from the origin. A lamp already there could flash.

That also explains the shallow \(x'\)-axis: it connects **separate events at different places**, all simultaneous in \(S'\). It does not describe something travelling between them.

---

**Learner**

ct prime is not perpendicular to x prime, but when you're representing constant value in ct prime, it's parallel to x prime. That's very strange.

**Tutor**

Yes—it’s unfamiliar because we usually use perpendicular axes. **Here, the axes are tilted, so we read coordinates using parallel lines, not perpendicular projections.**

Think of the two axes as directions for drawing:

- Moving **along \(ct'\)** changes \(ct'\), while \(x'\) stays fixed.
- Moving **parallel to \(x'\)** changes \(x'\), while \(ct'\) stays fixed.

So starting at your \(ct'=1.73\) mark and moving parallel to \(x'\) keeps you at **\(ct'=1.73\)**.

The coordinates tell you how far to go in each axis direction—not the perpendicular distance to the other axis.

---

**Learner**

Okay, next.

**Tutor**

Let’s use that line to compare the frames.

Choose another point **farther right on your line parallel to \(x'\)**.

- It has the **same \(t'\)** as the original point.
- It is **higher on the page**, so it has a **later \(t\)**.

Thus, these two events are **simultaneous in \(S'\), but not in \(S\)**. That’s the relativity of simultaneity, visible directly in your drawing.

Mark that second point **B**, and call the original point **A**.

---

**Learner**

Wait, let's start from the beginning. Something feels wrong.

**Tutor**

Yes. **I switched diagram conventions mid-explanation**, which made this confusing. We’ll keep **\(x\) horizontal and \(ct\) vertical for our frame**, as before.

Start with only this:

A clock moves right past us at \(0.6c\). **The moment it passes us is event A.** We choose that event as
\[
x=0,\qquad t=0.
\]

Draw just the \(x\) and \(ct\) axes, and put **A at their intersection**. Leave everything else off for now.

---

**Learner**

How do we know which one is primed, which one is stationary? Is the most normal-looking one, everything perpendicular, always the one that's not primed?

**Tutor**

**The primes are labels we choose.** They don’t mean a frame is “really moving” or “really stationary.”

For this problem, we chose:

- \(S\), unprimed: **our frame**. We are stationary in it.
- \(S'\), primed: **the clock’s frame**. The clock is stationary in it.

On **our current diagram**, we chose to draw \(x\) and \(ct\) perpendicular, so the primed axes appear tilted.

We could instead draw \(x'\) and \(ct'\) perpendicular. Then the **unprimed axes would appear tilted**. The physics would be unchanged.

---

**Learner**

these lorentz transformation formulas, is there a rule to which one to apply?

**Tutor**

**Yes: choose by which coordinates you know and which you want.**

With \(S'\) moving at \(+v\) relative to \(S\):

| Direction | Position formula | Time formula |
|---|---|---|
| Know unprimed → want primed | \(x'=\gamma(x-\beta ct)\) | \(ct'=\gamma(ct-\beta x)\) |
| Know primed → want unprimed | \(x=\gamma(x'+\beta ct')\) | \(ct=\gamma(ct'+\beta x')\) |

Here \(\beta=v/c\).

**For our event B:** we know \(x'=0\) and \(ct'=1\) light-hour, and want \(x\). So we choose:
\[
\boxed{x=\gamma(x'+\beta ct')}.
\]

The choice depends on **the known and requested coordinates**, not which axes look perpendicular.

---

**Learner**

Why aren't they identical if unprimed and primed are just labels? Or... They are negatives of one another because the relative velocities are different, something like that？

**Tutor**

**Yes—that’s exactly the reason: the relative velocity reverses.**

- In \(S\), the clock’s frame \(S'\) moves at **\(+0.6c\)**.
- In \(S'\), our frame \(S\) moves at **\(-0.6c\)**.

The transformation has the **same form** in either direction. Swapping the frames replaces \(\beta\) with \(-\beta\), turning the minus sign into a plus:
\[
x'=\gamma(x-\beta ct)
\quad\longleftrightarrow\quad
x=\gamma(x'+\beta ct').
\]

And \(\gamma\) stays the same because it depends on \(\beta^2\).

---

**Learner**

ok lets keep going, dont get side tracked here

**Tutor**

Back to event B. We know \(x'=0\), \(ct'=1\) light-hour, and want \(x\):

\[
x=1.25\bigl[0+0.6(1)\bigr]\text{ light-hours}.
\]

What distance does that give?

---

**Learner**

Give what we know and solve the Lorentz transformation step by step for me here, so I know where things are coming from.

**Tutor**

We want the clock’s distance from us **at event B: when its face reads 1:00**.

**1. What we know**

We set elapsed time to zero when it passed us at 12:00.

- The clock moves right in our frame at \(v=0.6c\), so \(\beta=0.6\).
- In its own frame, the clock stays at the origin: \(x'_B=0\).
- At B, one hour has elapsed on that clock: \(t'_B=1\,\mathrm{hr}\). Therefore,
  \[
  ct'_B=1\,\text{light-hour}.
  \]

**2. Calculate \(\gamma\)**

\[
\gamma=\frac{1}{\sqrt{1-\beta^2}}
=\frac{1}{\sqrt{1-0.6^2}}
=\frac{1}{0.8}
=1.25.
\]

**3. Choose the transformation**

We know **primed coordinates** and want the **unprimed position \(x_B\)**:
\[
x_B=\gamma(x'_B+\beta ct'_B).
\]

**4. Substitute**

\[
x_B=1.25\left[0+0.6(1\,\text{light-hour})\right]
=\boxed{0.75\,\text{light-hours}}.
\]

So **the clock is 0.75 light-hours away from us when it reads 1:00**.

On your diagram, draw a vertical dashed line from B down to the \(x\)-axis. Label where it meets that axis **0.75 light-hours**.

---

**Learner**

Give me another question. This time I do it myself. So don't make it too hard. The key is for me to do these questions while Loren's Transformation do the bookkeeping for me.

**Tutor**

**Generated**

A spaceship moves right at **\(0.6c\)** relative to Earth. As it passes Earth, both frames set their clocks to zero.

When the **spaceship’s clock reads 2 hours**, it emits a flash.

**Where and when does that flash occur in Earth’s frame?** Give position in light-hours and time in hours.

Use \(S\) for Earth and \(S'\) for the spaceship, with the ship at \(x'=0\). You may use \(\gamma=1.25\).

\[
x=\gamma(x'+\beta ct'),\qquad
ct=\gamma(ct'+\beta x').
\]

Draw your diagram and try both coordinates.

---

**Learner**

i get it now. Remember those simultaneity problems I had trouble understanding? Namely, a stationary observer observes that a flash at either end of a train occur simultaneously. but inside that train people observe that the flashes happen at different times. in our textbook, it’s said how it is, but I suspect that transformations is the way to visualize it gain intuitive understanding and see it more clearly

**Tutor**

**Yes—your tilted axes show exactly why this happens.**

First, “simultaneous” means the ground frame assigns the flashes the same **event time**, after accounting for light-travel delays. It doesn’t necessarily mean someone receives both flashes together.

Keep our convention: ground frame \(S\), train frame \(S'\), train moving right.

**Just draw this first:**

Mark two events on the same horizontal line:

- **A:** rear of the train flashes, on the left.
- **B:** front of the train flashes, on the right.

Their equal height means **\(t_A=t_B\)**: simultaneous in the ground frame.

Next we’ll read their times using the tilted \(ct'\)-axis—exactly as you’ve been doing.

---

**Learner**

I understand why CT prime is steep and leaning right, but I don't understand why X prime is shallow and rising right. Because the train is obviously slower than the speed of light. I simply don't understand why X prime is shallow and rising right.

**Tutor**

**The \(x'\)-axis isn’t the train’s path.** The steep \(ct'\)-axis is its path—that’s where its speed appears.

The \(x'\)-axis connects **different places at the same train-frame time**, \(t'=0\). Nothing travels along it.

Its tilt comes from:
\[
ct'=\gamma(ct-\beta x).
\]
For \(ct'=0\), we need
\[
ct=\beta x.
\]

Since the train moves right with \(0<\beta<1\), this line **rises right, more shallowly than the light line**.

Your speed objection would be correct **if this were an object’s path**. But it’s a line of simultaneous events.

---

**Learner**

？ I see that ct equals beta x, but this is, this is a line, but how do we know it is the line of x prime?

**Tutor**

Because **a frame’s space axis is where that frame’s time coordinate is zero**.

On the ordinary \(x\)-axis:
\[
ct=0,\qquad x\text{ can vary}.
\]

Likewise, on the \(x'\)-axis:
\[
ct'=0,\qquad x'\text{ can vary}.
\]

We set \(ct'=0\) in the transformation and found \(ct=\beta x\). So that line is **all the points whose primed time coordinate is zero**—which is exactly what the \(x'\)-axis means.

---

**Learner**

Beautiful, what's next?

**Tutor**

Now read **A’s time in the train frame**.

Through A, draw a dashed line **parallel to the \(x'\)-axis**, extending up and right until it meets the \(ct'\)-axis.

That intersection gives A’s \(ct'\) coordinate.

Does it meet the \(ct'\)-axis **above or below the origin**?

---

**Learner**

Beautiful. I was struggling so much with trouble dividing or multiplying, and a good way to do bookkeeping

**Tutor**

Exactly. **You now have a way to decide what to calculate**, instead of trying to remember whether to multiply or divide by \(\gamma\):

1. Identify the **event**.
2. Write its known coordinates and **which frame they belong to**.
3. Choose the transformation into the frame you want.
4. Use the diagram to check whether the result makes sense.

Time dilation and length contraction become shortcuts you can derive when needed. We can keep using **events → coordinates → transformation** as our main approach.

---

**Learner**

15？

**Tutor**

**Correct—15 years.** The explosion occurs at \(ct_E=75-60=15\) light-years.

You’ve answered both parts:

- **Star clock at arrival:** \(75\) years.
- **Sun clock at explosion:** \(15\) years.

Next, let’s use a Lorentz transformation on the same diagram: **what does the ship’s clock read at arrival?**

At arrival, \(ct=75\,\mathrm{ly}\) and \(x=60\,\mathrm{ly}\). Use
\[
ct'=\gamma(ct-\beta x),
\qquad \beta=0.8,\quad \gamma=\frac53.
\]

What do you get?

---

**Learner**

Yeah, I'm not too worried about that. I'm just, I just want extra practice converting ordinary relatively problems involving  Multiple events, multiple places, different perspectives, things happening, different lengths, length contraction , time dilation etc.&#x20;

generate something and gently guide me once again, but with slightly less handholding. symbolici only. have we been engaging with the practice log? dont because this is kind of a detour

**Tutor**

I read your practice log to select the earlier question, but **haven’t updated it during this detour**. I’ll keep this practice out of it.

**Generated**

A train has rest length \(L_0\) and moves right at speed \(v\) relative to a platform.

As its rear passes a platform observer, a light pulse is emitted from the rear toward the front. The train and platform clocks are set to zero at that emission event.

We’ll find, symbolically:

- When and where the pulse reaches the front, in both frames.
- The train’s length measured on the platform.

Use \(S\) for the platform and \(S'\) for the train, with the rear at \(x'=0\).

Call emission **A** and reception at the front **B**.

**Start in the train frame:** what are the coordinates \((x',ct')\) of A and B?

---

**Learner**

? How do I draw the x prime axis?

**Tutor**

Your **rear-of-train worldline is the \(ct'\)-axis**, because the rear stays at \(x'=0\).

To draw \(x'\), use
\[
ct=\beta x,\qquad \beta=\frac vc.
\]

Draw a **shallow line through A, rising right**, below the light line. With equal scales on \(x\) and \(ct\), it mirrors the steep \(ct'\)-axis across the light line.

Label it **\(x'\)**. Every event on it has \(t'=0\).

---

**Learner**

Skip, kind of trivial. Let's practice those signs that I'm still a little bit confused about.

**Tutor**

Let’s focus only on signs.

Frame \(S'\) moves **left at \(0.6c\)** relative to \(S\). You know an event’s coordinates in \(S\) and want \(x'\).

Using
\[
x'=\gamma(x-vt),
\]
**what signed value goes in for \(v\), and what does the expression inside the brackets become?** No calculation needed.

---

**Learner**

In the brackets it becomes x plus 0.6t. Let's resume with our train flash example. Keep in mind that maybe in the next few examples we're gonna look more closely at signs. But things are starting to align in my brain.

**Tutor**

**Correct sign:** the bracket becomes \(x+0.6ct\)—keep the \(c\), since \(v=-0.6c\). We’ll revisit signs in upcoming examples.

Back to the **train flash**:

- Train rest length: \(L_0\).
- Train moves right at \(v\) relative to the platform.
- **A:** light leaves the rear at \(x'=0,\ t'=0\).
- **B:** light reaches the front at \(x'=L_0\).

In the train frame, light travels the distance \(L_0\) at speed \(c\).

**Write B’s coordinates \((x'_B,ct'_B)\).** Then we’ll transform that event into the platform frame.

---

**Learner**

Let’s scrap this, what is my next step? Plot x’?

**Tutor**

**Yes—keep your diagram and set aside that calculation. Next, draw the \(x'\)-axis.**

Your rear-of-train line is already the \(ct'\)-axis.

Through A, draw the shallow line
\[
ct=\beta x,\qquad \beta=\frac vc.
\]

It rises right, **below the light line**. Label it \(x'\).

Where it crosses the front’s worldline, mark **C**. That is the front’s position at **train time \(t'=0\)**, so its coordinate is \(x'_C=L_0\).

---

**Learner**

Where does ct equals beta x come from? It comes from one of those Lorentz transformation formulas, right?

**Tutor**

**Right—from the time transformation:**
\[
ct'=\gamma(ct-\beta x).
\]

The **\(x'\)-axis is where \(ct'=0\)**. Substitute that:
\[
0=\gamma(ct-\beta x).
\]

Divide by \(\gamma\):
\[
0=ct-\beta x,
\]
so
\[
\boxed{ct=\beta x}.
\]

That tells us how to draw the \(x'\)-axis on our \(x,ct\) diagram.

---

**Learner**

So there are only two Lorentz transformation formulas to know?

**Tutor**

**Yes—for motion along one spatial direction, there are two core formulas:**
\[
\boxed{x'=\gamma(x-\beta ct)}
\]
\[
\boxed{ct'=\gamma(ct-\beta x)}
\]
where \(\beta=v/c\) and \(\gamma=1/\sqrt{1-\beta^2}\).

They convert an event’s **position and time** from \(S\) to \(S'\).

To go backward, swap primes and unprimes and reverse the velocity:
\[
x=\gamma(x'+\beta ct'),\qquad
ct=\gamma(ct'+\beta x').
\]

So the reverse formulas follow from the same two rules.

---

**Learner**

Would this be clarified by space time plot and Lorentz? Or should I develop standalone intuition?

**Tutor**

**Yes—use the spacetime plot and Lorentz transformations to develop the intuition.** You don’t need a separate intuitive explanation first.

For this problem, the diagram will show that **each observer compares a different pair of events**. The transformations will verify the clock readings. That is the explanation of how both can consistently measure the other’s clock as slower.

Let’s build it slowly:

- Draw Gamora’s axes: \(x\) horizontal, \(ct\) vertical.
- Gamora stays at \(x=0\), so her worldline is the vertical axis.
- Nebula passes her at the origin, then moves right: draw Nebula’s worldline rising right, steeper than the light line.

Just those two worldlines first.

---

**Learner**

This worksheet is not perfectly designed then.

**Tutor**

**Yes—the wording leaves an important assumption unstated.** “What is the time on Gamora’s clock when Nebula reaches the right end?” compares events at different places, so it should specify **“simultaneous in Gamora’s frame.”**

The calculation is valid under that intended interpretation. But using time dilation to establish length contraction before explaining simultaneity can reasonably leave you asking: **“Why can’t Nebula apply the same argument in reverse?”**

Your confusion exposed a missing explanation. The spacetime diagram makes that assumption visible.
