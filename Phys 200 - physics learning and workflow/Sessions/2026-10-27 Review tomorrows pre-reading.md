# Review tomorrows pre-reading

**Learner**

halves, i see

**Tutor**

Exactly—halves to **\(483\,\mathrm{nm}\)**.

Now, **why did this require quantum physics?**

Experiments show that the emitted spectrum has a peak, then drops toward zero at very short wavelengths. Classical physics instead predicted ever-increasing emission toward short wavelengths—even an infinite total emitted power. That failure is the **ultraviolet catastrophe**.

Planck’s key idea was that matter exchanges radiation energy in **discrete packets**:
\[
E_{\text{packet}}=hf.
\]
Higher-frequency radiation requires a bigger energy packet. At a fixed temperature, very large packets are difficult to supply, which suppresses high-frequency emission and removes the catastrophe.

This **doesn’t mean only certain colours are allowed**. Different frequencies are possible; the packet size depends on the frequency.

**Generated:** Radiation A has twice the frequency of radiation B. Which requires the larger energy packet, and by what factor?

---

**Learner**

still a little too much compression

**Tutor**

Let’s pause before Planck. I moved from the experimental result to the failure to the solution too quickly.

Imagine a hot object held at a **fixed temperature**. We collect its emitted light and separate it by wavelength, like using a prism.

We then ask: **how much power is emitted in each small wavelength range?**

The measured result looks like a hill:

- Little power at very short wavelengths.
- More power as we approach the peak.
- Less power again at wavelengths beyond the peak.

So the object emits a range of wavelengths, with **most of the power concentrated around some region**.

Physicists tried to predict that hill using classical physics. Their calculation worked reasonably well at long wavelengths. But toward shorter wavelengths, it predicted that the emitted power would keep rising without limit, instead of falling.

That is the **ultraviolet catastrophe**: a failed prediction. The actual hot object behaves normally; the classical calculation predicts an impossible amount of radiation.

For now, leave the explanation involving energy packets aside.

**In your own words, what was wrong with the classical prediction?**

---

**Learner**

So the classical prediction works well at long wavelengths. Does that mean it captures the true hill reasonably well and it predicts that this hill extends down to the extremely low and actually infinitely low wavelengths of light per hill? Or is it something else?

**Tutor**

It’s something else: **the classical prediction gets the long-wavelength tail right, but misses the peak and the drop on the short-wavelength side.**

Imagine starting at a very long wavelength and moving toward shorter wavelengths:

1. **At first, both the measurement and classical prediction rise.** They agree reasonably well here.
2. **The measured spectrum reaches a peak, then falls.**
3. **The classical prediction keeps rising.** It never turns over to form the hill.

So it isn’t a correctly shaped hill that simply extends too far. It’s a curve that keeps climbing where it should turn downward.

Also, arbitrarily short wavelengths are not themselves the problem. The measured blackbody spectrum extends toward shorter and shorter wavelengths, but the emitted power becomes vanishingly small there. **Classical physics predicts increasingly large power there instead.**

---

**Learner**

ok so classical physics predict a slope not a hill.

**Tutor**

Yes—**a curve that keeps rising toward shorter wavelengths, rather than turning over into a hill.** “Slope” captures that idea, though it isn’t a straight line.

Now take just the first piece of Planck’s idea: **energy is exchanged in packets of size \(hf\)**.

For light of a particular frequency \(f\), matter can emit or absorb one packet, two packets, three packets, and so on. Each packet carries energy \(hf\).

The packet size depends on frequency: **higher frequency means a larger packet**. Since \(f=c/\lambda\), shorter wavelengths require larger packets too.

**Generated:** Compared with red light, blue light has a higher frequency. Does emitting one packet of blue light require more energy or less energy?

---

**Learner**

require much more

**Tutor**

More energy, yes. How much more depends on the frequency ratio.

---

**Learner**

do i need to know why classical physics predicted a curve that keeps rising? high frequency packets are easier to produce.

**Tutor**

