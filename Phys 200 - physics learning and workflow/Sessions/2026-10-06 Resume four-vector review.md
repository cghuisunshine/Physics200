# Resume four-vector review

**Learner**

there is a nonzero delta

**Tutor**

Yes—a nonzero **time interval** between the flashes. The component \(\Delta X^0=c\Delta t\) records that elapsed laboratory time, multiplied by \(c\).

*Generated*

A spaceship moves to the right relative to the laboratory. From the spaceship’s frame, what is the **direction of the lamp’s displacement** between the first and second flashes?

---

**Learner**

positive x right

**Tutor**

The **spaceship** moves right relative to the lab. But we need the **lamp’s motion relative to the spaceship**.

Picture riding in the spaceship and looking at the lab lamp. As you travel right past it, which way does the lamp move relative to you?

---

**Learner**

ah, negative.

**Tutor**

Right—negative \(x\). The lamp moves left relative to the spaceship, so the second flash happens farther left in that frame.

This connects to what **makes something a four-vector**: its components must change between frames according to the Lorentz transformation. Having four entries alone is insufficient.

For a frame moving at \(+v\) along \(x\), any four-vector \(A^\mu\) must satisfy
\[
A'^0=\gamma_v(A^0-\beta_v A^1),
\qquad \beta_v=v/c.
\]
The time and \(x\) components mix.

*Generated*

Someone proposes the four-component quantity
\[
B^\mu=(0,x,y,z),
\]
with its first entry **defined to be zero in every frame**.

For an event with \(x\ne0\), the Lorentz rule would require
\[
B'^0=-\gamma_v\beta_v x.
\]

What conflict does this reveal about the proposed quantity?

---

**Learner**

the number of ticks on the ship clock. 

i have trouble interpreting this, because L earth/(propertime) doesn't seem like its velocity, some weird ass quantity. what does it mean physically? does it have a physical meaning?

**Tutor**

Yes—the elapsed time counted by the ship’s clock. And your objection is right: **\(L_{\text{Earth}}/\Delta\tau\) is not the ship’s ordinary Earth-frame velocity.** Calling it a spatial component of “four-velocity” doesn’t make it ordinary velocity.

It has a physical meaning: **how much Earth-measured distance the ship covers per second of its own aging.**

Imagine Earth’s frame has distance markers along the route. The ship’s crew asks:

> “How many kilometres of that Earth-measured route do we cover for every second that passes on our onboard clock?”

That is what this quantity measures. It combines two specified measurements intentionally; it does **not** claim to be distance measured in the ship’s frame.

For a small part of the journey,
\[
\underbrace{\frac{dx}{d\tau}}_{\text{Earth distance per ship second}}
=
\underbrace{\frac{dx}{dt}}_{\text{Earth distance per Earth second}}
\underbrace{\frac{dt}{d\tau}}_{\text{Earth seconds per ship second}}
=\gamma_u u_x.
\]
So the extra factor accounts for the different rates of elapsed time. We’ll connect this to the Lorentz-transformation requirement once this interpretation feels clearer.

*Generated*

A ship covers **four light-years of Earth-measured distance** while its crew ages **three years**. Someone divides these and says, “The ship travelled faster than light relative to Earth.”

What is wrong with that interpretation?

---

**Learner**

the amount of ticks per proper tick that the moving frame accumulated.

**Tutor**

That’s the right interpretation: primed-frame coordinate time elapsed per unit of the particle’s proper time.
