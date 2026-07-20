import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Label,
} from "recharts";

import ChartCard from "./ChartCard";


function LegendItem({ color, label, value, percentage }) {
  return (
    <div className="py-2 flex items-center justify-between">

      <div className="flex items-center gap-3">

        <div
            className="h-2.5 rounded-full transition-all duration-500"
            style={{
                width: `${Math.min(
                    70,
                    Math.max(12, percentage * 0.7)
                )}px`,
                backgroundColor: color,
            }}
        />

        <span className="text-sm text-slate-300">
          {label}
        </span>

      </div>

      <div className="flex items-center gap-8">

        <span className="w-12 text-right text-sm font-medium text-white">
          {value}
        </span>

        <span className="w-12 text-right text-sm text-slate-400">
          {percentage}%
        </span>

      </div>

    </div>
  );
}


export default function FraudDistributionChart({
  totalTransactions,
  fraudAlerts,
}) {
    const legitimate = totalTransactions - fraudAlerts;

    const data = [
        {
        name: "Legitimate",
        value: legitimate,
        },
        {
        name: "Fraud",
        value: fraudAlerts,
        },
    ];

    const legitimatePercentage =
        ((legitimate / totalTransactions) * 100).toFixed(1);

    const fraudPercentage =
        ((fraudAlerts / totalTransactions) * 100).toFixed(1);

    const COLORS = [
        "#3B82F6", // Blue
        "#EF4444", // Red
    ];

  return (
    <ChartCard
        title="Fraud Overview"
        description="Distribution of analyzed transactions"
        >
        <div className="flex flex-col">

            {/* Chart */}
            <div className="flex h-[240px] items-center justify-center">

            <div className="flex justify-center">
            <PieChart width={280} height={220}>

            <Pie
                data={data}
                dataKey="value"
                cx="50%"
                cy="45%"
                innerRadius={70}
                outerRadius={100}
                paddingAngle={3}
                stroke="none"
            >
                {data.map((entry, index) => (
                <Cell
                    key={entry.name}
                    fill={COLORS[index]}
                />
                ))}

                <Label
                    content={({ viewBox }) => {
                        const { cx, cy } = viewBox;

                        return (
                        <g>
                            <text
                            x={cx}
                            y={cy - 6}
                            textAnchor="middle"
                            fill="#FFFFFF"
                            fontSize="28"
                            fontWeight="700"
                            >
                            {fraudAlerts}
                            </text>

                            <text
                            x={cx}
                            y={cy + 20}
                            textAnchor="middle"
                            fill="#94A3B8"
                            fontSize="14"
                            >
                            Fraud
                            </text>
                        </g>
                        );
                    }}
                />
            </Pie>

            </PieChart>
            </div>

        </div>

        {/* Legend */}
        <div className="mt-4 border-t border-slate-800 pt-4 space-y-3">

            <LegendItem
            color="#3B82F6"
            label="Legitimate"
            value={legitimate}
            percentage={Number(legitimatePercentage)}
            />

            <LegendItem
            color="#EF4444"
            label="Fraud"
            value={fraudAlerts}
            percentage={Number(fraudPercentage)}
            />

        </div>

        </div>
    </ChartCard>
  );
}