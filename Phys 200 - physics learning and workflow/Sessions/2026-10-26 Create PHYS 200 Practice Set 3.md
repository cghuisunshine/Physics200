# Create PHYS 200 Practice Set 3

**Learner**

But it doesn’t have a sign error

**Tutor**

Your first line, \(B=E_{\text{sep}}-E_{\text{bound}}\), is correct.

But I read your final line as \(2\gamma\mu c^2-2mc^2\). Here:

- \(E_{\text{sep}}=2mc^2\): the **original constituents**, separated and at rest.
- \(E_{\text{bound}}=2\gamma\mu c^2\): the original bound system’s energy, equal to the daughters’ total energy by conservation.

So your definition gives
\[
B=2mc^2-2\gamma\mu c^2.
\]

The outgoing daughters are different particles from the original constituents; their energy isn’t \(E_{\text{sep}}\) in the binding-energy definition.

---

**Learner**

The separated system has higher energy

**Tutor**

Yes—the separated **original constituents** have higher energy than the bound system.

But the decay daughters aren’t those separated constituents: their rest masses are \(\mu\), not \(m\). Their total energy equals the bound system’s initial energy.

Thus:
\[
\underbrace{2mc^2}_{\text{separated original constituents}}
>
\underbrace{2\gamma(w)\mu c^2}_{\text{bound system's energy = decay products' energy}}.
\]

Your principle is correct; the two energy expressions were assigned to the opposite systems.

---

**Learner**

Yeah, it was a way bigger problem than just the sign there.

**Tutor**

You’re right—I misdiagnosed it as a sign error. The real issue was **which physical states the energies describe**: separating the original constituents and decaying into different particles are different processes.

Your binding-energy definition was correct. I should have identified that distinction immediately instead of telling you to reverse the subtraction.

---

**Learner**

Flag. Also b I can use the same chain of reasoning with a fixed?

**Tutor**

Yes—the algebraic approach in (b) is valid. Start from the corrected expression in (a); the condition for positive \(B\) reverses, so the final inequality will reverse too. I’ll flag the distinction between separating the original constituents and decaying into different particles.

---

**Learner**

B is not super intuitive to me. Is this algebra way the best way, or is there something I want to learn or need to learn here?

**Tutor**

**The algebra is a good way to solve (b).** The useful intuition is that **stronger binding leaves less energy available for the decay products**.

Keep \(m\) and \(\mu\) fixed:

- Greater binding energy means a lower initial bound-system energy.
- The daughters therefore receive less total energy.
- Their rest masses haven’t changed, so they have less kinetic energy and move more slowly.

That’s why positive binding gives an **upper bound on \(w\)**. At the boundary \(B=0\), the daughters use all the energy of the separated original constituents. Faster daughters would require more energy than that, contradicting positive binding.

You don’t need another method—use the algebra, and use “more binding → slower daughters” to check the direction of your inequality.

---

**Learner**

K=E excess-B?

**Tutor**

Yes—if by \(E_{\text{excess}}\) you mean the difference between the original constituents’ rest energy and the daughters’ rest energy:

\[
E_{\text{excess}}=2mc^2-2\mu c^2.
\]

Then the **combined kinetic energy of both daughters** is
\[
\boxed{K_{\text{total}}=E_{\text{excess}}-B.}
\]

So more energy tied up in binding means less available for their motion.

---

**Learner**

give me q1 original version'

**Tutor**

**Course — original HW6.2(4)**

A positronium atom at rest consists of an electron and a positron, each with rest mass \(m_e\). Its binding energy is approximately \(7\,\mathrm{eV}\), and \(m_ec^2\approx500\,\mathrm{keV}\).

Imagine a hypothetical particle, the **hypothon**, whose rest mass is \(60\%\) of the electron’s rest mass. The positronium atom decays into a hypothon and an anti-hypothon of the same mass.

**How fast are the two particles travelling after the decay?** Give your answer as a multiple of \(c\).

---

**Learner**

the only case where P max is when phtons are same direction opp of the m.

**Tutor**

