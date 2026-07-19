import {
  LayoutDashboard,
  BarChart3,
  FileText,
  Settings,
  ShieldCheck,
} from "lucide-react";

const menuItems = [
  { icon: LayoutDashboard, label: "Dashboard", active: true },
  { icon: BarChart3, label: "Analytics" },
  { icon: FileText, label: "Reports" },
  { icon: Settings, label: "Settings" },
];

export default function Sidebar() {
  return (
    <aside className="w-80 bg-slate-900 border-r border-slate-800 flex flex-col">
      <div className="flex items-center gap-3 px-6 py-8 border-b border-slate-800">
        <div className="rounded-xl bg-blue-600 p-3">
          <ShieldCheck size={28} />
        </div>

        <div>
            <h2 className="font-bold text-xl tracking-wide text-white">
            HFDP
            </h2>

            <p className="text-slate-400 text-sm">
            Hybrid Fraud Platform
            </p>
        </div>
      </div>

      <nav className="flex-1 p-5">
        <ul className="space-y-3">
          {menuItems.map(({ icon: Icon, label, active }) => (
            <li key={label}>
              <button
                className={`flex w-full items-center gap-3 rounded-xl px-4 py-3 transition ${
                  active
                    ? "bg-blue-600 text-white"
                    : "text-slate-400 hover:bg-slate-800 hover:text-white"
                }`}
              >
                <Icon size={20} />
                {label}
              </button>
            </li>
          ))}
        </ul>
      </nav>
    </aside>
  );
}