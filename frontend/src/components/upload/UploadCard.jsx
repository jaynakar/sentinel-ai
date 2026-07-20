import { useState, useRef } from "react";
import { Upload, FileText, CheckCircle } from "lucide-react";
import sentinelLogo from "../../assets/sentinel-logo.png";
import ProcessingPanel from "../processing/ProcessingPanel";


export default function UploadCard({
    appState,
    setAppState,
    setAnalysisData,
}) {

  const [selectedFile, setSelectedFile] = useState(null);
  const fileInputRef = useRef(null);

  const handleAnalyze = () => {
      setAppState("processing");
  };

  return (
    <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-8 shadow-xl">
      <div className="text-center">
        <h2 className="text-2xl font-bold">
          Analyze Transaction Dataset
        </h2>

        <p className="mt-2 text-slate-400">
          Upload a transaction dataset to detect fraudulent activity,
          generate explainable predictions, and create an investigation report.
        </p>
      </div>

      <div
        className={`mt-8 min-h-[420px] rounded-xl border-2 border-dashed bg-slate-950 p-8 transition-all duration-300
          ${
            selectedFile
              ? "border-slate-700"
              : "border-slate-700 hover:border-blue-500"
          }`}
      >
        <div className="flex min-h-[320px] flex-col items-center justify-center">

            {appState === "processing" ? (

              <ProcessingPanel
                onComplete={() => {
                  setAnalysisData({
                    transactionsProcessed: 1247,
                    fraudAlerts: 18,
                    highestRisk: 98.6,
                    confidence: 99.2,
                  });

                  setAppState("results");
                }}
              />

            ) : !selectedFile ? (
            <>

              <Upload size={48} className="text-blue-400" />

              <h3 className="mt-4 text-xl font-semibold">
                Drag & Drop CSV File
              </h3>

              <p className="mt-2 text-slate-400">
                or click below to browse
              </p>

              <input
                ref={fileInputRef}
                type="file"
                accept=".csv"
                className="hidden"
                onChange={(e) => {
                  if (e.target.files.length > 0) {
                    setSelectedFile(e.target.files[0]);
                  }
                }}
              />

              <button
                onClick={() => fileInputRef.current.click()}
                className="mt-6 rounded-lg bg-blue-600 px-6 py-3 font-semibold transition hover:bg-blue-700"
              >
                Select CSV File
              </button>

              <div className="mt-6 flex items-center gap-2 text-sm text-slate-500">
                <FileText size={18} />
                <span>CSV files only</span>
              </div>

            </>
          ) : (
            <>

              <div className="relative mb-5 flex h-20 w-20 items-center justify-center">

                  <div className="absolute inset-0 rounded-full bg-blue-500/80 blur-xl"></div>

                  <div
                    className="
                    mb-1
                    flex
                    h-20
                    w-24
                    items-center
                    justify-center
                    rounded-full
                    border
                    border-slate-800
                    bg-slate-900
                    transition-all
                    duration-500
                    "
                  >
                    {/* Logo */}
                    <img
                      src={sentinelLogo}
                      alt="Sentinel AI"
                      className="h-14 w-auto"
                    />
                    
                  </div>
                        
                  
              </div>

              <h3 className="mt-2 text-2xl font-bold tracking-tight text-white">
                {selectedFile.name}
              </h3>

              <p className="mt-1 text-sm text-slate-400">
                CSV • {(selectedFile.size / 1024).toFixed(2)} KB
              </p>

              <p
                className={`mt-5 flex items-center gap-2 rounded-full px-4 py-2 text-sm font-medium ${
                  appState === "results"
                    ? "bg-blue-500/10 text-blue-400"
                    : "bg-green-500/10 text-green-400"
                }`}
              >
                <CheckCircle size={18} />

                {appState === "results"
                  ? "Analysis Complete"
                  : "Ready for Analysis"}
              </p>

              {/* {appState === "results" && (
                <p className="mt-4 max-w-md text-center text-sm text-slate-400">
                  Your dataset has been analyzed successfully.
                  Review the dashboard insights below or upload another dataset.
                </p>
              )} */}

              <button
                onClick={() => {

                  if (appState === "results") {

                    setSelectedFile(null);
                    setAppState("idle");

                    if (fileInputRef.current) {
                      fileInputRef.current.value = "";
                    }

                  } else {

                    handleAnalyze();

                  }

                }}
                className="mt-6 rounded-lg bg-blue-600 px-8 py-3 text-base font-semibold transition hover:bg-blue-700"
              >
                {appState === "results"
                    ? "Upload New Dataset"
                    : "Analyze Dataset"}
              </button>

              <button
                onClick={() => setSelectedFile(null)}
                className="mt-3 text-sm text-slate-400 hover:text-white"
              >
                ↻ Choose Different File
              </button>

            </>
          )}

        </div>
      </div>
    </section>
  );
}