"""
file_validator.py

Validation utilities for uploaded CSV files.
"""

EXPECTED_COLUMNS = [

    "scaled_amount",

    "scaled_time",

    *[f"V{i}" for i in range(1, 29)],

]


def validate_extension(
    filename,
):
    """
    Validate uploaded file extension.
    """

    print()

    print("🛡 Security: Checking file extension...")

    if not filename.lower().endswith(".csv"):

        raise ValueError(
            "Only CSV files are allowed."
        )

    print("✅ Extension validated.")
    
    
def validate_columns(
    dataframe,
):
    """
    Validate CSV columns.
    """

    print()

    print("🛡 Security: Checking columns...")

    columns = list(dataframe.columns)

    if columns != EXPECTED_COLUMNS:

        raise ValueError(

            "CSV columns do not match the expected schema."

        )

    print("✅ Columns validated.")
    
    
def validate_missing_values(
    dataframe,
):
    """
    Validate missing values.
    """

    print()

    print("🛡 Security: Checking missing values...")

    if dataframe.isnull().values.any():

        raise ValueError(
            "CSV contains missing values."
        )

    print("✅ No missing values found.")
    
    
from pandas.api.types import is_numeric_dtype


def validate_numeric_columns(
    dataframe,
):
    """
    Validate that every column contains numeric values.
    """

    print()

    print("🛡 Security: Checking numeric columns...")

    for column in dataframe.columns:

        if not is_numeric_dtype(
            dataframe[column]
        ):

            raise ValueError(
                f"Column '{column}' contains non-numeric data."
            )

    print("✅ Numeric validation passed.")
    
    
    
def validate_duplicate_columns(
    dataframe,
):
    """
    Validate duplicate column names.
    """

    print()

    print("🛡 Security: Checking duplicate columns...")

    duplicated = dataframe.columns[
        dataframe.columns.duplicated()
    ]

    if len(duplicated) > 0:

        duplicates = duplicated.tolist()

        raise ValueError(
            f"Duplicate columns detected: {duplicates}"
        )

    print("✅ No duplicate columns found.")
    
    

def validate_csv(
    dataframe,
    filename,
):
    """
    Perform all CSV validation checks.
    """

    print()

    print("🛡 Security Officer: Starting CSV validation...")

    validate_extension(
        filename,
    )

    validate_columns(
        dataframe,
    )

    validate_missing_values(
        dataframe,
    )

    validate_numeric_columns(
        dataframe,
    )

    validate_duplicate_columns(
        dataframe,
    )

    print()

    print("✅ CSV validation completed successfully.")