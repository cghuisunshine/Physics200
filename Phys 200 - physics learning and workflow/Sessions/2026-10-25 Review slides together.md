# Review slides together

**Learner**

ah, no. frequency concerns energy per photon, but E0 denotes how energetic the whole beam is

**Tutor**

Yes—frequency determines energy per photon, while \(E_0\) is the electric-field amplitude, with intensity proportional to \(E_0^2\). So the heating-rate ranking is \(1=2>3\).

---

**Learner**

how many questions does it take to cover the whole slides?

**Tutor**

About **15–20 questions total**, including the two already presented:

- Waves and photons: 2–3
- Photoelectric effect: 6–8
- Absorption and conservation laws: 2–3
- Compton scattering: 3–4
- Blackbody radiation: 1–2

We’ll combine overlapping slides and move quickly through what you already know. Extra questions would only be for gaps you want to work on.

---

**Learner**

Because beam two has a higher energy per photon, for the same intensity, beam two has fewer photons.

**Tutor**

Correct—beam 2 has twice the energy per photon, so it delivers half as many photons per second at the same intensity and illuminated area.

---

**Learner**

no because the intensity of light is different from energy per photon. 

And since the latter is unchanged, the stopping voltage is identical, and so retarding voltage remains at the stopping voltage, and so the current does not flow again.

**Tutor**

Correct. More photons arrive, but the maximum electron kinetic energy stays unchanged, so the same retarding voltage still stops the current.

---

**Learner**

C

**Tutor**

Correct—fixed power and unchanged wavelength mean the same total number of photons arrives per second, so the total photocurrent stays the same.

---

**Learner**

C

**Tutor**

Correct—C. The initial momenta cancel, but the initial energy is \(E_{e,\text{initial}}+hf>m_ec^2\), while the final stationary electron has only \(m_ec^2\). Energy conservation therefore rules out this process.

---

**Learner**

i dont understand. momentum sink?

**Tutor**

Yes—**“momentum sink” is a useful description**, provided we mean the metal **takes up momentum**, rather than making it disappear.

The metal recoils, so momentum conservation applies to the whole system:
\[
\vec p_\gamma=\vec p_e+\vec p_{\text{metal}}.
\]

Because the metal has a very large mass, it can carry momentum with very little recoil kinetic energy:
\[
K_{\text{metal}}\approx\frac{p_{\text{metal}}^2}{2M}.
\]

That gives the system a way to conserve momentum while leaving almost all the photon’s energy available for overcoming the work function and giving the electron kinetic energy.

The isolated electron had to take **all** the photon’s energy and momentum itself; those requirements were incompatible. In the metal, the electron and the rest of the metal can share them.

---

**Learner**

wait a second, in our frame where photon is moving but electron is stationary, can't the electron take up the entire photon's energy and momentum?

**Tutor**

It can’t take **both** while remaining an electron of the same rest mass.

In your frame, the electron starts at rest. Let the incoming photon have energy \(E_\gamma\), so its momentum is \(E_\gamma/c\).

If the electron absorbs it completely, conservation requires
\[
E_f=m_ec^2+E_\gamma,
\qquad
p_f=\frac{E_\gamma}{c}.
\]

But the final electron must also satisfy
\[
E_f^2=p_f^2c^2+m_e^2c^4.
\]

Substituting gives
\[
(m_ec^2+E_\gamma)^2=E_\gamma^2+m_e^2c^4.
\]
Expanding and cancelling leaves
\[
2m_ec^2E_\gamma=0,
\]
which is impossible for a real incoming photon with \(E_\gamma>0\).

So your proposed energy and momentum transfers **conserve the totals**, but produce a final energy–momentum combination that an electron cannot have. The electron can instead **scatter** the photon, leaving an outgoing photon to carry away some energy and momentum.

---

**Learner**

whats useful to take away, here, that a particle can't completely absorb a photon's energy and momentum at the same time. 

i need a more useful intuition into the fact that momentum gets taken up by the huge relatively metal

**Tutor**

The useful takeaway is narrower: **a free electron cannot completely absorb a photon and remain a lone electron.** Other particles or systems can absorb photons if their internal energy—and therefore rest mass—can change.

For the metal, think of **recoil when you throw a ball**. You and the ball acquire equal and opposite momenta, but the much heavier person gets very little kinetic energy. Momentum and kinetic energy don’t have to be shared in the same proportions.

