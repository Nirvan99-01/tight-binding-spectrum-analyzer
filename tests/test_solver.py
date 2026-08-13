import numpy as np
import pytest
from tight_binding_analyzer.solver import solve_hamiltonian


def test_solve_hamiltonian_n_eigenvalues_and_eigenvectors():
    H = np.array([[1, 0.5], [0.5, 1]])
    eigenvalues, eigenvectors = solve_hamiltonian(H)
    assert eigenvalues.shape == (2,)
    assert eigenvectors.shape == (2, 2)

def test_solve_hamiltonian_eigenvalue_equation():
    H = np.array([[2, 1], [1, 2]])
    eigenvalues, eigenvectors = solve_hamiltonian(H)
    for i in range(len(eigenvalues)):
        assert np.allclose(H @ eigenvectors[:, i], eigenvalues[i] * eigenvectors[:, i])

def test_solve_hamiltonian_non_square():
    H = np.array([[1, 0]])
    with pytest.raises(ValueError):
        solve_hamiltonian(H)

def test_solve_hamiltonian_non_hermitian():
    H = np.array([[1, 2], [3, 4]])
    with pytest.raises(ValueError):
        solve_hamiltonian(H)


