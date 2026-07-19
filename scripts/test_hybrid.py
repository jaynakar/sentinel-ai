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
model = load_autoencoder()

# Reconstruct
reconstructed = reconstruct_transactions(
    model,
    X_test_scaled[:5],
)

# Reconstruction Error
errors = compute_reconstruction_error(
    X_test_scaled[:5],
    reconstructed,
)

# Hybrid Features
hybrid = create_hybrid_features(
    X_test_scaled[:5],
    errors,
)

print()

print("Hybrid Shape :", hybrid.shape)

print()

print(hybrid)