Yes—**the daughter’s momentum is largest when both photons travel in the same direction, opposite the daughter.** They then provide the required recoil momentum using the least possible energy.

Since the daughter’s rest mass is fixed, maximum momentum also means maximum speed.

---

**Learner**

So I don’t need two equations? Just this one?

**Tutor**

Your energy equation alone,
\[
Mc^2=pc+\sqrt{m^2c^4+p^2c^2},
\]
determines **\(p\)**. To answer the requested **speed**, also state \(v=pc^2/E\).

Or write everything directly in terms of speed:
\[
\boxed{Mc^2=\gamma(v)mv\,c+\gamma(v)mc^2.}
\]
That single equation determines \(v_{\max}\), with \(\gamma(v)=1/\sqrt{1-v^2/c^2}\).

Momentum conservation is already built into it: the photons’ combined momentum magnitude equals the daughter’s.

---

**Learner**

How would you justify B?

**Tutor**

Let \(\beta=v/c\). Your geometry gives
\[
\cos\theta=\frac{a}{\sqrt{a^2+b^2}},
\]
so the wavelength is longer precisely when
\[
\boxed{\gamma(v)\left(1-\frac{v}{c}\frac{a}{\sqrt{a^2+b^2}}\right)>1.}
\]
That inequality is already a sufficient condition in terms of \(a,b,v\).

**Yes, it can happen:** when \(b\) is much larger than \(a\), the motion is almost transverse to the photon’s path. Then \(\cos\theta\) is small, and the wavelength ratio approaches \(\gamma>1\).

Physically, the approach tends to shorten the wavelength, while time dilation tends to lengthen it. For sufficiently transverse motion, the latter wins—even though the distance is decreasing.

---

**Learner**

What's the original question, or is this, uh, your adaptation?

**Tutor**

**Q6 is my adaptation**, which is why it’s labelled “Generated.” It isn’t a verbatim homework or exam question.

I based it on Helliwell §13.2’s angular Doppler discussion, especially the distinction between angles measured in the source and observer frames. I added the coordinates \((a,b)\), leftward source motion, and part (b) about possible redshift while approaching to test your retained angle-construction flag.

There isn’t a single original question behind this one.

---

**Learner**

Again, beta is always positive, and the angle is in its receiver's perspective between the velocity of the emitter and the light beam.

**Tutor**

Yes—**in this Doppler formula**, \(\beta=v/c\) is the source’s positive **speed**, and \(\theta\) is the angle between the source’s velocity and the photon’s travel direction, **both measured in the receiver’s frame at emission**.

That differs from the **signed** \(\beta\) used in Lorentz transformations.

---

**Learner**

I don't understand why this is an invalid application.

**Tutor**

The formula is valid. **The substitution \(M_{\text{system}}=m+2m=3m\) is what’s invalid.**

For the whole system, you must use its total energy, total momentum, and **system invariant mass** together:
\[
E_{\text{total}}^2=M_{\text{system}}^2c^4+p_{\text{total}}^2c^2.
\]

In the parent’s rest frame, energy and momentum conservation give
\[
E_{\text{total}}=5mc^2,\qquad p_{\text{total}}=0.
\]
Therefore the two-daughter **system** has invariant mass \(5m\).

The \(3m\) is only the **sum of the daughters’ individual rest masses**. Their combined energy also includes their kinetic energy. Zero **net** momentum means their momenta cancel; it doesn’t remove that kinetic energy.

Your equation mixed the system’s total energy with the sum of individual rest masses.

---

**Learner**

What is system invariant mouse? And how can I tell if it is or not?

**Tutor**

**System invariant mass** is the mass associated with the whole collection of particles. You find it from their **total energy and total vector momentum**, measured in one frame:

\[
M_{\text{system}}^2c^4
=E_{\text{total}}^2-c^2|\mathbf p_{\text{total}}|^2.
\]

“Invariant” means every inertial observer calculates the same value, even though they measure different energies and momenta.

In the frame where total momentum is zero,
\[
M_{\text{system}}=\frac{E_{\text{total}}}{c^2}.
\]
That total energy includes the particles’ **rest energies and their kinetic energies**. They can move in opposite directions while their momenta cancel.

