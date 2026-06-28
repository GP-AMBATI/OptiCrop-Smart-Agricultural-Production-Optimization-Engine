interface FeatureCardProps {
  title: string;
  Icon: React.ComponentType<any>;
}

export default function FeatureCard({ title, Icon }: FeatureCardProps) {
  return (
    <div className="rounded-[28px] border border-slate-200/80 bg-white/95 p-6 shadow-soft">
      <div className="inline-flex h-12 w-12 items-center justify-center rounded-3xl bg-green-50 text-green-700 shadow-sm">
        <Icon className="h-6 w-6" />
      </div>
      <h3 className="mt-5 text-lg font-semibold text-slate-900">{title}</h3>
      <p className="mt-3 text-sm leading-6 text-slate-600">{`Designed to modernize crop selection with intuitive, AI-backed support.`}</p>
    </div>
  );
}
