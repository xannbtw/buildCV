/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          400: '#a3ddf5', 
          500: '#89CFF0', // TU COLOR: Baby Blue
          600: '#73badb', 
          900: '#1a4b63', 
        }
      }
    },
  },
  plugins: [],
}