# List velocity addition formulas

**Learner**

Give the variations of the velocity addition formula

**Tutor**

Let \(S'\) move at velocity \(v\) along \(+x\) relative to \(S\). An object has velocity \(u\) in \(S\) and \(u'\) in \(S'\).

**For motion along the same axis:**

| What you want | Formula |
|---|---|
| \(u\): object’s velocity in \(S\) | \(\displaystyle u=\frac{u'+v}{1+\frac{u'v}{c^2}}\) |
| \(u'\): object’s velocity in \(S'\) | \(\displaystyle u'=\frac{u-v}{1-\frac{uv}{c^2}}\) |
| \(v\): velocity of \(S'\) relative to \(S\) | \(\displaystyle v=\frac{u-u'}{1-\frac{uu'}{c^2}}\) |

Use **signed velocities**: motion in the negative direction gets a negative value.

**In terms of \(\beta=u/c\), \(\beta'=u'/c\), and \(\beta_v=v/c\):**

\[
\boxed{\beta=\frac{\beta'+\beta_v}{1+\beta'\beta_v}}
\qquad
\boxed{\beta'=\frac{\beta-\beta_v}{1-\beta\beta_v}}
\]

**If the object also moves perpendicular to the frame’s motion:**

\[
u'_x=\frac{u_x-v}{1-\frac{u_xv}{c^2}},
\qquad
u'_y=\frac{u_y}{\gamma_v\left(1-\frac{u_xv}{c^2}\right)},
\qquad
\gamma_v=\frac{1}{\sqrt{1-v^2/c^2}}.
\]

For the reverse transformation, swap primed and unprimed quantities and replace \(v\) with \(-v\). The \(z\)-component follows the same rule as \(y\).

---

**Learner**

The bottom equations are talking about movement along the x axis only?

**Tutor**

The **reference frame \(S'\) moves along the \(x\)-axis only**, but the **object can move in any direction**.

- \(u_x\) and \(u_y\) are the object’s velocity components measured in \(S\).
- \(u'_x\) and \(u'_y\) are its components measured in \(S'\).

Even though the frames move relative to each other only along \(x\), the object’s **\(y\)-velocity can change between frames**: \(y'=y\), but the elapsed time differs, so \(u'_y=dy'/dt'\) differs from \(u_y=dy/dt\).

If the object itself moves only along \(x\), then \(u_y=u'_y=0\), and you only need the first equation.

---

**Learner**

Timelike separated means delta s2 is negative

**Tutor**

Yes—using your course’s convention,
\[
\Delta s^2=\Delta x^2-c^2\Delta t^2,
\]
**timelike separation means \(\Delta s^2<0\)**: \(c|\Delta t|>|\Delta x|\).

There is enough time for something travelling **slower than light** to connect the two events.

---

**Learner**

They can’t be simultaneous in other frames, in other words delta T is too big to close

**Tutor**

Yes—**no inertial frame can make timelike-separated events simultaneous.** The time separation is too large relative to the spatial separation.

To make \(\Delta t'=0\), you would need
\[
v=\frac{c^2\Delta t}{\Delta x}.
\]
But timelike separation means \(c|\Delta t|>|\Delta x|\), so this requires **\(|v|>c\)**, which is impossible for an inertial frame.

Every inertial observer therefore agrees on **which event happened first**.
