import { Activity } from "lucide-react";

export default function Header() {
  return (
    <header className="flex items-center justify-between rounded-2xl border border-slate-800 bg-slate-900 px-8 py-6">
      <div>
        <h1 className="text-3xl font-bold text-white">
          Dashboard
        </h1>

        <p className="mt-1 text-slate-400">
          AI-powered Financial Fraud Detection Platform
        </p>
      </div>

      <div className="flex items-center gap-6">

        <div className="text-right">
          <p className="text-xs uppercase tracking-wide text-slate-500">
            Last Analysis
          </p>

          <p className="text-white font-semibold">
            Never
          </p>
        </div>

        <div className="flex items-center gap-2 rounded-full bg-green-500/10 px-4 py-2">
          <Activity size={16} className="text-green-400" />

          <span className="text-sm font-semibold text-green-300">
            System Online
          </span>
        </div>

      </div>
    </header>
  );
}