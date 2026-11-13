# Clarify this concept

**Learner**

dont one lag behind another slightly?

**Tutor**

No—for a **travelling plane electromagnetic wave in vacuum**, neither field lags behind the other. At the same location, they reach their peaks and cross zero simultaneously.

You might imagine “the changing electric field creates the magnetic field, which then creates the electric field” as sequential steps. But they evolve **together as one coupled wave**, without a delay between them.

The perspective in the picture can make them look shifted; the aligned plots at the bottom show their timing more clearly.

---

**Learner**

9.44* 10^20>

**Tutor**

Yes—**\(9.44\times10^{20}\) electrons/s** is correct. You can enter `9.44e20`.

---

**Learner**

are they easily derived using derivatives

**Tutor**

Yes—**take differentials of the Lorentz transformations, then divide**. Let \(S'\) move at \(+v\) relative to \(S\):

\[
dx'=\gamma_v(dx-v\,dt),\qquad
dt'=\gamma_v\left(dt-\frac{v}{c^2}dx\right).
\]

Since \(u_x=dx/dt\),
\[
u_x'=\frac{dx'}{dt'}
=\frac{\gamma_v(dx-v\,dt)}
{\gamma_v(dt-v\,dx/c^2)}
=\boxed{\frac{u_x-v}{1-vu_x/c^2}}.
\]

For the transverse direction, \(y'=y\), so \(dy'=dy\):
\[
u_y'=\frac{dy'}{dt'}
=\frac{dy}{\gamma_v(dt-v\,dx/c^2)}
=\boxed{\frac{u_y}{\gamma_v(1-vu_x/c^2)}}.
\]
The \(z\) derivation is identical.

**The transverse velocities change because the time denominator changes**, even though \(y\) and \(z\) themselves don’t. Replace \(v\to -v\) to obtain the slide’s plus-sign versions.

---

**Learner**

if time denominator changes why isn't it a straightforward gamma?

**Tutor**

Because **time dilation alone applies when the two events occur at the same position in one frame**.

For velocity, we follow a moving particle between two nearby events. In \(S\), it changes position by \(dx=u_x\,dt\), so
\[
dt'=\gamma_v\left(dt-\frac{v\,dx}{c^2}\right)
=\gamma_v\,dt\left(1-\frac{vu_x}{c^2}\right).
\]

That extra factor comes from the **position-dependent term in the time transformation**, which accounts for relativity of simultaneity.

Since \(dy'=dy\),
\[
u_y'=\frac{u_y}{\gamma_v(1-vu_x/c^2)}.
\]

**If \(u_x=0\)**—the particle moves purely sideways in \(S\)—then \(dx=0\), and it *does* reduce to the straightforward \(u_y'=u_y/\gamma_v\).

---

**Learner**

what is v here on the denominator

**Tutor**

\(v\) is the **velocity of frame \(S'\) relative to frame \(S\)**, along the \(x\)-axis.

In \(1-vu_x/c^2\):

- \(v\): how fast the **frames** move relative to each other.
- \(u_x\): the **particle’s \(x\)-velocity measured in \(S\)**.

For example, if \(S\) is Earth and \(S'\) is a spaceship, \(v\) is the spaceship’s velocity relative to Earth; \(u_x\) is the particle’s velocity along \(x\), measured on Earth.

---

**Learner**

what if the thing is moving in both the x and y direction

**Tutor**

Then use **both components of its velocity in \(S\)**:
\[
u_x=\frac{dx}{dt},\qquad u_y=\frac{dy}{dt}.
\]

If \(S'\) moves at \(v\) along \(x\), the transformed components are
\[
\boxed{u_x'=\frac{u_x-v}{1-vu_x/c^2}},
\qquad
\boxed{u_y'=\frac{u_y}{\gamma_v(1-vu_x/c^2)}}.
\]

**Only \(u_x\) appears in the shared denominator**, because the frames move relative to each other along \(x\): the time transformation contains \(dx\), but no \(dy\).

Also, \(\gamma_v=1/\sqrt{1-v^2/c^2}\) uses the **frame speed \(v\)**, not the particle’s total speed \(\sqrt{u_x^2+u_y^2}\).

---

**Learner**

do missing jar jar part b

**Tutor**

**Course — Missing Jar-Jar (b)**

A starship travels horizontally at \(0.6c\) relative to the ground. In the ship’s frame, it fires a laser pulse **straight downward**, perpendicular to its motion.

Taking \(+x\) along the ship’s motion and \(+y\) upward, **what are the horizontal and vertical components of the laser pulse’s velocity in the ground frame?**

---

**Learner**

give a few questions for me to practice, don't make them too long

**Tutor**

Three short ones, one at a time.

**Generated — 1/3**

In Earth’s frame, a particle has velocity components \(u_x=0.8c\) and \(u_y=0.3c\). A spaceship moves at \(0.6c\) along \(+x\) relative to Earth.

What are the particle’s velocity components in the spaceship’s frame?

---

**Learner**

0.5c/gamma

**Tutor**

Correct—\(0.5c/\gamma\). I’ll record that and move to the last question.
