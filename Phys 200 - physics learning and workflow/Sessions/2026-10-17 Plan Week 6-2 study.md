# Plan Week 6-2 study

**Learner**

why not Q1?

**Tutor**

**Q1 covers the photoelectric effect, while Q2 covers Compton scattering—the first topic in 6-2.** I chose Q2 to follow the slide order; Q1 comes naturally when we reach the photoelectric-effect slides.

There’s no prerequisite reason to skip Q1. If we were working through the tutorial in order, we’d start there.

---

**Learner**

lets do Q2

**Tutor**

**Course — Tutorial 6, Q2(a)**

A photon with momentum magnitude \(p\) travels along \(+x\) toward an electron initially at rest. The electron’s rest mass is \(m\). For a photon, \(E=pc\).

For the **photon and electron together**, write:

- Initial total energy.
- Initial total \(x\)-momentum.
- Initial total \(y\)-momentum.

Express your answers in terms of \(p,m,c\).

---

**Learner**

Maybe we should review a little bit on the cosine law.

**Tutor**

The **cosine law** relates three sides of a triangle to one angle:

\[
\boxed{c^2=a^2+b^2-2ab\cos\theta}
\]

Here, \(\theta\) is the angle **between sides \(a\) and \(b\)**, and \(c\) is the side **opposite that angle**. (Here \(c\) is just a side label, not the speed of light.)

At \(\theta=90^\circ\), \(\cos\theta=0\), so it becomes the Pythagorean theorem.

**Generated**

Two sides of a triangle have lengths \(5\) and \(8\), with a \(60^\circ\) angle between them. What is the length of the opposite side?

---

**Learner**

am i uspposed to know any of these by heart, or something else

**Tutor**

**Know the basic relationships; derive the expressions for this particular collision.**

The core relationships to be comfortable recalling are:

- Photon energy: \(E=pc\).
- Massive-particle energy: \(E^2=p^2c^2+m^2c^4\).
- Components: \(p_x=p\cos\theta,\ p_y=p\sin\theta\).
- Energy and momentum conservation.

You **don’t need to memorize** the electron momentum expression you just built—it follows from those basics.

For the current question, combine the two particles’ energies using those relationships. The electron is now moving, so its energy is no longer just \(mc^2\).

---

**Learner**

i got back from food, with blank paper, gimme what i need and give f again

**Tutor**

