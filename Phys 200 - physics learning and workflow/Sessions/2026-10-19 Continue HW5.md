# Continue HW5

**Learner**

ok but dont we use beta as new frame's velocity relative to the old?

**Tutor**

Yes—**when applying a Lorentz transformation**, \(\beta\) is the new frame’s velocity relative to the old frame, divided by \(c\).

Here, we’re **calculating momentum in the given frame**, so
\[
p_y=\gamma m v_y,\qquad
\gamma=\frac{1}{\sqrt{1-v^2/c^2}},
\]
where \(v\) is the **particle’s total speed in that frame**.

There’s no frame change here. Thus \(v_y=+0.2c\), and the momentum component is positive. The prime on your four-momentum isn’t needed.

---

**Learner**

didn't we do a particle frame to lab frame? or did we (should we) write the lab frame momentum straight away

**Tutor**

We wrote the **lab-frame momentum straight away**, using the particle’s given lab velocity:
\[
p_y=\gamma m v_y.
\]

You **could** instead transform from the particle’s rest frame to the lab. In that approach, the lab moves at \(-\mathbf v\) relative to the particle’s rest frame, so your negative frame velocity would be correct **inside the Lorentz transformation**. The transformation then gives positive lab momentum.

So your negative sign came from a valid alternative approach—you just mixed its **frame velocity** with the **particle velocity** in \(p_y=\gamma m v_y\).

---

**Learner**

yeah but its 3d, so we'd have to do some sort of twist and align shenanigans

**Tutor**

Exactly—if you wanted to use the familiar **\(x\)-only boost matrix**, you’d first align an axis with the particle’s velocity, boost, then rotate back. A general 3D boost can do this directly.

Here, writing \(\mathbf p=\gamma m\mathbf v\) immediately gives all three lab-frame components, so no rotations are needed.

---

**Learner**

this is just 0 eh?

**Tutor**

Yes—\(E=pc\), so the mass is zero. I’ll mark it solved and pull up the next question.

---

**Learner**

Oh, it does not conserve momentum because there's no item that is moving after the ship. There's no mass behind the ship

**Tutor**

Right—the initial momentum is zero, but afterward the ship has nonzero momentum with nothing carrying opposite momentum. That could be expelled matter or light; it doesn’t have to have rest mass.

---

**Learner**

Give this question as a standalone question.

**Tutor**

**Course**

A spaceship carrying fuel and a large bullet is initially at rest in an inertial frame, with no external forces acting on the system.

An onboard device converts all the fuel’s rest energy into kinetic energy of the ship and bullet. The bullet is ejected, and the ship recoils in the opposite direction.

In the original inertial frame, what is the ratio of their final momentum magnitudes?
\[
\frac{|\mathbf p_{\text{ship}}|}{|\mathbf p_{\text{bullet}}|}
\]

---

**Learner**

1?

**Tutor**

Correct—the total momentum starts at zero, so the ship and bullet must have equal and opposite momenta. I’ll mark this part solved.

---

**Learner**

why the generated Q?

**Tutor**

It’s the **same HW5 scenario and numbers**, but I changed the original multiple-choice question into “find the speeds or set up the equations.” Your practice guidelines require altered questions to be labelled “Generated.”

I should have preserved the original format while we’re reviewing HW5. I’ll do that going forward.

---

**Learner**

so i DID have to calculate it out. 

ok. give the adapted one, let me calculate it out

**Tutor**

You did need to identify numerical speeds; checking the options was one way. Let’s finish the calculation directly.

**Generated — adapted from HW5**

A spaceship of rest mass \(10^6\,\mathrm{kg}\) carries a bullet of rest mass \(10^5\,\mathrm{kg}\) and \(5000\,\mathrm{kg}\) of fuel. Everything is initially at rest.

A device converts all the fuel’s rest energy into kinetic energy of the ship and bullet, which move in opposite directions. No energy escapes, and their rest masses remain unchanged.