The same principle applies here:
\[
K=\frac{p^2}{2M}.
\]
**A massive object can carry substantial momentum at very little energy cost.** It moves extremely slowly, but its large mass makes \(Mv\) significant.

When a photon ejects an electron, the electron interacts with the surrounding metal. The metal recoils with whatever momentum is needed to balance the total—even opposite to the electron if necessary—while taking very little energy.

That’s why we can usually use
\[
hf\approx W+K_e
\]
without a noticeable metal-recoil energy term, **yet still need the metal when accounting for momentum**.

---

**Learner**

Hmm. I'm thinking no, because... Well, I don't know. Didn't you just mention that with the same momentum, the thing with the higher mass will carry less energy? But where is it from? I don't really know.

**Tutor**

Yes—your instinct is right. I moved too quickly: **the photon and atom obey different energy–momentum relations.**

For the slowly recoiling atom,
\[
K_{\text{atom}}=\frac{p^2}{2M}.
\]
This comes from \(p=Mv\) and \(K=\tfrac12Mv^2\). At the same momentum, a larger mass means a smaller speed—and therefore less kinetic energy.

For the photon,
\[
E_\gamma=pc.
\]
We **cannot** use \(p^2/(2M)\) for a photon.

Since their momentum magnitudes are equal,
\[
\frac{K_{\text{atom}}}{E_\gamma}
=\frac{p^2/(2M)}{pc}
=\frac{p}{2Mc}
\approx\frac{v_{\text{atom}}}{2c}.
\]
The atom moves much slower than light, so it carries much less kinetic energy than the photon.

**Equal momentum does not imply equal energy.** The object’s mass and its energy–momentum relation determine the energy associated with that momentum.

---

**Learner**

this is messy. illustrate using a series of problems

**Tutor**

Let’s build it through one problem at a time.

**Generated — 1**

Two objects each have momentum \(6\,\mathrm{kg\,m/s}\):

- Object A has mass \(2\,\mathrm{kg}\).
- Object B has mass \(6\,\mathrm{kg}\).

Using \(p=mv\) and \(K=\tfrac12mv^2\), find each object’s kinetic energy.

---

**Learner**

K is equal to one half p squared over m.

**Tutor**

Correct:
\[
K=\frac{p^2}{2m}.
\]

For our two objects, \(p=6\,\mathrm{kg\,m/s}\) for each, while \(m_A=2\,\mathrm{kg}\) and \(m_B=6\,\mathrm{kg}\). What kinetic energy does each have?

---

**Learner**

Larger mass means lower kinetic energy.

**Tutor**

Correct—**at fixed momentum**, the larger mass has less kinetic energy. Here, \(K_A=9\,\mathrm J\) and \(K_B=3\,\mathrm J\).

**Generated — 2**

A small object and a heavy block start at rest, then push apart. Their momenta are equal and opposite. The block has **100 times** the object’s mass. Both move nonrelativistically.

What is the ratio \(K_{\text{block}}/K_{\text{object}}\)?

---

**Learner**

One over a hundred.

**Tutor**

Correct—the block carries the same momentum magnitude but only \(1/100\) of the kinetic energy.

---

**Learner**

P over 2mc.

**Tutor**

Correct—that’s the complete symbolic ratio. With these values, the atom’s recoil kinetic energy is about \(3.3\times10^{-11}\) of the photon’s energy.

---

**Learner**

-9p

**Tutor**

Correct—the metal takes momentum \(-9p_\gamma\), to the left, so the total remains \(p_\gamma\).

---

**Learner**

1/10^20

**Tutor**

Almost—you’ve included the mass ratio, but the momentum magnitudes are **different**: \(9p_\gamma\) and \(10p_\gamma\).

What extra factor belongs in your ratio?

---

**Learner**

skip, next

**Tutor**

I’ll mark that one as skipped and move on to Compton scattering.

---

**Learner**

i mean , i know whats going on with nonrelativisic ones, how about relativistic?

**Tutor**

For relativistic recoil, replace \(K=p^2/(2m)\) with
\[
\boxed{K=\sqrt{p^2c^2+m^2c^4}-mc^2}.
\]
This is the total energy from the energy–momentum invariant, minus rest energy. Momentum conservation works exactly as before.

Let’s practice that before continuing Compton scattering.

**Generated**

An electron has rest energy \(mc^2=0.511\,\mathrm{MeV}\) and momentum \(p=1.00\,\mathrm{MeV}/c\).

Write an expression for its **kinetic energy**. You can leave the square root unevaluated.
