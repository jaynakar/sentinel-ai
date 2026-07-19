"""
file_processor.py

CSV processing utilities.
"""

import pandas as pd

from app.config import X_TEST_PATH


def read_csv_file(file):

    """
    Read uploaded CSV file.
    """

    print()

    print("📂 File Officer: Reading CSV...")

    dataframe = pd.read_csv(file)

    print(
        f"✅ CSV loaded ({len(dataframe):,} rows × {len(dataframe.columns)} columns)"
    )

    return dataframe


def dataframe_to_transactions(
    dataframe,
):
    """
    Convert DataFrame to transaction list.
    """

    print()

    print("📝 Translator: Preparing transactions...")

    transactions = dataframe.values.tolist()

    print(
        f"✅ Prepared {len(transactions):,} transactions."
    )

    return transactions