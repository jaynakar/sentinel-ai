import FraudDistributionChart from "./FraudDistributionChart";
// We'll create this in the next step
import RiskDistributionChart from "./RiskDistributionChart";

export default function AnalyticsSection({
  transactionsProcessed,
  fraudAlerts,
}) {
  return (

    <section className="mt-12">

    <div className="mb-5 flex items-center gap-4">
        <p className="text-xs font-semibold uppercase tracking-[0.25em] text-slate-500">
            Analysis
        </p>

        <div className="h-px flex-1 bg-slate-800" />
    </div>

  <div className="grid gap-6 lg:grid-cols-2">

    <FraudDistributionChart
      totalTransactions={transactionsProcessed}
      fraudAlerts={fraudAlerts}
    />

    <RiskDistributionChart />

  </div>

</section>


//     <section className="mt-13">
// {/* 
//       Section Header
//         <p className="mb-4 text-xs font-semibold uppercase tracking-[0.2em] text-slate-500">
//         Analysis
//         </p>
// */}

//       {/* Charts */}
//       <div className="grid gap-6 lg:grid-cols-2">

//         <FraudDistributionChart
//           totalTransactions={transactionsProcessed}
//           fraudAlerts={fraudAlerts}
//         />

//         <RiskDistributionChart />

//       </div>

//     </section>

  );
}