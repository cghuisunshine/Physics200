"""Build the offline PHYS 200 reader from local course sources.

Run with /private/tmp/data-structure-figures-venv/bin/python (PyMuPDF required).
KaTeX is used at build time only; the resulting HTML has no remote dependencies.
"""
from pathlib import Path
import base64
import html
import json
import re
import subprocess
from urllib.parse import quote
import fitz

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'PHYS_200_Review_and_Summary_Tutorial.html'
REFERENCE = Path('/Users/chenguagnghui/tutor/Physics_uni/Physics_Review_and_Summary_Tutorial.html')
MATH = REFERENCE.parent / 'assets/math'
SECTIONS = []


def section(title, group, sources, body, tags=''):
    SECTIONS.append(dict(title=title, group=group, sources=sources, body=body, tags=tags))


L = 'Lecture material/Lectures/'
Q = 'Additional material/PHYS200__Notes_on_Quantum-4.pdf'

section('Frames, events & the two postulates', 'Relativity', [(L+'Week 01.pdf', 24), (L+'Week 02-1.pdf', 8)], r'''
<p class="lead">Relativity begins by separating an event from the coordinates that different observers assign to it.</p>
<h3>What the words mean</h3>
<p>An <strong>inertial reference frame</strong> is a frame in which a free particle moves with constant velocity. An <strong>event</strong> is something happening at a particular place and time: a flash, a collision, or two objects passing each other. Coordinates label the event; changing frames changes its labels.</p>
<div class="concept-grid"><div><h4>1 · Relativity principle</h4><p>The laws of physics have the same form in every inertial frame. No inertial frame is a preferred state of absolute rest.</p></div><div><h4>2 · Light speed</h4><p>Light in vacuum has speed \(c\) in every inertial frame, independent of the motion of its source.</p></div></div>
<h3>Set up the frames before the algebra</h3>
<p>Throughout this reader, frame \(S'\) moves with signed velocity \(v\) along the positive \(x\)-axis of \(S\). The origins coincide at \(t=t'=0\). The primed origin therefore follows \(x=vt\). Reverse the sign of \(v\) to transform back.</p>
<div class="formula">\[\beta=\frac{v}{c},\qquad \gamma(v)=\frac{1}{\sqrt{1-v^2/c^2}}\]</div>
<p>Use \(|v|&lt;c\). At low speed, \(\gamma\approx1\). At \(0.6c\), \(\gamma=1.25\). A negative velocity changes boost signs, while \(\gamma\) stays positive.</p>
<div class="note"><strong>Seeing versus measuring.</strong> A distant flash reaches your eye later than it occurs. Coordinate time is assigned using synchronized clocks and corrected signal travel time; it is not simply the time you see the flash.</div>
<h3>Michelson–Morley: the course-level idea</h3>
<p>The experiment found no expected fringe shift from an ether wind as the apparatus orientation changed. Its conceptual role is to challenge a preferred light-propagation frame; the full experimental derivation is outside the main reading focus in <em>scope.txt</em>.</p>
''', 'inertial IFR postulates ether Michelson Morley beta gamma event synchronization')

section('Simultaneity & synchronized clocks', 'Relativity', [(L+'Week 02-1.pdf', 18), (L+'Week 03-2.pdf', 10)], r'''
<p class="lead">Two spatially separated events can be simultaneous in one frame and occur at different times in another.</p>
<p>To synchronize clocks at rest in one frame, send a light signal from A at \(t_1\), reflect it at B, and receive it back at A at \(t_2\). Assign the reflection the time \((t_1+t_2)/2\). This uses the same light speed in both directions in that inertial frame.</p>
<div class="formula">\[\Delta t'=\gamma(v)\left(\Delta t-\frac{v\Delta x}{c^2}\right)\]</div>
<p>If \(\Delta t=0\), then \(\Delta t'=-\gamma v\Delta x/c^2\). For \(v&gt;0\) and \(\Delta x&gt;0\), the event farther in the positive direction has an earlier primed time.</p>
<h3>Keep the same pair of events</h3>
<p>Label event 1 and event 2, write their coordinates in one frame, and transform both. Do not replace one event with a different clock reading just because it makes a familiar formula applicable.</p>
<div class="note"><strong>Why moving clocks can each run slow.</strong> Each frame uses its own set of synchronized clocks. Comparing readings at distant locations introduces relativity of simultaneity; it is not a contradiction between two measurements of one shared clock pair.</div>
<details class="example"><summary>Generated example · simultaneous flashes</summary><p>Two flashes are separated by 300 m and simultaneous in \(S\). For \(v=0.6c\), \(\Delta t'=-1.25(0.6)(300/c)=-0.75\,\mu\mathrm{s}\). The positive-\(x\) flash occurs earlier in \(S'\).</p></details>
''')

section('Proper time & length contraction', 'Relativity', [(L+'Week 02-2.pdf', 17), (L+'Week 03-1.pdf', 34)], r'''
<p class="lead">Identify the clock and the measurement events before choosing time dilation or length contraction.</p>
<h3>Proper time belongs to a worldline</h3>
<p>The <strong>proper time</strong> \(\Delta\tau\) is the elapsed time on a clock present at both events. For two events on an inertially moving clock, the clock’s rest frame has \(\Delta x'=0\).</p>
<div class="formula">\[\Delta t=\gamma(u)\Delta\tau,\qquad d\tau=dt\sqrt{1-u^2/c^2}\]</div>
<p>A moving clock accumulates less proper time than the coordinate time between its ticks in the observing frame. For a trip with several inertial legs, add the proper times of those legs; do not apply one inertial frame to the entire turnaround.</p>
<h3>Proper length belongs to the object’s rest frame</h3>
<p>The <strong>proper length</strong> \(L_0\) is the rest-frame separation of an object’s endpoints. Measuring the moving length requires recording both endpoints <em>at the same time in the measuring frame</em>.</p>
<div class="formula">\[L_{\parallel}=\frac{L_0}{\gamma(v)},\qquad L_{\perp}=L_{0,\perp}\]</div>
<div class="note"><strong>Two different conditions:</strong> time dilation uses two events at the same place in the clock frame; a length measurement uses two endpoint events at the same time in the measuring frame. They are different event selections.</div>
<h3>The ladder and twins</h3>
<p>For a ladder passing through a garage, simultaneous closing of both doors in the garage frame is not simultaneous in the ladder frame. For the twins, the travelling twin changes inertial frames at turnaround. Compare total proper time along each worldline.</p>
<details class="example"><summary>Generated example · unstable particle</summary><p>A particle has proper lifetime \(2.2\,\mu\mathrm{s}\) and speed \(0.8c\), giving \(\gamma=5/3\). Its mean lab lifetime is \(3.67\,\mu\mathrm{s}\), and its mean lab travel distance is \(u\gamma\tau\approx880\,\mathrm{m}\).</p></details>
''')

section('Lorentz & velocity transformations', 'Relativity', [(L+'Week 03-2.pdf', 7), (L+'Week 03-2.pdf', 26)], r'''
<p class="lead">Transform event coordinates first; velocity transformations follow by dividing transformed displacements.</p>
<div class="formula">\[x'=\gamma(v)(x-vt),\qquad t'=\gamma(v)\left(t-\frac{vx}{c^2}\right),\qquad y'=y,\quad z'=z\]</div>
<p>These equations assume coincident origins at zero time and a boost along \(x\). They also apply to coordinate differences. For the inverse, exchange primed and unprimed quantities and replace \(v\) by \(-v\).</p>
<h3>Particle velocity is a different variable</h3>
<p>Let the particle’s velocity in \(S\) be \(\mathbf u\). Divide \(dx'\) by \(dt'\), and similarly for the transverse components:</p>
<div class="formula">\[u_x'=\frac{u_x-v}{1-vu_x/c^2},\qquad u_y'=\frac{u_y}{\gamma(v)(1-vu_x/c^2)},\qquad u_z'=\frac{u_z}{\gamma(v)(1-vu_x/c^2)}\]</div>
<p>The transverse coordinates do not change under the boost, but the time increment does. This is why transverse <em>velocity</em> still changes.</p>
<details><summary>Where the denominator comes from</summary><p>Write \(dx'=\gamma(dx-vdt)\) and \(dt'=\gamma(dt-vdx/c^2)\). Divide both by \(dt\). Their ratio gives \((u_x-v)/(1-vu_x/c^2)\). The same denominator enters \(dy'/dt'\), with an additional \(\gamma\) because \(dy'=dy\).</p></details>
<div class="note"><strong>Check the direction.</strong> An object at rest in \(S\) has \(u_x'=-v\). A light ray with \(u_x=c\) still has \(u_x'=c\). A closing rate between two objects measured in one frame can exceed \(c\); the speed of either object measured in the other’s rest frame cannot.</div>
<div class="interactive" id="boost-demo"><h4>Explore a boost</h4><label for="boost">Frame velocity \(v/c\): <output id="boost-value">0.60</output></label><input id="boost" type="range" min="-95" max="95" value="60"><p>A particle at rest in S is measured in S′ with <strong id="boost-result"></strong>.</p><p class="fine">The boost γ depends on frame velocity, not on a separate particle’s speed.</p></div>
''')

