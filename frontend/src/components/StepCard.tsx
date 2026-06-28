interface StepCardProps {
  step: number;
  title: string;
  description: string;
  Icon: React.ComponentType<any>;
}

export default function StepCard({ step, title, description, Icon }: StepCardProps) {
  return (
    <article className="rounded-[32px] border border-slate-200/80 bg-white/95 p-8 shadow-soft transition hover:-translate-y-1 hover:shadow-xl">
      <div className="mb-6 inline-flex h-12 w-12 items-center justify-center rounded-3xl bg-gradient-to-br from-primary to-darkgreen text-white shadow-lg">
        <span className="text-lg font-semibold">{step}</span>
      </div>
      <div className="mb-4 inline-flex h-14 w-14 items-center justify-center rounded-3xl bg-slate-100 text-slate-900 shadow-sm">
        <Icon className="h-6 w-6" />
      </div>
      <h3 className="text-xl font-semibold text-slate-900">{title}</h3>
      <p className="mt-4 text-sm leading-6 text-slate-600">{description}</p>
    </article>
  );
}
