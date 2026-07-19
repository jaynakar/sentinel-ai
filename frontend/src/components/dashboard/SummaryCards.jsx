import {
  CreditCard,
  ShieldAlert,
  TriangleAlert,
  BadgeCheck,
} from "lucide-react";

import SummaryCard from "./SummaryCard";

export default function SummaryCards() {
  return (
    <section className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

      <SummaryCard
        title="Transactions"
        value="--"
        subtitle="Awaiting analysis"
        icon={<CreditCard size={28} />}
        color="blue"
      />

      <SummaryCard
        title="Fraud Detected"
        value="--"
        subtitle="Awaiting analysis"
        icon={<ShieldAlert size={28} />}
        color="red"
      />

      <SummaryCard
        title="Highest Risk"
        value="--"
        subtitle="Awaiting analysis"
        icon={<TriangleAlert size={28} />}
        color="amber"
      />

      <SummaryCard
        title="Confidence"
        value="--"
        subtitle="Awaiting analysis"
        icon={<BadgeCheck size={28} />}
        color="green"
      />

    </section>
  );
}