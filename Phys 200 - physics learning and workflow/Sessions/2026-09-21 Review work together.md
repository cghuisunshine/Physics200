# Review work together

**Learner**

how should i be taking the derivative of gamma?

**Tutor**

It depends on **which variable you differentiate with respect to**.

If you use \(v\), write
\[
\gamma(v)=\left(1-\frac{v^2}{c^2}\right)^{-1/2}.
\]
Apply the chain rule: differentiate the outer power, then multiply by the derivative of the inside:
\[
\frac{d\gamma}{dv}
=\underbrace{-\frac12\left(1-\frac{v^2}{c^2}\right)^{-3/2}}_{\text{outer derivative}}
\underbrace{\left(-\frac{2v}{c^2}\right)}_{\text{inner derivative}}
=\boxed{\frac{v}{c^2}\left(1-\frac{v^2}{c^2}\right)^{-3/2}}.
\]
So your approach was close—you were missing the \(v\) in \(-2v/c^2\).

**For Q1, it’s easier to differentiate with respect to \(z=v^2/c^2\):**
\[
\gamma(z)=(1-z)^{-1/2},
\qquad
\frac{d\gamma}{dz}
=-\frac12(1-z)^{-3/2}(-1)
=\frac12(1-z)^{-3/2}.
\]
Here the inner derivative is just \(-1\), because the variable is \(z\).

---

**Learner**

yeah but thats incomplete?

**Tutor**

Yes—you’re right. **The derivative alone doesn’t finish the Taylor expansion.** Continuing your approach with \(v\):

\[
\gamma(v)\approx\gamma(0)+\gamma'(0)v+\frac{\gamma''(0)}{2}v^2.
\]

We have \(\gamma(0)=1\) and
\[
\gamma'(v)=\frac{v}{c^2}\left(1-\frac{v^2}{c^2}\right)^{-3/2},
\qquad \gamma'(0)=0.
\]

Differentiate again using the **product rule**:
\[
\gamma''(v)=
\frac{1}{c^2}\left(1-\frac{v^2}{c^2}\right)^{-3/2}
+\frac{3v^2}{c^4}\left(1-\frac{v^2}{c^2}\right)^{-5/2}.
\]
At \(v=0\), this gives \(\gamma''(0)=1/c^2\). Therefore,
\[
\gamma(v)\approx 1+0v+\frac{1}{2c^2}v^2
=\boxed{1+\frac{v^2}{2c^2}}.
\]

The “two terms” are the first two **nonzero** terms; the linear term vanishes.

---

**Learner**

why doesn't it make a difference what variable you derive regards

**Tutor**

**It does change the derivative.** But if you carry out the Taylor expansion consistently, you get the same approximation for \(\gamma\).

With \(z=v^2/c^2\), the expansion is
\[
\gamma\approx 1+\frac12z.
\]
Substituting back gives
\[
\gamma\approx 1+\frac{v^2}{2c^2}.
\]

