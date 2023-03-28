# Self-study guide for the 1st lecture of the course “Superconducting quantum technologies”

## Introduction to the subject

1. Read the course specification

2. Find additional materials in the course folder

## Cavity QED with natural atoms

Find definitions for the following terms and write them down in your notebook

- Optical cavity

- Microwave cavity

- Cavity QED

- Circuit QED

## Two-level systems and qubits. Different qubit realizations

Find answers for the following questions

1. What is a qubit?

2. Examples of natural qubits?

3. Examples of physical platforms for artificial qubits?

4. What is the difference between a ground and an excited state of a qubit? Mathematical notations for a ground and excited state of qubit?

5. How many qubits are needed to make the following state $\vert 1001\rangle$?

6. When a spin $\frac{1}{2}$ is used to make a qubit, what is its ground state and excited state?

7. When a Rydberg atom is used to make a qubit, what is its ground state and excited state?

8. When a particle in a double-well potential is used to make a qubit, what is its ground state and excited states?

9. List all the popular types of superconducting qubits.

10. Consider charge qubits, flux qubits and phase qubits as examples. In each case, explain what physical quantity is quantized and what is the value of one quantum.

11. Looking at the slide “Superconducting quantum systems”, write down a typical dimension of a single superconducting qubit and of its smallest part, a single Josephson junction.

## Tools of quantum mechanics

1. What is the physical meaning of the squared magnitude of a wave function?

2. Make sure you understand what is a quantum operator? What  is the physical meaning of the expectation value for the quantum operator?

3. Can you write down matrix representation of the wavefunction $\vert 3\rangle$ in a number basis?

4. Can you write down matrix representation of an operator that swaps  $\vert \psi_1\rangle$ and  $\vert \psi_2\rangle$ in the basis $\{\vert\psi_1\rangle,\vert\psi_2\rangle\}$? Find eigenstates and eigenvalues of that operator.

## The Hamiltonians of a two-level system and the wavefunction. Bloch sphere

1. Write down a Hamiltonian of a two-level system in its eigenbasis. What is its eigenbasis? What are its eigenenergies?

2. Repeat the steps from the slides that convert one general representation of a two-level system wavefunction $\vert \Psi\rangle =\alpha\vert 0\rangle+\beta\vert 1\rangle$ to the other $\vert\Psi\rangle=\cos\frac{\theta}{2}\vert 0\rangle+e^{i\varphi}\sin\frac{\theta}{2}\vert 1\rangle$.

3. Learn how to map any arbitrary two-level system wavefunction to a point on the Bloch sphere. Compute coordinates on the sphere for the following states: $\vert 0\rangle$, $\vert 1\rangle$, $\frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}}$, $\frac{\vert 0\rangle - \vert 1\rangle}{\sqrt{2}}$,  $\frac{\vert 0\rangle + i\vert 1\rangle}{\sqrt{2}}$.

4. Learn how to write down a two-level system Hamiltonian with Pauli matrices.

## Double-well potential and the single electron charge qubit

In semiconductor systems, a single-electron charge qubit can be defined in a double quantum dot (DQD), in which one electron occupies the ground state of one dot or the other. See for example Toshimasa Fujisawa et al 2006 Rep. Prog. Phys. 69 759

1. In a case when ground states of both quantum dots are degenerate, write down a Hamiltonian that allows for tunneling of an electron between two quantum dots with frequency $\Delta$. Find eigenstates and eigenenergies of the Hamiltonian.

2. Degeneracy can be lifted by applying external electric field. In this case, energy difference $\varepsilon=eEd$ occurs between energies of the ground states in these quantum dots. Write down a Hamiltonian for this case and find its eigenenergies and eigenstates.

## Eigenstates and eigenenergies of a two-level system

Consider the Hamiltonian from the previous section.

1. Draw a graph of energy levels as a function of energy difference $\varepsilon$.

2. Compare ground states of the Hamiltonians with $\varepsilon=0$ and $\varepsilon \neq 0$. In which case an electron tends to localize in one quantum well?

3. Find an evolution operator for a case when $\varepsilon >0$ and $\Delta=0$. Using the evolution operator, compute evolution of both basis states $\vert 0\rangle$ and $\vert 1\rangle$ in such system. Does the population (that is probability) of these states changes with time?

4. Find an evolution operator for a case when $\varepsilon=0$ and $\Delta>0$. Using the evolution operator, compute evolution of both basis states $\vert 0\rangle$ and $\vert 1\rangle$ in such system. How long will it take for the system to change its state from $\vert 0\rangle$ to $\vert 1\rangle$? From $\vert 0\rangle$ to $\frac{\vert 0\rangle + i\vert 1\rangle}{\sqrt{2}}$?

5. Propose a method to control a relative phase $\varphi$ in $\vert\Psi\rangle=\cos\frac{\theta}{2}\vert 0\rangle+e^{i\varphi}\sin\frac{\theta}{2}\vert 1\rangle$.
