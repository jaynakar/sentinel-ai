export default function ChartCard({
  title,
  description,
  children,
}) {
  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">

      <div>
        <h3 className="text-lg font-semibold text-white">
          {title}
        </h3>

        {description && (
          <p className="mt-1 text-sm text-slate-400">
            {description}
          </p>
        )}

        <div className="mt-4 border-t border-slate-800" />
      </div>

      <div className="mt-6">
        {children}
      </div>

    </div>
  );
}