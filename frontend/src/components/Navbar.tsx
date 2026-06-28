import { motion } from 'framer-motion';
import { Leaf, Moon, Sun, Menu } from 'lucide-react';

interface NavbarProps {
  onToggleTheme: () => void;
}

const navItems = ['Home', 'Dashboard', 'History', 'About', 'Contact'];

export default function Navbar({ onToggleTheme }: NavbarProps) {
  return (
    <motion.header
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.55 }}
      className="fixed left-0 right-0 z-30 border-b border-white/50 bg-white/70 backdrop-blur-xl"
      style={{ height: 72 }}
    >
      <div className="mx-auto flex h-full max-w-7xl items-center justify-between px-6 sm:px-8 lg:px-10">
        <a href="#" className="flex items-center gap-3 text-xl font-bold text-slate-900">
          <span className="inline-flex h-11 w-11 items-center justify-center rounded-3xl bg-gradient-to-br from-primary to-darkgreen text-white shadow-glow">
            <Leaf size={20} />
          </span>
          OptiCrop
        </a>

        <nav className="hidden items-center gap-8 md:flex">
          {navItems.map((item) => (
            <a key={item} href={`#${item.toLowerCase()}`} className="group relative text-sm font-medium text-slate-700 transition hover:text-slate-900">
              {item}
              <span className="absolute left-0 top-full mt-1 h-[2px] w-full scale-x-0 bg-primary transition-transform duration-300 group-hover:scale-x-100" />
            </a>
          ))}
        </nav>

        <div className="flex items-center gap-3">
          <button
            type="button"
            onClick={onToggleTheme}
            className="inline-flex h-12 w-12 items-center justify-center rounded-2xl border border-slate-200 bg-white text-slate-700 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md"
            aria-label="Toggle theme"
          >
            <Sun size={18} />
          </button>
          <button className="inline-flex items-center gap-2 rounded-2xl bg-gradient-to-r from-primary to-darkgreen px-5 py-3 text-sm font-semibold text-white shadow-glow transition duration-300 hover:-translate-y-0.5 hover:shadow-lg">
            Login
          </button>
          <button className="inline-flex h-12 w-12 items-center justify-center rounded-2xl border border-slate-200 bg-white text-slate-700 shadow-sm md:hidden">
            <Menu size={18} />
          </button>
        </div>
      </div>
    </motion.header>
  );
}