Correct—heating makes high-frequency packets easier to produce. For this first pass, a qualitative explanation of the classical failure is enough; we can leave the full derivation aside.

---

**Learner**

ok i got it, lets keep going

**Tutor**

You’ve already practised the assigned Compton material recently: a photon scatters from an electron, transferring some energy to it, so the scattered photon has a longer wavelength. We’ll move to **polarizers**.

Light is an electromagnetic wave. Its electric field oscillates **perpendicular to the direction the light travels**.

Imagine light travelling straight toward you. Its electric field could oscillate:

- Up and down: **vertically polarized**.
- Left and right: **horizontally polarized**.

Those directions describe the **electric field**, not the photon’s direction of travel.

An ideal **polarizer** has a *transmission axis*. It passes the electric-field component along that axis and blocks the perpendicular component. A vertical polarizer therefore passes vertically polarized light and blocks horizontally polarized light.

Light that passes through comes out polarized along the polarizer’s axis.

**Generated:** Vertically polarized light passes through a vertical polarizer, then reaches a horizontal polarizer. Does any light emerge from the second polarizer?

---

**Learner**

nope. seems straightforward. how come the magnetic field isn't affected by it at all?

**Tutor**

Correct—no light emerges.

**The magnetic field is affected too.** We describe polarization using the electric field because specifying its direction also fixes the magnetic field’s direction.

In a light wave, the electric field, magnetic field, and direction of travel are mutually perpendicular. Their magnitudes are linked:
\[
B=\frac{E}{c}.
\]

The polarizer’s material responds to the electric field through its charges. That interaction determines which polarization passes, but the transmitted light is still a complete electromagnetic wave—with **both** electric and magnetic fields.

So when the horizontal polarizer blocks your vertically polarized beam, **both fields of that transmitted beam vanish**. There isn’t a magnetic wave continuing through by itself.

**Generated:** A beam travels toward you, with its electric field oscillating vertically. Along which direction does its magnetic field oscillate?

---

**Learner**

i know, but the polarizer blocks the E, not the B correct?

**Tutor**

**Yes, if you mean how the polarizer interacts with the light:** in an ordinary polarizing filter, the electric field drives charges in the material, and that response blocks one polarization.

But “blocks \(E\), not \(B\)” would be misleading about the result. It blocks the **whole electromagnetic wave** of that polarization. The associated magnetic field is also absent from the transmitted light; it doesn’t need to be blocked separately.

---

**Learner**

the result is that both are lost, i know, but the action it self is blocking the E field. then.

**Tutor**

Yes—that’s the distinction you meant. **The material interacts primarily with the electric field through its charges**, and that interaction removes the corresponding electromagnetic wave. You already understood the consequence for \(B\).

Now suppose the incoming polarization is **at an angle** to the transmission axis. The polarizer passes the component along its axis:
\[
E_{\text{out}}=E_{\text{in}}\cos\theta.
\]
Here \(\theta\) is the angle between the **incoming electric-field direction and the polarizer’s axis**.

Since intensity is proportional to field amplitude squared,
\[
I_{\text{out}}=I_{\text{in}}\cos^2\theta.
\]
This is **Malus’s law**. The transmitted light is polarized along the polarizer’s axis.

**Generated:** Vertically polarized light of intensity \(I_0\) reaches an ideal polarizer whose axis is \(45^\circ\) from vertical. What intensity emerges?

---

**Learner**

Wait, what? Something tells me that it's zero. But also, it's got a component that agrees with the 45, right?

**Tutor**

Yes—your **component reasoning is right**. The zero result would apply if the photon arriving at the horizontal polarizer were still vertically polarized.

But after passing the first polarizer, its polarization is **\(45^\circ\)**. The second polarizer acts on that current state; the original vertical polarization no longer determines its transmission.

So the relevant comparison is:

\[
\text{incoming polarization: }45^\circ,
\qquad
\text{second axis: }90^\circ.
\]

**What angle separates those two directions?**

---

**Learner**

oh so you can twist light?

**Tutor**

