import numpy as np
import matplotlib.pyplot as plt
import time

def galton_classical_simulation(n, N=10000):
    start_time = time.time()
    positions = []
    for _ in range(N):
        pos = 0
        for _ in range(n):
            pos += np.random.choice([-1, 1])
        positions.append(pos)
    end_time = time.time()
    plt.hist(positions, bins=range(-n-1, n+2), density=True, alpha=0.5, label='Classical')
    plt.title(f'Classical Galton Board (n={n}, N={N})')
    plt.xlabel('Final Position')
    plt.ylabel('Probability')
    plt.legend()
    plt.savefig(f'results/classical_distribution_n{n}.png')
    plt.close()
    return positions, end_time - start_time

if __name__ == "__main__":
    n = 3
    positions, sim_time = galton_classical_simulation(n)
    print(f"Classical simulation time for n={n}: {sim_time:.2f} seconds")
