# Quantum Galton Board  
*Ipsita Sinha – July 2025*

---

## Introduction

Our first step was to implement the given circuit for the first layer and verify the results by plotting the measurements obtained from **qubit 1** and **qubit 3**.

As mentioned in the paper, we introduce:

- 4 qubits (including ancillary qubits),
- and 2 classical bits for measurement.

---

We apply the following operations:

- A **Hadamard gate** on the ancillary qubit,
- An **X gate** on qubit 2 — this implies the ball is placed on the board.

To trace the **trajectory** of the ball (left or right), we use the ancillary qubit as a control and perform:

- A **SWAP gate** between qubit 1 and qubit 2 (if the ball travels left),
- Then **measure qubit 1**.

Next, we apply:

- A **CNOT gate**, with qubit 2 as control and ancillary as target, to reset the ancillary to \(|0\rangle\) for reuse.
- A second **SWAP**, this time between qubit 2 and qubit 3 using the ancillary as control — this captures if the ball traveled to the other side.

Finally, we **measure qubit 3**.

---

### Circuit Validation

- The circuit is executed in a loop and drawn to confirm correctness.
- After running the simulator, we plot a **histogram of measurements**.
- As expected, running the simulator for a larger number of shots causes the distribution to **converge to a normal (Gaussian) distribution**.

---

## Multi-Layer Implementation

We extended the approach to a **three-layer quantum Galton board**.

At this stage, we encountered several challenges:

- Understanding how the number of **bins**, **qubits**, and **layers** relate to each other.
- Figuring out the circuit expansion strategy to simulate deeper layers of quantum scattering.

As noted:

> The number of bins is always one less than the number of layers.

---

### Modular Circuit Design

To manage complexity, we **broke the code into smaller modules**:

1. **Setup** – Initialization of qubits and classical registers  
2. **First Layer Circuit** – Implements the basic 1-layer path  
3. **Second Layer** – Extends path logic and gate resets  
4. **Third Layer** – Final scattering logic and measurements

This modularization allowed us to debug each layer incrementally and ensure that gate operations aligned with expected bin transitions.

---

### Observations

- With each additional layer, the quantum circuit grows in complexity.
- Measurement histograms continue to approximate a binomial distribution.
- This supports the **quantum analog** of the classical Galton box where superposition and entanglement guide the probabilistic paths of the “ball.”

---