**Yes—in the sense that the transmitted light can emerge with a different polarization direction.** Its direction of travel stays the same.

A polarizer passes the electric-field component along its axis. So vertically polarized light entering a \(45^\circ\) polarizer emerges polarized at \(45^\circ\), with reduced intensity.

That gives a surprising result:

- **Vertical → horizontal polarizer:** no light passes.
- **Vertical → \(45^\circ\) polarizer → horizontal polarizer:** some light passes!

The intermediate polarizer changes the polarization of the light it transmits, giving that light a component along the final horizontal axis.

Returning to our photon: after it passes the \(45^\circ\) polarizer, **what is its probability of passing the horizontal polarizer—\(45^\circ\) away?**

---

**Learner**

oh so its NOT zero

**Tutor**

Exactly—**it’s not zero**. After the first polarizer, the photon’s polarization is \(45^\circ\) from horizontal, so
\[
P(\text{passes horizontal}\mid\text{passed first})
=\cos^2 45^\circ=\frac12.
\]

That’s the key: **each polarizer acts on the polarization arriving at it**, which may have changed at the previous polarizer.

**Generated:** Starting with 1000 vertically polarized photons, roughly how many pass through **both** the \(45^\circ\) polarizer and then the horizontal polarizer?

---

**Learner**

ok lets keep going with the content

**Tutor**

Next is the **double-slit experiment with electrons**.

Imagine an electron source aimed at a barrier with two narrow slits. Behind the barrier is a screen that records where each electron lands.

Each electron makes **one localized dot** on the screen. But after many electrons arrive, the dots form alternating bands: many hits in some regions, very few in others. This is an **interference pattern**, like overlapping waves produce.

The surprising part: **the pattern still builds up when electrons are sent one at a time**, with only one electron in the apparatus at once. So it cannot require different electrons interacting with each other.

Quantum mechanics describes the electron before detection using a **wavefunction**. Contributions associated with the two slits interfere, determining where detection is likely. Each actual detection still produces a single dot.

**Generated:** Suppose we reduce the emission rate so electrons travel through the apparatus one at a time, without measuring which slit they pass through. After enough electrons arrive, would you expect the interference pattern to disappear or remain?

---

**Learner**

okay? trivial question though, you just said that it remains

**Tutor**

You’re right—that just asked you to repeat the sentence. I’ll use questions that require applying the idea.

The next important distinction is **superposition versus not knowing**.

“An electron went through one slit, but we don’t know which” treats the two possibilities like ordinary alternatives. We would add their **probabilities**.

Quantum mechanics instead combines the two **probability amplitudes**—the quantities whose squared magnitudes give probabilities. These amplitudes can reinforce or cancel each other:
\[
P(x)=|\psi_1(x)+\psi_2(x)|^2.
\]
Here \(\psi_1(x)\) and \(\psi_2(x)\) are the contributions from the two slits to detection at position \(x\).

That cancellation explains the dark bands: a place can be reachable through either slit individually, yet have almost no detections when both contributions interfere.

**Generated:** At one point on the screen, the two contributions are \(\psi_1=a\) and \(\psi_2=-a\), with \(a\ne0\). Would closing slit 2 increase or decrease the probability density of detecting an electron there?

---

**Learner**

why the fucj would we have gaps?

**Tutor**

Because **I skipped part of the assigned content**. You asked for a first pass through the relevant reading, and I moved from blackbody radiation to polarizers without covering the classical instability of atoms. That’s a gap in my teaching, not your understanding.

I also spent time on obvious checks instead of ensuring coverage. I’ll use the reading and these questions to keep the remaining explanation complete, without assuming I’ve taught things I haven’t.

---

**Learner**

ok maybe i should do it myself. then lets work though these question first and then tell me exactly what to read/learn

**Tutor**

We’ll work through these first. Then I’ll give you the exact reading sections and a checklist of what we covered, what needs review, and what I skipped.