section('Spacetime intervals & causality', 'Relativity', [(L+'Week 04-1.pdf', 15), (L+'Week 05-1.pdf', 19)], r'''
<p class="lead">An invariant classifies the relation between two events even when their space and time separations change.</p>
<p>The lecture convention puts a minus sign on the time term:</p>
<div class="formula">\[\Delta s^2=-c^2\Delta t^2+\Delta x^2+\Delta y^2+\Delta z^2\]</div>
<table><thead><tr><th>Separation</th><th>Condition</th><th>Physical meaning</th></tr></thead><tbody><tr><td>Timelike</td><td>\(\Delta s^2&lt;0\)</td><td>A slower-than-light object can connect the events. Their time order is invariant for ordinary inertial boosts.</td></tr><tr><td>Lightlike / null</td><td>\(\Delta s^2=0\)</td><td>A light signal can connect the events.</td></tr><tr><td>Spacelike</td><td>\(\Delta s^2&gt;0\)</td><td>No light-speed-or-slower signal connects them. Different frames may reverse their time order.</td></tr></tbody></table>
<div class="formula">\[\Delta\tau=\frac{\sqrt{-\Delta s^2}}{c}\quad\text{(inertial clock, timelike pair)}\]</div>
<h3>Read the diagram</h3>
<p>With \(ct\) vertical and \(x\) horizontal on equal scales, light travels on lines at 45°. A worldline for a massive particle stays inside the light cone. A simultaneous line in \(S'\) satisfies \(ct=\beta x\), while the \(ct'\)-axis satisfies \(x=\beta ct\).</p>
<svg class="diagram" viewBox="0 0 620 300" role="img" aria-labelledby="cone-title"><title id="cone-title">Spacetime diagram with future and past light cones, a stationary worldline, and a spacelike event</title><path d="M310 150L175 15H445Z M310 150L175 285H445Z" fill="#e4eddf"/><path d="M40 150H580 M310 285V12" stroke="#60796b" stroke-width="1.5"/><path d="M175 15L445 285 M445 15L175 285" stroke="#bf9049" stroke-width="2"/><path d="M310 275V25" stroke="#235c4e" stroke-width="3"/><circle cx="310" cy="150" r="5" fill="#235c4e"/><circle cx="500" cy="110" r="5" fill="#bf9049"/><g fill="#193d37" font-size="14" font-family="sans-serif"><text x="324" y="27">ct</text><text x="575" y="174">x</text><text x="330" y="80">Future light cone</text><text x="330" y="243">Past light cone</text><text x="421" y="99">Spacelike event</text><text x="323" y="172">Here, now</text></g></svg>
<div class="note"><strong>Convention check.</strong> Some books reverse every sign in \(\Delta s^2\). The physics agrees, but the words “positive” and “negative” swap. This page follows the lecture and local formula sheet.</div>
''')

section('Four-vectors: position to momentum', 'Relativity', [(L+'Week 05-2.pdf', 28), (L+'Week 05-2.pdf', 29)], r'''
<p class="lead">A four-vector is defined by how it transforms, not just by having four entries.</p>
<p>The position four-vector is \(X=(ct,x,y,z)\). Differences between events transform with the Lorentz matrix. Dividing by the invariant proper-time increment preserves this transformation rule.</p>
<div class="formula">\[X\ \longrightarrow\ U=\frac{dX}{d\tau}=\gamma(u)(c,\mathbf u)\ \longrightarrow\ P=mU=(E/c,\mathbf p)\]</div>
<p>Here \(\mathbf u\) is the particle’s velocity in the frame where you are constructing the components. Thus \(P^0=E/c\), \(P^1=p_x\), \(P^2=p_y\), and \(P^3=p_z\). Every component has momentum units. The time component contains total energy, including rest energy.</p>
<h3>Constructing versus transforming</h3>
<p><strong>Construct:</strong> use \(\gamma(u)\) to calculate a particle’s \(E\) and \(\mathbf p\) in one frame. <strong>Transform:</strong> use \(\gamma(v)\) to change those components to a frame moving at \(v\).</p>
<div class="formula">\[E'=\gamma(v)(E-vp_x),\qquad p_x'=\gamma(v)\left(p_x-\frac{vE}{c^2}\right),\qquad p_y'=p_y,\quad p_z'=p_z\]</div>
<div class="note"><strong>Rest-particle check.</strong> If \(\mathbf p=0\) in S, then \(E'=\gamma(v)mc^2\) and \(p_x'=-\gamma(v)mv\). The negative sign is the particle’s motion seen from S′.</div>
<h3>The invariant norm</h3>
<p>With the lecture metric, \(P\cdot P=-E^2/c^2+\mathbf p^2=-m^2c^2\). Rearranging gives the usual energy–momentum relation. For a photon, use \(P=(E/c,\mathbf p)\) directly; a photon has no rest frame or proper-time four-velocity.</p>
''')

section('Energy, collisions & system mass', 'Relativity', [(L+'Week 05-2.pdf', 34), (L+'Week 06-1.pdf', 24)], r'''
<p class="lead">Conserve total energy and each momentum component. Apply the invariant to the particle or system you actually mean.</p>
<div class="formula">\[\mathbf p=\gamma(u)m\mathbf u,\quad E=\gamma(u)mc^2,\quad K=E-mc^2,\quad E^2=p^2c^2+m^2c^4\]</div>
<p>Each massive particle has its own \(\gamma(u)\). At low speed, \(K\approx mu^2/2\) and \(p\approx mu\). For a photon, \(m=0\) and \(E=pc\).</p>
<h3>Make a before-and-after ledger</h3>
<ol><li>Choose one frame and assign signed momentum components.</li><li>Write \(\sum E_{\rm before}=\sum E_{\rm after}\) and the analogous equations for \(p_x,p_y,p_z\).</li><li>For each particle, connect its energy, momentum and rest mass using its own invariant.</li><li>If a system is the useful object, add its energies and vector momenta first, then form its invariant.</li></ol>
<div class="formula">\[M_{\rm system}^2c^4=E_{\rm total}^2-c^2\left|\sum_i\mathbf p_i\right|^2,\qquad \mathbf V_{\rm CM}=\frac{c^2\mathbf p_{\rm total}}{E_{\rm total}}\]</div>
<p>Zero net momentum does not mean zero constituent kinetic energy. Two oppositely directed photons can have positive system mass. Two parallel photons have zero invariant system mass. Individual rest masses need not add to the mass of a composite system.</p>
<h3>Binding, decay and thresholds</h3>
<div class="formula">\[M_{\rm bound}c^2=\sum_i m_i c^2-B\qquad (B&gt;0)\]</div>
<p>Binding energy is defined relative to specified separated constituents. For a decay, use the parent rest energy as the available energy in the parent rest frame. At a production threshold, the final particles have the least possible energy in the centre-of-momentum frame; lab kinetic energy can remain in motion of that frame.</p>
<details class="example"><summary>Generated example · two photons form one system</summary><p>Photons have energies 9 MeV along +x and 1 MeV along −x. Then \(E_{\rm tot}=10\,\mathrm{MeV}\), \(p_{\rm tot}=8\,\mathrm{MeV}/c\), and \(Mc^2=\sqrt{10^2-8^2}=6\,\mathrm{MeV}\). Thus \(M=6\,\mathrm{MeV}/c^2\) and \(V_{\rm CM}=0.8c\).</p></details>
<div class="note"><strong>Units catch errors.</strong> MeV is energy, MeV/c is momentum, and MeV/c² is mass. The invariant uses the square of the net vector momentum, not a sum of momentum magnitudes.</div>
''')

section('Relativistic Doppler shift', 'Relativity', [('Lecture material/Tutorials/Week 05 - Tutorial - solutions.pdf', 1)], r'''
<p class="lead">A Doppler formula needs a named frame for its angle and a clear distinction between emitted and received frequency.</p>
<h3>Transform the photon energy</h3>
<p>For a photon of frequency \(f\) in S, let \(\theta_S\) be the angle between its propagation direction and the positive boost direction, measured in S. Since \(p_x=(hf/c)\cos\theta_S\):</p>
<div class="formula">\[f'=\gamma(v)f(1-\beta\cos\theta_S)\]</div>
<p>This formula transforms the same photon between frames. It is often safer than memorizing a geometry-specific sign.</p>
<h3>Two useful emitter/receiver forms</h3>
<p>Let E denote the emitter rest frame and R the receiver rest frame. In the first expression, \(\alpha\) is the angle between the receiver velocity and the photon propagation direction, both in E. In the second, \(\theta\) is the angle between the emitter velocity and photon propagation direction, both in R. Here \(\beta\) is the relative speed divided by \(c\), and \(\gamma\) uses that speed.</p>
<div class="formula">\[f_R=\gamma f_E(1-\beta\cos\alpha),\qquad \lambda_R=\frac{\lambda_E}{\gamma(1-\beta\cos\alpha)}\]</div>
<div class="formula">\[\lambda_R=\gamma\lambda_E(1-\beta\cos\theta)\]</div>
<p>The angles are not interchangeable: changing frames also changes the photon’s propagation direction (aberration).</p>
<table><thead><tr><th>Longitudinal motion</th><th>Received / emitted frequency</th></tr></thead><tbody><tr><td>Approaching</td><td>\(f_R/f_E=\sqrt{(1+\beta)/(1-\beta)}\)</td></tr><tr><td>Receding</td><td>\(f_R/f_E=\sqrt{(1-\beta)/(1+\beta)}\)</td></tr></tbody></table>
<div class="note"><strong>“Transverse” needs a frame.</strong> If the receiver velocity is perpendicular to the photon in E, \(f_R=\gamma f_E\). If the emitter velocity is perpendicular to the photon in R, \(f_R=f_E/\gamma\). These are different geometries.</div>
''')