With \(v\), the expansion is
\[
\gamma\approx 1+\underbrace{\gamma'(0)}_{0}v
+\frac12\underbrace{\gamma''(0)}_{1/c^2}v^2
=1+\frac{v^2}{2c^2}.
\]

So **a first-order term in \(z\) is a second-order term in \(v\)**, because \(z=v^2/c^2\). We’re keeping the same contribution, just expressing it using different variables.

If you stopped at first order in \(v\), you’d get only \(\gamma\approx1\)—so matching the order of the retained terms matters.

---

**Learner**

so does it take derivative reguarding v or z?

**Tutor**

**For this question, differentiate with respect to \(z=v^2/c^2\).** The wording asks you to expand near \(v^2/c^2=0\), treating that whole quantity as the variable.

Write \(\gamma(z)=(1-z)^{-1/2}\), use
\[
\gamma(z)\approx\gamma(0)+\gamma'(0)z,
\]
then substitute \(z=v^2/c^2\) back in.

Differentiating with respect to \(v\) also works, but requires the second derivative here.

---

**Learner**

step by step derive with reguard to v, and tell me how they're equivalent, one has an extra factor of dz dv and the other doesnt.

**Tutor**

You’re right that differentiating with respect to \(v\) introduces an extra factor \(\frac{dz}{dv}\). **The derivatives are different; the final Taylor approximations agree.** Here’s how.

**1. Define the two functions.**

Let
\[
z(v)=\frac{v^2}{c^2},\qquad f(z)=(1-z)^{-1/2}.
\]
Then \(\gamma(v)=f(z(v))\).

Differentiating \(f\) with respect to \(z\):
\[
f'(z)=\frac12(1-z)^{-3/2}.
\]

**2. Differentiate \(\gamma\) with respect to \(v\).**

The chain rule requires your extra factor:
\[
\frac{d\gamma}{dv}
=\frac{df}{dz}\frac{dz}{dv}
=\frac12(1-z)^{-3/2}\frac{2v}{c^2}.
\]
Thus
\[
\gamma'(v)=\frac{v}{c^2}\left(1-\frac{v^2}{c^2}\right)^{-3/2},
\qquad \gamma'(0)=0.
\]

**3. Differentiate again.**

Starting from \(\gamma'=f'(z)z'\), apply the product and chain rules:
\[
\gamma''(v)=f''(z)(z')^2+f'(z)z''.
\]
The pieces are
\[
f''(z)=\frac34(1-z)^{-5/2},
\qquad z'=\frac{2v}{c^2},
\qquad z''=\frac{2}{c^2}.
\]
So
\[
\gamma''(v)
=\frac{3v^2}{c^4}\left(1-\frac{v^2}{c^2}\right)^{-5/2}
+\frac1{c^2}\left(1-\frac{v^2}{c^2}\right)^{-3/2}.
\]
At \(v=0\):
\[
\gamma''(0)=0+\frac1{c^2}.
\]

**4. Build the Taylor expansion in \(v\).**

\[
\gamma(v)\approx\gamma(0)+\gamma'(0)v+\frac{\gamma''(0)}{2}v^2
=1+0+\frac{v^2}{2c^2}.
\]

**5. Compare with expanding in \(z\).**

\[
f(z)\approx f(0)+f'(0)z=1+\frac12z
=1+\frac{v^2}{2c^2}.
\]

The extra chain-rule factor **never disappeared**. In the \(v\) calculation, it makes the first derivative zero at \(v=0\), and differentiating again produces the coefficient of \(v^2\):
\[
\underbrace{\frac12\gamma''(0)v^2}_{\text{quadratic term in }v}
=\frac12\left[f'(0)\frac{2}{c^2}\right]v^2
=\underbrace{f'(0)z}_{\text{linear term in }z}.
\]

That is exactly why the two routes agree.

---

**Learner**

always use liebniz notation

**Tutor**

Got it—I’ll use **Leibniz notation** throughout: \(\frac{d\gamma}{dv}\), \(\frac{d^2\gamma}{dv^2}\), and \(\frac{dz}{dv}\), rather than prime notation.

---

**Learner**

re do it then

**Tutor**

The derivatives with respect to \(v\) and \(z\) **are different**. The Taylor approximations agree because we include the chain-rule factors when using \(v\).

Let
\[
z=\frac{v^2}{c^2},\qquad \gamma=(1-z)^{-1/2}.
\]

**1. Differentiate with respect to \(v\).**

First,
\[
\frac{d\gamma}{dz}=\frac12(1-z)^{-3/2},
\qquad
\frac{dz}{dv}=\frac{2v}{c^2}.
\]

Using the chain rule,
\[
\frac{d\gamma}{dv}
=\frac{d\gamma}{dz}\frac{dz}{dv}
=\frac12(1-z)^{-3/2}\frac{2v}{c^2}
=\frac{v}{c^2}\left(1-\frac{v^2}{c^2}\right)^{-3/2}.
\]
At \(v=0\),
\[
\left.\frac{d\gamma}{dv}\right|_{v=0}=0.
\]

**2. Differentiate again with respect to \(v\).**

Apply the product rule to the chain-rule expression:
\[
\frac{d^2\gamma}{dv^2}
=\frac{d}{dv}\left(\frac{d\gamma}{dz}\frac{dz}{dv}\right)
=\frac{d^2\gamma}{dz^2}\left(\frac{dz}{dv}\right)^2
+\frac{d\gamma}{dz}\frac{d^2z}{dv^2}.
\]

Here,
\[
\frac{d^2\gamma}{dz^2}=\frac34(1-z)^{-5/2},
\qquad
\frac{d^2z}{dv^2}=\frac{2}{c^2}.
\]
Therefore,
\[
\frac{d^2\gamma}{dv^2}
=\frac34(1-z)^{-5/2}\left(\frac{2v}{c^2}\right)^2
+\frac12(1-z)^{-3/2}\frac{2}{c^2}.
\]

At \(v=0\), we also have \(z=0\), so
\[
\left.\frac{d^2\gamma}{dv^2}\right|_{v=0}
=0+\frac12\frac{2}{c^2}
=\frac1{c^2}.
\]

**3. Construct the Taylor expansion in \(v\).**

\[
\gamma(v)\approx
\gamma(0)
+\left.\frac{d\gamma}{dv}\right|_{v=0}v
+\frac12\left.\frac{d^2\gamma}{dv^2}\right|_{v=0}v^2.
\]
Substituting,
\[
\gamma(v)\approx1+0+\frac{v^2}{2c^2}.
\]

**4. Compare with the expansion in \(z\).**

When expanding directly in \(z\),
\[
\gamma(z)\approx
\gamma(0)+\left.\frac{d\gamma}{dz}\right|_{z=0}z
=1+\frac12z
=1+\frac{v^2}{2c^2}.
\]

**The extra \(\frac{dz}{dv}\) factor is required only when differentiating with respect to \(v\).** When expanding in \(z\), we differentiate with respect to \(z\) and multiply the resulting coefficient by \(z\).

The matching terms are
\[
\boxed{
\frac12\left.\frac{d^2\gamma}{dv^2}\right|_{v=0}v^2
=
\left.\frac{d\gamma}{dz}\right|_{z=0}z
=
\frac{v^2}{2c^2}
}.
\]
A linear term in \(z\) is a quadratic term in \(v\), because \(z=v^2/c^2\).
