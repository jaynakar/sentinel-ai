"""
report_generator.py

Generate fraud investigation reports.
"""

from datetime import datetime

from reportlab.lib.units import inch

from reportlab.lib import colors

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
)
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle,
)
from reportlab.lib.enums import (
    TA_CENTER,
    TA_LEFT,
)


PRIMARY_COLOR = colors.HexColor("#203864")      # Deep Blue

SUCCESS_COLOR = colors.HexColor("#15803D")      # Green

WARNING_COLOR = colors.HexColor("#B91C1C")      # Red

LIGHT_BLUE = colors.HexColor("#EFF6FF")

LIGHT_GREEN = colors.HexColor("#F0FDF4")

LIGHT_RED = colors.HexColor("#FEF2F2")


def get_risk_theme(
    risk_level,
):
    """
    Return report colors based on risk level.
    """

    if risk_level == "Critical":

        return {
            "text": "#B91C1C",
            "background": LIGHT_RED,
            "border": WARNING_COLOR,
        }

    elif risk_level in ["High", "Medium"]:

        return {
            "text": "#D97706",
            "background": colors.HexColor("#FFF7ED"),
            "border": colors.HexColor("#D97706"),
        }

    else:

        return {
            "text": "#15803D",
            "background": LIGHT_GREEN,
            "border": SUCCESS_COLOR,
        }


def build_report_header(
    elements,
    styles,
):
    """
    Build report title section.
    """

    elements.append(

        Paragraph(

            "<b>HYBRID FRAUD DETECTION PLATFORM</b>",

            styles["ReportTitle"]

        )

    )

    elements.append(

        Paragraph(

            "Fraud Investigation Report",

            styles["ReportSubtitle"]

        )

    )

    elements.append(

        Spacer(
            1,
            0.35 * inch,
        )

    )


def generate_pdf_report(
    summary,
    flagged_transactions,
    output_path,
):
    
    """
    Generate fraud investigation PDF report.
    """

    print()

    print("📄 Report Officer: Generating PDF report...")

    document = SimpleDocTemplate(
        str(output_path)
    )

    styles = getSampleStyleSheet()
    
    # --------------------------------------------------
    # Custom Report Styles
    # --------------------------------------------------

    styles.add(

        ParagraphStyle(

            name="ReportTitle",

            parent=styles["Title"],

            alignment=TA_CENTER,

            fontName="Helvetica-Bold",

            fontSize=24,
            
            leading=26,

            textColor=PRIMARY_COLOR,

            spaceAfter=0,

        )

    )

    styles.add(

        ParagraphStyle(

            name="ReportSubtitle",

            parent=styles["Heading2"],

            alignment=TA_CENTER,

            fontName="Helvetica",

            fontSize=16,

            textColor=colors.HexColor("#666666"),

            spaceAfter=20,

        )

    )
    
    styles.add(

    ParagraphStyle(

            name="Metadata",

            parent=styles["Normal"],

            alignment=TA_CENTER,

            fontSize=11,

            textColor=colors.HexColor("#777777"),

            leading=18,

            spaceAfter=8,

        )

    )

    styles.add(

        ParagraphStyle(

            name="SectionHeading",

            parent=styles["Heading1"],

            alignment=TA_LEFT,

            fontSize=18,

            spaceBefore=18,

            spaceAfter=12,

        )

    )

    styles.add(

        ParagraphStyle(

            name="Body",

            parent=styles["BodyText"],

            fontSize=11,

            leading=20,

            spaceAfter=10,

        )

    )
    
    
    styles.add(

        ParagraphStyle(

            name="RiskTitle",

            parent=styles["Heading1"],

            alignment=TA_CENTER,

            fontName="Helvetica-Bold",

            fontSize=14,

            textColor=colors.HexColor("#555555"),

            spaceAfter=6,

        )

    )

    styles.add(

        ParagraphStyle(

            name="RiskLevel",

            parent=styles["Title"],

            alignment=TA_CENTER,

            fontName="Helvetica-Bold",

            fontSize=26,

            textColor=colors.HexColor("#111111"),

            spaceAfter=18,

        )

    )

    elements = []
    
    # --------------------------------------------------
    # Report Header
    # --------------------------------------------------

    build_report_header(
        elements,
        styles,
    )
    
    
    elements.append(

        HRFlowable(

            width="100%",

            thickness=0.8,

            color=colors.HexColor("#CFCFCF"),

        )

    )

    elements.append(

        Spacer(
            1,
            0.15 * inch,
        )

    )

    elements.append(

        Paragraph(

            "EXECUTIVE RISK RATING",

            styles["RiskTitle"]

        )

    )

    risk_level = summary["highest_risk"]

    theme = get_risk_theme(
        risk_level
    )

    elements.append(

        Paragraph(

            f'<font color="{theme["text"]}"><b>{risk_level.upper()}</b></font>',

            styles["RiskLevel"]

        )

    )

    elements.append(

        Spacer(
            1,
            0.10 * inch,
        )

    )

    elements.append(

        HRFlowable(

            width="100%",

            thickness=0.8,

            color=colors.HexColor("#CFCFCF"),

        )

    )

    elements.append(

        Spacer(
            1,
            0.30 * inch,
        )

    )

    # --------------------------------------------------
    # Platform Information
    # --------------------------------------------------

    elements.append(

        Paragraph(

            "<b>Platform Information</b>",

            styles["SectionHeading"]

        )

    )

    platform_data = [

        ["Generated",
        datetime.now().strftime("%d %B %Y %I:%M %p")],

        ["Model",
        "Hybrid Autoencoder + XGBoost"],

        ["Decision Threshold",
        "0.15"],

        ["Platform Version",
        "1.0"],

    ]

    platform_table = Table(

        platform_data,

        colWidths=[170, 260],

    )

    platform_table.setStyle(

        TableStyle([

            ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),

            ("FONTNAME", (1, 0), (1, -1), "Helvetica"),

            ("FONTSIZE", (0, 0), (-1, -1), 10),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

            ("TOPPADDING", (0, 0), (-1, -1), 8),

            ("LINEBELOW", (0, 0), (-1, -1), 0.3, colors.HexColor("#DDDDDD")),

            ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#333333")),

            ("TEXTCOLOR", (1, 0), (1, -1), colors.HexColor("#555555")),

        ])

    )

    elements.append(
        platform_table
    )

    elements.append(

        Spacer(
            1,
            0.30 * inch,
        )

    )
    
