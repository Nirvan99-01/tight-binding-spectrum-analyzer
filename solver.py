import numpy as np


def solve_hamiltonian(H: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Solve the Hamiltonian matrix to find eigenvalues and eigenvectors.
    
    Parameters
    ----------
    H : np.ndarray
        Hamiltonian matrix of shape (N, N).

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        A tuple containing the eigenvalues and eigenvectors.
    
    Raises
    ------
    TypeError
        If H is not a numpy ndarray.
    ValueError
        If H is not a 2D square matrix or if it is not Hermitian.
    """

    if not isinstance(H, np.ndarray):
        raise TypeError("H must be a numpy ndarray.")
    if H.ndim != 2:
        raise ValueError("H must be a 2D array.")
    if H.shape[0] != H.shape[1]:
        raise ValueError("H must be a square matrix.")
    if not np.allclose(H, H.conj().T):
        raise ValueError("H must be a Hermitian matrix.")

    eigenvalues, eigenvectors = np.linalg.eigh(H)
    return eigenvalues, eigenvectors
