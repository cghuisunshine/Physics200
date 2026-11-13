# Check four-vector course alignment

**Learner**

having trouble

**Tutor**

Start by writing the **total energy and momentum before the collision**, in the frame where the car is initially at rest.

For each object,
\[
E=\gamma mc^2,\qquad p_x=\gamma m u_x,
\]
where \(m\) is its rest mass, \(u_x\) its velocity, and \(\gamma=1/\sqrt{1-u^2/c^2}\).

The stationary car has **zero momentum but still has rest energy**.

What do you get for the combined initial energy and momentum? You can leave the masses in grams and keep \(c\) symbolic.

---

**Learner**

spacetime diagrams aren't super useful in relativisic mass and energy?

**Tutor**

Right—**spacetime diagrams are usually less useful for mass-and-energy problems.** They show *where and when* events happen, so they’re especially helpful for simultaneity, elapsed times, lengths, and frame changes.

For collisions, a diagram can show trajectories meeting, but it doesn’t directly show the particles’ energies or rest masses. A **before-and-after sketch with masses and velocity arrows**, followed by energy and momentum conservation, is usually more useful.

Your two equations are exactly the useful setup for this problem.

---

**Learner**

calculate the first equation, Find big gamma using u2 and C squared to isolate for big M 2.

**Tutor**

Yes—that completes it:
\[
u_2=\frac{(5/3)(5)(0.8c)}{(5/3)(5)+50}
=\frac{4}{35}c.
\]
Then
\[
\Gamma=\frac{1}{\sqrt{1-u_2^2/c^2}}\approx1.00660,
\qquad
M_2=\frac{\gamma m+M}{\Gamma}\approx57.95\ \text{g}.
\]

The \(c^2\) cancels from both sides of the energy equation. The final rest mass exceeds \(55\text{ g}\) because some initial kinetic energy becomes internal energy of the combined object.

---

**Learner**

MeV is mega eV?

**Tutor**

Yes—**MeV means mega-electronvolt**:
\[
1\ \mathrm{MeV}=10^6\ \mathrm{eV}.
\]

It’s a unit of **energy**; \(\mathrm{MeV}/c^2\) is a unit of **mass**. So a mass of \(1777\ \mathrm{MeV}/c^2\) corresponds to a rest energy of \(1777\ \mathrm{MeV}\).

---

**Learner**

No, I thought there was a simpler derivation that we did before.

**Tutor**

Yes—the **four-momentum invariant, evaluated in the rest frame**. I took the longer route.

Using your course’s sign convention,
\[
-\left(\frac{E}{c}\right)^2+p^2
\]
has the same value in every frame.

In the particle’s rest frame, \(p=0\) and \(E=mc^2\), so that value is \(-m^2c^2\). Therefore,
\[
-\frac{E^2}{c^2}+p^2=-m^2c^2
\quad\Longrightarrow\quad
\boxed{E^2=p^2c^2+m^2c^4}.
\]

---

**Learner**

this is always true for something moving in 1 dimension?

**Tutor**

Yes—and **it also holds in two or three dimensions**:
\[
E^2=p^2c^2+m^2c^4,
\qquad p^2=p_x^2+p_y^2+p_z^2.
\]

In one dimension, only one momentum component is nonzero, so \(p^2=p_x^2\).

Here \(E\) is **total energy**, \(m\) is **rest mass**, and energy and momentum must be measured in the **same frame**.

---

**Learner**

Wait, isn't my equation correct? Because total energy before is equal to total energy after.

**Tutor**

**Energy before equals energy after—yes.** The issue is that the given \(4000\ \mathrm{MeV}\) belongs **only to the tau**, not to both particles together.

Since \(X\) starts at rest,
\[
m_Xc^2=E_{\text{tau}}+E_{\text{antineutrino}}
=4000\ \mathrm{MeV}+E_{\text{antineutrino}}.
\]

Your conservation principle is right; the right-hand side was missing one particle’s energy.

---

**Learner**

Does the anti-neutrino have any energy? Because it has no mass? I mean, what is it?

