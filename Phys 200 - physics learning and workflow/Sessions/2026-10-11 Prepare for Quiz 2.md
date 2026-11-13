# Prepare for Quiz 2

**Learner**

1.00019, divide instead

**Tutor**

Correct—you divide by the relative Lorentz factor, giving approximately \(1.0002\,\mathrm m\). I’ll mark this as completed after feedback.

---

**Learner**

I have the ground frame as upright

**Tutor**

Yes—your upright axes are the **ground frame**. The tree’s worldline is vertical, Batman’s slopes left, and the Joker’s slopes right. Your diagram is consistent; I switched frames unnecessarily.

Let \(E_A=(x_A,ct_A)\) be Batman receiving the light. Your sloping line through \(E_A\) marks events simultaneous **in Batman’s frame**, drawn on ground-frame axes.

We can keep your diagram and use that line to relate the tree, Joker, and Batman positions.

---

**Learner**

disreguard my equations. only take my graph baby step me

**Tutor**

We’ll use only your graph, one step at a time.

Call the origin **\(O\)**: the Joker sets the tree on fire there. Your red line carries the light from \(O\) to **\(E_A\)**, where Batman receives it.

Now label the point where your **downward-sloping simultaneity line crosses the Joker’s worldline** as **\(E_J\)**.

---

**Learner**

give a reasoning runthrough. right now im not getting where we're going

**Tutor**

We’re trying to find **the slope of the Joker’s worldline**, because that tells us his velocity. To do that, we need the coordinates of **one point on his line: \(E_B\)**.

Here’s how the information in the question locates that point on **your ground-frame graph**:

1. **The light locates \(E_A\).**  
   It leaves the origin and reaches Batman, so
   \[
   x_A=ct_A.
   \]
   We don’t know \(t_A\), but we can express everything in terms of it.

2. **“Halfway” locates \(E_B\) horizontally.**  
   Your sloping line connects the tree, Joker, and Batman at the **same Batman-frame time**. Along this line, the spatial Lorentz transformation scales all horizontal separations by the same factor, so their ratio stays \(1:1\). Thus the Joker’s event is horizontally halfway between the tree at \(x_C=0\) and Batman at \(x_A\):
   \[
   x_B=\frac{x_A}{2}=\frac12ct_A.
   \]
   These three events occur at different ground-frame times.

3. **The sloping line locates \(E_B\) vertically.**  
   Its slope is \(-0.60\). Moving left from \(A\) to \(B\) by \(x_A/2\) therefore takes us up by \(0.30x_A\):
   \[
   ct_B=ct_A+0.30x_A=1.30ct_A.
   \]

4. **Now we have the Joker’s distance and travel time.**  
   He travels from the origin to \(E_B\), so
   \[
   u=\frac{x_B}{t_B}
   =\frac{0.50ct_A}{1.30t_A}
   =\boxed{\frac5{13}c}
   \]
   rightward, toward Batman.

**The whole purpose was to locate \(E_B\): halfway gives its horizontal position, simultaneity gives its height, and those give the Joker’s velocity.**

---

**Learner**

should the x' arrow also point right? draw the graph again for me

**Tutor**

