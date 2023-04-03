# Self-study guide for the 2nd lecture of the course "Superconducting quantum technologies"

## Superconductivity. Josephson junction. Josephson energy

Knowing basic facts from the superconductivity theory is crucial for
understanding how superconducting quantum circuits work. Try to answer
the following questions using information from the slides, books and the
internet.

1. What is a normal metal and what is a superconductor?

2. Name at least three metals that become superconducting at low
   temperatures. For each material, find its critical temperature
   $T_{C}$ at which it transitions from a normal metal to a
   superconductor.

3. What is a Cooper pair? Who is Cooper? What holds two electrons
   together?

4. What is a spin of an electron? Which possible values of a spin can a
   Cooper pair have? Is it a boson or a fermion? Which value does it
   take in conventional superconductors?

5. What is a Fermi energy in normal metals? At which energies do
   electrons sit in normal metals?

6. At what energy do Cooper pairs sit in a superconductor?

7. What is a quasiparticle in a superconductor? What is a
   superconducting gap? Does it take energy $\Delta$ or $2\Delta$ to
   break a Cooper pair into a non-coherent pair of electrons?

8. What values can magnetic flux take in a closed loop of a
   superconducting wire? What will happen with the flux through the
   loop when external magnetic field changes?

9. Write a wave function for a condensate of Cooper pairs in a
   superconductor. What is the meaning of its magnitude squared?

10. Since the wave function is a complex function, does its phase mean
    anything? Is it connected somehow with quantization of magnetic flux
    in a closed superconducting loop?

11. Consider a superconducting loop that breaks in one place with an
    insulator junction of thickness $a$. External magnetic flux is 0.
    Since superconducting wavefunction may enter insulator by some
    depth, for a small Josephson junction, a general form of
    wavefunction inside an insulator is
    $\Psi = A\cosh{\kappa x} + B\sinh{\kappa x}$. Using the boundary
    conditions on the left bank
    $\Psi\left( - \frac{a}{2} \right) = \sqrt{n_{s}}e^{- i\frac{\Delta\varphi}{2}}$
    and on the right bank
    $\Psi\left( \frac{a}{2} \right) = \sqrt{n_{s}}e^{i\frac{\Delta\varphi}{2}}$,
    obtain A and B coefficients. After that calculate superconducting
    current through a Josephson junction using the current equation from
    quantum mechanics
    $I = - i2e\frac{\hslash}{2m}\left( \Psi^{*}\frac{\partial}{\partial x}\Psi - \Psi\frac{\partial}{\partial x}\Psi^{*}\  \right)$.

12. Derive a formula for the Josephson energy, by computing how much
    work is done by switching a superconducting current through a
    Josephson junction.

13. Plot Josephson energy versus phase difference on a Josephson
    junction.

## Charging energy

Charging energy is the energy needed to keep an extra electron on a
neutral conducting island.

1. Using formulas from the slide, calculate charging energy
   $E_{C} = \frac{e^{2}}{2C}$ for a sphere with radius $a = 1\ \mu$m.
   Calculate typical thermal fluctuation at $T = 1\ K$. Compare $E_{C}$
   with $k_{B}T$.

2. Look at the comparison table of charging energies for different
   sizes of a sphere. Do not look at the bottom of the slide and try
   explain it yourself why low temperatures and nanostructures are
   needed to make qubits.

## The Cooper pair box. Electrostatic energies

1. Find an energy needed to keep $N$ extra Cooper pairs on a
   superconducting island. Draw an energy spectrum of a superconducting
   island taking into account quantization of an island energy due to
   an integer number of extra Cooper pairs.

2. What is the new definition for the charging energy in the case of a
   superconducting island?

3. Write an operator in the Dirac notation for the charge of a
   superconducting island. Take into account that an island not only
   can have extra Cooper pairs but also can lack them.

4. Using the charge operator, write down a Hamiltonian for a
   superconducting island.

5. Looking at the scheme of a Cooper-pair box with applied gate voltage
   $V_{g}$, write down an expression for the energy of a neutrally
   charged island. Assume that $C_{g} \ll C$. Draw a graph of this
   energy versus the gate voltage $V_{g}$.

6. In the case of an island initially charged with $Q = 2eN$, write a
   corrected expression for its energy. On the same plot draw a few
   graphs of the island potential energy versus
   $n_{g} = \frac{C_{g}V_{g}}{2e}$ for various initial charges.

7. What is a quantum mechanical Hamiltonian for a superconducting
   island with applied gate voltage?

## Quantum mechanics of electric circuits

1. Flux $\Phi$ and charge $Q$ are two conjugate variables when it comes
   to electric circuits. How to express an electric charge of a
   capacitance in terms of magnetic flux? How to express magnetic flux
   through an inductive element in terms of an electric charge?

