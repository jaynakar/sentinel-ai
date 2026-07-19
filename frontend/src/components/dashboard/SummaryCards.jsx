import {
  CreditCard,
  ShieldAlert,
  TriangleAlert,
  BadgeCheck,
} from "lucide-react";

import SummaryCard from "./SummaryCard";

export default function SummaryCards({ appState }) {
  return (
    <section className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

      <SummaryCard
        title="Transactions Processed"
        value={appState === "results" ? "1,247" : "--"}
        subtitle={appState === "results" ? "Transactions analyzed" : "Awaiting analysis"}
        icon={<CreditCard size={28} />}
        color="blue"
      />

      <SummaryCard
        title="Fraud Alerts"
        value={appState === "results" ? "18" : "--"}
        subtitle={appState === "results" ? "High-risk transactions" : "Awaiting analysis"}
        icon={<ShieldAlert size={28} />}
        color="red"
      />

      <SummaryCard
        title="Highest Risk Score"
        value={appState === "results" ? "98.6%" : "--"}
        subtitle={appState === "results" ? "Maximum fraud probability" : "Awaiting analysis"}
        icon={<TriangleAlert size={28} />}
        color="amber"
      />

      <SummaryCard
        title="Model Confidence"
        value={appState === "results" ? "99.2%" : "--"}
        subtitle={appState === "results" ? "Model confidence" : "Awaiting analysis"}
        icon={<BadgeCheck size={28} />}
        color="green"
      />

    </section>
  );
}