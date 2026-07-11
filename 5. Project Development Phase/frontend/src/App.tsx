import { AnimatePresence, motion } from 'framer-motion';
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import {
  ArrowRight,
  BarChart3,
  Brain,
  CheckCircle2,
  ChevronDown,
  Clipboard,
  Eye,
  Leaf,
  ShieldCheck,
  Sparkles,
  Shield,
  Target,
  User,
  Users,
  Zap,
} from 'lucide-react';
import FeatureCard from './components/FeatureCard';
import Footer from './components/Footer';
import Hero from './components/Hero';
import Navbar from './components/Navbar';
import RecommendationForm from './components/RecommendationForm';
import ResultDisplay from './components/ResultDisplay';
import StepCard from './components/StepCard';
import StatsSection from './components/StatsSection';

function ClipboardIcon(props: React.ComponentProps<'svg'>) {
  return <Clipboard {...props} />;
}

const steps = [
  {
    title: 'Enter Soil & Weather Data',
    icon: ClipboardIcon,
    description: 'Add N, P, K, temperature, humidity, pH, and rainfall metrics to begin.',
  },
  {
    title: 'AI Analysis',
    icon: Brain,
    description: 'Your inputs are processed with advanced machine learning models.',
  },
  {
    title: 'Best Crop Recommendation',
    icon: Leaf,
    description: 'Receive the optimal crop choice for your field and conditions.',
  },
  {
    title: 'Improve Yield',
    icon: BarChart3,
    description: 'Use the result to increase productivity and sustainability.',
  },
];

const features = [
  {
    title: 'Smart Recommendations',
    subtitle: 'Personalized crop suggestions based on soil science.',
    icon: Leaf,
  },
  {
    title: 'Accurate & Reliable',
    subtitle: 'Validated model predictions with stable results.',
    icon: ShieldCheck,
  },
  {
    title: 'Data-Driven Insights',
    subtitle: 'Meaningful analytics for sustainable planning.',
    icon: BarChart3,
  },
];

const benefits = [
  {
    title: 'Combine Soil, Climate & Weather',
    icon: Leaf,
  },
  {
    title: 'Advanced Machine Learning',
    icon: Brain,
  },
  {
    title: 'Increase Productivity',
    icon: BarChart3,
  },
  {
    title: 'Sustainable Agriculture',
    icon: Zap,
  },
];

interface FormValues {
  n: string;
  p: string;
  k: string;
  temperature: string;
  humidity: string;
  ph: string;
  rainfall: string;
}

function App() {
  const [isDark, setIsDark] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [result, setResult] = useState<{ crop: string; confidence: number } | null>(null);
  const { register, handleSubmit, formState } = useForm<FormValues>({
    defaultValues: {
      n: '90',
      p: '40',
      k: '40',
      temperature: '25',
      humidity: '80',
      ph: '6.5',
      rainfall: '200',
    },
  });

  const onSubmit = async (data: FormValues) => {
    setSubmitted(true);
    try {
      const response = await fetch('/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          n: parseFloat(data.n),
          p: parseFloat(data.p),
          k: parseFloat(data.k),
          temperature: parseFloat(data.temperature),
          humidity: parseFloat(data.humidity),
          ph: parseFloat(data.ph),
          rainfall: parseFloat(data.rainfall),
        }),
      });

      const responseData = await response.json();
      if (responseData.crop) {
        setResult({
          crop: responseData.crop,
          confidence: responseData.confidence,
        });
      }
    } catch (error) {
      console.error('Error:', error);
    } finally {
      window.setTimeout(() => setSubmitted(false), 1900);
    }
  };

  return (
    <div className={isDark ? 'bg-slate-950 text-slate-100' : 'bg-background text-slate-900'}>
      <Navbar onToggleTheme={() => setIsDark(!isDark)} />
      <main className="relative overflow-hidden">
        <div className="pointer-events-none absolute inset-x-0 top-0 -z-10 h-[560px] bg-[radial-gradient(circle_at_top,_rgba(22,163,74,0.14),_transparent_46%)]" />
        <div className="pointer-events-none absolute right-0 top-24 -z-10 h-72 w-72 rounded-full bg-gradient-to-br from-primary to-darkgreen opacity-30 blur-3xl" />

        <section className="mx-auto max-w-7xl px-6 py-16 sm:px-8 lg:px-10">
          <Hero features={features} />
        </section>

        <section className="mx-auto max-w-7xl px-6 pb-24 sm:px-8 lg:px-10">
          {result ? (
            <ResultDisplay crop={result.crop} confidence={result.confidence} />
          ) : (
            <RecommendationForm
              register={register}
              handleSubmit={handleSubmit}
              formState={formState}
              onSubmit={onSubmit}
              loading={submitted}
            />
          )}
        </section>

        <section className="mx-auto max-w-7xl px-6 pb-12 sm:px-8 lg:px-10">
          <div className="text-center">
            <span className="inline-flex rounded-full border border-green-200 bg-lightgreen px-4 py-1 text-sm font-semibold uppercase tracking-[0.18em] text-darkgreen">
              How It Works
            </span>
            <h2 className="mt-6 text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">How It Works</h2>
            <p className="mx-auto mt-4 max-w-2xl text-base text-slate-600">OptiCrop turns raw agricultural data into high-confidence crop action plans with a premium AI workflow.</p>
          </div>

          <div className="mt-14 grid gap-6 lg:grid-cols-4">
            {steps.map((step, index) => (
              <StepCard key={step.title} step={index + 1} title={step.title} Icon={step.icon} description={step.description} />
            ))}
          </div>
        </section>

        <section className="bg-darkgreen px-6 py-16 text-white sm:px-8 lg:px-10">
          <div className="mx-auto max-w-7xl">
            <div className="mb-12 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
              <div>
                <p className="uppercase tracking-[0.24em] text-green-200">Trusted by modern farms</p>
                <h2 className="mt-3 text-3xl font-bold text-white sm:text-4xl">AI crop insights that feel premium.</h2>
              </div>
              <div className="rounded-full bg-white/10 px-5 py-3 text-sm text-white/90 shadow-soft backdrop-blur-xl">22+ crop varieties, 2.2k samples, and rising.</div>
            </div>

            <StatsSection />
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
}

export default App;
