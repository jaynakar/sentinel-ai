from app.file_processor import read_csv_file

from app.file_validator import (
    validate_csv,
)

from app.config import X_TEST_PATH


df = read_csv_file(
    X_TEST_PATH
)

validate_csv(
    df,
    X_TEST_PATH.name,
)

print()

print("🎉 Validation Successful.")