# Write a solution

**Learner**

render latex

**Tutor**

Given
\[
x(t)=ct^2-bt^3,\qquad t\geq 0,\qquad c,b>0.
\]

**(a) Units**

Both terms must have units of metres:
\[
\boxed{[c]=\mathrm{m/s^2}},\qquad
\boxed{[b]=\mathrm{m/s^3}}.
\]

**(b) Velocity and acceleration**

\[
\boxed{v(t)=\frac{dx}{dt}=2ct-3bt^2}
\]
\[
\boxed{a(t)=\frac{dv}{dt}=2c-6bt}
\]

**(c) Time and position of reversal**

Set the velocity equal to zero:
\[
t(2c-3bt)=0.
\]
The positive root is
\[
\boxed{t_{\mathrm{rev}}=\frac{2c}{3b}}.
\]
Velocity changes from positive to negative at this time, confirming a reversal.

The position is
\[
\begin{aligned}
x_{\mathrm{rev}}
&=c\left(\frac{2c}{3b}\right)^2
-b\left(\frac{2c}{3b}\right)^3\\
&=\frac{4c^3}{9b^2}-\frac{8c^3}{27b^2}\\
&=\boxed{\frac{4c^3}{27b^2}}.
\end{aligned}
\]

**(d) Acceleration at reversal**

\[
a(t_{\mathrm{rev}})
=2c-6b\left(\frac{2c}{3b}\right)
=\boxed{-2c}.
\]

**(e) Positive time of return to the origin**

\[
x(t)=t^2(c-bt)=0.
\]
The positive solution is
\[
\boxed{t_{\mathrm{return}}=\frac{c}{b}}.
\]

**(f) Total distance travelled**

The particle travels from the origin to its turning point, then back to the origin:
\[
D=2x_{\mathrm{rev}}
=\boxed{\frac{8c^3}{27b^2}}.
\]