**Q2:** Classical physics says an accelerating charge radiates energy. An orbiting electron is accelerating because its direction changes, so it should **radiate and continuously lose energy: (b)**. It would spiral inward, making the atom unstable—contrary to what we observe.

**Q3:** Which listed effect provides evidence of light behaving as particles?

(a) Coriolis effect  
(b) Doppler effect  
(c) Compton scattering  
(d) Single-slit interference

---

**Learner**

c?

**Tutor**

Yes—**(c), Compton scattering**. A photon transfers energy and momentum to an electron, consistent with a collision involving a particle of light.

**Q4:** Which scientist is usually credited with first performing the double-slit experiment with light?

(a) Newton  
(b) Muller  
(c) Fresnel  
(d) Young  
(e) De Broglie

---

**Learner**

uh ok. lets learn the whole thing without gaps starting now

**Tutor**

Yes. I’ll keep track of coverage, explain new ideas before using them, and ask application questions—not questions that simply repeat my last sentence. We’ll take the time needed rather than force everything into 30 minutes.

Our sequence is:

1. Blackbody radiation, classical atomic instability, and atomic spectra.
2. Compton scattering.
3. Polarization: fields, intensity, unpolarized light, and individual photons.
4. Matter waves and double-slit interference.
5. Quantum states, eigenstates, superposition, probabilities, and wavefunctions.

We’ll build on what you already understood, starting with a distinction in **blackbody radiation** that we haven’t properly covered.

**The peak of a spectrum and the total emitted power are different things.**

Imagine separating the emitted light into wavelength ranges. Each range carries some of the emitted power. A spectrum shows how that power is distributed.

- The **peak’s horizontal position** tells you which wavelength has the strongest emission per unit wavelength.
- The **area under the entire curve** tells you the total power emitted per unit surface area.

That’s why we have two separate laws:
\[
\lambda_{\text{peak}}T=b
\quad\text{and}\quad
\frac{P}{A}=\sigma T^4.
\]

The first locates the peak. The second describes the **whole spectrum added together**, not just the height of the peak.

You already correctly found that doubling temperature halves the peak wavelength and multiplies emitted power by 16 **when area stays fixed**.

**Generated:** Two spherical blackbodies have the same temperature, but sphere B has twice the radius of sphere A. How does their **total emitted power** compare? Use \(A=4\pi R^2\).

---

**Learner**

everything i need to know and nothing i dont

**Tutor**

Understood. **The assigned reading and its learning objectives will set our scope.** I’ll cover every required concept and calculation, skip optional extensions and unnecessary derivations, and avoid repeating things you’ve already demonstrated.

We’ll drop the sphere question—it adds geometry without addressing a current gap. Next is **classical atomic instability**, which I previously skipped.

An electron orbiting a nucleus continually changes direction, so it is **accelerating**, even if its speed stays constant. Classical electromagnetism predicts that an accelerating charge emits radiation. That radiation carries energy away from the electron–nucleus system.

The predicted result is that the electron’s orbit shrinks and it spirals into the nucleus. **Classical physics therefore fails to explain why atoms remain stable.**

That is the required takeaway here; you don’t need a calculation of the collapse time.

---

**Learner**

next. these are horrible questions

**Tutor**

Those questions only required substituting into what I’d just said. I’ll stop inserting them and explain the content in connected chunks.

You’ve already practised Compton scattering, so we can move to the missing part of polarization: **unpolarized light**.

A linearly polarized beam has a definite electric-field oscillation direction. An unpolarized beam has no preferred direction: its electric-field direction varies randomly in the plane perpendicular to its travel.

For an **ideal polarizer**:

- **Unpolarized input:** half the intensity passes, \(I_{\text{out}}=I_{\text{in}}/2\), regardless of the axis orientation.
- **Linearly polarized input:** use \(I_{\text{out}}=I_{\text{in}}\cos^2\theta\), where \(\theta\) is measured from the incoming polarization to the axis.

The first result comes from averaging \(\cos^2\theta\) over all incoming polarization directions; that average is \(1/2\).