section('Light: fields, photons & intensity', 'Light & quanta', [(L+'Week 06-2.pdf', 23), (L+'Week 08-1.pdf', 20)], r'''
<p class="lead">A light beam has a wave description and a photon description. Both must give the same energy flow.</p>
<div class="formula">\[E(x,t)=E_0\cos(kx-\omega t+\phi),\quad k=\frac{2\pi}{\lambda},\quad\omega=2\pi f,\quad c=\lambda f\]</div>
<p>For a plane wave in vacuum, the electric field, magnetic field and propagation direction are perpendicular, and \(B_0=E_0/c\). Frequency sets the photon energy; amplitude sets the classical intensity.</p>
<div class="formula">\[E_\gamma=hf=\frac{hc}{\lambda},\qquad p_\gamma=\frac{E_\gamma}{c}=\frac{h}{\lambda}\]</div>
<div class="formula">\[I=\frac{P}{A}=\frac12\epsilon_0cE_0^2=\frac{\dot N\,hf}{A}\]</div>
<p>Here \(\dot N\) counts photons per unit time through area \(A\), and \(E_0\) is peak field amplitude. At fixed frequency, raising intensity raises photon arrival rate. At fixed intensity, doubling frequency halves the photon flux and leaves field amplitude unchanged.</p>
<h3>Keep total power separate from intensity</h3>
<p>Spreading a beam over twice the area halves its intensity. If the whole beam still reaches a detector, its total photon arrival rate is unchanged when total power and frequency are fixed.</p>
<div class="note"><strong>Conversion chain:</strong> wavelength → frequency → energy → momentum. A useful local-sheet constant is \(hc\approx1240\,\mathrm{eV\,nm}\). Convert eV to joules before combining with SI mass or Planck’s constant in J·s.</div>
<details class="example"><summary>Generated example · a 500 nm photon</summary><p>\(E_\gamma=1240/500=2.48\,\mathrm{eV}\). The frequency is about \(6.00\times10^{14}\,\mathrm{Hz}\). Its momentum is \(h/\lambda\approx1.33\times10^{-27}\,\mathrm{kg\,m/s}\).</p></details>
''')

section('The photoelectric effect', 'Light & quanta', [(L+'Week 07-1.pdf', 9), (L+'Week 07-1.pdf', 17)], r'''
<p class="lead">One absorbed photon gives an electron a discrete amount of energy. The work function sets the minimum energy cost of escape.</p>
<div class="formula">\[K_{\max}=hf-W=\frac{hc}{\lambda}-W,\qquad e|V_s|=K_{\max}\]</div>
<p>\(W\) is the metal’s work function. The elementary charge \(e\) is positive here, and \(|V_s|\) is the magnitude of the retarding stopping voltage. Photoelectrons have a range of energies; the stopping potential probes the maximum.</p>
<div class="formula">\[f_0=\frac{W}{h},\qquad \lambda_0=\frac{hc}{W}\]</div>
<table><thead><tr><th>Change</th><th>Single-photon photoelectric prediction</th></tr></thead><tbody><tr><td>Increase intensity at fixed frequency above threshold</td><td>More emitted electrons per time under fixed collection conditions; same maximum kinetic energy.</td></tr><tr><td>Increase frequency at fixed intensity</td><td>Higher maximum kinetic energy; fewer incident photons per time.</td></tr><tr><td>Increase intensity below threshold</td><td>No emission in the ordinary one-photon model.</td></tr></tbody></table>
<h3>Read a graph</h3>
<p>A graph of \(K_{\max}\) versus frequency has slope \(h\) and extrapolated intercept \(-W\). Versus wavelength, \(hc/\lambda-W\) decreases with a positive second derivative; the physical emission branch ends at \(\lambda_0\). Beyond it, do not report negative electron kinetic energy.</p>
<details class="example"><summary>Generated example · work function 2.0 eV, wavelength 400 nm</summary><p>Photon energy is 3.10 eV, so \(K_{\max}=1.10\,\mathrm{eV}\). A stopping-voltage magnitude of 1.10 V stops even the fastest photoelectrons.</p></details>
''')

section('Compton scattering', 'Light & quanta', [(L+'Week 07-1.pdf', 29), (L+'Week 06-2.pdf', 5)], r'''
<p class="lead">A photon scattering from an initially stationary free electron transfers energy and momentum to it.</p>
<div class="formula">\[\lambda'-\lambda=\frac{h}{m_ec}(1-\cos\theta)=\lambda_C(1-\cos\theta),\qquad \lambda_C=\frac{h}{m_ec}\]</div>
<p>\(\theta\) is the angle between incoming and outgoing photon directions, in the initial electron rest frame. It is not the recoil electron’s angle. For \(\theta=0\), the shift is zero; for backscattering, it is \(2\lambda_C\). The electron Compton wavelength is approximately 2.43 pm.</p>
<div class="formula">\[E_\gamma'=\frac{E_\gamma}{1+(E_\gamma/m_ec^2)(1-\cos\theta)},\qquad K_e=E_\gamma-E_\gamma'\]</div>
<p>Recover electron momentum from vector conservation, \(\mathbf p_e=\mathbf p_\gamma-\mathbf p_\gamma'\). Its kinetic energy generally needs the relativistic relation.</p>
<h3>Classical comparison</h3>
<p>In weak-field classical scattering from a nonrelativistic driven electron, the oscillating incident field accelerates the charge and the charge radiates at the driving frequency. The observed angle-dependent wavelength shift requires the photon energy–momentum description.</p>
<div class="note"><strong>Terminology:</strong> the Compton wavelength \(\lambda_C\) is a fixed particle scale; the Compton wavelength <em>shift</em> \(\Delta\lambda\) depends on angle. Week 6-2 explicitly labels its four-vector derivation “not tested”; the scattering relation and its physical meaning remain relevant.</div>
''')

section('Blackbody radiation', 'Light & quanta', [(L+'Week 08-1.pdf', 6), (L+'Week 08-1.pdf', 8)], r'''
<p class="lead">Thermal radiation has a temperature-dependent spectrum. Quantization removes the classical ultraviolet divergence.</p>
<p>An ideal <strong>blackbody</strong> absorbs all incident radiation and has a universal equilibrium emission spectrum set by its temperature. The Planck spectrum is consistent with energy quanta \(hf\); the classical prediction fails at high frequency.</p>
<div class="formula">\[\lambda_{\max}T=b,\qquad b\approx2.898\times10^{-3}\,\mathrm{m\,K}\]</div>
<div class="formula">\[\frac{P}{A}=\sigma T^4,\qquad \sigma\approx5.670\times10^{-8}\,\mathrm{W\,m^{-2}K^{-4}}\]</div>
<p>Wien’s law above refers to the peak of the spectrum plotted per unit wavelength. Stefan–Boltzmann gives total emitted power per area for an ideal blackbody. For a surface with emissivity \(\varepsilon\), multiply by \(\varepsilon\); idealized net radiative loss to surroundings at \(T_s\) is \(\varepsilon\sigma A(T^4-T_s^4)\).</p>
<div class="note"><strong>Scaling:</strong> doubling the absolute temperature halves the peak wavelength and multiplies total emitted power by 16 at fixed area. Use kelvin. The frequency-spectrum peak is not obtained by simply taking \(c/\lambda_{\max}\).</div>
<div class="interactive"><h4>Change the temperature</h4><label for="temperature">Temperature: <output id="temperature-value">5800 K</output></label><input id="temperature" type="range" min="1000" max="10000" step="100" value="5800"><div id="temperature-result" aria-live="polite"></div><p class="fine">Ideal blackbody, fixed area. Power is relative to a 5800 K body.</p></div>
''')

section('Interference & diffraction', 'Light & quanta', [(L+'Week 08-1.pdf', 23), (L+'Week 08-1.pdf', 25)], r'''
<p class="lead">Add amplitudes for coherent alternatives, then square their combined magnitude to predict intensity or probability.</p>
<div class="formula">\[\Delta\phi=\frac{2\pi\Delta r}{\lambda},\quad \Delta r=m\lambda\ \text{(bright)},\quad \Delta r=(m+\tfrac12)\lambda\ \text{(dark)}\]</div>
<p>These bright/dark conditions assume coherent paths with the same initial phase; complete darkness also requires equal contributing amplitudes. A path difference of \(3.5\lambda\) gives destructive interference under these assumptions.</p>
<h3>Double-slit geometry</h3>
<div class="formula">\[d\sin\theta=m\lambda,\qquad y_m\approx\frac{m\lambda D}{d},\qquad \Delta y\approx\frac{\lambda D}{d}\]</div>
<p>\(d\) is the slit separation and \(D\) the distance to a distant screen. The screen formulas use small angles and the far-field approximation. Slit width controls the diffraction envelope; slit separation controls the interference spacing. A single slit of width \(a\) has minima at \(a\sin\theta=m\lambda\), for nonzero integer \(m\).</p>
<h3>Single particles still produce a pattern</h3>
<p>Each detection is localized. Many particles prepared in the same coherent state build up a distribution given by the squared combined amplitude. For two alternatives, \(|\psi_1+\psi_2|^2\) contains an interference cross term. Simply adding \(|\psi_1|^2+|\psi_2|^2\) omits it. Which-path information can remove the coherence required for interference.</p>
<div class="note"><strong>Recorded Quiz 3 boundary.</strong> Week 08-1 marks the end of its Long Quiz 3 material at PDF page 34 (printed slide 37), at the transition to Probability Density. Diffraction before that marker is included in the recorded scope.</div>
''')

