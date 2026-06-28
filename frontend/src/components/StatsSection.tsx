import { BarChart3 } from 'lucide-react';

const stats = [
  { label: 'Crops Supported', value: '22+' },
  { label: 'Farmers Enabled', value: '12K+' },
  { label: 'Prediction Accuracy', value: '92%' },
  { label: 'Data Sources', value: '5' },
];

export default function StatsSection() {
  return (
    <div className="grid gap-6 lg:grid-cols-4">
      {stats.map((stat) => (
        <div key={stat.label} className="rounded-[28px] border border-white/10 bg-white/10 p-7 text-white shadow-soft backdrop-blur-xl">
          <p className="text-sm uppercase tracking-[0.2em] text-green-200">{stat.label}</p>
          <p className="mt-4 text-4xl font-semibold">{stat.value}</p>
        </div>
      ))}
    </div>
  );
}
