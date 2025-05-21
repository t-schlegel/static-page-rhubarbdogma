/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./**/*.html', './script.js'],
  theme: {
    extend: {
      fontFamily: {
        serif: ['"Times New Roman"', 'Times', 'serif']
      },
      animation: {
        'twinkle': 'twinkle 2s ease-in-out infinite',
        'sparkle': 'sparkle 2s ease-in-out infinite',
        'pulse': 'pulse 2s ease-in-out infinite',
        'float': 'float 2s ease-in-out infinite',
        'shimmer': 'shimmer 2s ease-in-out infinite'
      },
      keyframes: {
        sparkle: {
          '0%, 100%': { opacity: '0', transform: 'scale(0)' },
          '50%': { opacity: '1', transform: 'scale(1)' },
        },
        pulse: {
          '0%, 100%': { opacity: '0.4', transform: 'scale(0.8)', filter: 'drop-shadow(0 0 2px rgba(255, 255, 255, 0.6))' },
          '50%': { opacity: '1', transform: 'scale(1.1)', filter: 'drop-shadow(0 0 8px rgba(255, 255, 255, 0.9)) drop-shadow(0 0 12px rgba(255, 215, 0, 0.6))' },
        },
        twinkle: {
          '0%, 100%': { 
            opacity: '0.15',
            transform: 'rotate(0deg) scale(0.8)',
            filter: 'drop-shadow(0 0 2px rgba(40, 40, 40, 0.3))'
          },
          '50%': { 
            opacity: '0.9',
            transform: 'rotate(180deg) scale(1.1)',
            filter: 'drop-shadow(0 0 4px rgba(40, 40, 40, 0.5)) drop-shadow(0 0 8px rgba(170, 170, 170, 0.7))'
          },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0) scale(1)', opacity: '0.5' },
          '50%': { transform: 'translateY(-10px) scale(1.1)', opacity: '1' },
        },
        shimmer: {
          '0%, 100%': { opacity: '0.5', transform: 'translateX(0) scale(1)', filter: 'hue-rotate(0deg)' },
          '50%': { opacity: '1', transform: 'translateX(5px) scale(1.1)', filter: 'hue-rotate(180deg)' },
        },
      },
      scale: {
        '130': '1.3'
      }
    },
  },
  plugins: [],
}