To tell which mass belongs in the formula, ask **what your \(E\) and \(\mathbf p\) describe**:

- **One particle:** use that particle’s rest mass.
- **The whole collection:** use the system invariant mass—not automatically the sum of the particles’ rest masses.

For Q7, \(m\) and \(2m\) describe individual daughters. The whole isolated system retains invariant mass \(5m\) after the decay.

---

**Learner**

Feed this question to me again.

**Tutor**

**Generated — Q7(a)**

A particle of rest mass \(5m\) is at rest. It decays into daughter A of rest mass \(m\) and daughter B of rest mass \(2m\). In this frame, A moves along \(+x\) and B along \(-x\). No other particles are produced.

Find the **total energy and signed \(x\)-momentum of each daughter** in this frame.

A correct symbolic expression or sufficient equations determining the quantities is a complete answer.

---

**Learner**

How does one even fucking simplify this?

**Tutor**

The two-square-root equation is awkward. **You don’t need to simplify it for this set**, but there’s a cleaner way if you want explicit energies.

You already have
\[
E_A+E_B=5mc^2.
\]

Because the daughters have equal momentum magnitudes,
\[
E_A^2=m^2c^4+p^2c^2,\qquad
E_B^2=4m^2c^4+p^2c^2.
\]

Subtracting cancels the momentum terms:
\[
E_B^2-E_A^2=3m^2c^4.
\]

Factor the left side and use the known energy sum:
\[
(E_B-E_A)\underbrace{(E_B+E_A)}_{5mc^2}=3m^2c^4,
\]
so
\[
E_B-E_A=\frac35mc^2.
\]

Now you have **the sum and difference of the energies**—two linear equations, with no square roots left.

---

**Learner**

What was the original question that you generated this from?

**Tutor**

Q7 was primarily adapted from **your earlier mock’s Q6**, which read:

> A particle of rest mass \(10m\) moves at \(+0.60c\) along the laboratory \(x\)-axis. It decays into two particles, each of rest mass \(3m\). In the parent’s rest frame, daughter A moves along \(+x\) and daughter B along \(-x\). No other particles are produced.
>
> (a) Find each daughter’s energy and signed momentum in the parent’s rest frame.  
> (b) Find those quantities in the laboratory.  
> (c) Find each daughter’s signed laboratory velocity.

That mock question was itself generated from the **Week 6 kaon-decay example**, involving two identical daughters.

For Set 3, I changed the daughters to **unequal masses** and reversed the parent’s laboratory motion. **The unequal masses introduced the extra algebra you’re encountering**; that complication wasn’t in the original mock question.

---

**Learner**

A split energy in half, then use Eeach squared =  formula. To find momentum. 

For b, use ordinary Lorentz transformation. Inverse version. List this out

**Tutor**

**For the original mock Q6 with equal-mass daughters, yes:**

**(a) In the parent’s rest frame**

Split the parent’s energy equally:
\[
E_A^*=E_B^*=\frac{10mc^2}{2}=5mc^2.
\]

Apply the invariant to each daughter, whose rest mass is \(3m\):
\[
p^*=\frac{\sqrt{(5mc^2)^2-(3mc^2)^2}}{c}=4mc.
\]
Thus \(p_A^*=+4mc\) and \(p_B^*=-4mc\).

**(b) Transform from the parent’s rest frame to the lab**

The parent moves at \(V=+0.60c\) in the lab. Using the **inverse, plus-sign form**, with
\[
\Gamma=\frac1{\sqrt{1-V^2/c^2}},
\]
apply to **each daughter**:
\[
\boxed{E_{\rm lab}=\Gamma(E^*+Vp_x^*)},
\qquad
\boxed{p_{x,\rm lab}=\Gamma\left(p_x^*+\frac{VE^*}{c^2}\right)}.
\]

Use the same \(V\) and \(\Gamma\) for both daughters; their signed \(p_x^*\) values differ.

For **Set 3 Q7**, the transformation approach still works, but you cannot split the energy equally because the daughters have unequal rest masses.
