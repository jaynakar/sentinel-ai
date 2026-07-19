"""
report_service.py

Service responsible for generating
fraud investigation reports.
"""

from pathlib import Path

from app.report_generator import (
    generate_pdf_report,
)


REPORTS_DIRECTORY = Path("reports")

REPORTS_DIRECTORY.mkdir(
    exist_ok=True,
)


def create_report_path():
    """
    Create report output path.
    """

    return REPORTS_DIRECTORY / "investigation_report.pdf"


def generate_investigation_report(
    summary,
    flagged_transactions,
):
    """
    Generate investigation report
    and return its location.
    """

    output_path = create_report_path()

    generate_pdf_report(
        summary,
        flagged_transactions,
        output_path,
    )

    return output_path