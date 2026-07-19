"""
hybrid.py

Creates Hybrid Features by combining
scaled transaction features with the
Autoencoder reconstruction error.

Responsibilities
----------------
- Create hybrid feature vectors
"""

import numpy as np


def create_hybrid_features(
    scaled_features,
    reconstruction_error,
):
    """
    Create Hybrid Feature Matrix.

    Parameters
    ----------
    scaled_features : numpy.ndarray

    reconstruction_error : numpy.ndarray

    Returns
    -------
    numpy.ndarray
        Hybrid feature matrix
        (30 features + reconstruction error)
    """

    print("🧩 Creating Hybrid Features...")

    hybrid_features = np.column_stack(
        (
            scaled_features,
            reconstruction_error,
        )
    )

    print(
        f"✅ Hybrid feature matrix created "
        f"({hybrid_features.shape[1]} features)"
    )

    return hybrid_features