<div align="center">

<img src="docs/images/sentinel-logo-v1.png" alt="Sentinel AI Logo" width="450"/>


### Detect. Explain. Protect.

### Intelligent Financial Fraud Detection Platform

<br>

*An enterprise-grade platform that combines Hybrid AI, Explainable AI, and interactive analytics to detect, explain, and investigate financial fraud.*

<br>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange?style=for-the-badge)
![SHAP](https://img.shields.io/badge/Explainable_AI-SHAP-purple?style=for-the-badge)

</div>

<br>

## ✨ Highlights

- 🧠 **Hybrid AI Detection** — Combines an Autoencoder with XGBoost to detect both known and anomalous fraud patterns.
- 📊 **Interactive Dashboard** — Visualize fraud insights, transaction summaries, and model predictions in a modern React interface.
- 📄 **Automated Investigation Reports** — Generate professional PDF reports with risk analysis and actionable recommendations.
- 🔍 **Explainable AI** — Enhance model transparency using SHAP-based explanations.
- ⚡ **High-Performance API** — FastAPI backend designed for efficient fraud prediction and report generation.

# 📖 Project Overview

Financial fraud continues to evolve, making traditional rule-based detection systems increasingly ineffective against sophisticated attack patterns.

**Sentinel AI** is an end-to-end intelligent fraud detection platform that combines **Deep Learning**, **Machine Learning**, and **Explainable AI** to identify suspicious financial transactions with high accuracy.

Unlike conventional approaches that rely solely on supervised classification, Sentinel AI integrates an **Autoencoder** for anomaly detection with an **XGBoost classifier** to improve the detection of both known and previously unseen fraud patterns.

The platform extends beyond prediction by providing:

- 📊 Interactive analytics dashboard
- 🧠 AI-powered fraud risk assessment
- 📄 Automated PDF investigation reports
- 🔍 Explainable AI insights
- ⚡ High-performance REST API built with FastAPI

The result is a complete fraud investigation workflow rather than just a prediction model.

# 💡 Why Sentinel AI?

Financial institutions process millions of transactions every day, while fraudulent activities account for only a tiny fraction of the data.

This extreme class imbalance makes fraud detection one of the most challenging problems in machine learning.

Traditional supervised models often struggle to recognize previously unseen fraud patterns because they learn only from historical examples.

Sentinel AI addresses this challenge through a **Hybrid Detection Framework**.

Instead of depending entirely on labeled fraud samples, the platform first learns the normal behavior of legitimate transactions using an Autoencoder. The reconstruction error produced by the Autoencoder is then combined with the original transaction features and supplied to an XGBoost classifier.

This hybrid approach allows the model to leverage both anomaly detection and supervised learning, improving its ability to identify suspicious transactions while maintaining strong precision and recall.

The platform further enhances transparency through explainable predictions, comprehensive analytics, and automatically generated investigation reports that support informed decision-making.

# ✨ Core Features

| Feature | Description |
|---------|-------------|
| 🧠 Hybrid AI Detection | Combines Autoencoder anomaly detection with XGBoost classification |
| 📂 Batch CSV Analysis | Analyze hundreds or thousands of transactions in a single upload |
| 📊 Interactive Dashboard | Real-time visualization of fraud statistics and transaction insights |
| 🎯 Risk Scoring | Fraud probability, confidence score, and risk categorization |
| 📄 Investigation Reports | Generate professional PDF investigation reports automatically |
| 🔍 Explainable AI | SHAP-based explanations to improve model transparency |
| ⚡ FastAPI Backend | High-performance REST API for prediction and reporting |
| 🎨 Modern React Frontend | Clean and responsive interface built with React and Tailwind CSS |