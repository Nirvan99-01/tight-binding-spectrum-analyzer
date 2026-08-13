import numpy as np 
import pytest
from tight_binding_analyzer.analysis import energy_spacings


def test_energy_spacings():
    eigenvalues = np.array([1.0, 1.5, 2.5, 3.0])
    spacings = energy_spacings(eigenvalues)
    expected_spacings = np.array([0.5, 1.0, 0.5])
    assert np.allclose(spacings, expected_spacings)

def test_energy_spacings_value_error():
    eigenvalues = np.array([[1.0, 1.5, 2.5], [3.0, 4.0, 5.0]])
    with pytest.raises(ValueError):
        energy_spacings(eigenvalues)

def test_energy_spacings_value_error_min_elements():
    eigenvalues = np.array([0.5])
    with pytest.raises(ValueError):
        energy_spacings(eigenvalues)