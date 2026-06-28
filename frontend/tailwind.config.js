export default {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#16A34A',
        darkgreen: '#065F46',
        lightgreen: '#DCFCE7',
        surface: '#FFFFFF',
        background: '#F8FAFC',
      },
      boxShadow: {
        soft: '0 24px 80px rgba(15, 23, 42, 0.08)',
        glow: '0 0 0 1px rgba(22, 163, 74, 0.12), 0 24px 60px rgba(22, 163, 74, 0.12)',
      },
      borderRadius: {
        xl: '24px',
      },
      backgroundImage: {
        'hero-gradient': 'linear-gradient(135deg, #065F46 0%, #16A34A 100%)',
      },
    },
  },
  plugins: [],
};
