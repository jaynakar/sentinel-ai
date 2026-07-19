from app.config import *

print("=" * 50)
print("Hybrid Fraud Detection Project")
print("=" * 50)

print(f"Project Root       : {BASE_DIR}")
print(f"Dataset            : {RAW_DATA_PATH}")
print(f"Autoencoder Model  : {AUTOENCODER_MODEL_PATH}")
print(f"Hybrid Scaler      : {HYBRID_SCALER_PATH}")
print(f"XGBoost Model      : {XGBOOST_MODEL_PATH}")
print(f"Random Forest      : {RANDOM_FOREST_MODEL_PATH}")
print(f"Threshold          : {DEFAULT_THRESHOLD}")
print(f"Original Features  : {ORIGINAL_FEATURES}")
print(f"Hybrid Features    : {HYBRID_FEATURES}")