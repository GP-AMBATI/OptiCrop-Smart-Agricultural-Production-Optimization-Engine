export default function Footer() {
  return (
    <footer className="border-t border-slate-200/60 bg-white/90 py-10 text-slate-700">
      <div className="mx-auto flex max-w-7xl flex-col gap-6 px-6 sm:px-8 lg:px-10 xl:flex-row xl:items-center xl:justify-between">
        <div>
          <p className="text-lg font-semibold text-slate-900">OptiCrop</p>
          <p className="mt-3 max-w-xl text-sm leading-6 text-slate-600">Built for farmers, agronomists, and field managers who want AI-powered crop planning with a premium UX.</p>
        </div>
        <div className="flex flex-wrap items-center gap-4 text-sm text-slate-600">
          <a href="#" className="transition hover:text-slate-900">Privacy</a>
          <a href="#" className="transition hover:text-slate-900">Terms</a>
          <a href="#" className="transition hover:text-slate-900">Contact</a>
        </div>
      </div>
    </footer>
  );
}
