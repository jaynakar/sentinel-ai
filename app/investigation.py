"""
investigation.py

Utilities for fraud investigation.
"""

def find_flagged_transactions(
    predictions,
    dataframe,
):
    """
    Find suspicious transactions.
    """

    print()

    print("🕵 Investigation Officer: Looking for suspicious transactions...")

    flagged = []

    for index, prediction in enumerate(
        predictions
    ):

        if prediction["prediction_code"] == 1:

            transaction = dataframe.iloc[index]
            
            flagged.append(

                {

                    "row_number": index + 1,

                    "prediction_code": prediction["prediction_code"],

                    "label": prediction["label"],

                    "fraud_probability": prediction["fraud_probability"],

                    "confidence": prediction["confidence"],

                    "risk_level": prediction["risk_level"],

                    "threshold": prediction["threshold"],

                    "model": prediction["model"],
                    
                    "transaction_preview": {

                        "scaled_amount": float(
                            transaction["scaled_amount"]
                        ),

                        "scaled_time": float(
                            transaction["scaled_time"]
                        ),

                    },

                }

            )

    print(
        f"✅ Found {len(flagged)} suspicious transactions."
    )

    return flagged