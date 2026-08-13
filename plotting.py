import matplotlib.pyplot as plt
import numpy as np


def plot_spectrum(eigenvalues: np.ndarray, title="Energy Spectrum") -> None:
    """Plot the energy spectrum.
    
    Parameters
    ----------
    eigenvalues : np.ndarray
        Array of eigenvalues.
    title : str, optional
        Title for the plot.

    Returns
    -------
    None

    Raises
    ------
    TypeError
        If eigenvalues is not a numpy ndarray.
    ValueError
        If eigenvalues is not a 1D array.
    """

    if not isinstance(eigenvalues, np.ndarray):
        raise TypeError("eigenvalues must be a numpy ndarray.")
    if eigenvalues.ndim != 1:
        raise ValueError("eigenvalues must be a 1D array.")
    
    x = np.arange(len(eigenvalues))
    plt.scatter(x, eigenvalues)
    plt.title(title)
    plt.xlabel('State Index')
    plt.ylabel('Energy')
    plt.show()


def plot_energy_diff(energy_diffs: np.ndarray, title="Energy Spacings") -> None:
    """Plot the energy spacings.
    
    Parameters
    ----------
    energy_diffs : np.ndarray
        Array of energy spacings.
    title : str, optional
        Title for the plot.

    Returns
    -------
    None

    Raises
    ------
    TypeError
        If energy_diffs is not a numpy ndarray.
    ValueError
        If energy_diffs is not a 1D array.
    """

    if not isinstance(energy_diffs, np.ndarray):
        raise TypeError("energy_diffs must be a numpy ndarray.")
    if energy_diffs.ndim != 1:
        raise ValueError("energy_diffs must be a 1D array.")
    
    x = np.arange(len(energy_diffs))
    plt.scatter(x, energy_diffs)
    plt.title(title)
    plt.xlabel('Spacing Index')
    plt.ylabel('Energy Spacing')
    plt.show()