**Calculate the final speed of each, as a fraction of \(c\), in the original rest frame.**

---

**Learner**

Ok but is this the easiest way?

**Tutor**

**For calculating the speeds from scratch, yes—this is one of the cleanest methods.** It avoids solving coupled equations with velocity-dependent square roots. For the original multiple-choice question, testing the options is easier.

You can shorten the arithmetic by using **tonnes**: \(M=1000\), \(m_b=100\), \(T=1105\). Your existing result then gives
\[
\gamma_s=\frac{T^2+M^2-m_b^2}{2TM}
=\frac{1105^2+1000^2-100^2}{2(1105)(1000)}.
\]
Then \(v_s/c=\sqrt{1-\gamma_s^{-2}}\).

For the bullet, use your energy-conservation equation:
\[
\gamma_b=\frac{T-\gamma_sM}{m_b},
\]
then the same speed relation. **No second derivation is needed.**

---

**Learner**

ok you gotta start giving standalone questions. i throw away my answer the moment i finish it

**Tutor**

Understood—I’ll include all needed information in each question.

**Course**

A parent particle of rest mass \(400\,\mathrm{MeV}/c^2\) moves at \(+0.7c\) along the lab’s \(x\)-axis. It decays into two particles, each of rest mass \(175\,\mathrm{MeV}/c^2\).

In the **parent’s rest frame**, their energies and momenta are:

| Particle | Total energy | \(x\)-momentum |
|---|---:|---:|
| Daughter 1 | \(200\,\mathrm{MeV}\) | \(+96.8246\,\mathrm{MeV}/c\) |
| Daughter 2 | \(200\,\mathrm{MeV}\) | \(-96.8246\,\mathrm{MeV}/c\) |

Both have zero \(y\)- and \(z\)-momentum. The two frames’ axes are aligned.

Find the **total energy and signed \(x\)-momentum of each daughter in the lab frame**.

---

**Learner**

actually, give the whole questio for me

**Tutor**

**Course — HW5.8: Imaginum decay**

The exotic particle Imaginum has rest mass \(m_I=400\,\mathrm{MeV}/c^2\). It decays into two identical particles, each with rest mass \(m_d=175\,\mathrm{MeV}/c^2\).

In the lab, an Imaginum particle is produced moving in the \(+x\) direction with speed \(v=0.7c\).

Use units of **MeV for energy** and **MeV/\(c\) for momentum**. For momentum, give the \(x\)-component \(p_x\), which may be negative.

For Question 2, assume the decay is collinear in the Imaginum center-of-momentum frame: one decay product is emitted along \(+x\), and the other along \(-x\).

**1. Center-of-momentum frame**

Find \(E\) and \(p_x\) for:

- The Imaginum particle.
- Decay product 1.
- Decay product 2.

**2. Lab frame**

Find \(E\) and \(p_x\) for:

- The Imaginum particle.
- Decay product 1.
- Decay product 2.

---

**Learner**

beta =-0.7c, eh?

**Tutor**

Yes—the **lab moves at \(-0.7c\) relative to the parent’s rest frame**, so for that transformation:
\[
\boxed{\beta=-0.7}
\]
No \(c\) on \(\beta\): it’s dimensionless, since \(\beta=v/c\).

---

**Learner**

ok, i'll do full attempt later, next

**Tutor**

I’ll save the full lab-frame calculation for your later retry and get the next homework question.

---

**Learner**

So Higgs boson would have 157.5 giga electron volts over c squared, which is plenty of room for the other two protons, right?

**Tutor**

The Higgs would have **total energy \(157.5\,\mathrm{GeV}\)**—without the \(c^2\) denominator—leaving \(21.5\,\mathrm{GeV}\) for the two protons.

But comparing that with their rest energies isn’t enough: **the protons must also balance the Higgs’s momentum**.

Can they do that with the remaining energy?

