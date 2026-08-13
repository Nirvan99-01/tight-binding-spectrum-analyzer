import numpy as np


def energy_spacings(eigenvalues: np.ndarray) -> np.ndarray:
    """Calculate the energy spacings between consecutive eigenvalues.
    
    Parameters
    ----------
    eigenvalues : np.ndarray
        Array of eigenvalues.

    Returns
    -------
    np.ndarray
        Array of energy spacings.

    Raises
    ------
    TypeError
        If eigenvalues is not a numpy ndarray.
    ValueError
        If eigenvalues is not a 1D array or if it contains fewer than two elements.
    """

    if not isinstance(eigenvalues, np.ndarray):
        raise TypeError("eigenvalues must be a numpy ndarray.")
    if eigenvalues.ndim != 1:
        raise ValueError("eigenvalues must be a 1D array.")
    if len(eigenvalues) < 2:
        raise ValueError("eigenvalues must contain at least two elements to calculate spacings.")

    spacings = np.diff(eigenvalues)
    return spacings