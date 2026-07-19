from app.preprocessing import (
    load_dataset,
    dataset_summary,
    split_dataset,
    scale_features,
)

df = load_dataset()

dataset_summary(df)

print()

X_train, X_test, y_train, y_test = split_dataset(df)

print()

X_train_scaled, X_test_scaled, scaler = scale_features(
    X_train,
    X_test,
)

print()

print("Scaled Training Shape :", X_train_scaled.shape)
print("Scaled Testing Shape  :", X_test_scaled.shape)