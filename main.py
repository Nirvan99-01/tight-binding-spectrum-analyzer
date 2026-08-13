from .hamiltonian import build_hamiltonian
from .solver import solve_hamiltonian
from .analysis import energy_spacings
from .plotting import plot_spectrum, plot_energy_diff

def main():
    H = build_hamiltonian(50, 1.0, 0.2)
    eigenvalues, eigenvectors = solve_hamiltonian(H)
    print("H.shape:", H.shape)
    print("First 5 Eigenvalues:", eigenvalues[:5])
    print("Eigenvectors shape:", eigenvectors.shape)
    plot_spectrum(eigenvalues)
    energy_diffs = energy_spacings(eigenvalues)
    print("First 5 Energy Spacings:", energy_diffs[:5])
    plot_energy_diff(energy_diffs)

if __name__ == "__main__":
    main()
