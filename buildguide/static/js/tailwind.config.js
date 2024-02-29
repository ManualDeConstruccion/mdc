module.exports = {
  mode: 'layers',
  content: ['*.html/','./src/js/*.js',
    './docs/*.html','./authentication/*.html','./components/*.html','./content/*.html','./forms/*.html','./ecommerce/*.html','./project/*.html'],
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        gray: {
          50:  '#f8f7ff',
          100: '#f6f5ff',
          200:  '#eff0fe',
          300:  '#e0e0fc',
          400:  '#98A5C0',
          500:  '#84848f',
          600:  '#595983',
          700:  '#1e1f48',
          800:  '#141430',
          900:  '#0a0a18',
          950:  '#050329'
        },
      }
    },
    fontFamily: {
      sans: ['Nunito', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
  },
  variants: {
    extend: {
       backgroundOpacity: ['dark']
    }
  },
  plugins: []
}