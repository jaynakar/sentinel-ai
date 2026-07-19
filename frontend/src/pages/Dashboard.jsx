import { useState } from "react";
import Layout from "../components/common/Layout";
import Header from "../components/common/Header";
import UploadCard from "../components/upload/UploadCard";
import SummaryCards from "../components/dashboard/SummaryCards";


export default function Dashboard() {

    const [analysisData, setAnalysisData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    
    return (
        <Layout>
        <div className="space-y-8 p-8">
            <Header />
            <UploadCard />
            <SummaryCards />
        </div>
        </Layout>
    );
    }