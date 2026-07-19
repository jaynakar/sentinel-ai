from app.preprocessing import (
    load_dataset,
    split_dataset,
    scale_features,
)

from app.autoencoder import (
    load_autoencoder,
    reconstruct_transactions,
    compute_reconstruction_error,
)

from app.hybrid import (
    create_hybrid_features,
)

from app.predictor import (
    load_predictor,
    predict_probability,
    predict_class,
)

# Load dataset
df = load_dataset()

# Split
X_train, X_test, y_train, y_test = split_dataset(df)

# Scale
X_train_scaled, X_test_scaled, scaler = scale_features(
    X_train,
    X_test,
)

# Autoencoder
autoencoder = load_autoencoder()

reconstructed = reconstruct_transactions(
    autoencoder,
    X_test_scaled[:5],
)

errors = compute_reconstruction_error(
    X_test_scaled[:5],
    reconstructed,
)

hybrid = create_hybrid_features(
    X_test_scaled[:5],
    errors,
)

# XGBoost
predictor = load_predictor()

probabilities = predict_probability(
    predictor,
    hybrid,
)

predictions = predict_class(
    probabilities,
)

print()

print("Fraud Probabilities")
print(probabilities)

print()

print("Predictions")
print(predictions)
