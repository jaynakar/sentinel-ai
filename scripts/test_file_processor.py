from app.file_processor import (
    read_csv_file,
    dataframe_to_transactions,
)

from app.config import X_TEST_PATH

df = read_csv_file(
    X_TEST_PATH
)

transactions = dataframe_to_transactions(
    df
)

print()

print(type(transactions))

print()

print(len(transactions))

print()

print(transactions[0])