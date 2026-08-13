import numpy as np
import pytest
from tight_binding_analyzer.hamiltonian import build_hamiltonian

def test_build_hamiltonian_shape():
    H = build_hamiltonian(5, 1.0, 0.2)
    assert H.shape == (5, 5)

def test_build_hamiltonian_is_symmetric():
    H = build_hamiltonian(5, 1.0, 0.2)
    assert np.allclose(H, H.conj().T)

def test_diagonal_and_off_diagonal_elements():
    H = build_hamiltonian(4, 1.5, 0.3)
    assert np.isclose(H[0, 0], 1.5)
    assert np.isclose(H[1, 1], 1.5)
    assert np.isclose(H[0, 1], 0.3)
    assert np.isclose(H[1, 0], 0.3)

def test_invalid_n_raises_value_error():
    with pytest.raises(ValueError):
        build_hamiltonian(1, 1.0, 0.2)

def test_invalid_n_type_raises_type_error():
    with pytest.raises(TypeError):
        build_hamiltonian("5", 1.0, 0.2)
