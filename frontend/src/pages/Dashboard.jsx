import { useState } from "react";
import Layout from "../components/common/Layout";
import Header from "../components/common/Header";
import UploadCard from "../components/upload/UploadCard";
import SummaryCards from "../components/dashboard/SummaryCards";
import AnalyticsSection from "../components/charts/AnalyticsSection";


export default function Dashboard() {

    const [analysisData, setAnalysisData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [appState, setAppState] = useState("idle");
    
    return (
        <Layout>
        <div className="space-y-8 p-8">
            <Header />
            <UploadCard
                appState={appState}
                setAppState={setAppState}
                setAnalysisData={setAnalysisData}
            />

            <SummaryCards
                appState={appState}
                analysisData={analysisData}
            />
            <AnalyticsSection
                // transactionsProcessed={
                //     analysisData?.transactionsProcessed ?? 0
                // }
                // fraudAlerts={
                //     analysisData?.fraudAlerts ?? 0
                // }
                transactionsProcessed={1247}
                fraudAlerts={18}
            />
        </div>
        </Layout>
    );
    }