---

**Learner**

i mean from start to finish, this Q

**Tutor**

The shortest complete solution is:

The Higgs has \(\gamma=1.25\), so
\[
E_H=(1.25)(126)=157.5\,\mathrm{GeV},
\qquad
p_Hc=(157.5)(0.6)=94.5\,\mathrm{GeV}.
\]

Energy conservation leaves the two protons
\[
E_{\text{protons}}=179-157.5=21.5\,\mathrm{GeV}.
\]

Momentum conservation requires their combined momentum to have magnitude \(94.5\,\mathrm{GeV}/c\). But **\(E_{\text{protons}}\ge|\mathbf p_{\text{protons}}|c\)**, which would require
\[
21.5\ge94.5.
\]

This is false, so **the Higgs cannot be emitted at \(0.6c\)**.

---

**Learner**

pc equals E for massless particles, but pc equals beta E for massive particles? Feels counterintuitive.

**Tutor**

They’re consistent: **\(\beta=v/c=1\) for a massless particle**, so \(pc=\beta E\) becomes \(pc=E\).

For a massive particle, some total energy is **rest energy**, so total energy exceeds \(pc\):
\[
E^2=(pc)^2+(mc^2)^2.
\]

A useful extreme: a massive particle **at rest** has momentum zero but energy \(mc^2\). As it moves closer to \(c\), \(pc/E=\beta\) approaches 1.

The relation \(pc=\beta E\) works for both; the formulas involving \(\gamma m\) can only be used for massive particles.

---

**Learner**

All them getting momentum from energy for a massive particle is really simple then.

**Tutor**

Yes—**if you know its speed**:
\[
p=\frac{\beta E}{c}.
\]

If you know its **rest mass and total energy** instead:
\[
p=\frac{\sqrt{E^2-m^2c^4}}{c}.
\]

Here \(E\) means **total energy**, not just kinetic energy.

---

**Learner**

move on then

**Tutor**

**Course — HW5.10(3)**

An unstable particle of rest mass \(179\,\mathrm{GeV}/c^2\), initially at rest, decays into two identical particles, each of rest mass \(78\,\mathrm{GeV}/c^2\).

How fast does each daughter move in this frame? Give \(\beta=v/c\) to **two decimal places**.

---

**Learner**

need help for 2

**Tutor**

The **meson’s rest frame** is the frame where the meson produced by the collision is stationary. The incoming electron and positron are still moving in that frame.

Because the final momentum is zero, conservation requires
\[
\mathbf p_{e^-}+\mathbf p_{e^+}=0.
\]
Their momentum **magnitudes are equal**. Treating their masses as negligible, \(E=|p|c\), so their energies are equal too.

Their combined energy becomes the meson’s rest energy, \(10.58\,\mathrm{GeV}\). **How much energy does each incoming particle therefore have?**

---

**Learner**

its now tuesday. lets keep on going.

**Tutor**

Let’s resume **HW5.11**, where you stopped. Here’s the whole question so you have all the information together.

**Course**

An electron and positron collide head-on to produce a single \(\Upsilon(4S)\) meson of rest mass \(10.58\,\mathrm{GeV}/c^2\). The electron’s **lab-frame energy is \(9\,\mathrm{GeV}\)**. Treat the electron and positron masses as negligible.

1. Find the meson’s invariant \(I=E^2-(pc)^2\). **Completed:** \(111.9364\,\mathrm{GeV}^2\).
2. In the **meson’s rest frame**, find the energies of the incoming electron and positron.
3. Find the positron’s energy in the **lab frame**.
4. Find the meson’s **total energy, momentum magnitude, and speed \(v/c\)** in the lab frame.

**Start with part 2:** what energy does each incoming particle have in the meson’s rest frame?

---

**Learner**

aren't energies from massless things invariant?

**Tutor**

No—**a massless particle’s energy depends on the reference frame**, just like its momentum. For example, different observers measure different photon frequencies, hence different energies \(E=hf\).

