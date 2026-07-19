import { Upload, FileText } from "lucide-react";


export default function UploadCard() {
  return (
    <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-8 shadow-xl">
      <div className="text-center">
        <h2 className="text-2xl font-bold">
          Upload Transaction Dataset
        </h2>

        <p className="mt-2 text-slate-400">
          Upload a CSV file to analyze transactions for potential fraud.
        </p>
      </div>

      <div className="mt-8 rounded-xl border-2 border-dashed border-slate-700 bg-slate-950 p-8 transition hover:border-blue-500">
        <div className="flex flex-col items-center">
          <Upload size={48} className="text-blue-400" />

          <h3 className="mt-4 text-xl font-semibold">
            Drag & Drop CSV File
          </h3>

          <p className="mt-2 text-slate-400">
            or click below to browse
          </p>

          <button className="mt-6 rounded-lg bg-blue-600 px-6 py-3 font-semibold transition hover:bg-blue-700">
            Select CSV File
          </button>

          <div className="mt-6 flex items-center gap-2 text-sm text-slate-500">
            <FileText size={18} />
            CSV files only
          </div>
        </div>
      </div>
    </section>
  );
}