const cssnano = require('cssnano');

module.exports = {
  tailwindcss: {config: './tailwind.config.js'},
  plugins: [
    // require('postcss-import'),
    require('tailwindcss'),
      cssnano({
        preset: "default",
      }),
    require('autoprefixer'),
  ]
}