# --------------------------------------------------
# Executive Assessment
# --------------------------------------------------

    elements.append(

        Paragraph(

            "<b>Executive Assessment</b>",

            styles["SectionHeading"]

        )

    )

    elements.append(

        Spacer(
            1,
            0.15 * inch,
        )

    )

    if summary["fraud_detected"] == 0:

            summary_text = f"""

            <b>{summary['total_transactions']}</b> financial transactions were analyzed using the Hybrid Fraud Detection Platform.

            <br/><br/>

            <b>No transactions</b> exceeded the configured fraud threshold.

            <br/><br/>

            The overall risk assessment for the analyzed dataset is
            <b>{summary['highest_risk']}</b>.

            <br/><br/>

            <b>No suspicious activity was detected.</b>
            Routine monitoring is recommended.

            <br/><br/>

            <b>Average Prediction Confidence:</b> {summary['average_confidence'] * 100:.2f}%

            """

    else:

            summary_text = f"""

            A total of <b>{summary['total_transactions']}</b> financial transactions
            were analyzed using the Hybrid Fraud Detection Platform.

            <br/><br/>

            <b>{summary['fraud_detected']}</b> transaction(s) exceeded the configured
            fraud threshold and were classified as
            <b>{summary['highest_risk']}</b> risk.

            <br/><br/>

            <b>Immediate Manual Investigation</b> is recommended
            for all flagged transactions.

            <br/><br/>

            <b>Average Prediction Confidence:</b>
            {summary['average_confidence'] * 100:.2f}%

            """

    elements.append(

        Paragraph(

            summary_text,

            styles["Body"]

        )

    )

    elements.append(

        Spacer(
            1,
            0.20 * inch,
        )

    )

    # --------------------------------------------------
    # Investigation Results
    # --------------------------------------------------

    elements.append(

        HRFlowable(

            width="100%",

            thickness=0.8,

            color=colors.HexColor("#BDBDBD"),

        )

    )

    elements.append(

        Spacer(
            1,
            0.10 * inch,
        )

    )

    elements.append(

        Paragraph(

            '<font color="#1E3A8A"><b>INVESTIGATION RESULTS</b></font>',

            styles["SectionHeading"]

        )

    )

    elements.append(

        Spacer(
            1,
            0.1 * inch,
        )

    )


    if not flagged_transactions:

        success_theme = get_risk_theme("Very Low")

        elements.append(

            Paragraph(

                f'<font color="{success_theme["text"]}"><b>✓ ANALYSIS COMPLETED SUCCESSFULLY</b></font>',

                styles["Heading2"]

            )

        )

        elements.append(

            Spacer(
                1,
                0.10 * inch,
            )

        )
        
        success_table = Table(

            [[

                Paragraph(

                    f'<font color="{success_theme["text"]}"><b>Analysis Result</b></font><br/><br/>'

                    'The uploaded dataset was successfully analyzed.<br/><br/>'

                    '<b>No suspicious or potentially fraudulent transactions were detected.</b>',

                    styles["Body"]

                )

            ]],

            colWidths=[470]

        )

        success_table.setStyle(

            TableStyle([

                ("BACKGROUND", (0,0), (-1,-1), success_theme["background"]),

                ("BOX", (0,0), (-1,-1), 0.6, success_theme["border"]),

                ("LEFTPADDING", (0,0), (-1,-1), 14),

                ("RIGHTPADDING", (0,0), (-1,-1), 14),

                ("TOPPADDING", (0,0), (-1,-1), 12),

                ("BOTTOMPADDING", (0,0), (-1,-1), 12),

            ])

        )

        elements.append(success_table)
        
        elements.append(

            Spacer(
                1,
                0.20 * inch,
            )

        )

        elements.append(

            Paragraph(

                '<font color="#1E3A8A"><b>ANALYSIS SUMMARY</b></font>',

                styles["SectionHeading"]

            )

        )

        summary_data = [

            ["Total Transactions", summary["total_transactions"]],

            ["Fraud Detected", summary["fraud_detected"]],

            ["Risk Level", summary["highest_risk"]],

            ["Average Confidence", f'{summary["average_confidence"]*100:.2f}%'],

        ]

        summary_table = Table(

            summary_data,

            colWidths=[200,170]

        )

        summary_table.setStyle(

            TableStyle([

                ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),

                ("BOTTOMPADDING",(0,0),(-1,-1),8),

                ("TOPPADDING",(0,0),(-1,-1),8),

                ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#F7F7F7")),

                ("LINEBELOW",(0,0),(-1,-1),0.3,colors.HexColor("#DDDDDD")),

                ("BOX",(0,0),(-1,-1),0.5,colors.HexColor("#DDDDDD")),

            ])

        )

        elements.append(summary_table)
        
        
        elements.append(

            Spacer(
                1,
                0.25 * inch,
            )

        )

        recommendation_table = Table(

            [[

                Paragraph(

                    f'<font color="{success_theme["text"]}"><b>✓ RECOMMENDED ACTION</b></font><br/><br/>'

                    'Routine monitoring is sufficient.<br/><br/>'

                    'No immediate manual investigation is required.',

                    styles["Body"]

                )

            ]],

            colWidths=[470]

        )

        recommendation_table.setStyle(

            TableStyle([

                ("BACKGROUND",(0,0),(-1,-1),success_theme["background"]),

                ("BOX",(0,0),(-1,-1),0.6,success_theme["border"]),

                ("LEFTPADDING",(0,0),(-1,-1),14),

                ("RIGHTPADDING",(0,0),(-1,-1),14),

                ("TOPPADDING",(0,0),(-1,-1),12),

                ("BOTTOMPADDING",(0,0),(-1,-1),12),

            ])

        )

        elements.append(recommendation_table)
            
            

    else:

        for transaction in flagged_transactions:
            
            risk_level = transaction["risk_level"]

            theme = get_risk_theme(
                risk_level
            )
                

            elements.append(

                Paragraph(

                    f'<font color="{theme["text"]}"><b>Investigation Case #{transaction["row_number"]}</b></font>',

                    styles["Heading2"]

                )

            )

            case_data = [

                [
                    "Status",
                    Paragraph(
                        f'<font color="{theme["text"]}"><b>{transaction["label"].upper()}</b></font>',
                        styles["Body"],
                    ),
                ],

                [
                    "Risk Level",
                    Paragraph(
                        f'<font color="{theme["text"]}"><b>{transaction["risk_level"]}</b></font>',
                        styles["Body"],
                    ),
                ],

                ["Fraud Probability",
                f"{transaction['fraud_probability']*100:.2f}%"],

                ["Confidence",
                f"{transaction['confidence']*100:.2f}%"],

                ["Threshold",
                f"{transaction['threshold']:.2f}"],

            ]

            case_table = Table(

                case_data,

                colWidths=[170, 220],

            )

            case_table.setStyle(

                TableStyle([

                    ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),
                    ("FONTNAME",(1,0),(1,-1),"Helvetica"),

                    ("FONTSIZE",(0,0),(-1,-1),10),

                    ("BOTTOMPADDING",(0,0),(-1,-1),9),
                    ("TOPPADDING",(0,0),(-1,-1),9),

                    ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#F7F7F7")),

                    ("LINEBELOW",(0,0),(-1,-1),0.35,colors.HexColor("#DDDDDD")),

                    ("BOX",(0,0),(-1,-1),0.5,colors.HexColor("#D9D9D9")),

                    ("TEXTCOLOR",(0,0),(0,-1),colors.HexColor("#222222")),

                    ("TEXTCOLOR",(1,0),(1,-1),colors.HexColor("#555555")),

                ])

            )

            elements.append(
                case_table
            )
            
            
            elements.append(

                Spacer(
                    1,
                    0.5 * inch,
                )

            )

            recommendation_table = Table(

                [[

                    Paragraph(

                        f'<font color="{theme["text"]}"><b>■ RECOMMENDED ACTION</b></font><br/><br/>'
                        '<b>Immediate Manual Investigation</b> is recommended based on the model prediction.',

                        styles["Body"]

                    )

                ]],

                colWidths=[470]

            )

            recommendation_table.setStyle(

                TableStyle([

                    ("BACKGROUND", (0,0), (-1,-1), theme["background"]),

                    ("BOX", (0,0), (-1,-1), 0.6, theme["border"]),

                    ("LEFTPADDING", (0,0), (-1,-1), 14),

                    ("RIGHTPADDING", (0,0), (-1,-1), 14),

                    ("TOPPADDING", (0,0), (-1,-1), 12),

                    ("BOTTOMPADDING", (0,0), (-1,-1), 12),

                ])

            )

            elements.append(recommendation_table)

            elements.append(

                Spacer(
                    1,
                    0.18 * inch,
                )

            )
            
            
            preview = transaction.get("transaction_preview")

            if preview:

                snapshot = [

                    ["Scaled Amount",
                    f"{preview['scaled_amount']:.6f}"],

                    ["Scaled Time",
                    f"{preview['scaled_time']:.6f}"],

                ]

                snapshot_table = Table(

                    snapshot,

                    colWidths=[170,200]

                )

                snapshot_table.setStyle(

                    TableStyle([

                        ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),

                        ("BOTTOMPADDING",(0,0),(-1,-1),7),

                        ("TOPPADDING",(0,0),(-1,-1),7),

                        ("LINEBELOW",(0,0),(-1,-1),0.25,colors.HexColor("#DDDDDD")),

                    ])

                )

                elements.append(

                    Spacer(
                        1,
                        0.10 * inch,
                    )

                )

                elements.append(

                    Paragraph(

                        '<font color="#1E3A8A"><b>TRANSACTION OVERVIEW</b></font>',

                        styles["SectionHeading"]

                    )

                )

                elements.append(snapshot_table)


    elements.append(

    Spacer(
        1,
        0.35 * inch,
    )

)

    elements.append(

        HRFlowable(
            
            width="100%",
            
            thickness=0.5,
            
            color=colors.HexColor("#D0D0D0"),
        )

    )

    elements.append(

        Spacer(
            1,
            0.10 * inch,
        )

    )

    elements.append(

        Paragraph(

            "Hybrid Fraud Detection Platform • Investigation Report v1.0",

            styles["Metadata"]

        )

    )
            

    document.build(
        elements
    )

    print()

    print(
        "✅ Investigation Report Generated."
    )