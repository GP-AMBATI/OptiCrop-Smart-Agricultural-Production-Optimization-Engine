import { ArrowRight } from 'lucide-react';
import { UseFormRegister, UseFormHandleSubmit, UseFormStateReturn } from 'react-hook-form';

interface FormValues {
  n: string;
  p: string;
  k: string;
  temperature: string;
  humidity: string;
  ph: string;
  rainfall: string;
}

interface RecommendationFormProps {
  register: UseFormRegister<FormValues>;
  handleSubmit: UseFormHandleSubmit<FormValues>;
  formState: UseFormStateReturn<FormValues>;
  onSubmit: (data: FormValues) => void;
  loading: boolean;
}

const inputFields: Array<{ label: string; name: keyof FormValues; unit?: string; min?: number; max?: number; step?: number }> = [
  { label: 'Nitrogen (N)', name: 'n', unit: 'mg/kg', min: 0, max: 150, step: 1 },
  { label: 'Phosphorus (P)', name: 'p', unit: 'mg/kg', min: 0, max: 150, step: 1 },
  { label: 'Potassium (K)', name: 'k', unit: 'mg/kg', min: 0, max: 150, step: 1 },
  { label: 'Temperature', name: 'temperature', unit: '°C', min: 0, max: 50, step: 0.1 },
  { label: 'Humidity', name: 'humidity', unit: '%', min: 0, max: 100, step: 0.1 },
  { label: 'Soil pH', name: 'ph', min: 0, max: 14, step: 0.1 },
  { label: 'Rainfall', name: 'rainfall', unit: 'mm', min: 0, max: 500, step: 0.1 },
];

export default function RecommendationForm({ register, handleSubmit, formState, onSubmit, loading }: RecommendationFormProps) {
  return (
    <div className="rounded-[36px] border border-slate-200/80 bg-white/90 p-8 shadow-soft backdrop-blur-xl">
      <div className="mb-8 flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <p className="text-sm font-semibold uppercase tracking-[0.24em] text-primary">Predict Your Best Crop</p>
          <h2 className="mt-3 text-3xl font-bold text-slate-900">Enter field conditions to get a recommendation.</h2>
        </div>
        <div className="rounded-3xl bg-slate-100 px-4 py-3 text-sm text-slate-600 shadow-sm">Model accuracy: 92.4%</div>
      </div>

      <form onSubmit={handleSubmit(onSubmit)} className="grid gap-6 lg:grid-cols-2">
        {inputFields.map((field) => (
          <label key={field.name} className="grid gap-3 rounded-3xl border border-slate-200/80 bg-slate-50 p-4">
            <span className="text-sm font-semibold text-slate-700">{field.label}</span>
            <input
              type="number"
              step={field.step}
              min={field.min}
              max={field.max}
              {...register(field.name, { required: true })}
              className="w-full rounded-3xl border border-slate-200 bg-white px-4 py-4 text-slate-900 shadow-sm outline-none transition focus:border-primary focus:ring-2 focus:ring-primary/20"
            />
            <span className="text-xs text-slate-500">{field.unit || 'Value'}</span>
          </label>
        ))}

        <div className="lg:col-span-2 rounded-3xl border border-slate-200/80 bg-gradient-to-r from-primary/10 to-darkgreen/10 p-6">
          <div className="flex items-center justify-between gap-4 text-slate-700">
            <div>
              <h3 className="text-lg font-semibold">Ready for smarter crop decisions?</h3>
              <p className="mt-2 text-sm leading-6 text-slate-600">Use your soil and weather data to predict the most profitable crop for your fields.</p>
            </div>
            <button
              type="submit"
              disabled={loading}
              className="inline-flex items-center gap-2 rounded-full bg-slate-900 px-6 py-3 text-sm font-semibold text-white transition hover:bg-slate-800 disabled:cursor-not-allowed disabled:opacity-60"
            >
              {loading ? 'Analyzing…' : 'Generate Recommendation'}
              <ArrowRight size={18} />
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}
