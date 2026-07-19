"""
utils.py

Common utility functions used
throughout the project.
"""

import numpy as np

from app.config import ORIGINAL_FEATURES


def validate_features(features):
    """
    Validate transaction features.
    """

    print("🛡 QA Officer: Validating input...")

    features = np.asarray(features)

    if features.ndim == 1:
        features = features.reshape(1, -1)

    if features.shape[1] != ORIGINAL_FEATURES:
        raise ValueError(
            f"Expected {ORIGINAL_FEATURES} features "
            f"but received {features.shape[1]}."
        )

    if np.isnan(features).any():
        raise ValueError(
            "Input contains NaN values."
        )

    print("✅ Input validation successful.")

    return features