section('Polarization & quantum measurement', 'Quantum states', [(Q, 11), (L+'Week 09-1.pdf', 5)], r'''
<p class="lead">Polarization provides a two-state model of superposition, probabilities and the change caused by measurement.</p>
<h3>Classical and single-photon versions</h3>
<div class="formula">\[I_{\rm out}=I_{\rm in}\cos^2\theta\]</div>
<p>Malus’s law applies to linearly polarized light incident on an ideal linear polarizer, with \(\theta\) between its polarization and the transmission axis. Ideal unpolarized light loses half its intensity at the first polarizer.</p>
<div class="formula">\[|\psi\rangle=a|H\rangle+b|V\rangle,\qquad |a|^2+|b|^2=1\]</div>
<p>In the H/V measurement basis, probabilities are \(|a|^2\) and \(|b|^2\). Complex coefficients carry phase information. For a linear polarization at angle \(\theta\) to H, one may choose \(a=\cos\theta\) and \(b=\sin\theta\).</p>
<h3>A measurement changes the state</h3>
<p>A photon transmitted by an H polarizer emerges in the H state. A second H polarizer then transmits it with certainty in the ideal model. A 45° polarizer followed by a V polarizer gives two further factors of 1/2. Inserting the middle polarizer between crossed H and V axes can therefore allow transmission.</p>
<div class="formula">\[I_0\ \xrightarrow{\ H\ }\ \frac{I_0}{2}\ \xrightarrow{\ 45^\circ\ }\ \frac{I_0}{4}\ \xrightarrow{\ V\ }\ \frac{I_0}{8}\quad\text{(unpolarized input)}\]</div>
<div class="note"><strong>Amplitude versus probability.</strong> Coefficients can be negative or complex. Probabilities are nonnegative squared magnitudes. Relative phase can change probabilities in another measurement basis even when H/V probabilities stay fixed.</div>
''')

section('Wavefunctions & probability density', 'Quantum states', [(Q, 14), (L+'Week 08-1.pdf', 36)], r'''
<p class="lead">The wavefunction is a probability amplitude. Its squared magnitude is a density, whose integral over a region is a probability.</p>
<div class="formula">\[\rho(x)=|\psi(x)|^2=\psi^*(x)\psi(x),\qquad P(a\le x\le b)=\int_a^b |\psi(x)|^2\,dx\]</div>
<div class="formula">\[\int_{-\infty}^{\infty}|\psi(x)|^2\,dx=1\]</div>
<p>For a normalized one-dimensional position wavefunction, \(\psi\) has units \(\mathrm{m}^{-1/2}\), and \(\rho\) has units \(\mathrm{m}^{-1}\). A density can exceed 1; the integrated probability remains between 0 and 1. A single exact point has zero probability in an ordinary continuous distribution.</p>
<h3>Superposition and measurement</h3>
<p>A state can be expanded in eigenstates of an observable. In a normalized orthonormal discrete basis, \(|\psi\rangle=\sum_n c_n|n\rangle\), and a measurement returns eigenvalue \(n\)’s associated value with probability \(|c_n|^2\). An eigenstate gives one definite value of the corresponding observable.</p>
<h3>Complex numbers are essential</h3>
<div class="formula">\[z=a+ib,\qquad z^*=a-ib,\qquad |z|^2=a^2+b^2,\qquad e^{i\phi}=\cos\phi+i\sin\phi\]</div>
<p>A global phase multiplying the entire state leaves all probabilities unchanged. Relative phase between terms can change interference. Do not confuse the real part of a wavefunction with its probability density.</p>
<details class="example"><summary>Generated example · normalize a constant amplitude</summary><p>If \(\psi=A\) on \(0\le x\le L\) and zero elsewhere, then \(|A|^2L=1\). Choose \(A=1/\sqrt L\) up to a global phase. The probability in the first quarter is \(1/4\). This discontinuous idealization is a probability example, not a stationary infinite-well solution.</p></details>
''')

section('Matter waves, eigenstates & wavepackets', 'Quantum states', [(L+'Week 09-1.pdf', 29), (L+'Week 09-2.pdf', 6)], r'''
<p class="lead">A definite momentum corresponds to a plane wave. Localization requires a spread of momenta.</p>
<div class="formula">\[\lambda=\frac{h}{p},\qquad p=\hbar k,\qquad \hbar=\frac{h}{2\pi}\]</div>
<p>For a slow massive particle, \(K=p^2/(2m)\), so \(\lambda=h/\sqrt{2mK}\). This approximation requires \(K\ll mc^2\). Otherwise, use \(pc=\sqrt{K(K+2mc^2)}\). A massive particle does not obey the photon relation \(E=pc\).</p>
<h3>Two representations of the same state</h3>
<div class="formula">\[\psi(x)=\frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{\infty}\widetilde\psi(p)e^{ipx/\hbar}\,dp\]</div>
<div class="formula">\[\widetilde\psi(p)=\frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{\infty}\psi(x)e^{-ipx/\hbar}\,dx\]</div>
<p>The normalization factor is also \(1/\sqrt h\), as on the local formula sheet. \(|\widetilde\psi(p)|^2\) is momentum probability density. Position and momentum wavefunctions contain the same state information in different bases.</p>
<h3>Ideal eigenstates versus physical packets</h3>
<p>A momentum eigenstate has spatial factor \(e^{ipx/\hbar}\) and constant position density. On the whole real line it cannot be normalized to unit probability by an ordinary finite constant. A normalizable wavepacket combines momentum components. Narrower position localization needs a broader momentum distribution.</p>
<details class="example"><summary>Generated example · a 4.5 eV electron</summary><p>Because 4.5 eV is tiny compared with \(m_ec^2\approx511000\,\mathrm{eV}\), use the nonrelativistic expression. \[\lambda=\frac{hc}{\sqrt{2(m_ec^2)K}}\approx\frac{1240}{\sqrt{2(511000)(4.5)}}\,\mathrm{nm}\approx0.578\,\mathrm{nm}.\]Writing the denominator with the rest <em>energy</em> makes the eV units consistent.</p></details>
''')

section('Expectation values & uncertainty', 'Quantum states', [(L+'Week 09-2.pdf', 32), (L+'Week 09-2.pdf', 35)], r'''
<p class="lead">Expectation values describe ensemble averages; uncertainties describe statistical spread in identically prepared states.</p>
<div class="formula">\[\langle x\rangle=\int x|\psi(x)|^2\,dx,\qquad (\Delta x)^2=\langle x^2\rangle-\langle x\rangle^2\]</div>
<div class="formula">\[\langle p\rangle=\int p|\widetilde\psi(p)|^2\,dp,\qquad (\Delta p)^2=\langle p^2\rangle-\langle p\rangle^2\]</div>
<p>Integrals run over the full allowed range. \(\Delta x\) and \(\Delta p\) are standard deviations, not arbitrary full widths. An expectation value need not be one of the outcomes of a single measurement.</p>
<div class="formula">\[\Delta x\,\Delta p\ge\frac{\hbar}{2}\]</div>
<p>Heisenberg uncertainty follows from the relation between position and momentum representations. It is an intrinsic restriction on their spreads in one quantum state, rather than just a statement about imperfect equipment. A minimum-uncertainty Gaussian attains equality.</p>
<div class="interactive"><h4>A minimum-uncertainty Gaussian</h4><label for="packet">Position standard deviation: <output id="packet-value">1.0 nm</output></label><input id="packet" type="range" min="1" max="50" value="10"><p id="packet-result" aria-live="polite"></p><svg class="diagram" id="packet-plot" viewBox="0 0 600 200" role="img" aria-label="Position probability density for a Gaussian with adjustable width"><path d="M25 170H575" stroke="#b4c3b5"/><path id="packet-curve" fill="#e4eddf" stroke="#235c4e" stroke-width="2"/><text x="290" y="193" fill="#66756f" font-size="12">position x (nm)</text></svg><p class="fine">The plotted density is normalized; narrowing it increases its peak. Momentum spread is calculated from Δp = ℏ/(2Δx).</p></div>
<details class="example"><summary>Generated example · a uniform distribution</summary><p>For the uniform position density on \([0,L]\), \(\langle x\rangle=L/2\) and \(\langle x^2\rangle=L^2/3\). Thus \(\Delta x=L/\sqrt{12}\). Subtract the square of the mean; \(\sqrt{\langle x^2\rangle}\) alone is not the standard deviation.</p></details>
''')