Yes—the positive \(x'\) direction points down and right along your simultaneity line. I’ll redraw it with the ground-frame axes upright and label the events.

---

**Learner**

regular brainless lorents transform wont work?

**Tutor**

**Yes—straight Lorentz transformations work.** I made this more geometric than necessary.

Keep ground coordinates \((x,ct)\), with ignition at the origin. Batman moves at \(\beta=-0.60\), so
\[
ct'=\gamma(ct+0.60x),\qquad
x'=\gamma(x+0.60ct).
\]

Then translate the problem into equations:

- Light reaches Batman at \(A\): \(x_A=ct_A\).
- \(A,B,C\) are simultaneous for Batman: \(t'_A=t'_B=t'_C\).
- The Joker is halfway: \(x'_B=(x'_A+x'_C)/2\).
- The tree stays at \(x_C=0\).

Substitute the Lorentz formulas, solve for \(x_B,t_B\), then use \(u=x_B/t_B\).

These formulas put both coordinate origins at **ignition**. Batman’s coordinate needn’t be zero; the midpoint equation handles that.

---

**Learner**

handhold me, from the graph

**Tutor**

We’ll stay with **your ground-frame graph**, one step at a time.

Look at the sloping line containing \(E_C\), \(E_B\), and \(E_A\). It connects the tree, Joker, and Batman **at the same Batman-frame time**.

“Joker is halfway” therefore means the two **Batman-frame distances** are equal:
\[
\boxed{x'_B-x'_C=x'_A-x'_B.}
\]

That’s our starting equation. We **keep \(x'_C\)**: the tree lies at \(x_C=0\) on your upright axis, but that does not make its Batman-frame coordinate zero.

Write that equation beside your graph; we’ll handle just one of those distances next.

---

**Learner**

we dont have to, one little step at a time, whichever way i need to be learning to do it systematically and consistently

**Tutor**

We’ll use a consistent sequence, one step at a time.

**First: choose the frame where the condition is stated.** Here, “halfway” is stated in **Batman’s frame**, so we’ll work there first.

Draw upright \(x'\) and \(ct'\) axes. Put Batman at \(x'=0\); his worldline is the vertical axis.

Just that for now.

---

**Learner**

But it asked about ground frame. Maybe upright frame should be ground

**Tutor**

The answer must be in the **ground frame**, but the calculation can start in either frame. Upright axes simply show which frame’s coordinates you’re using.

**Let’s keep your ground-frame graph.** It works, and we’ll stick with it.

Our first step is to label the unknown: call the Joker’s ground-frame velocity \(u\). Since his worldline passes through the origin,
\[
\boxed{x_B=u\,t_B.}
\]

That’s the velocity we’re trying to find.

---

**Learner**

i know that we should find the coordinates of B

**Tutor**

Right. To locate \(B\), first use the fact that **\(A\) and \(B\) happen at the same Batman-frame time**:
\[
t'_B=t'_A.
\]

Using Batman’s velocity \(v=-0.60c\), the time Lorentz transformation gives
\[
\boxed{ct_B+0.60x_B=ct_A+0.60x_A.}
\]

That is our first equation connecting \(B\)’s unknown coordinates to \(A\).

---

**Learner**

how could i have known this is a next step? also how about valocity addition?

**Tutor**

**You choose the next equation by translating a condition in the question.**

Here, “the Joker is halfway when Batman receives the light, **in Batman’s frame**” compares positions at one Batman-frame time. Your graph represents that with \(A,B,C\) on the same sloping line. That tells you:
\[
t'_A=t'_B=t'_C.
\]
Because you want ground-frame coordinates, the **time Lorentz transformation** connects that condition to \(x_B,t_B\).

**Velocity addition is also a valid route.** It connects the Joker’s velocity in Batman’s frame, \(u'\), to his ground velocity, \(u\). But initially both are unknown. You must first use the halfway condition to find \(u'\); then velocity addition gives \(u\).

So there are two routes:

- **Your ground-frame graph:** use simultaneity and halfway to find \(B\), then \(u=x_B/t_B\).
- **Batman’s frame:** use halfway to find \(u'\), then transform the velocity.

I kept switching between these routes, which made the sequence harder to follow. We’ll stick with your ground-frame graph.

---

**Learner**

lets start

**Tutor**

We’ll start in **Batman’s frame**, using an ordinary position sketch.

Put Batman at \(x'=0\). At the instant the Joker lights the tree, put **both the tree and Joker at \(x'=-D\)**, where \(D\) is their initial distance from Batman:

\[
\underbrace{\text{Tree + Joker}}_{x'=-D}
\quad \xrightarrow{\hspace{1.5cm}D\hspace{1.5cm}}\quad
\underbrace{\text{Batman}}_{x'=0}
\]

Call this instant \(t'=0\). Batman stays at \(x'=0\).

---

**Learner**

ok

**Tutor**

The light travels from the tree at \(x'=-D\) to Batman at \(x'=0\), at speed \(c\).

**How much time passes in Batman’s frame before it reaches him?**

---

**Learner**

D/c

**Tutor**

Correct: \(t'=D/c\).

In Batman’s frame, the tree moves **right at \(0.60c\)**. How far does it move during that time?

---

**Learner**

D

**Tutor**

The light travels \(D\). The tree is slower, so its distance is
\[
(0.60c)\frac{D}{c}=0.60D.
\]

It started at \(x'=-D\) and moved right by \(0.60D\). **What is its new position?**

---

**Learner**

0.8d

**Tutor**

Correct: \(+0.80D\). The elapsed time is \(D/c\).

**What is the Joker’s velocity in Batman’s frame?**

---

**Learner**

.8c

**Tutor**

Correct: \(u'=+0.80c\).

Now convert to the ground frame. Batman’s ground velocity is \(v=-0.60c\):
\[
u=\frac{u'+v}{1+u'v/c^2}.
\]

**Substitute those two signed velocities.**

---

**Learner**

ok. lets now do the spacetime diagram, which shouldn't be more difficult

**Tutor**

Yes—the same reasoning fits directly onto a spacetime diagram. **Keep Batman’s frame upright** so we can reuse everything you just found.

Draw horizontal \(x'\) and vertical \(ct'\) axes:

- Batman’s worldline is the vertical axis, \(x'=0\).
- Mark ignition at \((x',ct')=(-D,0)\).

**Draw the light ray from \((-D,0)\) up and right at \(45^\circ\)**, using equal scales on both axes, until it meets Batman’s worldline.

---

**Learner**

why shoulnt i write Ct'A as 0,0?

**Tutor**

**You can choose \(A\) to be \((x'_A,ct'_A)=(0,0)\).** But then the transformations must include that shifted origin.

The formulas I just used put ignition at both origins. For your choice, write:
\[
ct'_A=\gamma\big[(ct_A-ct_A)+0.60(x_A-x_A)\big]=0,
\]
\[
ct'_J=\gamma\big[(ct_J-ct_A)+0.60(x_J-x_A)\big].
\]

Since \(J\) is simultaneous with \(A\), set \(ct'_J=0\):
\[
\boxed{0=\gamma\big[(ct_J-ct_A)+0.60(x_J-x_A)\big].}
\]

Same result. **Your origin choice is valid—I switched conventions without making that clear.**

---

**Learner**

but technically everyhting is delta

**Tutor**

**Yes—if you’re using the difference form, everything is a delta, and the origin doesn’t matter.** I overcomplicated that.

Between \(A\) and \(J\):
\[
c(t'_J-t'_A)
=\gamma\left[c(t_J-t_A)+0.60(x_J-x_A)\right].
\]

They’re simultaneous in Batman’s frame, so the left side is zero. You can also choose \(t'_A=0\), making \(t'_J=0\).

The only distinction: **\(t_J-t_A\) is the interval from \(A\) to \(J\); \(t_J\) alone is the time from ignition to \(J\).**

---

**Learner**

gamma * 10^-7 with beta=0.8

**Tutor**

Correct—that gives the **laboratory lifetime**:
\[
\Delta t=\gamma(0.8)\times10^{-7}\,\mathrm s.
\]

The question asks for **distance travelled**; your answer is one step short.

---

**Learner**

my brain is so DUMB today wtf?

**Tutor**

You’re frustrated, and today has taken a lot of effort. But **you just independently used interval invariance, correctly set up time dilation, and spotted that a spatial LT could solve this directly.** Those are meaningful pieces of understanding.

The sticking point here was identifying \(\Delta x'=0\), not the whole problem. And the long Batman detour—including my confusing guidance—didn’t help.

**Take five minutes away from the page.** Then we can return with one clean problem. No need to judge your ability from this session.
