"""
fraud_detector.py

Main orchestration layer of the Hybrid Fraud Detection Framework.

Responsibilities
----------------
- Coordinate all project modules
- Produce final fraud predictions
"""

from app.utils import validate_features
from app.preprocessing import scale_features
from app.autoencoder import (
    reconstruct_transactions,
    compute_reconstruction_error,
)
from app.hybrid import create_hybrid_features
from app.predictor import (
    predict_probability,
    predict_class,
)
from app.config import (
    DEFAULT_THRESHOLD,
    MODEL_NAME,
)


class FraudDetector:
    """
    Main pipeline for fraud detection.
    """

    def __init__(
        self,
        autoencoder,
        predictor,
        scaler,
    ):
        self.autoencoder = autoencoder
        self.predictor = predictor
        self.scaler = scaler
        
        
    def prepare_hybrid_features(
    self,
    features,
    ):
        """
        Prepare Hybrid Features from
        scaled transaction features.
        """

        print("👔 Manager: Preparing Hybrid Features...")

        reconstructed = reconstruct_transactions(
            self.autoencoder,
            features,
        )

        reconstruction_error = compute_reconstruction_error(
            features,
            reconstructed,
        )

        hybrid_features = create_hybrid_features(
            features,
            reconstruction_error,
        )

        print("✅ Hybrid Features Ready.")

        return hybrid_features
    
    
    def get_confidence(
        self,
        probability,
        prediction,
    ):
        """
        Compute confidence for the predicted class.
        """

        if prediction == 1:
            return float(probability)

        return float(1 - probability)
    
    
    def get_risk_level(
        self,
        probability,
    ):
        """
        Determine risk level from fraud probability.
        """

        if probability < 0.01:
            return "Very Low"

        elif probability < 0.05:
            return "Low"

        elif probability < DEFAULT_THRESHOLD:
            return "Moderate"

        elif probability < 0.50:
            return "High"

        return "Critical"
    
    
    def build_prediction_response(
        self,
        prediction,
        label,
        probability,
        confidence,
        risk_level,
    ):
        """
        Build final prediction response.
        """

        return {

            "status": "Success",

            "prediction_code": prediction,

            "label": label,

            "fraud_probability": probability,

            "confidence": confidence,

            "risk_level": risk_level,

            "threshold": DEFAULT_THRESHOLD,

            "model": MODEL_NAME,

        }
    
    
    def build_batch_summary(
        self,
        predictions,
    ):
        """
        Build summary for a batch prediction.
        """

        total_transactions = len(predictions)

        fraud_detected = sum(
            prediction["prediction_code"]
            for prediction in predictions
        )

        normal_transactions = (
            total_transactions - fraud_detected
        )

        average_confidence = sum(
            prediction["confidence"]
            for prediction in predictions
        ) / total_transactions

        highest_risk = max(
            (
                prediction["risk_level"]
                for prediction in predictions
            ),
            key=lambda risk: (
                "Very Low",
                "Low",
                "Moderate",
                "High",
                "Critical",
            ).index(risk),
        )

        return {

            "total_transactions": total_transactions,

            "fraud_detected": fraud_detected,

            "normal_transactions": normal_transactions,

            "average_confidence": round(
                average_confidence,
                4,
            ),

            "highest_risk": highest_risk,

        }
        
    
    def predict(
    self,
    scaled_features,
    ):
        """
        Complete fraud detection pipeline.
        """

        print("🚀 Manager: Starting Fraud Detection Pipeline...")

        scaled_features = validate_features(
            scaled_features
        )
        
        hybrid_features = self.prepare_hybrid_features(
            scaled_features,
        )

        probabilities = predict_probability(
            self.predictor,
            hybrid_features,
        )

        predictions = predict_class(
            probabilities,
        )

        prediction = int(predictions[0])

        label = (
            "Fraud"
            if prediction == 1
            else "Normal"
        )
        
        confidence = self.get_confidence(
            probabilities[0],
            prediction,
        )
        
        risk_level = self.get_risk_level(
            probabilities[0]
        )

        print("✅ Fraud Detection Pipeline Complete.")


        return self.build_prediction_response(

            prediction,

            label,

            float(probabilities[0]),

            confidence,

            risk_level,

        )
        
        
    def predict_batch(
    self,
    scaled_features,
    ):
        """
        Complete batch fraud detection pipeline.
        """

        print()

        print("🚀 Manager: Starting Batch Fraud Detection Pipeline...")

        scaled_features = validate_features(
            scaled_features
        )

        hybrid_features = self.prepare_hybrid_features(
            scaled_features,
        )

        probabilities = predict_probability(
            self.predictor,
            hybrid_features,
        )

        predictions = predict_class(
            probabilities,
        )

        results = []

        for probability, prediction in zip(
            probabilities,
            predictions,
        ):

            label = (
                "Fraud"
                if prediction == 1
                else "Normal"
            )

            confidence = self.get_confidence(
                probability,
                prediction,
            )

            risk_level = self.get_risk_level(
                probability,
            )

            results.append(

                self.build_prediction_response(

                    int(prediction),

                    label,

                    float(probability),

                    confidence,

                    risk_level,

                )

            )

        print("✅ Batch Fraud Detection Pipeline Complete.")

        return results