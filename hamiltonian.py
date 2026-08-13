import numpy as np


def build_hamiltonian(N: int, E: float, V: float) -> np.ndarray:

    """Construct the tight-binding Hamiltonian matrix.

    Parameters
    ----------
    N : int
        Number of sites in the chain.
    E : float
        On-site energy.
    V : float
        Coupling energy between adjacent sites.

    Returns
    -------
    np.ndarray
        Hamiltonian matrix of shape (N, N).

    Raises
    ------
    TypeError
        If N is not an integer, or if E and V are not numeric.
    ValueError
        If N is less than 2.
    """
    
    if not isinstance(N, int):
        raise TypeError("N must be an integer.")
    if not isinstance(E, (int, float)):
        raise TypeError("E must be a number.")
    if not isinstance(V, (int, float)):
        raise TypeError("V must be a number.")
    if N < 2:
        raise ValueError("N must be at least 2 to construct a valid Hamiltonian.")
    H = (
        np.diag(np.full(N, E))
        + np.diag(np.full(N - 1, V), k=1)
        + np.diag(np.full(N - 1, V), k=-1)
    )
    return H