2. In quantum mechanics coordinate and momentum are two conjugate
   variables with a canonical commutation relation
   $\left\lbrack \widehat{x},\widehat{p} \right\rbrack = i\hslash$.
   Does the same commutation relation apply to charge and flux
   observables? Which variable would be an alias for a coordinate, a
   momentum, a mass of a particle? What would be a kinetic energy?

3. Chose an approach when flux is a coordinate and charge is a
   momentum. Find their dimensionless variants $\widehat{\varphi}$ and
   $\widehat{N}$. Write their commutation relation.

4. For a circuit with a capacitance and a Josephson junction write a
   quantized Hamiltonian. Which term is related to the potential energy
   and which to the kinetic energy?

5. When a flux basis $\{|\phi\rangle\}$ is chosen, how will flux and
   charge operators act on a vector $|\phi\rangle$ from the basis?

6. When a charge basis $\{|N\rangle\}$ is chosen, how will charge
   operator act on a vector $|N\rangle$ from the basis? It is not
   trivial to write a flux operator in a discrete charge basis. Find
   how an operator $e^{i\widehat{\varphi}}$ acts on a vector
   $|N\rangle$. After that, find an expression for
   $\cos\widehat{\varphi}$.

7. You already know a matrix representation for a charge operator
   $\widehat{N}$ in the charge basis. What is a matrix representation
   for $\cos\widehat{\varphi}$ in this basis?

## Hamiltonian of the Cooper-pair box

1. In the previous section you wrote a quantized Hamiltonian for a
   circuit made of a capacitance and a Josephson junction. Rewrite this
   Hamiltonian with Dirac notation. Write the Hamiltonian as a trimmed
   matrix which acts on vectors from the charge basis $\{|N\rangle\}$.

2. In the homework assignment, you will be asked to model the energy
   spectrum of the Hamiltonian as a function of gate charge
   $n = \frac{C_{g}V_{g}}{2e}$. Looking at the result spectrum on the
   slides, find the splitting in the spectrum caused by adding a
   Josephson junction to a Cooper-pair box.

3. From the energy spectrum it follows that a Cooper-pair box can stay
   in its ground state even if $n$ would change. It means that the
   number of Cooper pairs can change on the superconducting island.
   Through what channel do they tunnel from the reservoir to the
   island?

## The Charge qubit

1. We can trim the matrix of the Hamiltonian by choosing two quantum
   states that are close to each other around the $n = \frac{1}{2}$
   point. Think what is the condition for such approximation?

2. Using the trimmed Hamiltonian, find the value of the energy level
   splitting? Compare the Hamiltonian, its eigenenergies and
   eigenstates with the one from the end of the first lecture.

## First qubit demonstration\*

\* Advanced part of the lecture

Briefly read the article *Y. Nakamura, Yu. A. Pashkin, and J. S. Tsai.
\"Coherent control of macroscopic quantum states in a single-Cooper-pair
box", Nature 398, 786 (1999)*. This article was the first to report
observation of quantum oscillations in a superconducting qubit, namely a
Cooper-pair box or charge qubit.

Answer the following questions by searching information in the text.
Questions may have multiple right answers. Use the slides of the lecture
to aid understanding the paper.

1. What is a single-Cooper-pair box?
   
   a.  A nanometer-scale semiconductor device
   
   b.  A superconducting electrode connected to a reservoir via a
   
       Josephson junction
   
   c.  A quantum dot containing a single electron
   
   d.  A two-level system in a nuclear spin quantum computer

2. What is a Josephson junction and how is it important in the
   functioning of a single-Cooper-pair box?

3. How many electrons does the Cooper-pair box contain?
   
   a.  Only one
   
   b.  A few hundred
   
   c.  A large number
   
   d.  It varies depending on the gate voltage

4. What is the role of the gate voltage in the Cooper-pair box?
   
   a.  It changes the number of electrons in the box
   
   b.  It controls the size of the box
   
   c.  It changes the relative energy of the two lowest-energy states
   
   d.  It reduces the single-electron charging energy of the box

5. What happens when a short voltage pulse is applied to the pulse
   gate?
   
   a.  The Cooper pairs tunnel through the Josephson junction
   
   b.  The electrostatic energies of the charge states change
   
   c.  The two charge states become degenerate
   
   d.  The wavefunction coherently evolves between $|0\rangle$ and
   
       $|2\rangle$

6. How is the resulting state detected?
   
   a.  By measuring the rise and fall times of the pulse
   
   b.  By measuring the current through a probe junction
   
   c.  By measuring the electrostatic energies of the charge states
   
   d.  By measuring the single-electron charging energy of the box

7. What is the superconductivity gap?
   
   a.  The energy difference between the two lowest-energy states
   
   b.  The energy required for Cooper pairs to tunnel through the
   
       Josephson junction
   
   c.  The energy required to create a highly resistive probe junction
   
   d.  The energy of the quasiparticles in the excited states

8. Explain what is seen in Fig. 1(a). What material corresponds to the
   black color and what corresponds to the grey color structures? Find
   two Josephson junctions that connect the box to the reservoir.