**In both cases, the transmitted light is polarized along the filter’s axis.** That determines how you handle a second filter: its input is now polarized, so use Malus’s law with the angle **between the two filter axes**.

For example, unpolarized light passing through two filters separated by \(60^\circ\) has
\[
I_{\text{final}}
=\underbrace{\frac{I_0}{2}}_{\text{first filter}}
\underbrace{\cos^2 60^\circ}_{\text{second filter}}
=\frac{I_0}{8}.
\]

The key distinction is **what kind of light reaches each filter**. The factor \(1/2\) is not a rule to apply automatically at every filter.

---

**Learner**

elaborate a bit? not understanding this

**Tutor**

Let’s leave the symbols aside and use the polarizers you already understand.

Imagine preparing **many photons with exactly the same polarization**, then sending them individually toward a **vertical polarizer**.

If you prepare them vertically polarized, every photon passes. You can predict each result with certainty. That makes vertical polarization an **eigenstate of this measurement**.

If you prepare them horizontally polarized, every photon is blocked. Again, the result is certain. Horizontal polarization is another eigenstate—**“eigenstate” doesn’t mean it passes; it means the outcome is definite.**

Now prepare every photon at \(45^\circ\). About half pass and half are blocked. Even though they all have the same initial polarization, you cannot predict which individual photons will pass. So \(45^\circ\) polarization is **not an eigenstate of the vertical-polarizer measurement**.

But rotate the polarizer to \(45^\circ\). Those same prepared photons now pass with certainty. Their state **is an eigenstate of this new measurement**.

So the word means:

> **An eigenstate is a state for which a specified measurement has a certain outcome.**

“Superposition” is how we express a state using the eigenstates of the measurement we’re considering. Relative to a vertical polarizer, the \(45^\circ\) state has both vertical and horizontal components—just as a diagonal vector has both vertical and horizontal components.

Those components let us calculate the two outcome probabilities. **They don’t mean that the photon was secretly vertical or horizontal before reaching the filter.** It was prepared at \(45^\circ\), and that is a distinct state.

We can hold off on the coefficients until that distinction is clear.

---

**Learner**

ok i'd have to see a few questions that uses these notations for me to practice matching scenario to the notation to what they mean

**Tutor**

We’ll practise translating **scenario → notation → meaning**, one question at a time.

**Generated:** Every photon in a beam is prepared in the state
\[
|\psi\rangle=\frac{\sqrt3}{2}|V\rangle+\frac12|H\rangle,
\]
where \(|V\rangle\) and \(|H\rangle\) mean vertical and horizontal polarization.

The photons encounter an ideal **vertical polarizer**. Which description is correct?

**A.** Each photon has a \(3/4\) probability of passing.

**B.** Each photon has a \(\sqrt3/2\) probability of passing.

**C.** Each photon passes, but retains only \(3/4\) of its energy.

**D.** The notation says \(3/4\) of the photons were prepared vertically and \(1/4\) horizontally.

Choose one and briefly explain what the coefficient \(\sqrt3/2\) represents.

---

**Learner**

lets do more practice

**Tutor**

**Generated:** A photon is prepared in
\[
|\psi\rangle=\frac{\sqrt3}{2}|V\rangle+\frac12|H\rangle.
\]

It encounters a **horizontal polarizer**, followed by a **vertical polarizer**.

A student claims: “The probability of passing both is
\[
\left|\frac12\right|^2\left|\frac{\sqrt3}{2}\right|^2=\frac{3}{16}.
\]”

Is that reasoning correct? Explain using the photon’s state after the first polarizer.

---

**Learner**

LaTeX is not rendering properly.

**Tutor**

Here it is in plain text:

A photon is prepared in the state:

**|ψ⟩ = (√3/2)|V⟩ + (1/2)|H⟩**

It encounters a **horizontal polarizer**, followed by a **vertical polarizer**.

A student claims: “The probability of passing both is **(1/2)² × (√3/2)² = 3/16**.”

Is that reasoning correct? Explain using the photon’s state after the first polarizer.
