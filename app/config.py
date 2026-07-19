from pathlib import Path

# ==========================================================
# Project Root
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================================
# Data
# ==========================================================

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

RAW_DATA_PATH = RAW_DATA_DIR / "creditcard.csv"

X_TEST_PATH = PROCESSED_DATA_DIR / "X_test.csv"

X_TRAIN_PATH = PROCESSED_DATA_DIR / "X_train.csv"

Y_TEST_PATH = PROCESSED_DATA_DIR / "y_test.csv"

Y_TRAIN_PATH = PROCESSED_DATA_DIR / "y_train.csv"

# ==========================================================
# Models
# ==========================================================

MODELS_DIR = BASE_DIR / "models"

AUTOENCODER_MODEL_PATH = (
    MODELS_DIR
    / "autoencoder"
    / "autoencoder_tuned_model.h5"
)

XGBOOST_MODEL_PATH = (
    MODELS_DIR
    / "xgboost"
    / "xgb_hybrid_final.json"
)

RANDOM_FOREST_MODEL_PATH = (
    MODELS_DIR
    / "random_forest"
    / "rf_hybrid_final.joblib"
)

HYBRID_SCALER_PATH = (
    MODELS_DIR
    / "scalers"
    / "scaler_hybrid_final.joblib"
)

FEATURE_SCALER_PATH = (
    MODELS_DIR
    / "scalers"
    / "scaler_hybrid_final.joblib"
)


# ==========================================================
# Model Information
# ==========================================================

MODEL_NAME = "Hybrid Autoencoder + XGBoost"


# ==========================================================
# Outputs
# ==========================================================

OUTPUT_DIR = BASE_DIR / "outputs"

PLOTS_DIR = OUTPUT_DIR / "plots"
REPORTS_DIR = OUTPUT_DIR / "reports"
SHAP_DIR = OUTPUT_DIR / "shap"

# ==========================================================
# Threshold
# ==========================================================

DEFAULT_THRESHOLD = 0.15

# ==========================================================
# Model Information
# ==========================================================

ORIGINAL_FEATURES = 30
HYBRID_FEATURES = 31

RANDOM_STATE = 42   