section('The Schrödinger equation', 'Quantum reading map', [(Q, 30), (Q, 31)], r'''
<p class="lead">A nonrelativistic wavefunction evolves according to the kinetic-energy operator and the potential energy.</p>
<p class="scope-note">Reading-map topic · Notes §§5.6.2, 7.2–7.4; available lecture files stop at Week 9. This is not a claim of verified later lecture or quiz coverage.</p>
<div class="formula">\[i\hbar\frac{\partial\Psi}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2\Psi}{\partial x^2}+V(x)\Psi\]</div>
<p>For a time-independent potential, an energy eigenstate separates into a spatial function and a simple time factor:</p>
<div class="formula">\[\Psi_E(x,t)=\psi_E(x)e^{-iEt/\hbar},\qquad -\frac{\hbar^2}{2m}\frac{d^2\psi_E}{dx^2}+V(x)\psi_E=E\psi_E\]</div>
<h3>What “stationary” means</h3>
<p>The phase evolves, but its magnitude is one. Thus \(|\Psi_E(x,t)|^2=|\psi_E(x)|^2\) is independent of time. A superposition of different energies generally has relative phases that evolve at different rates and can produce time-dependent density.</p>
<h3>Check a proposed solution</h3>
<ol><li>Identify \(V(x)\) and where the candidate is defined.</li><li>Calculate its second derivative.</li><li>Substitute into the time-independent equation and check whether the same constant \(E\) works at every allowed position.</li><li>Check boundary conditions and normalization separately.</li></ol>
<details class="example"><summary>Generated example · free plane wave</summary><p>For \(V=0\), \(\psi=e^{ikx}\) has \(\psi''=-k^2\psi\). The equation gives \(E=\hbar^2k^2/(2m)=p^2/(2m)\). It is an ideal generalized eigenstate, not a normalizable localized state on the whole line.</p></details>
''')

section('Bound states & atomic spectra', 'Quantum reading map', [(Q, 34), (Q, 35)], r'''
<p class="lead">Boundary conditions and normalizability select allowed energies. Transitions between them produce spectral lines.</p>
<p class="scope-note">Reading-map topic · Notes §§8.2–8.4; selected OpenStax §§7.4, 6.4, 8.1. Later lecture coverage is not established by the files here.</p>
<h3>Particle in an infinite one-dimensional box</h3>
<p>Take \(V=0\) for \(0&lt;x&lt;L\) and infinite walls outside. Require \(\psi(0)=\psi(L)=0\). These conditions allow discrete standing waves:</p>
<div class="formula">\[\psi_n(x)=\sqrt{\frac{2}{L}}\sin\frac{n\pi x}{L},\qquad E_n=\frac{n^2\pi^2\hbar^2}{2mL^2}=\frac{n^2h^2}{8mL^2},\qquad n=1,2,\ldots\]</div>
<p>The ground state has positive energy. Setting \(n=0\) gives the identically zero function, not a normalized physical state. Doubling the well width reduces every energy by a factor of four.</p>
<h3>Hydrogen and spectral transitions</h3>
<div class="formula">\[E_n=-\frac{13.6\,\mathrm{eV}}{n^2},\qquad hf=\frac{hc}{\lambda}=|E_f-E_i|\]</div>
<p>The hydrogen formula uses the usual elementary hydrogen approximation and a zero at the ionization limit. Emission lowers the atomic energy; absorption raises it. An absorption line also requires an occupied initial level and an allowed transition; an energy difference alone does not guarantee line strength.</p>
<h3>Superpositions of energy eigenstates</h3>
<div class="formula">\[\Psi(x,t)=\sum_n c_n\psi_n(x)e^{-iE_nt/\hbar},\qquad \sum_n|c_n|^2=1\]</div>
<p>Energy measurements give \(E_n\) with probability \(|c_n|^2\) for an orthonormal eigenbasis. Position probabilities come from the magnitude squared of the entire sum, retaining interference terms.</p>
<details class="example"><summary>Generated example · hydrogen 3 → 2</summary><p>The emitted energy is \(13.6(1/4-1/9)=1.889\,\mathrm{eV}\). Thus \(\lambda\approx1240/1.889=656.5\,\mathrm{nm}\), with rounding from the constants.</p></details>
''')

section('Tunnelling through a barrier', 'Quantum reading map', [(Q, 37), ('final_formulas.pdf', 2)], r'''
<p class="lead">A wavefunction can penetrate a region where the total energy is below the potential, giving nonzero transmission through a finite barrier.</p>
<p class="scope-note">Reading-map topic · Notes §9.1 and OpenStax §7.6. Notes §§9.2–9.3 are optional extensions.</p>
<p>For a rectangular barrier of height \(V_0\), width \(d\), and incident energy \(E&lt;V_0\), the spatial equation inside the barrier has exponential solutions:</p>
<div class="formula">\[\kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar},\qquad \psi(x)=Ae^{\kappa x}+Be^{-\kappa x}\]</div>
<p>Both terms can be needed inside a finite barrier to satisfy matching conditions. A purely decaying term describes penetration into a semi-infinite forbidden region. The amplitude decay length is \(\ell=1/\kappa\).</p>
<div class="formula">\[T\sim e^{-2\kappa d}=e^{-2d/\ell}\]</div>
<p>This captures the leading exponential suppression for an opaque barrier, matching the simplified expression on the local formula sheet. The exact rectangular-barrier transmission has a prefactor and matching factors; do not treat the exponential alone as a universal exact result.</p>
<div class="note"><strong>Physical meaning.</strong> Transmission falls strongly with increased barrier width, particle mass, or height above the particle energy. In a static barrier, the transmitted particle has the same total energy as the incident particle; tunnelling does not supply extra energy to climb over the barrier.</div>
<h3>Applications</h3>
<p>Alpha decay involves escape through a nuclear potential barrier. Scanning tunnelling microscopes use the strong dependence of electron transmission on separation to resolve surface structure.</p>
''')

section('Terminology & formula map', 'Reference', [('final_formulas.pdf', 1)], r'''
<p class="lead">Recall each term from its definition, then work in the other direction: name the concept from the expression.</p>
<table><thead><tr><th>Term</th><th>Meaning / identifying relation</th></tr></thead><tbody>
<tr><td>Event</td><td>A spacetime occurrence with coordinates \((ct,x,y,z)\).</td></tr>
<tr><td>Lorentz factor</td><td>\(\gamma(v)=1/\sqrt{1-v^2/c^2}\); always name which speed.</td></tr>
<tr><td>Proper time</td><td>Elapsed time on the clock present at both events.</td></tr>
<tr><td>Proper length</td><td>Length of an object in its own rest frame.</td></tr>
<tr><td>Invariant</td><td>A quantity whose value does not change under a Lorentz transformation.</td></tr>
<tr><td>Four-momentum</td><td>\(P=(E/c,\mathbf p)\), transforms as a four-vector.</td></tr>
<tr><td>Rest / total / kinetic energy</td><td>\(E_0=mc^2\), \(E=\gamma mc^2\), \(K=E-E_0\).</td></tr>
<tr><td>System invariant mass</td><td>\(Mc^2=\sqrt{E_{\rm tot}^2-c^2p_{\rm tot}^2}\).</td></tr>
<tr><td>Binding energy</td><td>Positive energy needed to separate a bound system into specified constituents at rest far apart.</td></tr>
<tr><td>Intensity</td><td>Energy per unit area per unit time; units W/m².</td></tr>
<tr><td>Work function</td><td>Minimum photon energy for photoemission in the one-photon model.</td></tr>
<tr><td>Stopping potential</td><td>Retarding voltage magnitude satisfying \(e|V_s|=K_{\max}\).</td></tr>
<tr><td>Compton wavelength</td><td>\(h/(mc)\), a particle scale; distinct from the angle-dependent shift.</td></tr>
<tr><td>de Broglie wavelength</td><td>\(h/p\), for matter as well as photons.</td></tr>
<tr><td>Probability amplitude / density</td><td>\(\psi\) / \(|\psi|^2\); integrate the density to get a probability.</td></tr>
<tr><td>Eigenstate</td><td>A state giving a definite value of a specified observable.</td></tr>
<tr><td>Superposition</td><td>A linear combination of states; add amplitudes before calculating probability.</td></tr>
<tr><td>Expectation value</td><td>The ensemble mean, such as \(\langle x\rangle=\int x|\psi|^2dx\).</td></tr>
<tr><td>Uncertainty</td><td>Standard deviation, e.g. \(\Delta x=\sqrt{\langle x^2\rangle-\langle x\rangle^2}\).</td></tr>
<tr><td>Stationary state</td><td>An energy eigenstate with time-independent probability density.</td></tr>
<tr><td>Tunnelling</td><td>Transmission through a finite classically forbidden region.</td></tr>
</tbody></table>
<h3>Useful conversions</h3>
<div class="formula">\[c\approx3.00\times10^8\,\mathrm{m/s},\quad h\approx6.626\times10^{-34}\,\mathrm{J\,s},\quad \hbar\approx1.055\times10^{-34}\,\mathrm{J\,s}\]</div>
<div class="formula">\[1\,\mathrm{eV}\approx1.602\times10^{-19}\,\mathrm J,\quad hc\approx1240\,\mathrm{eV\,nm},\quad m_ec^2\approx511\,\mathrm{keV}\]</div>
<p>Use the precision requested by the course. The original formula sheet is available below and in the source library. The notation on this page is typeset anew; original previews preserve the supplied files.</p>
''', 'glossary vocabulary terminology formula constants units')


def esc(s):
    return html.escape(str(s), quote=True)


def source_url(path, page=None):
    return quote(path, safe='/') + (f'#page={page}' if page else '')