**Tutor**

Yes—**a massless particle can carry energy and momentum.** Zero mass means zero **rest energy**, not zero total energy:
\[
E^2=p^2c^2+m^2c^4
\quad\xrightarrow{m=0}\quad E=pc.
\]
Light is another example.

An **antineutrino** is an electrically neutral elementary particle, the antiparticle of a neutrino. It interacts extremely weakly with matter, which makes it difficult to detect. **This problem treats it as massless.**

Here, \(X\) initially has zero momentum. After it decays, the tau and antineutrino must have **equal and opposite momenta**. That gives you a way to determine the antineutrino’s energy from the tau’s motion.

---

**Learner**

Conservation of momentum makes it so that their momentums are opposite in magnitude, equal in magnitude, opposite in direction.

**Tutor**

Exactly. Equal momentum magnitudes give equal photon energies because \(E=pc\). I’ll record this as correct.

---

**Learner**

wait how are protons and electrons connected with hydrogen

**Tutor**

An ordinary **hydrogen atom has one proton and one electron**. Its nucleus is just the proton.

Inside the Sun, hydrogen is **ionized**: the electrons are separated from the nuclei. So counting hydrogen nuclei means counting protons.

In this reaction, **four protons are consumed for each helium nucleus formed**. That means four hydrogen nuclei are used—not two. The “two electrons” describes the **net reaction**, not the number of hydrogen atoms.

---

**Learner**

what bappened to those 2 electrons

**Tutor**

Of the four electrons originally associated with four hydrogen atoms, **two are consumed in the net reaction**. During fusion, two protons become neutrons and emit positrons; those positrons annihilate with two electrons, releasing energy.

The **other two electrons remain in the Sun’s plasma**. If the helium nucleus later formed a neutral atom, it would need those two electrons.

---

**Learner**

too rusty to try this, give a few ramp up questions

**Tutor**

We’ll build up to it, one question at a time.

**Generated**

In the lab, a photon has energy \(6\ \mathrm{MeV}\) and travels in the **negative \(x\)-direction**.

For a photon, \(E=pc\), where \(p\) is momentum **magnitude**.

**What is its signed momentum component \(p_x\), in \(\mathrm{MeV}/c\)?**

---

**Learner**

hey, the part between lorentz transforms and end of relativity feels underlearned

**Tutor**

Yes—that matches what today’s work shows. **We’ve moved through the later material faster than you’ve had time to learn it.** I treated several topics as practice-ready when you still needed teaching.

You’ve shown some solid pieces: setting up conservation equations, using zero total momentum, and applying the energy–momentum relation in simpler problems. But connecting those pieces still often needs prompting. Four-momentum transformations, decays, and mass–energy applications remain uneven.

We should switch from mixed practice to a **problem-led learning sequence**:

1. Relativistic momentum; total, rest, and kinetic energy.
2. The energy–momentum relation, including photons.
3. Collisions and decays within one frame.
4. Four-momentum and changing frames.
5. Binding energy, centre-of-momentum frames, thresholds, Doppler, and Compton scattering.

For each, I’ll introduce only what the next problem needs, give a few varied attempts, and check it again later without prompts. Guided completion won’t count as independent understanding.

**Let’s pause the photon-transform question and rebuild from energy and momentum.** We can move quickly through anything you demonstrate securely.

---

**Learner**

mu right

**Tutor**

\(mu\) is the **low-speed limit**, yes. The relativistic expression is
\[
p=\gamma mu,\qquad \gamma=\frac{1}{\sqrt{1-u^2/c^2}}.
\]
When \(u\ll c\), \(\gamma\approx1\), so \(p\approx mu\).

For a particle moving at \(u=0.6c\), what is its momentum in terms of \(m\) and \(c\)?

---

**Learner**

next

**Tutor**

We’ll skip that calculation and move to the next slide topic: energy.

---

**Learner**

2mc

**Tutor**

The factor \(2\) is right—just missing the square on \(c\): **\(K=2mc^2\)**. Energy has units of \(mc^2\); \(mc\) has units of momentum.
