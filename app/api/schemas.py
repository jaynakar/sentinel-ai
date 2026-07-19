from pydantic import BaseModel
from typing import List


class PredictionRequest(BaseModel):
    """
    Incoming prediction request.
    """

    features: List[float]


class PredictionResponse(BaseModel):

    status: str

    prediction_code: int

    label: str

    fraud_probability: float

    confidence: float

    risk_level: str

    threshold: float

    model: str
    
    
class BatchPredictionRequest(BaseModel):
    """
    Batch prediction request.
    """

    transactions: list[PredictionRequest]

    
class BatchSummary(BaseModel):
    """
    Batch summary.
    """

    total_transactions: int

    fraud_detected: int

    normal_transactions: int

    average_confidence: float

    highest_risk: str


class TransactionPreview(BaseModel):

    scaled_amount: float

    scaled_time: float
    
    
class FlaggedTransaction(BaseModel):

    row_number: int

    prediction_code: int

    label: str

    fraud_probability: float

    confidence: float

    risk_level: str

    threshold: float

    model: str
    
    transaction_preview: TransactionPreview
    
    
class BatchPredictionResponse(BaseModel):
    """
    Batch prediction response.
    """

    summary: BatchSummary

    flagged_transactions: list[FlaggedTransaction]

    predictions: list[PredictionResponse]
