"""
autoencoder.py

Handles everything related to the Autoencoder.

Responsibilities
----------------
- Load trained Autoencoder
- Reconstruct transactions
- Compute reconstruction error
"""

import numpy as np

from tensorflow.keras.models import load_model

from app.config import AUTOENCODER_MODEL_PATH


def load_autoencoder():
    """
    Load the trained Autoencoder model.

    Returns
    -------
    tensorflow.keras.Model
        Loaded Autoencoder model.
    """

    print("🧠 Loading Autoencoder...")

    model = load_model(
        AUTOENCODER_MODEL_PATH,
        compile=False
    )

    print("✅ Autoencoder loaded successfully.")

    return model


def reconstruct_transactions(model, features):
    """
    Reconstruct input transactions using the trained Autoencoder.

    Parameters
    ----------
    model : tensorflow.keras.Model
        Loaded Autoencoder.

    features : numpy.ndarray
        Scaled feature matrix.

    Returns
    -------
    numpy.ndarray
        Reconstructed transactions.
    """

    print("🔄 Reconstructing transactions...")

    reconstructed = model.predict(
        features,
        verbose=0
    )

    print("✅ Reconstruction completed.")

    return reconstructed


def compute_reconstruction_error(
    original_features,
    reconstructed_features,
):
    """
    Compute reconstruction error (Mean Squared Error)
    for every transaction.

    Parameters
    ----------
    original_features : numpy.ndarray

    reconstructed_features : numpy.ndarray

    Returns
    -------
    numpy.ndarray
        Reconstruction error for each transaction.
    """

    print("📈 Computing reconstruction error...")

    reconstruction_error = np.mean(
        np.square(
            original_features -
            reconstructed_features
        ),
        axis=1,
    )

    print("✅ Reconstruction error calculated.")

    return reconstruction_error