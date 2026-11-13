# Explain four-vector applications

**Learner**

ok i know the definition of 4 vector and the definitino of the four velocity and four momentum. i dont understand them super well, and i especially dont know how they apply

**Tutor**

The missing piece is probably **what these objects let you do**. Knowing their definitions doesn’t automatically make that clear.

A four-vector packages quantities that **mix together when you change reference frames**. For example, different observers disagree about the time and position of an event, so we combine them:
\[
X^\mu=(ct,x,y,z).
\]
The benefit is that one Lorentz transformation tells you how the whole package changes.

**Four-velocity describes motion using the traveller’s own clock.**
Ordinary velocity uses the observing frame’s time: \(d\mathbf{x}/dt\). Four-velocity uses proper time:
\[
U^\mu=\frac{dX^\mu}{d\tau}=(\gamma c,\gamma\mathbf v).
\]
Because all observers agree on the proper time along that traveller’s path, this derivative transforms as a four-vector. Its spatial part is \(\gamma\mathbf v\), rather than ordinary velocity.

**Four-momentum is where this becomes especially useful in problems.**
For a particle with rest mass \(m\),
\[
P^\mu=mU^\mu
=\left(\frac Ec,\mathbf p\right),
\qquad
E=\gamma mc^2,\quad \mathbf p=\gamma m\mathbf v.
\]
This tells you that **energy and momentum are parts of the same object**—changing frames mixes them, just as it mixes time and position.

You mainly apply four-momentum in three ways:

- **Change frames:** knowing energy and momentum in one frame lets you find them in another.
- **Analyse collisions and decays:** total four-momentum is conserved, giving energy conservation and momentum conservation together.
- **Relate energy, momentum, and mass:** its invariant gives
  \[
  E^2-p^2c^2=m^2c^4.
  \]

Let’s make just one piece concrete first: **a massive particle is sitting still in your frame. What do you think its four-momentum \((E/c,\mathbf p)\) is?**
