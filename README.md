# Monte Carlo Quantum Galton Board

## Project Name
Monte Carlo Quantum Galton Board

## Team Name
Quantum Pioneers

## Team Members
- **Jerison**: WISER Enrollment ID: gst-8vtomJcLfgtcBKK
- **Nero**: WISER Enrollment ID: gst-sMD4rUbGsjcTnWk
- **Ipsita**: WISER Enrollment ID: gst-N6LT9Gwq5jTZsiR

## Project Summary (500 Words)
The Monte Carlo Quantum Galton Board project, developed for the Womanium & WISER Quantum Program 2025, implements quantum and classical simulations of a Galton Board to demonstrate quantum computational advantages in solving high-dimensional problems, as outlined in the "Universal Statistical Simulator" paper ([arXiv:2202.01735](https://arxiv.org/abs/2202.01735)). This project aligns with the hackathon’s theme of quantum algorithms for differential equations, with applications in particle transport and sustainable energy systems, supporting UN Sustainable Development Goal 7 (Affordable and Clean Energy). Our team—Jerison (Physics BS, Python and quantum noise expertise), Nero (Physics BS, theoretical physics), and Ipsita (Physics MS, quantum information and chemical engineering)—leverages Qiskit and Python to deliver a comprehensive solution, comparing quantum circuits with classical Monte Carlo methods to highlight potential exponential speed-ups.

**Task 1: 2-Pager Summary**  
We summarized the "Universal Statistical Simulator" paper, detailing the quantum Galton Board’s circuit design, which uses three types of quantum gates (Hadamard, controlled, and phase) to achieve an exponential speed-up, computing 2ⁿ trajectories with O(n²) resources. The summary connects the approach to PDEs, such as the Boltzmann transport equation, used in nuclear reactor simulations for sustainable energy.

**Task 2: General Galton Box Circuit and Classical Simulation**  
We developed a quantum circuit in Qiskit for a Galton Board with arbitrary layers (n), using the Grover-Rudolph method ([arXiv:quant-ph/0208112](https://arxiv.org/abs/quant-ph/0208112)) to prepare a state encoding the binomial distribution p(k) = C(n,k)/2ⁿ, verified to approximate a Gaussian distribution for large n using Qiskit’s Aer simulator. A classical Monte Carlo simulation, modeling N particles over n layers, was implemented to compare computational efficiency. The quantum circuit’s O(n²) gate count contrasts with the classical O(Nn) operations, showcasing potential quantum advantages for large n.

**Task 3: Modified Circuits**  
The quantum circuit was adapted to produce an exponential distribution and a Hadamard quantum walk, simulated with a noiseless all-to-all sampler. Outputs were verified against target distributions using Matplotlib, ensuring accuracy and alignment with theoretical expectations.

**Task 4: Noise-Optimized Circuits**  
We optimized the circuits for a real quantum hardware noise model (IBM Quantum’s depolarizing noise), applying error mitigation techniques like measurement error correction and gate reduction. This maximized accuracy and the number of layers, demonstrating practical quantum computing capabilities.

**Task 5: Distribution Distance Calculation**  
Distances between obtained and target distributions (binomial, exponential, and Hadamard walk) were computed using Kullback-Leibler divergence via SciPy’s `stats` module, with multiple simulation runs to account for stochastic uncertainty.

This project serves as a prototype for Jerison’s quantum hardware company, showcasing scalable quantum algorithms for PDE solvers in sustainable energy applications. The open-source repository, built with Qiskit, SciPy, NumPy, and Matplotlib, includes Jupyter notebooks, scripts, and visualizations, ensuring accessibility and reproducibility. All resources are properly referenced, adhering to hackathon guidelines. The project’s deliverables highlight technical merit, novelty, and societal impact, positioning our team for success in the hackathon and beyond.

*Word count: 497*

## Project Presentation Deck
[Link to Presentation Deck](https://github.com/QuantumPioneers/QuantumGaltonBoard2025/blob/main/presentation/Monte_Carlo_Presentation.pdf) (Placeholder, to be updated upon completion)

## Repository Structure
```
QuantumGaltonBoard2025/
├── README.md
├── task_1/
│   └── summary.pdf
├── task_2/
│   ├── quantum_galton.ipynb
│   ├── classical_galton.py
│   └── results/
│       ├── binomial_distribution.png
│       └── complexity_comparison.md
├── task_3/
│   ├── exponential_distribution.ipynb
│   ├── hadamard_walk.ipynb
│   └── results/
│       ├── exponential_distribution.png
│       └── hadamard_walk_distribution.png
├── task_4/
│   ├── noisy_circuits.ipynb
│   └── results/
│       ├── noisy_binomial.png
│       ├── noisy_exponential.png
│       └── noisy_hadamard.png
├── task_5/
│   ├── distance_calculation.ipynb
│   └── results/
│       ├── kl_divergence_results.md
│       └── uncertainty_analysis.png
├── presentation/
│   └── Monte_Carlo_Presentation.pdf
├── requirements.txt
└── LICENSE
```

## Installation and Setup
1. Clone the repository: `git clone https://github.com/QuantumPioneers/QuantumGaltonBoard2025.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run Jupyter notebooks or Python scripts in the respective task directories.

## Usage
- **Task 1**: View `task_1/summary.pdf` for the project summary.
- **Task 2**: Run `task_2/quantum_galton.ipynb` for the quantum circuit and `task_2/classical_galton.py` for the classical simulation. Results are in `task_2/results/`.
- **Task 3**: Run `task_3/exponential_distribution.ipynb` and `task_3/hadamard_walk.ipynb` for modified circuits.
- **Task 4**: Run `task_4/noisy_circuits.ipynb` for noise-optimized simulations.
- **Task 5**: Run `task_5/distance_calculation.ipynb` for distribution distance analysis.

## References
- Carney, M., & Varcoe, B. (2022). Universal Statistical Simulator. [arXiv:2202.01735](https://arxiv.org/abs/2202.01735)
- Grover, L., & Rudolph, T. (2002). Creating superpositions that correspond to efficiently integrable probability distributions. [arXiv:quant-ph/0208112](https://arxiv.org/abs/quant-ph/0208112)
- Qiskit Documentation: [https://qiskit.org/documentation/](https://qiskit.org/documentation/)
- SciPy Documentation: [https://docs.scipy.org/doc/scipy/reference/](https://docs.scipy.org/doc/scipy/reference/)
- NumPy Documentation: [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)
- Matplotlib Documentation: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)
- Qiskit Textbook: [https://qiskit.org/textbook/ch-algorithms/quantum-walks.html](https://qiskit.org/textbook/ch-algorithms/quantum-walks.html)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
