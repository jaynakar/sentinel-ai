import sentinelLogo from "../../assets/sentinel-logo.png";
import { useEffect, useState } from "react";


export default function ProcessingPanel({ onComplete }) {

    const steps = [
        "Initializing AI Engine...",
        "Loading Hybrid AI Models...",
        "Running Autoencoder...",
        "Generating Reconstruction Error...",
        "Running XGBoost...",
        "Calculating Fraud Risk...",
        "Generating SHAP Explanations...",
        "Creating Investigation Report..."
    ];
    const [progress, setProgress] = useState(8);
    const [currentStage, setCurrentStage] = useState(0);
    const stages = [
    {
        progress: 5,
        title: "Initializing AI Engine...",
        detail: "Preparing Sentinel AI Core..."
    },
    {
        progress: 18,
        title: "Loading Hybrid AI Models...",
        detail: "Loading Autoencoder and XGBoost..."
    },
    {
        progress: 35,
        title: "Running Autoencoder...",
        detail: "Detecting anomalous transactions..."
    },
    {
        progress: 52,
        title: "Generating Reconstruction Error...",
        detail: "Building hybrid feature vector..."
    },
    {
        progress: 68,
        title: "Running XGBoost...",
        detail: "Calculating fraud probability..."
    },
    {
        progress: 82,
        title: "Calculating Fraud Risk...",
        detail: "Scoring every transaction..."
    },
    {
        progress: 94,
        title: "Generating SHAP Explanations...",
        detail: "Explaining model decisions..."
    },
    {
        progress: 100,
        title: "Creating Investigation Report...",
        detail: "Finalizing analysis..."
    }
    ];

    useEffect(() => {

        let stageIndex = 0;

        const timer = setInterval(() => {

            stageIndex++;

            if (stageIndex >= stages.length) {

                clearInterval(timer);

                onComplete();

                return;

            }

            setCurrentStage(stageIndex);
            setProgress(stages[stageIndex].progress);

        }, 1500);

        return () => clearInterval(timer);

    }, []);

    return (
        <div className="mt-8 rounded-xl border border-slate-800 bg-slate-950 p-12">

        <div className="flex flex-col items-center">

            <div className="relative">

            <div className="absolute inset-0 rounded-full bg-blue-500/20 blur-2xl animate-pulse"></div>

            <img
                src={sentinelLogo}
                alt="Sentinel AI"
                className="relative h-20 w-auto animate-pulse"
            />

            </div>

            <h2 className="mt-6 text-2xl font-bold">
            Sentinel AI Core
            </h2>

            <p className="mt-2 text-slate-400">
            {stages[currentStage].title}
                <div className="mt-8 w-full max-w-md">

                <div className="mb-3 flex justify-between text-xs uppercase tracking-wider text-slate-500">
                    <span>Progress</span>
                    <span>{progress}%</span>
                </div>
                

                <div className="h-2 overflow-hidden rounded-full bg-slate-800">

                    <div
                    className="h-full rounded-full bg-blue-500 transition-all duration-700"
                    style={{ width: `${progress}%` }}
                    ></div>

                </div>

                <p className="mt-6 text-sm text-slate-400">
                    {stages[currentStage].detail}
                </p>

                </div>
            </p>

        </div>

        </div>
    );
}