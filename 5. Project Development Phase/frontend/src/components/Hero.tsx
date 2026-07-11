import { motion } from 'framer-motion';
import { ArrowRight, Leaf, ShieldCheck, BarChart3, Sparkles, Brain } from 'lucide-react';
import FeatureCard from './FeatureCard';

interface HeroProps {
  features: Array<{ title: string; subtitle: string; icon: React.ComponentType<any> }>;
}

export default function Hero({ features }: HeroProps) {
  return (
    <div className="grid items-center gap-12 lg:grid-cols-[1.05fr_0.95fr]">
      <motion.div initial={{ opacity: 0, x: -40 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.7 }}>
        <div className="inline-flex items-center gap-3 rounded-full border border-green-200 bg-lightgreen px-4 py-2 text-sm font-semibold text-darkgreen shadow-sm">
          <Leaf className="h-4 w-4" />
          Premium AI for sustainable agriculture
        </div>
        <h1 className="mt-8 max-w-3xl text-5xl font-bold tracking-tight text-slate-900 sm:text-6xl">
          AI-Powered <span className="text-primary">Crop Recommendation</span> for Optimal Agriculture
        </h1>
        <p className="mt-6 max-w-2xl text-lg leading-8 text-slate-600">
          OptiCrop analyzes soil nutrients, weather conditions, rainfall, humidity and environmental data to recommend the most suitable crop using machine learning.
        </p>

        <div className="mt-10 grid gap-4 sm:grid-cols-3">
          <FeatureCard title="Smart Recommendations" Icon={Leaf} />
          <FeatureCard title="Accurate & Reliable" Icon={ShieldCheck} />
          <FeatureCard title="Data-Driven Insights" Icon={BarChart3} />
        </div>

        <button className="mt-10 inline-flex items-center gap-3 rounded-[22px] bg-gradient-to-r from-primary to-darkgreen px-6 py-4 text-base font-semibold text-white shadow-glow transition duration-300 hover:-translate-y-0.5 hover:shadow-xl">
          Start Prediction
          <ArrowRight size={18} />
        </button>
      </motion.div>

      <motion.div initial={{ opacity: 0, y: 40 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.7 }} className="relative">
        <div className="glass-card relative overflow-hidden rounded-[32px] border border-white/70 p-6 shadow-soft">
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_left,_rgba(22,163,74,0.28),_transparent_30%)]" />
          <div className="relative rounded-[28px] bg-slate-950/95 p-8 text-white shadow-2xl">
            <div className="h-[420px] rounded-[28px] bg-[url('https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1400&q=80')] bg-cover bg-center" />
            <div className="mt-6 rounded-[28px] bg-slate-900/95 p-6 shadow-xl backdrop-blur-xl">
              <h3 className="text-xl font-semibold">Why OptiCrop?</h3>
              <div className="mt-5 grid gap-4">
                <div className="flex items-start gap-3 rounded-3xl border border-white/10 bg-white/10 p-4 backdrop-blur-xl">
                  <Leaf className="h-5 w-5 text-green-300" />
                  <div>
                    <p className="font-semibold">Combine Soil, Climate & Weather</p>
                  </div>
                </div>
                <div className="flex items-start gap-3 rounded-3xl border border-white/10 bg-white/10 p-4 backdrop-blur-xl">
                  <Brain className="h-5 w-5 text-green-300" />
                  <div>
                    <p className="font-semibold">Advanced Machine Learning</p>
                  </div>
                </div>
                <div className="flex items-start gap-3 rounded-3xl border border-white/10 bg-white/10 p-4 backdrop-blur-xl">
                  <BarChart3 className="h-5 w-5 text-green-300" />
                  <div>
                    <p className="font-semibold">Increase Productivity</p>
                  </div>
                </div>
                <div className="flex items-start gap-3 rounded-3xl border border-white/10 bg-white/10 p-4 backdrop-blur-xl">
                  <Sparkles className="h-5 w-5 text-green-300" />
                  <div>
                    <p className="font-semibold">Sustainable Agriculture</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </motion.div>
    </div>
  );
}