def original_previews(sources):
    parts = []
    for path, page in sources:
        with fitz.open(ROOT/path) as doc:
            pix = doc[page-1].get_pixmap(matrix=fitz.Matrix(1.35, 1.35), alpha=False)
            data = base64.b64encode(pix.tobytes('png')).decode()
        name = Path(path).name
        parts.append(f'<figure><a href="{source_url(path,page)}" target="_blank" rel="noopener">Open {esc(name)} · PDF page {page} ↗</a><img class="source-image" loading="lazy" src="data:image/png;base64,{data}" alt="Original {esc(name)}, PDF page {page}; open the linked PDF for selectable source text"><figcaption>{esc(path)} · PDF page {page} (PDF page numbers may differ from printed slide numbers)</figcaption></figure>')
    return '<details class="original"><summary>Original source pages · equations &amp; figures</summary>'+''.join(parts)+'</details>'


def library():
    groups = {}
    for path in sorted(ROOT.rglob('*.pdf')):
        rel = path.relative_to(ROOT).as_posix()
        if '/.' in rel:
            continue
        group = ('Lectures' if rel.startswith('Lecture material/Lectures/') else
                 'Tutorials' if '/Tutorials/' in rel or '/Original tutorial worksheets/' in rel or '/Week 01/' in rel else
                 'Textbooks & quantum notes' if path.name in ['PHYS200__Notes_on_Quantum-4.pdf','Helliwell - Special Relativity.pdf','OpenStax - University Physics Volume 3.pdf','knight-all.pdf','ch2-complex-numbers.pdf'] else
                 'Past exams' if '/Past exams/' in rel else
                 'Practice solutions' if '/Quantum solutions/' in rel or '/Relativity solutions/' in rel else
                 'Generated practice sets' if rel.startswith('output/pdf/') else 'Practice banks & formula sheets')
        groups.setdefault(group, []).append((rel, path.name))
    result = '<p>Original local files open in a new tab. Keep this HTML in the PHYS 200 directory for these links to work. The tutorial, math and embedded previews work offline by themselves.</p><p>Course scope: <a href="scope.txt" target="_blank" rel="noopener">scope.txt ↗</a>. Reading-map topics do not imply that every chapter in a linked textbook is assigned.</p>'
    for group, items in groups.items():
        result += f'<details class="library-group"><summary>{esc(group)} <span class="fine">· {len(items)} files</span></summary><ul>'
        for path, name in items:
            result += f'<li data-file-search="{esc(path.lower())}"><a href="{source_url(path)}" target="_blank" rel="noopener">{esc(name)} ↗</a><small>{esc(path)}</small></li>'
        result += '</ul></details>'
    return result


