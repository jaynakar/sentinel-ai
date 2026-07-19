export default function ResultsDashboard() {
  return (
    <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-10">

      <div className="flex flex-col items-center">

        <div className="flex h-20 w-20 items-center justify-center rounded-full bg-green-500/10">

          <svg
            className="h-10 w-10 text-green-500"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.5"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M5 13l4 4L19 7"
            />
          </svg>

        </div>

        <h2 className="mt-6 text-3xl font-bold text-white">
          Analysis Complete
        </h2>

        <p className="mt-2 text-slate-400">
          Sentinel AI successfully analyzed your transaction dataset.
        </p>

      </div>

    </section>
  );
}