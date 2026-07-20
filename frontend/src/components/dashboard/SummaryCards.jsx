import {
  CreditCard,
  ShieldAlert,
  TriangleAlert,
  BadgeCheck,
} from "lucide-react";

import SummaryCard from "./SummaryCard";
import { motion } from "framer-motion";

export default function SummaryCards({
    appState,
    analysisData,
}) {

  const cards = [
    {
      title: "Transactions Processed",
      value:
        appState === "results"
          ? analysisData?.transactionsProcessed
          : "--",
      subtitle:
        appState === "results"
          ? "Transactions analyzed"
          : "Awaiting analysis",
      icon: <CreditCard size={28} />,
      color: "blue",
    },

    {
      title: "Fraud Alerts",
      value:
        appState === "results"
          ? analysisData?.fraudAlerts
          : "--",
      subtitle:
        appState === "results"
          ? "Fraudulent transactions detected"
          : "Awaiting analysis",
      icon: <ShieldAlert size={28} />,
      color: "red",
    },

    {
      title: "Highest Risk Score",
      value:
        appState === "results"
          ? analysisData?.highestRisk
          : "--",
      subtitle:
        appState === "results"
          ? "Maximum fraud probability"
          : "Awaiting analysis",
      icon: <TriangleAlert size={28} />,
      color: "amber",
    },

    {
      title: "Model Confidence",
      value:
        appState === "results"
          ? analysisData?.confidence
          : "--",
      subtitle:
        appState === "results"
          ? "Overall prediction confidence"
          : "Awaiting analysis",
      icon: <BadgeCheck size={28} />,
      color: "green",
    },
  ];

  return (
    <section className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

      {cards.map((card, index) => (
        <motion.div
          key={card.title}
          initial={{ opacity: 0, y: 30 }}
          animate={{
            opacity: appState === "results" ? 1 : 0.6,
            y: appState === "results" ? 0 : 30,
          }}
          transition={{
            duration: 0.55,
            delay: appState === "results" ? index * 0.18 : 0,
            ease: "easeOut",
          }}
        >
          <SummaryCard
            title={card.title}
            value={card.value}
            subtitle={card.subtitle}
            icon={card.icon}
            color={card.color}
          />
        </motion.div>
      ))}

    </section>
  );
}