What stays invariant is its **zero rest mass**:
\[
E^2-p^2c^2=0.
\]
Every observer finds \(E=|p|c\), but they needn’t agree on the values of \(E\) or \(p\).

So the electron’s energy can be \(5.29\,\mathrm{GeV}\) in the meson’s rest frame and \(9\,\mathrm{GeV}\) in the lab, even when we neglect its mass.

---

**Learner**

so they disagree on the color

**Tutor**

Yes—observers moving relative to each other can measure different **frequencies and wavelengths** for the same light, so they can assign it different colours. That’s the **relativistic Doppler effect**.

An observer moving toward the light source measures a blueshift; one moving away measures a redshift. Both still measure the light’s speed as \(c\).

---

**Learner**

For these massless particles, the first two entries would be the same quantity if they were moving along the x-axis, right?

**Tutor**

Yes—**equal in magnitude**, since four-momentum is
\[
P^\mu=(E/c,\;p_x,\;p_y,\;p_z).
\]

For a massless particle moving entirely along \(x\):
\[
+x:\quad (E/c,\;E/c,\;0,\;0),
\]
\[
-x:\quad (E/c,\;-E/c,\;0,\;0).
\]

The energy entry stays positive; the momentum entry carries the direction.

---

**Learner**

8.986?

**Tutor**

If you mean the **positron’s lab energy**, \(8.986\,\mathrm{GeV}\) isn’t correct. Can you show your setup so I can identify where it went off?

---

**Learner**

So in our lab frame, the energy of the electron increases by a factor of 1.7, which is gamma. And you multiply 1.58 by 1.7. You minus 9, you get 8.986.

**Tutor**

The error is identifying **\(9/5.29\approx1.7\) as \(\gamma\)**. A particle’s energy transforms as
\[
E_{\rm lab}=\gamma(E'-\beta cp_x'),
\]
so its change includes **both energy and momentum**. The electron’s factor of \(1.7\) isn’t the frame’s Lorentz factor. The oppositely moving positron gets a different factor.

Your final subtraction would work if you had the correct meson lab energy, but multiplying its rest energy \(10.58\,\mathrm{GeV}\) by \(1.7\) doesn’t give that.

Try using the **whole system’s invariant** instead: calling the unknown positron lab energy \(x\), what are the total lab energy and total signed momentum? Take the electron’s direction as \(+x\).

---

**Learner**

i thought we had four vector where everything is simply multiplied by gamma?

**Tutor**

**A four-vector transforms by a matrix, not by multiplying every entry by \(\gamma\).** For a boost along \(x\):
\[
\begin{pmatrix}E_{\rm new}/c\\p_{x,\rm new}\end{pmatrix}
=
\begin{pmatrix}
\gamma&-\beta\gamma\\
-\beta\gamma&\gamma
\end{pmatrix}
\begin{pmatrix}E_{\rm old}/c\\p_{x,\rm old}\end{pmatrix}.
\]
So **energy and \(x\)-momentum mix**.

You may be remembering a particle initially **at rest**, with four-momentum \((mc,0,0,0)\). Its zero initial momentum makes the energy transformation simplify to
\[
E_{\rm new}=\gamma mc^2.
\]

Here, the electron is already moving in the meson’s rest frame, so its momentum term is nonzero—you must include it.

---

**Learner**

im remembering something else where every single entry is multiplied by gamma

**Tutor**

You’re remembering the **four-momentum written in terms of a massive particle’s velocity**:
\[
P^\mu=\gamma m
\begin{pmatrix}
c\\v_x\\v_y\\v_z
\end{pmatrix}.
\]
Yes—every entry has the same \(\gamma\).

Here, \(\gamma\) comes from **the particle’s speed in the frame where you’re measuring it**. This formula constructs its four-momentum in that frame.

