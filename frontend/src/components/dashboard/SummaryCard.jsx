export default function SummaryCard({
  title,
  value,
  subtitle,
  icon,
  color = "blue",
}) {
  const colors = {
    blue: "bg-blue-500/10 border-blue-500/30 text-blue-400",
    green: "bg-emerald-500/10 border-emerald-500/30 text-emerald-400",
    amber: "bg-amber-500/10 border-amber-500/30 text-amber-400",
    red: "bg-red-500/10 border-red-500/30 text-red-400",
  };

  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6 transition-all duration-300 hover:-translate-y-1 hover:border-blue-500/40 hover:shadow-xl hover:shadow-blue-500/5">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm uppercase tracking-wide text-slate-400">
            {title}
          </p>

          <h2 className="mt-3 text-3xl font-bold text-white">
            {value}
          </h2>

          <p className="mt-2 text-sm text-slate-500">
            {subtitle}
          </p>
        </div>

        <div className={`rounded-xl border p-4 ${colors[color]}`}>
          {icon}
        </div>
      </div>
    </div>
  );
}