A photon initially has momentum \(p\) along \(+x\). It hits an electron of rest mass \(m\), initially stationary. The photon leaves with momentum \(p'\) at angle \(\theta\) above \(+x\).

Your results so far:
\[
E_{\text{initial}}=pc+mc^2
\]
\[
p_e^2=(p-p'\cos\theta)^2+p'^2\sin^2\theta
\]
\[
E_{\text{final}}=p'c+\sqrt{m^2c^4+c^2\left[(p-p'\cos\theta)^2+p'^2\sin^2\theta\right]}.
\]

**Course — Q2(f)**

Set \(E_{\text{initial}}=E_{\text{final}}\), then **solve for \(p'\) in terms of \(p,m,\theta,c\)**.

---

**Learner**

this is so messy

**Tutor**

Yes—the unexpanded momentum expression makes it look worse than it is.

First simplify just
\[
(p-p'\cos\theta)^2+p'^2\sin^2\theta.
\]

**Expand the square and combine terms using \(\cos^2\theta+\sin^2\theta=1\).** Leave the energy equation aside for this step.

---

**Learner**

write out the short derivation

**Tutor**

Start with conservation of momentum:
\[
p_e^2=p^2+p'^2-2pp'\cos\theta.
\]

Energy conservation gives
\[
pc+mc^2=p'c+\sqrt{m^2c^4+p_e^2c^2}.
\]
Isolate the root, divide by \(c\), then square:
\[
[p-p'+mc]^2=m^2c^2+p^2+p'^2-2pp'\cos\theta.
\]

Expand and cancel \(m^2c^2,p^2,p'^2\):
\[
-2pp'+2mc(p-p')=-2pp'\cos\theta,
\]
so
\[
mc(p-p')=pp'(1-\cos\theta).
\]

**For the scattered momentum**, collect \(p'\):
\[
\boxed{p'=\frac{mcp}{mc+p(1-\cos\theta)}}.
\]

**For the wavelength shift**, divide the same equation by \(mcpp'\) and multiply by \(h\):
\[
\frac{h}{p'}-\frac{h}{p}=\frac{h}{mc}(1-\cos\theta).
\]
Since \(\lambda=h/p\),
\[
\boxed{\lambda'-\lambda=\frac{h}{mc}(1-\cos\theta)}.
\]

---

**Learner**

I’m not with pen paper rn but tell me about the wavelength shift

**Tutor**

The **wavelength shift** tells you how much the photon’s wavelength increases after it scatters off an initially stationary, free electron:

\[
\boxed{\lambda'-\lambda=\frac{h}{m_ec}(1-\cos\theta)}
\]

The photon transfers some energy to the electron. Since photon energy is \(E=hc/\lambda\), **losing energy means a longer wavelength**.

The scattering angle determines how much it changes:

- **\(0^\circ\):** straight ahead → no wavelength shift.
- **\(90^\circ\):** sideways → shift of \(h/(m_ec)\).
- **\(180^\circ\):** directly backward → maximum shift, \(2h/(m_ec)\).

An interesting feature: **the absolute shift depends only on the angle and the target’s mass, not the incoming wavelength.** The same shift is therefore a much bigger percentage change for a short-wavelength photon.

Quick mental check: if the photon leaves with a longer wavelength, what happens to the electron’s kinetic energy?

---

**Learner**

How was it derived from my last line?

**Tutor**

Your last line, after cancelling the 2s, was
\[
p'=\frac{mcp}{mc+p(1-\cos\theta)}.
\]

**Take the reciprocal:**
\[
\frac1{p'}=\frac{mc+p(1-\cos\theta)}{mcp}
=\frac1p+\frac{1-\cos\theta}{mc}.
\]

Subtract \(1/p\), then multiply by \(h\):
\[
\frac h{p'}-\frac hp=\frac h{mc}(1-\cos\theta).
\]

Since photon wavelength is \(\lambda=h/p\), the left side is simply \(\lambda'-\lambda\):
\[
\boxed{\lambda'-\lambda=\frac h{mc}(1-\cos\theta)}.
\]

---

**Learner**

This is the thing to know for exams

**Tutor**

**Yes—the Compton wavelength-shift formula is the main result to know and apply:**
\[
\boxed{\lambda'-\lambda=\frac{h}{m_ec}(1-\cos\theta)}.
\]

Know that \(\theta\) is the **photon’s deflection angle**, and that a longer wavelength means the photon lost energy to the electron.

Whether you must **memorize it or reproduce its derivation** still depends on the exam instructions; we haven’t verified that.

---

**Learner**

This is from the stationary electron being hit?

**Tutor**

Yes—an **initially stationary, free electron** is struck by a photon.

Afterward, the photon scatters through angle \(\theta\), and the electron recoils. The formula gives the photon’s wavelength change **in the frame where the electron was initially at rest**.

---

**Learner**

Ok, next

**Tutor**

I’ll mark that example as skipped after the angle correction and move on.

---

**Learner**

These are just applications of this formula? What’s next

**Tutor**

Yes—(h) and (i) are direct substitutions into the wavelength-shift formula.

Next, **(j) asks why visible light scattering from electrons bound in a metal might produce an even smaller shift** than the free-electron prediction. There’s also an optional question about whether a free electron can absorb a photon completely.

After that, we return to 6-2: **photons and electromagnetic waves, then the photoelectric effect**. The slides’ four-vector Compton derivation is marked not tested.

---

**Learner**

Metals have delocalized electrons already?

**Tutor**

Yes—metals have **delocalized conduction electrons**. But “delocalized” doesn’t mean they behave as isolated free electrons; they still interact with the metal.

If the recoil is shared with the surrounding material, the **effective recoiling mass is much larger** than \(m_e\). Looking at the mass in the denominator of the wavelength-shift formula, what would that do to the shift?

---

**Learner**

What is recoil

**Tutor**

**Recoil is the motion an object gains when momentum is transferred to it.**

Here, the photon hits the electron and changes momentum. The electron picks up momentum and starts moving—that’s its recoil.

It doesn’t necessarily mean moving backward; the direction follows from momentum conservation.

---

**Learner**

Give the wavelength shift formula agin

**Tutor**

\[
\boxed{\Delta\lambda=\lambda'-\lambda=\frac{h}{m_ec}(1-\cos\theta)}
\]

For an **initially stationary, free electron**, with \(\theta\) the photon’s scattering angle.

---

**Learner**

Ah, in short metals have their electrons delocalized (conjugated system?) the light is interacting with more of the metal

**Tutor**

Yes—**“the recoil can involve more of the material”** is the useful idea.

Metals have delocalized conduction electrons, but *conjugated system* usually refers to connected molecular \(p\)-orbitals, so it isn’t the term to use here.

For this explanation: **if the surrounding material shares the recoil, the effective recoiling mass is larger, so the photon loses less energy and its wavelength shift is smaller.** Delocalization alone doesn’t guarantee that.

---

**Learner**

How are metals uniquely more surrounding material share recoil

**Tutor**

**They aren’t unique in that respect.** Atoms, molecules, and nonmetal solids can also recoil collectively when light scatters elastically from them.

The distinction is **an isolated free electron versus an electron interacting with a larger bound system**. In some scattering processes, that larger system takes the momentum while remaining internally unchanged. Its larger mass means less recoil energy and therefore a smaller wavelength shift.

So your question exposes a weakness in my earlier explanation: **metallic delocalization isn’t the reason by itself.** The tutorial’s metal sheet is an example of material where the free-electron assumption may fail.

---

**Learner**

In what other scenarios do the free electrons assumption also fail

**Tutor**

The free-electron assumption can fail whenever the electron’s interactions with its surroundings matter during the collision—for example:

- **Electrons bound in atoms:** the photon may make the whole atom recoil, excite it, or eject an electron.
- **Electrons in molecules:** energy can also go into molecular rotation, vibration, or electronic excitation.
- **Electrons in solids, including insulators:** momentum and energy can involve the lattice or other electrons.

**These don’t all produce a smaller wavelength shift.** The smaller-shift explanation specifically applies when a heavier bound system takes the recoil without internal excitation.

Also, even a free electron may already be moving; then our **initially stationary-electron** formula no longer applies directly.

---

**Learner**

But the course doesn’t teach us how to distinguish this? What’s the takeaway from j?

**Tutor**

**The takeaway from (j) is simply that the free-electron model has limits.** You’re not being asked here to classify all possible scattering processes—I took the explanation too far.

An exam-ready answer is:

> Electrons in the metal are not isolated free particles. If the surrounding material shares the recoil, the effective recoiling mass is larger, giving a smaller wavelength shift than the free-electron prediction.

You don’t need the delocalization or conjugation argument. For ordinary Compton calculations, use the stated assumption of an initially stationary, free electron.
