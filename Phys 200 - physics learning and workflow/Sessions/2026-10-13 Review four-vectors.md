# Review four-vectors

**Learner**

yeah we haven't talked about why we differentiated with respect to tao.

**Tutor**

Right—I stated that we use \(\tau\), but didn’t explain why.

We want a velocity-like quantity built from the four-displacement
\[
dX^\mu=(c\,dt,dx,dy,dz).
\]
That means dividing by a time interval. **The choice of time matters because we want the result to remain a four-vector.**

If each observer divides by their own coordinate time, they use different denominators:
\[
\frac{dX^\mu}{dt}
\quad\text{and}\quad
\frac{dX'^\mu}{dt'}.
\]
The numerator changes by a Lorentz transformation, but the denominator changes too. The resulting components therefore don’t follow the four-vector transformation rule.

Instead, both observers divide by **the same particle-clock interval \(d\tau\)**. For example, start with
\[
dx'=\gamma_v(dx-v\,dt).
\]
Dividing by that shared interval gives
\[
\frac{dx'}{d\tau}
=\gamma_v\left(\frac{dx}{d\tau}-v\frac{dt}{d\tau}\right),
\]
or
\[
U'^x=\gamma_v\left(U^x-\frac vc U^0\right).
\]
That is exactly the required four-vector rule.

So **we differentiate with respect to proper time because it gives us a velocity-like quantity that transforms as a four-vector**. Its spatial components measure distance in the observer’s frame per second elapsed on the particle’s clock. Ordinary velocity still uses the observer’s coordinate time.

---

**Learner**

teach in terms of questions. lets begin.

**Tutor**

**Generated**

A particle moves along the \(x\)-axis. You propose defining its four-velocity using the lab’s time:
\[
B^\mu=\frac{dX^\mu}{dt}=(c,u,0,0).
\]

In another frame, you use the same definition:
\[
B'^\mu=\frac{dX'^\mu}{dt'}.
\]

From this definition alone, what must the zeroth component \(B'^0\) equal?

---

**Learner**

c

**Tutor**

Correct: \(B'^0=c\), by its definition.

Now test whether that agrees with the four-vector rule:
\[
B'^0=\gamma_v\left(B^0-\frac vc B^1\right).
\]

**Generated**

Take a particle at rest in the lab, so \(B^\mu=(c,0,0,0)\). A second frame moves at a nonzero speed \(v\).

What does the transformation rule predict for \(B'^0\), and does it agree with the value \(c\) required by the definition?

---

**Learner**

if i take for granted that taking derivative respect to t' violates a rule for the 4 vector

**Tutor**

Yes—you can take that result as given for now: **using each frame’s coordinate time to define \(dX^\mu/dt\) does not produce a four-vector.** We can move on to what using proper time gives us.

Proper time \(\tau\) is time measured by the particle’s own clock. For a particle moving at speed \(u\) in the lab,
\[
dt=\gamma_u\,d\tau.
\]

We define
\[
U^\mu=\frac{dX^\mu}{d\tau}.
\]

**Generated**

The particle’s lab position is \(x=ut\). Using the chain rule,
\[
U^x=\frac{dx}{d\tau}
=\frac{dx}{dt}\frac{dt}{d\tau}.
\]

What does this give for \(U^x\) in terms of \(u\) and \(\gamma_u\)?

---

**Learner**

This is u, gamma u.

**Tutor**

Correct: \(U^x=\gamma_u u\).

Applying the same derivative to all four components gives
\[
U^\mu=(\gamma_u c,\gamma_u u,0,0).
\]
Multiplying by the particle’s rest mass \(m\) gives **four-momentum**:
\[
P^\mu=mU^\mu=(\gamma_u mc,\gamma_u mu,0,0).
\]
Its spatial component is relativistic momentum, \(p_x=\gamma_u mu\). Its zeroth component represents energy through \(P^0=E/c\).

**Generated**

For a particle **at rest**, \(u=0\) and \(\gamma_u=1\). What are its momentum \(p_x\) and energy \(E\)?

---

**Learner**

this is a velocity like thing, but its not really velocity is it

**Tutor**

Exactly. **Its spatial components aren’t ordinary velocity**, because the distance and elapsed time are measured using different frames’ measurements:
\[
u_x=\frac{dx}{dt},
\qquad
U^x=\frac{dx}{d\tau}=\gamma_u u_x.
\]

Four-velocity describes how all four spacetime coordinates change **per second of the particle’s own aging**. Ordinary velocity describes spatial motion per second of the chosen frame’s time.

For the spaceship example—4 light-years travelled in Earth coordinates during 3 onboard years—what does \(U^x=4/3\) light-years per onboard year tell you, and why doesn’t it establish faster-than-light motion?

---

**Learner**

but somehow when we go a step further these celocity like things become actual momentum?

**Tutor**

Yes—and that connection needs justification. **Multiplying four-velocity by mass gives a candidate for physical momentum; the name alone doesn’t establish it.**

Its spatial part is
\[
\mathbf p=m\frac{d\mathbf x}{d\tau}
=\gamma_u m\mathbf u.
\]
This is **relativistic momentum**. The familiar \(m\mathbf u\) is its low-speed approximation.

Why identify this quantity as momentum? It approaches \(m\mathbf u\) at low speeds, and its conservation—together with the energy component—agrees with collision experiments and works consistently between inertial frames. Being a four-vector alone does **not** guarantee conservation.

So the physical lesson is that **momentum isn’t exactly mass times ordinary velocity**. That familiar relationship is an approximation.

Let’s examine the connection through a question: as \(u\) gets much smaller than \(c\), what happens to \(\gamma_u\), and therefore to \(\gamma_u m\mathbf u\)?

---

**Learner**

lets not get side tracked too far here, lets go back and this is gonna be my first ish apss

**Tutor**

We’ll treat this as a **first pass** and build the main connections without proving every step.

We have
\[
U^\mu=(\gamma_u c,\gamma_u\mathbf u).
\]
Multiplying by rest mass gives
\[
P^\mu=mU^\mu
=(\gamma_u mc,\gamma_u m\mathbf u)
=\left(\frac Ec,\mathbf p\right).
\]

The first component encodes **energy**; the other three encode **momentum**.

Using the first component,
\[
\frac Ec=\gamma_u mc,
\]
what is the particle’s energy \(E\)?

---

**Learner**

what is t? stop giving anything that i can't figure out myslef

**Tutor**

\(t\) is **time measured in the frame whose coordinates \(x,y,z\) you’re using**. If those are lab coordinates, \(t\) is lab time.

\(\tau\) is **time measured by a clock travelling with the particle**.

I’ll define the symbols and let you work out the steps.

---

**Learner**

MC squared gamma.

**Tutor**

Correct: \(E=\gamma mc^2\).

For a particle **at rest**, what does this give for its energy?

---

**Learner**

MC squared.

**Tutor**

Correct—its **rest energy** is \(E_0=mc^2\).

Kinetic energy is the extra energy due to motion: \(K=E-E_0\). Using your two results, what is \(K\) for the moving particle?

---

**Learner**

should i write the four vectors vertical?

**Tutor**

Either is fine. A vertical column is convenient, especially for matrix transformations:
\[
P^\mu=
\begin{pmatrix}
E/c\\
p_x\\
p_y\\
p_z
\end{pmatrix}.
\]
Keep the order **time, \(x\), \(y\), \(z\)**.

---

**Learner**

wait a second, for these questions i have to LT each one?

**Tutor**

**No—you don’t have to start from position and Lorentz-transform it every time.** There are two routes:

- If you know the particle’s velocity in the frame you want, construct its four-momentum directly:
  \[
  P^\mu=(\gamma mc,\gamma m u_x,\gamma m u_y,\gamma m u_z).
  \]
  Here \(\gamma\) uses the particle’s speed in that frame.
- If you know its four-momentum in another frame, Lorentz-transform that four-momentum directly.

For this question, the first route is enough: **what is the stationary lab particle’s velocity as measured from the spaceship?**

---

**Learner**

how to lorentz tranform 4 vectors again

**Tutor**

For a frame \(S'\) moving at \(+v\) along \(x\) relative to \(S\), **any four-vector** transforms as
\[
\begin{aligned}
A'^0&=\gamma_v(A^0-\beta A^x),\\
A'^x&=\gamma_v(A^x-\beta A^0),\\
A'^y&=A^y,\\
A'^z&=A^z,
\end{aligned}
\qquad
\beta=\frac vc,\quad
\gamma_v=\frac1{\sqrt{1-v^2/c^2}}.
\]

Only the zeroth and \(x\)-components mix. For four-momentum, substitute \(P\) for \(A\), remembering that \(P^0=E/c\).

Your particle is at rest in the lab, so
\[
P^\mu=(mc,0,0,0).
\]
**What do the first two transformation equations give for \(P'^0\) and \(P'^x\)?**

---

**Learner**

-beta gamma ct

**Tutor**

Correct: \(x'=-\beta\gamma_v ct\). So
\[
X'^\mu=(\gamma_v ct,\;-\beta\gamma_v ct,\;0,\;0).
\]

The particle is at rest in the lab, so its proper-time interval satisfies \(d\tau=dt\).

Using \(P'^\mu=m\,dX'^\mu/d\tau\), **what four-momentum do you get?**

---

**Learner**

give the problem again

**Tutor**

A particle of rest mass \(m\) is **stationary in the lab**. A spaceship moves along the lab’s \(+x\) direction at speed \(v\).

Find the particle’s **four-momentum as measured in the spaceship frame**:
\[
P'^\mu=
\begin{pmatrix}
E'/c\\
p'_x\\
p'_y\\
p'_z
\end{pmatrix}.
\]

---

**Learner**

show via lorents transform

**Tutor**

For a frame moving at \(+v\) along \(x\), the full Lorentz transformation is
\[
\begin{pmatrix}
ct'\\x'\\y'\\z'
\end{pmatrix}
=
\begin{pmatrix}
\gamma&-\beta\gamma&0&0\\
-\beta\gamma&\gamma&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}
\begin{pmatrix}
ct\\0\\0\\0
\end{pmatrix},
\qquad \beta=\frac vc.
\]

The last two rows give
\[
y'=0(ct)+0(0)+1(0)+0(0)=0,
\]
\[
z'=0(ct)+0(0)+0(0)+1(0)=0.
\]

So the transformed position is
\[
X'^\mu=
\begin{pmatrix}
\gamma ct\\
-\beta\gamma ct\\
0\\
0
\end{pmatrix}.
\]

---

**Learner**

how did you get the matrix

**Tutor**

The matrix is just the **coefficients from the Lorentz equations**, arranged in rows.

Start with
\[
\begin{aligned}
ct'&=\gamma ct-\beta\gamma x,\\
x'&=-\beta\gamma ct+\gamma x,\\
y'&=y,\\
z'&=z.
\end{aligned}
\]

The input column is ordered \((ct,x,y,z)\). Each matrix row lists what multiplies those four inputs.

For example,
\[
ct'=\gamma(ct)+(-\beta\gamma)x+0y+0z
\]
gives the first row
\[
(\gamma,\;-\beta\gamma,\;0,\;0).
\]

**Using \(y'=y\), what coefficients would you put in the third row?**

---

**Learner**

this chat has been frustrating.

**Tutor**

Yes. I kept introducing unexplained notation, giving away steps you wanted to derive, and then asking tiny substitution questions. When you asked where something came from, I sometimes repeated it instead of addressing the missing reasoning. That made this harder than it needed to be.

You asked for a first pass through questions. I’ll keep one frame setup, define new symbols before using them, and distinguish what we’re taking as given from what you can derive. No more matrices or extra machinery unless they help.

We can restart from your correct work: **you derived four-velocity, multiplied by mass, and obtained total, rest, and kinetic energy.** The point to rebuild is how those quantities change between frames.