**Changing frames** is a separate operation: you apply the Lorentz matrix to that four-momentum, using the relative velocity **between the frames**.

For this question’s negligible-mass approximation, use \((E/c,\mathbf p)\), with \(E=|\mathbf p|c\), rather than \(\gamma m(c,\mathbf v)\).

---

**Learner**

need help with 3. holy fuck im bad

**Tutor**

You got part 2 right. The sticking point here is how to connect the two frames.

We can do part 3 **without finding a boost**. Let the unknown positron lab energy be \(x\), in GeV, and take the electron’s direction as positive.

Since we neglect their masses, \(pc=E\). The beams move oppositely, so:
\[
E_{\text{total}}=9+x,\qquad p_{\text{total}}c=9-x.
\]

They form one meson of rest energy \(10.58\,\mathrm{GeV}\), so:
\[
(9+x)^2-(9-x)^2=(10.58)^2.
\]

That’s the whole physics setup. **Try expanding the left side—what cancels?**

---

**Learner**

holy fuck im terrible at this. I need way more practise. i didn't know that this formula applies for TOTALS.

**Tutor**

That’s a specific gap we can practise. I hadn’t clearly explained that the invariant applies to a **whole system**.

For any collection of particles:
\[
E_{\text{tot}}=\sum_i E_i,\qquad
\mathbf p_{\text{tot}}=\sum_i\mathbf p_i,
\]
and
\[
E_{\text{tot}}^2-|\mathbf p_{\text{tot}}|^2c^2
=M_{\text{system}}^2c^4.
\]

**Add the energies and vector momenta first, then square.** The system mass includes internal motion; it isn’t generally the sum of the individual rest masses. Even two massless particles can have a nonzero system mass.

Here, the incoming pair and outgoing meson have the same total energy and momentum, so they have the same invariant.

Let’s practise just that idea before returning to the algebra:

**Generated:** Two photons each have energy \(3\,\mathrm{GeV}\), one moving along \(+x\), the other along \(-x\). What are their **total energy and total momentum**?

---

**Learner**

Q4 now

**Tutor**

**Course — HW5.11(4)**

An electron and positron collide head-on to produce a single meson of rest mass \(10.58\,\mathrm{GeV}/c^2\). Treat the incoming particles’ masses as negligible.

In the lab:
- The electron moves along \(+x\) with energy \(9\,\mathrm{GeV}\).
- The positron moves along \(-x\) with energy \(3.10934\,\mathrm{GeV}\) (the result from part 3).

Find the meson’s **total energy, momentum magnitude, and speed \(v/c\)** in the lab frame.

---

**Learner**

Well here, the momentum magnitude you get from summing the momentum of electron and positron. Total energy you can get from rest mass and the momentum we calculate. And rest total energy we know. We also know energy when it's moving, so we can find gamma and therefore speed pretty easily, right?

**Tutor**

Yes—that method works. **Add momentum with signs**, since the beams oppose:
\[
p_{\Upsilon,x}=\frac{9-3.10934}{c}\,\mathrm{GeV}.
\]

Then your route is valid:
\[
E_\Upsilon=\sqrt{(m_\Upsilon c^2)^2+(p_\Upsilon c)^2},
\qquad
\gamma=\frac{E_\Upsilon}{m_\Upsilon c^2},
\qquad
\beta=\sqrt{1-\gamma^{-2}}.
\]

You can also shorten it: energy conservation gives \(E_\Upsilon=9+3.10934\,\mathrm{GeV}\), then \(\beta=p_\Upsilon c/E_\Upsilon\).

---

**Learner**

Help me with question six.

**Tutor**

Choose \(+x\) along the **20 MeV photon**. In the original frame,
\[
E_{\text{tot}}=30\,\mathrm{MeV},\qquad
p_{x,\text{tot}}=+10\,\mathrm{MeV}/c.
\]

