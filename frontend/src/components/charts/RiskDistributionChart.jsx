import ChartCard from "./ChartCard";
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";

const data = [
  { level: "Very Low", count: 780 },
  { level: "Low", count: 310 },
  { level: "Medium", count: 98 },
  { level: "High", count: 42 },
  { level: "Critical", count: 17 },
];



export default function RiskDistributionChart() {

    function CustomTooltip({ active, payload, label }) {

        if (!active || !payload?.length) return null;

        const isCritical = label === "Critical";

        return (

            <div className="rounded-xl border border-slate-700 bg-slate-900 px-4 py-3 shadow-xl">

                <p
                    className={`text-sm font-semibold ${
                        isCritical
                            ? "text-red-400"
                            : "text-white"
                    }`}
                >
                    {isCritical ? "Critical Risk" : label}
                </p>

                <p className="mt-1 text-sm text-slate-300">
                    {payload[0].value} Transactions
                </p>

            </div>

        );
    }

    return (

        <ChartCard
        title="Transaction Risk Distribution"
        description="Risk score distribution across transactions"
        >
            <div className="h-[280px]">
                <ResponsiveContainer width="100%" height="100%">
                    <BarChart
                        data={data}
                        margin={{
                            top: 10,
                            right: 10,
                            left: -20,
                            bottom: 10,
                            
                        }}
                        >
                            <CartesianGrid
                                vertical={false}
                                stroke="#1e293b"
                            />
                            <XAxis
                                dataKey="level"
                                axisLine={false}
                                tickLine={false}
                                tick={{
                                    fill: "#64748b",
                                    fontSize: 11,
                                }}
                            />
                            <YAxis
                                axisLine={false}
                                tickLine={false}
                                tick={{
                                    fill: "#94a3b8",
                                    fontSize: 12,
                                }}
                            />
                            <Tooltip
                                cursor={{
                                    fill: "rgba(59,130,246,0.05)"
                                }}
                                content={<CustomTooltip />}
                            />
                            <Bar
                                dataKey="count"
                                radius={[10,10,0,0]}
                                barSize={30}
                            >
                                {data.map((entry, index) => (
                                    <Cell
                                        key={index}
                                        fill={
                                            entry.level === "Critical"
                                                ? "#ef4444"
                                                : "#3b82f6"
                                        }
                                    />
                                ))}
                            </Bar>

                    </BarChart>
                </ResponsiveContainer>
            </div>
        </ChartCard>
  );
}