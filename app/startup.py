"""
startup.py

Application startup.
Loads all ML models once.
"""

from app.autoencoder import load_autoencoder
from app.predictor import load_predictor
from app.preprocessing import load_feature_scaler

from app.fraud_detector import FraudDetector


detector = None


def initialize():

    global detector

    print()

    print("=" * 50)
    print("🚀 Starting Hybrid Fraud Detection API")
    print("=" * 50)

    autoencoder = load_autoencoder()

    predictor = load_predictor()

    scaler = load_feature_scaler()

    detector = FraudDetector(
        autoencoder,
        predictor,
        scaler,
    )

    print()

    print("✅ Detector initialized successfully.")

    return detector