def build():
    ref = REFERENCE.read_text()
    css = re.search(r'<style>(.*?)@font-face', ref, re.S).group(1)
    css += r'''
    :root{--reading-width:1080px}html{scroll-behavior:smooth}h3{font:400 23px/1.3 Georgia,serif;margin:30px 0 12px}h4{font-size:13px;margin:0 0 8px}.content{font-size:calc(15px * var(--text-scale,1));padding:26px 32px 32px;line-height:1.75}.content p{margin:0 0 16px}.lead{font:400 23px/1.45 Georgia,serif;color:#284f42;margin-bottom:22px!important}.concept-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:20px 0}.concept-grid>div{padding:20px;border:1px solid var(--line);border-radius:8px;background:#f9faf5}.concept-grid p{margin:0;font-size:.94em}.formula{position:relative;background:#f5f7f1;border:1px solid #dfe7d9;border-radius:8px;padding:8px 16px;margin:20px 0;overflow-x:auto;cursor:copy}.formula:hover{border-color:#91aa92}.formula:focus-visible{outline:2px solid var(--accent);outline-offset:3px}.formula .katex-display{margin:10px 0}.katex{font-size:1.08em!important}.note,.scope-note{background:#faf5e9;border-left:3px solid var(--gold);padding:15px 18px;font-size:.93em;margin:22px 0}.scope-note{color:#78612d}.fine{font-size:11px;color:var(--muted)}details{border:1px solid var(--line);border-radius:8px;margin:20px 0;background:#fff}summary{cursor:pointer;padding:14px 18px;font-size:13px;font-weight:600}details[open]>summary{border-bottom:1px solid var(--line);margin-bottom:16px}details>p,details>ol,details>.formula{margin-left:18px!important;margin-right:18px!important}details>p:last-child{margin-bottom:18px}.original{background:#fbfcf9}.original figure{margin:16px;padding:12px;background:#fff;border:1px solid var(--line);border-radius:6px}.original figure>a{font-size:12px;color:var(--accent)}.source-image{margin-top:12px}.original figcaption{font-size:10px;color:var(--muted);margin-top:10px;overflow-wrap:anywhere}table{border-collapse:collapse;width:100%;font-size:.9em;margin:20px 0}th,td{text-align:left;vertical-align:top;padding:13px 14px;border-bottom:1px solid var(--line)}th{background:#edf2e9;color:#3d5a49}td:first-child{min-width:130px;font-weight:500}.table-wrap{overflow-x:auto}.diagram{width:100%;height:auto;max-height:330px;display:block;margin:18px auto}.interactive{border:1px solid #cbdcc5;background:#f7faf3;padding:20px;border-radius:8px;margin:24px 0}.interactive label{display:block;font-size:13px}.interactive input[type=range]{width:100%;accent-color:var(--accent);margin:18px 0}.interactive p:last-child{margin-bottom:0}.interactive output{font-weight:700}.source-line{line-height:1.6!important}.source-line a{color:var(--accent)}.source-tag{font-size:10px;letter-spacing:1px;color:#987634;margin-bottom:6px}.group-label{font-size:10px;color:#8d793f;text-transform:uppercase;letter-spacing:1.2px;margin:20px 9px 8px}.chapter-link{padding-top:9px;padding-bottom:9px}.toc-title{margin-bottom:12px}.library-link{width:100%;text-align:left;font-size:12px;margin-top:10px}.library-content{padding:10px 30px 30px}.library-group ul{list-style:none;padding:0 18px 10px}.library-group li{padding:10px 0;border-bottom:1px solid var(--line);font-size:13px}.library-group li:last-child{border:0}.library-group small{display:block;font-size:10px;color:var(--muted);overflow-wrap:anywhere}.header-actions a{font-size:12px}#status{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:var(--accent);color:white;border-radius:8px;padding:10px 18px;box-shadow:0 4px 20px #0002;z-index:20;font-size:13px;max-width:90vw}.copy-hint{max-width:var(--reading-width);margin:-8px auto 18px;font-size:11px;color:var(--muted)}.intro p{max-width:850px}.chapter-heading p{max-width:740px}.scope-pill{display:inline-block;background:#edf1e7;border-radius:12px;font-size:10px;padding:3px 9px;margin-top:10px}.empty-search{font-size:12px;color:var(--muted);padding:14px 6px}.chapter-footer button{font-size:12px}.header-actions button{font-size:12px}.chapter-heading{scroll-margin-top:15px}.library-head{display:flex;align-items:center;justify-content:space-between;padding:25px 30px;border-bottom:1px solid var(--line)}.library-head h2{font:400 27px Georgia;margin:0}.library-head button{font-size:12px}body.presentation .content{font-size:calc(19px * var(--text-scale,1))}body.presentation .chapter-heading h2{font-size:32px}body.presentation .original{display:none}.content ul,.content ol{padding-left:23px}.content li{margin:8px 0}.original summary{color:var(--accent)}.toolbar .left{flex-wrap:wrap}.toolbar .tools{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.toolbar .tools button{font-size:11px}button,a,input,select,summary{touch-action:manipulation}.noscript{padding:20px;background:#faf5e9;color:#193d37}.nav-collapsed aside{display:none}.content a:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
    @media(max-width:850px){.content{padding:18px 18px 24px;font-size:calc(14px * var(--text-scale,1))}.lead{font-size:21px}.concept-grid{grid-template-columns:1fr}.chapter-heading{flex-wrap:wrap}.review-button{max-width:none}.header-actions{flex-wrap:wrap}.toolbar .tools{gap:6px}.formula{padding:7px 10px}h3{font-size:21px}.library-content{padding:12px 16px}.library-head{padding:20px 16px}th,td{padding:10px;min-width:115px}.intro h1{font-size:36px}.source-tag{font-size:9px}.chapter-heading h2{font-size:25px}.original figure{margin:10px;padding:8px}}
    @media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
    @media print{.original,.interactive,.copy-hint,#status,.example>summary{display:none!important}.content{font-size:11pt;padding:10px 0}.content .lead{font-size:16pt}.formula{break-inside:avoid}.concept-grid{break-inside:avoid}.chapter-heading{display:block}.source-line{font-size:9pt!important}article{break-before:page}h3{break-after:avoid}.content details[open]{border:0}.content table{font-size:9pt}.scope-pill{display:none}body.presentation .content{font-size:11pt}}
    '''
    nav, articles, index = [], [], []
    last_group = None
    for number, s in enumerate(SECTIONS, 1):
        if s['group'] != last_group:
            nav.append(f'<div class="group-label">{esc(s["group"])}</div>')
            last_group = s['group']
        nav.append(f'<a class="chapter-link" href="#chapter-{number}" data-chapter="{number}"><span class="chapter-number">{number:02}</span><span class="chapter-name">{esc(s["title"])}</span><span class="chapter-tick" aria-hidden="true"></span></a>')
        source_links = ' · '.join(f'<a href="{source_url(path,page)}" target="_blank" rel="noopener">{esc(Path(path).name)} · PDF p. {page} ↗</a>' for path, page in s['sources'])
        body = re.sub(r'(<table>.*?</table>)',r'<div class="table-wrap">\1</div>',s['body'],flags=re.S)
        articles.append(f'''<article id="chapter-{number}" data-chapter="{number}" aria-labelledby="title-{number}"><div class="chapter-heading"><div><div class="eyebrow">{esc(s['group'])} · {number:02} / {len(SECTIONS):02}</div><h2 id="title-{number}">{esc(s['title'])}</h2><p class="source-line">{source_links}</p></div><button class="review-button" type="button" aria-pressed="false">Mark reviewed</button></div><div class="content">{body}{original_previews(s['sources'])}</div><div class="chapter-footer"><span>PHYS 200 · Course review</span><button class="continue" data-next="{min(number+1,len(SECTIONS))}" {'disabled' if number==len(SECTIONS) else ''}>Next section →</button></div></article>''')
        text = re.sub('<[^>]+>', ' ', s['body'])
        index.append(dict(number=number,title=s['title'],group=s['group'],search=html.unescape(s['title']+' '+s['group']+' '+s['tags']+' '+text).lower()))
        print(f'Built {number:02} {s["title"]}',flush=True)
    count = len(SECTIONS)
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="PHYS 200 relativity and quantum physics study companion, built from local lectures, tutorials, quantum notes and course scope."><title>PHYS 200 · Review &amp; Summary</title><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='32' fill='%23235c4e'/%3E%3Ctext x='32' y='46' text-anchor='middle' fill='white' font-size='46' font-family='serif'%3Eφ%3C/text%3E%3C/svg%3E"><style>{css}</style>__MATH_CSS__</head><body>
<a class="skip" href="#reader">Skip to tutorial</a>
<header><div class="brand"><span class="brand-mark" aria-hidden="true">φ</span><div><strong>PHYS 200</strong><small>Relativity &amp; quanta · Study companion</small></div></div><div class="header-actions"><button id="library-button" type="button">Source library ↗</button><button type="button" id="toc-toggle" aria-expanded="true" aria-controls="sidebar">Hide chapters</button><label for="view">View</label><select id="view" aria-label="Reading view"><option value="chapter">Chapter</option><option value="all">All chapters</option><option value="presentation">Presentation</option></select><button id="print" type="button">Print</button></div></header>
<div class="layout"><aside id="sidebar" aria-label="Chapter navigation"><div class="toc-title"><strong>Contents</strong><span class="eyebrow">{count} sections</span></div><label class="eyebrow" for="search">Find a chapter or concept</label><input type="search" id="search" placeholder="Search, e.g. momentum" autocomplete="off"><div id="search-count" aria-live="polite">All sections</div><nav>{''.join(nav)}</nav><p id="empty" class="empty-search" hidden>No sections match. Try a shorter term.</p><button class="library-link" id="library-nav" type="button">Browse original course files ↗</button><div class="progress"><span id="progress-label">0 of {count} sections reviewed</span><progress id="progress" max="{count}" value="0" aria-label="Review progress"></progress><p>Saved in this browser. A review check is a reading marker, not a practice result.</p></div></aside>
<main id="reader" tabindex="-1"><div class="intro"><div class="eyebrow">Course notes / lectures / worked ideas</div><h1>Review &amp; Summary</h1><p>A guided companion to the PHYS 200 materials in this directory. Relativity, light and quantum states, with typeset equations and original source previews. The later quantum sections follow the reading map in <a href="scope.txt" target="_blank" rel="noopener">scope.txt</a>.</p><span class="scope-pill">Lectures: Weeks 1–9 · Quantum Notes v2 · {count} review sections</span></div>
<div class="toolbar"><div class="left"><button id="previous" type="button" aria-label="Previous section">←</button><small id="position">Section 1 of {count}</small><button id="next" type="button" aria-label="Next section">→</button></div><div class="tools"><button id="copy-chapter" type="button">Copy text</button><button id="details-toggle" type="button" aria-expanded="false">Show source pages</button><div class="zoom"><button id="zoom-out" type="button" aria-label="Decrease text size">−</button><output id="zoom-label" aria-live="polite">100%</output><button id="zoom-in" type="button" aria-label="Increase text size">+</button></div></div></div>
<p class="copy-hint" id="keyboard-hint">← / → to navigate · Double-click a formula to copy its notation · Original pages expand below each section</p>
<noscript><p class="noscript">JavaScript is disabled. All tutorial sections remain readable below. Navigation controls and saved progress require JavaScript.</p></noscript>
{''.join(articles)}
<section id="library" hidden><div class="library-head"><h2>Source library</h2><button id="close-library" type="button">Back to tutorial</button></div><div class="library-content"><label class="eyebrow" for="file-search">Find a source file</label><input id="file-search" type="search" placeholder="Search file names or folders"><p id="file-count" class="fine" aria-live="polite"></p>{library()}</div></section>
<footer>Built from the local PHYS 200 collection · Scope snapshot: 13 November 2026 · Summaries and generated examples are newly written; embedded source pages are original. Review markers do not update the practice log. Math typeset with KaTeX (MIT).</footer></main></div><div id="status" role="status" hidden></div>
<script id="search-data" type="application/json">{json.dumps(index).replace('</','<\\/')}</script>
<script>__SCRIPT__</script></body></html>'''
    script = r'''
    (()=>{'use strict';
    const $=s=>document.querySelector(s), articles=[...document.querySelectorAll('article')], links=[...document.querySelectorAll('.chapter-link')], index=JSON.parse($('#search-data').textContent), total=articles.length;
    const store={get(key,fallback){try{return JSON.parse(localStorage.getItem('phys200-reader-'+key))??fallback}catch{return fallback}},set(key,value){try{localStorage.setItem('phys200-reader-'+key,JSON.stringify(value))}catch{}}};
    let current=1, mode='chapter', reviewed=new Set(store.get('reviewed',[]).filter(n=>Number.isInteger(n)&&n>=1&&n<=total)), zoom=1, libraryOpen=false, mobileOpen=false, desktopCollapsed=store.get('nav-collapsed',false);
    const media=matchMedia('(max-width:850px)');
    function toast(message){$('#status').textContent=message;$('#status').hidden=false;clearTimeout(toast.timer);toast.timer=setTimeout(()=>$('#status').hidden=true,2400)}
    function navigation(){const expanded=mode!=='presentation'&&(media.matches?mobileOpen:!desktopCollapsed);$('#sidebar').hidden=!expanded;document.body.classList.toggle('nav-collapsed',!expanded);$('#toc-toggle').hidden=mode==='presentation';$('#toc-toggle').setAttribute('aria-expanded',String(expanded));$('#toc-toggle').textContent=expanded?'Hide chapters':'Show chapters'}
    function syncSources(){const visible=articles.filter(a=>!a.hidden), boxes=visible.flatMap(a=>[...a.querySelectorAll('details.original')]), opened=boxes.length>0&&boxes.every(d=>d.open);$('#details-toggle').textContent=opened?'Hide source pages':'Show source pages';$('#details-toggle').setAttribute('aria-expanded',String(opened))}
    function show(n,scroll=true){current=Math.max(1,Math.min(total,Number(n)||1));libraryOpen=false;$('#library').hidden=true;$('.toolbar').hidden=false;$('#keyboard-hint').hidden=mode==='all';document.body.classList.toggle('presentation',mode==='presentation');navigation();for(const a of articles)a.hidden=mode!=='all'&&Number(a.dataset.chapter)!==current;for(const link of links){if(Number(link.dataset.chapter)===current)link.setAttribute('aria-current','page');else link.removeAttribute('aria-current')}$('#position').textContent=`Section ${current} of ${total}`;$('#previous').disabled=current===1;$('#next').disabled=current===total;try{history.replaceState(null,'',`#chapter-${current}`)}catch{}document.title=index[current-1].title+' · PHYS 200';syncSources();if(scroll){if(mode==='all')articles[current-1].scrollIntoView({block:'start'});else window.scrollTo({top:0,behavior:'instant'})}}
    function updateProgress(){for(const a of articles){const n=Number(a.dataset.chapter),done=reviewed.has(n),button=a.querySelector('.review-button');button.setAttribute('aria-pressed',String(done));button.textContent=done?'✓ Reviewed':'Mark reviewed';links[n-1].querySelector('.chapter-tick').textContent=done?'✓':''}$('#progress').value=reviewed.size;$('#progress-label').textContent=`${reviewed.size} of ${total} sections reviewed`}
    links.forEach(link=>link.addEventListener('click',e=>{e.preventDefault();show(link.dataset.chapter);if(media.matches){mobileOpen=false;navigation()}}));
    articles.forEach(a=>a.querySelector('.review-button').addEventListener('click',()=>{const n=Number(a.dataset.chapter);reviewed.has(n)?reviewed.delete(n):reviewed.add(n);store.set('reviewed',[...reviewed]);updateProgress()}));
    document.querySelectorAll('.continue').forEach(b=>b.addEventListener('click',()=>show(b.dataset.next)));
    $('#previous').addEventListener('click',()=>show(current-1));$('#next').addEventListener('click',()=>show(current+1));$('#view').addEventListener('change',e=>{mode=e.target.value;show(current)});$('#print').addEventListener('click',()=>window.print());
    $('#toc-toggle').addEventListener('click',()=>{if(media.matches)mobileOpen=!mobileOpen;else{desktopCollapsed=!desktopCollapsed;store.set('nav-collapsed',desktopCollapsed)}navigation()});media.addEventListener('change',()=>{mobileOpen=false;navigation()});
    const normalize=s=>s.toLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g,'').replace(/schroedinger/g,'schrodinger');
    $('#search').addEventListener('input',e=>{const terms=normalize(e.target.value).trim().split(/\s+/).filter(Boolean);let count=0;links.forEach((link,i)=>{const match=terms.every(t=>normalize(index[i].search).includes(t));link.hidden=!match;if(match)count++});$('#search-count').textContent=terms.length?`${count} matching section${count===1?'':'s'}`:'All sections';$('#empty').hidden=count!==0;document.querySelectorAll('.group-label').forEach(label=>{let node=label.nextElementSibling,visible=false;while(node&&!node.matches('.group-label')){if(!node.hidden)visible=true;node=node.nextElementSibling}label.hidden=!visible})});
    function setZoom(n){zoom=Math.max(.85,Math.min(1.5,Math.round(n*100)/100));document.documentElement.style.setProperty('--text-scale',zoom);$('#zoom-label').textContent=`${Math.round(zoom*100)}%`;$('#zoom-out').disabled=zoom<=.85;$('#zoom-in').disabled=zoom>=1.5;store.set('zoom',zoom)}$('#zoom-in').addEventListener('click',()=>setZoom(zoom+.1));$('#zoom-out').addEventListener('click',()=>setZoom(zoom-.1));
    async function copy(text){try{await navigator.clipboard.writeText(text);toast('Copied to clipboard')}catch{const f=document.createElement('textarea');f.value=text;f.style.cssText='position:fixed;left:-9999px';document.body.append(f);f.select();const ok=document.execCommand('copy');f.remove();toast(ok?'Copied to clipboard':'Select the text, then copy it with your keyboard')}}
    $('#copy-chapter').addEventListener('click',()=>{const clone=articles[current-1].cloneNode(true);clone.querySelectorAll('.original,.interactive,button,.chapter-footer').forEach(x=>x.remove());clone.querySelectorAll('.katex').forEach(k=>k.replaceWith(k.querySelector('annotation')?.textContent||k.textContent));clone.querySelectorAll('.formula').forEach(k=>k.replaceWith('\n'+k.dataset.formula+'\n'));copy(clone.textContent.replace(/\n\s*\n/g,'\n\n').trim())});
    document.querySelectorAll('.formula').forEach(f=>{f.tabIndex=0;f.setAttribute('role','button');f.setAttribute('aria-label','Copy formula: '+f.dataset.formula);f.title='Double-click to copy formula notation';f.addEventListener('dblclick',()=>copy(f.dataset.formula));f.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();copy(f.dataset.formula)}})});
    $('#details-toggle').addEventListener('click',()=>{const open=$('#details-toggle').getAttribute('aria-expanded')!=='true';articles.filter(a=>!a.hidden).forEach(a=>a.querySelectorAll('details.original').forEach(d=>d.open=open));syncSources()});document.querySelectorAll('details.original').forEach(d=>d.addEventListener('toggle',syncSources));
    function openLibrary(){libraryOpen=true;document.body.classList.remove('presentation');articles.forEach(a=>a.hidden=true);$('#library').hidden=false;$('.toolbar').hidden=true;$('#keyboard-hint').hidden=true;window.scrollTo({top:0,behavior:'instant'});$('#file-search').focus()}
    $('#library-button').addEventListener('click',openLibrary);$('#library-nav').addEventListener('click',()=>{openLibrary();if(media.matches){mobileOpen=false;navigation()}});$('#close-library').addEventListener('click',()=>show(current));
    const fileItems=[...document.querySelectorAll('[data-file-search]')];$('#file-count').textContent=`${fileItems.length} local PDF files`;$('#file-search').addEventListener('input',e=>{const terms=normalize(e.target.value).trim().split(/\s+/).filter(Boolean);let count=0;fileItems.forEach(li=>{li.hidden=!terms.every(t=>normalize(li.dataset.fileSearch).includes(t));if(!li.hidden)count++});document.querySelectorAll('.library-group').forEach(d=>{d.hidden=![...d.querySelectorAll('li')].some(li=>!li.hidden);if(terms.length)d.open=!d.hidden});$('#file-count').textContent=`${count} matching file${count===1?'':'s'}`});
    document.addEventListener('keydown',e=>{if(e.target.closest('input,select,textarea,button,summary,[role=button]')||e.ctrlKey||e.altKey||e.metaKey||e.shiftKey||getSelection()?.isCollapsed===false||mode==='all'||libraryOpen)return;if(e.key==='ArrowRight'){e.preventDefault();show(current+1)}if(e.key==='ArrowLeft'){e.preventDefault();show(current-1)}});
    window.addEventListener('hashchange',()=>{const m=location.hash.match(/^#chapter-(\d+)$/);if(m)show(m[1])});
    function boost(){const b=Number($('#boost').value)/100,g=1/Math.sqrt(1-b*b);$('#boost-value').textContent=b.toFixed(2);$('#boost-result').textContent=`u′x = ${(-b).toFixed(2)}c and γ(v) = ${g.toFixed(3)}`};$('#boost').addEventListener('input',boost);boost();
    function temperature(){const t=Number($('#temperature').value),nm=2.898e6/t;$('#temperature-value').textContent=t+' K';$('#temperature-result').textContent=`Peak wavelength: ${nm.toFixed(0)} nm · Total power: ${(t/5800)**4<.01?((t/5800)**4).toFixed(4):((t/5800)**4).toFixed(2)} × the 5800 K value.`};$('#temperature').addEventListener('input',temperature);temperature();
    function packet(){const sigma=Number($('#packet').value)/10;$('#packet-value').textContent=sigma.toFixed(1)+' nm';$('#packet-result').textContent=`For Δx = ${sigma.toFixed(1)} nm, minimum Δp = ${(1.054571817e-34/(2*sigma*1e-9)).toExponential(3)} kg·m/s.`;let d='M25 170';for(let i=0;i<=550;i++){const x=(i-275)/27.5,rho=Math.exp(-x*x/(2*sigma*sigma))/(Math.sqrt(2*Math.PI)*sigma);d+=`L${25+i} ${170-35*rho}`}d+='L575 170Z';$('#packet-curve').setAttribute('d',d)};$('#packet').addEventListener('input',packet);packet();
    // Expand generated examples for print, then restore their original disclosure state.
    let printState=[];addEventListener('beforeprint',()=>{printState=[...document.querySelectorAll('.example')].map(d=>[d,d.open]);printState.forEach(([d])=>d.open=true)});addEventListener('afterprint',()=>printState.forEach(([d,open])=>d.open=open));
    updateProgress();setZoom(Number(store.get('zoom',1))||1);const initial=location.hash.match(/^#chapter-(\d+)$/);show(initial?initial[1]:1,false);
    })();
    '''
    # Keep the exact original TeX on display blocks for accessible formula copying.
    def formula_attr(m):
        raw = re.sub(r'^\s*\\\[|\\\]\s*$', '', m.group(1)).strip()
        return '<div class="formula" data-formula="'+esc(raw)+'">'+m.group(1)+'</div>'
    page = re.sub(r'<div class="formula">(.*?)</div>',formula_attr,page,flags=re.S)
    page = page.replace('__SCRIPT__',script)
    # Render every equation before delivery; no runtime math library is necessary.
    render_js = r'''
    const fs=require('fs'), katex=require(process.argv[1]);
    let input=fs.readFileSync(0,'utf8');
    const decode=s=>s.replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&amp;/g,'&').replace(/&#x27;/g,"'").replace(/&quot;/g,'"');
    input=input.replace(/\\\[([\s\S]*?)\\\]/g,(_,s)=>katex.renderToString(decode(s),{displayMode:true,throwOnError:true,output:'htmlAndMathml'}));
    input=input.replace(/\\\(([\s\S]*?)\\\)/g,(_,s)=>katex.renderToString(decode(s),{displayMode:false,throwOnError:true,output:'htmlAndMathml'}));
    process.stdout.write(input);
    '''
    # Restrict typesetting to markup before the JSON/script block.
    markup, scripts = page.split('<script id="search-data"',1)
    result = subprocess.run(['node','-e',render_js,str(MATH/'katex.cjs')],input=markup,text=True,capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr[:6000])
    rendered = result.stdout
    katex_css = (MATH/'katex.min.css').read_text()
    # Keep only WOFF2 sources; each font is embedded to make the page standalone.
    katex_css = re.sub(r'src:url\(([^)]+\.woff2)\) format\("woff2"\)[^;]*;',r'src:url(\1) format("woff2");',katex_css)
    def embed_font(m):
        path = MATH / m.group(1)
        mime = 'font/woff2' if path.suffix=='.woff2' else 'application/octet-stream'
        return 'url(data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode()+')'
    katex_css = re.sub(r'url\((fonts/[^)]+)\)',embed_font,katex_css)
    math_license = '<!-- KaTeX license\n'+(MATH/'LICENSE').read_text()+'\n-->'
    page = (rendered+'<script id="search-data"'+scripts).replace('__MATH_CSS__',math_license+'<style>'+katex_css+'</style>')
    OUT.write_text(page)
    (Path(__file__).parent/'tutorial_sections.json').write_text(json.dumps(SECTIONS,indent=2,ensure_ascii=False))
    print(f'Saved {OUT} ({OUT.stat().st_size/1024/1024:.1f} MB)',flush=True)


if __name__=='__main__':
    build()
