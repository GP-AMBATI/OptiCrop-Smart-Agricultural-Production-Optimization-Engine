import { CheckCircle2, AlertCircle } from 'lucide-react';

interface ResultProps {
  crop: string;
  confidence: number;
}

export default function ResultDisplay({ crop, confidence }: ResultProps) {
  return (
    <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
      <div className="rounded-[36px] border border-green-200 bg-gradient-to-br from-green-50 to-lightgreen/20 p-8 shadow-lg backdrop-blur-xl">
        <div className="flex items-start gap-4">
          <CheckCircle2 size={32} className="text-darkgreen flex-shrink-0 mt-1" />
          <div className="flex-1">
            <h3 className="text-2xl font-bold text-darkgreen mb-2">Recommendation Ready!</h3>
            <div className="space-y-3">
              <div>
                <p className="text-sm font-semibold text-slate-600 uppercase tracking-wide">Recommended Crop</p>
                <p className="text-3xl font-bold text-darkgreen mt-1 capitalize">{crop}</p>
              </div>
              <div>
                <p className="text-sm font-semibold text-slate-600 uppercase tracking-wide">Confidence Score</p>
                <div className="flex items-center gap-3 mt-2">
                  <div className="flex-1 h-2 bg-gray-200 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-gradient-to-r from-primary to-darkgreen transition-all duration-500" 
                      style={{ width: `${confidence}%` }}
                    />
                  </div>
                  <span className="text-2xl font-bold text-darkgreen">{confidence.toFixed(1)}%</span>
                </div>
              </div>
              <p className="text-sm text-slate-600 mt-4">
                Based on your soil nutrients, weather conditions, and environmental factors, this crop is predicted to be your best choice for optimal yield.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
