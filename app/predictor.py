"""
predictor.py

Handles loading the trained XGBoost model
and generating fraud predictions.

Responsibilities
----------------
- Load trained XGBoost model
- Predict fraud probability
- Predict fraud class
"""

import numpy as np
from xgboost import XGBClassifier

from app.config import (
    XGBOOST_MODEL_PATH,
    DEFAULT_THRESHOLD,
)

def load_predictor():
    """
    Load the trained XGBoost model.

    Returns
    -------
    XGBClassifier
    """

    print("🕵 Loading XGBoost Predictor...")

    model = XGBClassifier()

    model.load_model(XGBOOST_MODEL_PATH)

    print("✅ XGBoost loaded successfully.")

    return model


def predict_probability(
    model,
    hybrid_features,
):
    """
    Predict fraud probability.

    Parameters
    ----------
    model : XGBClassifier

    hybrid_features : numpy.ndarray

    Returns
    -------
    numpy.ndarray
        Fraud probabilities.
    """

    print("🔍 Predicting fraud probability...")

    probabilities = model.predict_proba(
        hybrid_features
    )[:, 1]

    print("✅ Probability prediction completed.")

    return probabilities


def predict_class(
    probabilities,
    threshold=DEFAULT_THRESHOLD,
):
    """
    Convert probabilities into
    fraud predictions.
    """

    print(f"🎯 Applying threshold ({threshold})...")

    predictions = (
        probabilities >= threshold
    ).astype(int)

    print("✅ Prediction completed.")

    return predictions