We want a new frame where the **total momentum is zero**. Apply the momentum Lorentz transformation to the total four-momentum:
\[
p'_{x,\text{tot}}
=\gamma\left(p_{x,\text{tot}}-\beta\frac{E_{\text{tot}}}{c}\right).
\]

Set \(p'_{x,\text{tot}}=0\). Since \(\gamma\neq0\), this becomes
\[
0=10-30\beta.
\]

**What does that give for \(\beta=V/c\)?**

---

**Learner**

Is there an easier way, or this is THE way?

**Tutor**

Yes—the shortcut is
\[
\boxed{\frac{V_{\rm CM}}c=\frac{|\mathbf p_{\rm tot}|c}{E_{\rm tot}}}.
\]

Here that gives
\[
\frac{V_{\rm CM}}c=\frac{10}{30}=\frac13,
\]
so the requested answer is **\(0.333\)**.

The Lorentz-transformation method explains *why* this shortcut works. It applies to the **whole system**, even though each photon individually travels at \(c\).

---

**Learner**

Ah, the Lorentz transformation applies to the whole system too. Okay. Question six is flagged, eh?

**Tutor**

Yes—**Q6 is still flagged for an independent retry**.

And exactly: add the particles’ four-momenta, then Lorentz-transform that total. It gives the same result as transforming each particle first and then adding.

---

**Learner**

Well, I use Lorentz transforms with E over c prime is equal to gamma times E over c minus beta momentum.

**Tutor**

Yes—**that’s a valid approach**:
\[
\frac{E'}c=\gamma\left(\frac Ec-\beta p_x\right).
\]

Taking \(+x\) along the 20 MeV photon, the COM frame moves at \(\beta=+1/3\), so
\[
E'=\frac{1}{\sqrt{1-(1/3)^2}}
\left[30-\frac13(10)\right]\mathrm{MeV}.
\]

In that frame the new particle is at rest, so **\(m=E'/c^2\)**. Your method works—check your substitution against this, especially the minus sign and the momentum term.

---

**Learner**

write the invariant formula in standard form

**Tutor**

\[
\boxed{E_{\text{tot}}^{\,2}=|\mathbf p_{\text{tot}}|^{2}c^{2}+M^{2}c^{4}}
\]

Here \(M\) is the **rest mass of the whole system**, not the sum of its particles’ rest masses.

---

**Learner**

i thought its -E/C squraed + p squared?

**Tutor**

Yes—that’s the course’s four-momentum convention:
\[
\boxed{-\left(\frac{E_{\rm tot}}c\right)^2+|\mathbf p_{\rm tot}|^2=-M^2c^2.}
\]

Multiplying by \(-c^2\) gives the equivalent form:
\[
E_{\rm tot}^2-|\mathbf p_{\rm tot}|^2c^2=M^2c^4.
\]

I should have used your course’s convention when you asked for the standard form.

---

**Learner**

mass of the same particle is invariant, but momentum isnt, i see

**Tutor**

Exactly. **Rest mass is invariant; energy and momentum depend on the frame.** They change together so that
\[
-\left(\frac Ec\right)^2+|\mathbf p|^2=-m^2c^2
\]
stays the same.

---

**Learner**

"mass" as it is given in questions is invariant

**Tutor**

Yes—in this course, **“mass” means rest mass**, which is invariant.

It doesn’t change between frames. The frame-dependent quantities are **energy and momentum**.

---

**Learner**

How is binding energy defined again? The energy it takes to put those two things together? Or is it the energy it releases by joining together? Something like that.

**Tutor**

**Binding energy is the energy required to separate a bound system into its free constituents**, with no leftover kinetic energy.

Equivalently, it’s the **energy released when those free constituents form the bound system**.

\[
\boxed{E_{\text{binding}}=
\left(\sum m_{\text{free constituents}}-M_{\text{bound system}}\right)c^2}
\]

The bound system has **less rest mass**. Forming it releases energy; pulling it apart requires that energy back.
