# Find four-vector introduction

**Learner**

in this case S squared is negative, we need complex numbers, right?

**Tutor**

**Only if you insist on taking \(\sqrt{S^2}\).** Usually, we leave the spacetime interval as \(S^2\), which can be negative—it isn’t the square of an ordinary distance.

With **your course’s convention**, timelike events satisfy
\[
S^2=-c^2(\Delta\tau)^2<0.
\]
To find proper time, use
\[
\boxed{\Delta\tau=\frac{\sqrt{-S^2}}{c}},
\]
which is real.

The video uses the opposite sign, so it writes \(s^2=c^2(\Delta\tau)^2>0\) and \(s=c\Delta\tau\). **Neither convention requires complex numbers.**

---

**Learner**

these vectors are invariant? X, U, P, A, F are invariant?

**Tutor**

**Their components are not invariant.** \(X,U,P,A,F\) are four-vectors, so their components **change according to the Lorentz transformations** when you change frames.

For example,
\[
P=(E/c,p_x,p_y,p_z).
\]
Different observers generally measure different energy and momentum, so they obtain different components of \(P\).

What **is invariant** is its **Minkowski squared magnitude**. Using your course’s sign convention,
\[
P\cdot P=-\frac{E^2}{c^2}+p_x^2+p_y^2+p_z^2=-m^2c^2.
\]
Every observer gets the same value for this combination.

The same principle applies to all five:

- **Components:** frame-dependent.
- **Minkowski dot products**, such as \(U\cdot U\) or \(A\cdot A\): frame-independent.

You may hear “the vector itself is unchanged”: that means observers describe the **same geometric object using different components**. It does **not** mean \(X'=X\), \(P'=P\), etc.

---

**Learner**

but if they're expressed as a sum then they're indeed invariant?

**Tutor**

**Yes—if you mean the sum of components multiplied by their basis vectors.**

For example,
\[
X=X^0e_0+X^1e_1+X^2e_2+X^3e_3.
\]
Here \(X^\mu\) are the components, and \(e_\mu\) are the basis vectors defining the coordinate directions.

When you change frames, **both the components and the basis vectors change**, compensating so that
\[
\boxed{X=\sum_{\mu=0}^{3}X^\mu e_\mu
       =\sum_{\mu=0}^{3}X'^\mu e'_\mu}.
\]
The complete geometric vector is the same. This applies to \(U,P,A,F\) too.

But simply adding the components, \(X^0+X^1+X^2+X^3\), is **not invariant**.

So your point is correct for the **vector expressed in its basis**—my previous answer distinguished that from its changing components.
