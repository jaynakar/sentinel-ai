from fastapi import APIRouter
from app.api.schemas import (
    PredictionRequest,
    PredictionResponse,
    BatchPredictionRequest,
    BatchPredictionResponse,
    BatchSummary,
    FlaggedTransaction,
)
from fastapi import UploadFile, File
from app.file_validator import validate_csv
import app.startup as startup
from fastapi import HTTPException
from app.file_processor import (
    read_csv_file,
    dataframe_to_transactions,
)
from app.investigation import (
    find_flagged_transactions,
)
from app.report_service import (
    generate_investigation_report,
)
from fastapi.responses import FileResponse
from pathlib import Path


router = APIRouter()


@router.get("/")
def home():

    return {
        "message": "Hybrid Fraud Detection API is running."
    }


@router.post(
    "/predict",
    response_model=PredictionResponse,
)
def predict(
    request: PredictionRequest,
):

    result = startup.detector.predict(
        [request.features]
    )

    return PredictionResponse(
        **result
    )
    
    
@router.post(
    "/predict-batch",
    response_model=BatchPredictionResponse,
)
def predict_batch(
    request: BatchPredictionRequest,
):

    predictions = []

    for transaction in request.transactions:

        result = startup.detector.predict(
            [transaction.features]
        )

        predictions.append(
            PredictionResponse(**result)
        )
        
    summary = startup.detector.build_batch_summary(
        [
            prediction.model_dump()
            for prediction in predictions
        ]
    )

    return BatchPredictionResponse(

        summary=BatchSummary(
            **summary
        ),

        predictions=predictions,

    )
    

@router.post(
     "/predict-csv",
    response_model=BatchPredictionResponse,         
)

def predict_csv(
    file: UploadFile = File(...),
):

    try:

        dataframe = read_csv_file(
            file.file
        )

        validate_csv(
            dataframe,
            file.filename,
        )

        transactions = dataframe_to_transactions(
            dataframe
        )

        results = startup.detector.predict_batch(
            transactions
        )

        predictions = [
            PredictionResponse(**result)
            for result in results
        ]
        
        prediction_data = [
            prediction.model_dump()
            for prediction in predictions
        ]

        summary = startup.detector.build_batch_summary(
            prediction_data
        )

        flagged = find_flagged_transactions(
            prediction_data,
            dataframe,
        )
        
        report_path = generate_investigation_report(
            summary,
            flagged,
        )

        return BatchPredictionResponse(

            summary=BatchSummary(
                **summary
            ),

            flagged_transactions=[

                FlaggedTransaction(
                    **transaction
                )

                for transaction in flagged

            ],

            predictions=predictions,

        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )
        
        
@router.get("/reports/latest")
def download_latest_report():

    report_path = Path("reports") / "investigation_report.pdf"

    if not report_path.exists():

        raise HTTPException(
            status_code=404,
            detail="No investigation report found.",
        )

    return FileResponse(
        path=report_path,
        media_type="application/pdf",
        filename="investigation_report.pdf",
    )