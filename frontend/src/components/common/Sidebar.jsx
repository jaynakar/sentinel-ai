import {
  LayoutDashboard,
  BarChart3,
  FileText,
  Settings,
  ShieldCheck,
} from "lucide-react";
import logo from "../../assets/sentinel-logo-horizontal.png";


const menuItems = [
  { icon: LayoutDashboard, label: "Dashboard", active: true },
  { icon: BarChart3, label: "Analytics" },
  { icon: FileText, label: "Reports" },
  { icon: Settings, label: "Settings" },
];

export default function Sidebar() {
  return (
    <aside className="w-72 bg-slate-900 border-r border-slate-800 flex flex-col">
      <div className="flex justify-center items-center py-6 border-b border-slate-800">

        <div>
            <img
                src={logo}
                alt="Sentinel AI"
                className="w-58 h-auto"
            />
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