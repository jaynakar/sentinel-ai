"""
preprocessing.py

Handles all dataset preprocessing for the Hybrid Fraud Detection Framework.

Responsibilities:
- Load dataset
- Split train/test data
- Scale features
"""

import pandas as pd
import joblib

from app.config import FEATURE_SCALER_PATH
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from app.config import (
    RAW_DATA_PATH,
    RANDOM_STATE,
    FEATURE_SCALER_PATH,
)

def load_dataset():
    """
    Load the credit card fraud dataset.

    Returns
    -------
    pandas.DataFrame
        Complete dataset.
    """

    print("📂 Loading dataset...")

    df = pd.read_csv(RAW_DATA_PATH)

    print(f"✅ Dataset loaded successfully ({df.shape[0]:,} rows × {df.shape[1]} columns)")

    return df

def split_dataset(df):
    """
    Split the dataset into training and testing sets.

    Parameters
    ----------
    df : pandas.DataFrame
        Complete fraud dataset.

    Returns
    -------
    tuple
        X_train, X_test, y_train, y_test
    """

    print("✂ Splitting dataset...")

    X = df.drop(columns="Class")
    y = df["Class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        stratify=y,
        random_state=RANDOM_STATE,
    )

    print(f"✅ Training samples : {len(X_train):,}")
    print(f"✅ Testing samples  : {len(X_test):,}")

    return X_train, X_test, y_train, y_test


def scale_features(X_train, X_test):
    """
    Scale training and testing features using StandardScaler.

    Parameters
    ----------
    X_train : pandas.DataFrame
        Training features.

    X_test : pandas.DataFrame
        Testing features.

    Returns
    -------
    tuple
        X_train_scaled,
        X_test_scaled,
        scaler
    """

    print("⚙ Scaling features...")

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = scaler.transform(X_test)

    print("✅ Features scaled successfully.")

    return X_train_scaled, X_test_scaled, scaler


def dataset_summary(df):
    """
    Display basic information about the dataset.
    """

    print("\n📊 Dataset Summary")
    print("-" * 40)

    print(f"Rows      : {df.shape[0]:,}")
    print(f"Columns   : {df.shape[1]}")

    fraud_count = df["Class"].sum()
    normal_count = len(df) - fraud_count

    print(f"Normal Transactions : {normal_count:,}")
    print(f"Fraud Transactions  : {fraud_count:,}")

    print(f"Fraud Ratio         : {fraud_count / len(df):.6%}")
    
    
def load_feature_scaler():

    print("⚙ Loading Feature Scaler...")

    scaler = joblib.load(
        FEATURE_SCALER_PATH
    )

    print("✅ Feature Scaler loaded successfully.")

    return scaler