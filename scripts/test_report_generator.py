from pathlib import Path

from app.report_generator import (
    generate_pdf_report,
)


summary = {

    "total_transactions": 100,

    "fraud_detected": 1,

    "normal_transactions": 99,

    "average_confidence": 0.9998,

    "highest_risk": "Critical",

}


flagged_transactions = [

    {

        "row_number": 43,

        "prediction_code": 1,

        "label": "Fraud",

        "fraud_probability": 0.9841513633728027,

        "confidence": 0.9841513633728027,

        "risk_level": "Critical",

        "threshold": 0.15,

        "model": "Hybrid Autoencoder + XGBoost",

        "transaction_preview": {

            "scaled_amount": -0.353189,

            "scaled_time": -0.796133,

        },

    }

]

REPORTS_DIR = Path("reports")

REPORTS_DIR.mkdir(
    exist_ok=True
)

output_path = REPORTS_DIR / "investigation_report.pdf"

generate_pdf_report(

    summary,

    flagged_transactions,

    output_path,

)