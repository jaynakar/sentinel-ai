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

df = load_dataset()

X_train, X_test, y_train, y_test = split_dataset(df)

X_train_scaled, X_test_scaled, scaler = scale_features(
    X_train,
    X_test,
)

model = load_autoencoder()

print()

reconstructed = reconstruct_transactions(
    model,
    X_test_scaled[:5]
)

errors = compute_reconstruction_error(
    X_test_scaled[:5],
    reconstructed,
)

print()

print("Reconstruction Errors")

print(errors)
# print("Reconstructed Shape :", reconstructed.shape)