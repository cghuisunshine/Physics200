# Review Quiz 2 content

**Learner**

week 3 thurs was BEFORE quiz 1?

**Tutor**

**Yes—Week 3 Thursday was before at least some Quiz 1 sittings.** Its opening slide tells students booked immediately after class to rebook for 3 p.m. or later.

I shouldn’t have equated “Week 3 Thursday material” with “taught after Quiz 1.” **The explicit Quiz 2 scope still includes Lorentz transformations and velocity addition**, regardless of when they were taught.

---

**Learner**

what happens if some moving thing shines a light forward? qualitatively

**Tutor**

The light travels forward at **\(c\) in both the moving object’s frame and the ground frame**. The object’s speed does not get added to the light’s speed.

From the ground, the light moves at \(c\) while the object follows at \(v\), so their gap grows at \(c-v\).

From the object’s own frame, it is stationary and the light moves away at \(c\). Those different gap-growth rates are consistent because the frames measure space and time differently.

---

**Learner**

how differently?

**Tutor**

Suppose the object moves forward at speed \(v\), and emits the light when both frames’ origins coincide.

In the **ground frame**, after time \(t\):
\[
x_{\text{light}}=ct,\qquad x_{\text{object}}=vt.
\]
So their simultaneous separation is \((c-v)t\).

But the moving frame doesn’t simply subtract the object’s position—it transforms **both space and time**. For the event at the light pulse,
\[
x'=\gamma(x-vt)=\gamma(c-v)t,
\]
\[
t'=\gamma\left(t-\frac{vx}{c^2}\right)
=\gamma t\left(1-\frac vc\right).
\]
Therefore,
\[
\frac{x'}{t'}=
\frac{\gamma(c-v)t}{\gamma(1-v/c)t}
=\boxed{c}.
\]

**The crucial difference is simultaneity:** the ground measures the light’s and object’s positions at the same ground time. Those two position measurements are **not simultaneous in the moving frame**. The moving observer uses a different pair of simultaneous events to measure the gap—so you cannot take the ground’s gap-growth rate \(c-v\) as the moving observer’s measured light speed.

---

**Learner**

the velocities along the y and z changes due to time dilation only? even though its not moving in the x direction

**Tutor**

**For this ball, yes:** because \(u_x=0\) in the ship, its vertical velocity changes solely through the time-dilation factor.

Two successive events on the ball’s path have the **same ship-frame \(x\)**, so
\[
\Delta t_{\text{Earth}}=\gamma_v\Delta t_{\text{ship}},
\qquad
\Delta y_{\text{Earth}}=\Delta y_{\text{ship}}.
\]
Earth measures the same upward displacement over a longer time, giving
\[
u_{y,\text{Earth}}=\frac{u_{y,\text{ship}}}{\gamma_v}.
\]

The ball has no horizontal motion **in the ship**, but it does move horizontally **relative to Earth**. The \(\gamma_v\) here comes from the relative speed of the frames.

**In general**, if \(u_x\neq0\), the extra \(1\pm u_xv/c^2\) factor also appears: relativity of simultaneity contributes to the transformed time interval. So transverse velocities do not always change by time dilation alone.

Also, a zero component stays zero—here \(u_z=0\), so Earth still measures \(u_z'=0\).

---

**Learner**

give the question again

**Tutor**

A spaceship moves right at \(0.6c\) relative to Earth. Inside the ship, someone throws a ball **straight upward at \(0.5c\)**, with no horizontal motion relative to the ship.

The Lorentz factor between the frames is \(\gamma=1.25\).

You correctly found that Earth measures the ball’s horizontal velocity as \(0.6c\). **What vertical velocity does Earth measure?**

---

**Learner**

derive these things with me?

**Tutor**

Yes—let’s derive the velocity transformations together, keeping the frame convention consistent.

Let \(S'\) move at velocity \(v\) along \(+x\) relative to \(S\). The Lorentz transformations are
\[
x'=\gamma(x-vt),\qquad
t'=\gamma\left(t-\frac{vx}{c^2}\right),\qquad
y'=y,\qquad z'=z.
\]

For two nearby events along the ball’s path,
\[
dt'=\gamma\left(dt-\frac{v\,dx}{c^2}\right).
\]

The ball’s horizontal velocity in \(S\) is \(u_x=dx/dt\).

**Divide the equation by \(dt\): what expression do you get for \(dt'/dt\) in terms of \(u_x\)?**

---

**Learner**

give some course gallelean transform questions

**Tutor**

**Course**

An observer rides on a wagon moving at \(50\,\mathrm{m/s}\) to the right relative to the ground. Their primed coordinates place the back of the wagon at \(x'=0\) and the floor at \(y'=0\).

At \(t'=0\), a kangaroo at \(x'=0,\ y'=2\,\mathrm m\) simply drops from rest relative to the wagon.

**Write \(x'(t')\) and \(y'(t')\) during the fall.** Neglect air resistance.

---

**Learner**

50 and -9.8 t

**Tutor**

Those look like **velocities**, but the question asks for **positions**.

Also, \(50\,\mathrm{m/s}\) is the wagon’s velocity relative to the ground. In the **wagon’s frame**, the kangaroo has no horizontal motion.

Try again: write \(x'(t')\) and \(y'(t')\), including its initial height of \(2\,\mathrm m\).

---

**Learner**

skip ,next

**Tutor**

I’ll mark that one skipped and move to the ground-frame part.

---

**Learner**

next skip

**Tutor**

I’ll skip that one too and switch to a direct frame-transformation question.
