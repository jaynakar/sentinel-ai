from app.preprocessing import (
    load_dataset,
    split_dataset,
    scale_features,
)

from app.autoencoder import load_autoencoder
from app.predictor import load_predictor

from app.fraud_detector import FraudDetector

df = load_dataset()

X_train, X_test, y_train, y_test = split_dataset(df)

X_train_scaled, X_test_scaled, scaler = scale_features(
    X_train,
    X_test,
)

autoencoder = load_autoencoder()

predictor = load_predictor()

detector = FraudDetector(
    autoencoder,
    predictor,
    scaler,
)

probabilities, predictions = detector.predict(
    X_test_scaled[:5]
)

print()

print("Fraud Probabilities")

print(probabilities)

print()

print("Predictions")

print(predictions)



# ==========================================
# Testing Invalid Input
# ==========================================

print()

print("=" * 50)
print("Testing Invalid Input")
print("=" * 50)

try:
    detector.predict(
        [[1, 2, 3]]
    )

except Exception as e:
    print()
    print("Caught Error:")
    print(e)