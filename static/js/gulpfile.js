// Gulp file
const { src, dest, watch, series, parallel } = require('gulp');
const del                  = require('del');
const options              = require("./config"); //options from config.js
const browserSync          = require('browser-sync');
const postcss              = require('gulp-postcss');
const concat               = require('gulp-concat');
const uglify               = require('gulp-terser');
const cleanCSS             = require('gulp-clean-css');
const purgecss             = require('gulp-purgecss');
const logSymbols           = require('log-symbols');

//Load Previews on Browser on dev
function livePreview(done){
  browserSync.init({
    files: "./*.html",
    startPath: "./",
    server: {
      baseDir: "./",
    },
    port: options.config.port || 5000
  });
  done();
}
function watchFiles(){
  watch('./**/*.html',series(devStyles,previewReload));
  watch([options.config.tailwindjs, `${options.paths.src.tailwindcss}/**/*`],series(devStyles, previewReload));
  watch(`${options.paths.src.js}/theme.js`,series(previewReload));
  console.log("\n\t" + logSymbols.info,"Watching for Changes..\n");
}
function previewReload(done){
  console.log("\n\t" + logSymbols.info,"Reloading Browser Preview.\n");
  browserSync.reload();
  done();
}

// delete dist
function devClean(){
  console.log("\n\t" + logSymbols.info,"Cleaning dist folder for fresh start.\n");
  return del([options.paths.dist.base]);
}
// generate css
function devStyles(){
  const tailwindcss = require('tailwindcss'); 
  return src(`${options.paths.src.tailwindcss}/tailwindcss.css`)
    .pipe(postcss([
      tailwindcss(options.config.tailwindjs),
      require('autoprefixer'),
    ]))
    .pipe(concat({ path: 'style.css'}))
    .pipe(dest(options.paths.src.css));
}

// minify css
function prodStyles(){
  return src(`${options.paths.src.css}/style.css`).pipe(purgecss({
    content: ['./*.html','./docs/*.html','./src/js/*.js','./authentication/*.html','./components/*.html','./content/*.html','./forms/*.html','./ecommerce/*.html','./project/*.html'],
    defaultExtractor: content => {
      const broadMatches = content.match(/[^<>"'`\s]*[^<>"'`\s:]/g) || []
      const innerMatches = content.match(/[^<>"'`\s.()]*[^<>"'`\s.():]/g) || []
      return broadMatches.concat(innerMatches)
    }
  }))
  .pipe(cleanCSS({compatibility: 'ie8'}))
  .pipe(dest(options.paths.dist.css));
}
// minify js
function prodScripts(){
  return src([
    `${options.paths.vendors}/alpinejs/dist/cdn.min.js`,
    `${options.paths.vendors}/flatpickr/dist/flatpickr.min.js`,
    `${options.paths.vendors}/flatpickr/dist/plugins/rangePlugin.js`,
    `${options.paths.vendors}/simple-datatables/dist/umd/simple-datatables.js`,
    `${options.paths.vendors}/@yaireo/tagify/dist/tagify.min.js`,
    `${options.paths.vendors}/pristinejs/dist/pristine.min.js`
  ])
  .pipe(concat({ path: 'scripts.js'}))
  .pipe(uglify())
  .pipe(dest(options.paths.dist.js));
}

// finish log
function buildFinish(done){
  console.log("\n\t" + logSymbols.info,`Production is complete. Files are located at ${options.paths.dist.base}\n`);
  done();
}

// Clean vendors
function cleanvendor() {
  return del(["./vendors/"]);
}
// Copy File from vendors
function copyvendors() {
  return src([
    './node_modules/*@yaireo/*tagify/**/*',
    './node_modules/*alpinejs/**/*',
    './node_modules/*chart.js/**/*',
    './node_modules/*dragula/**/*',
    './node_modules/*dropzone/**/*',
    './node_modules/*flatpickr/**/*',
    './node_modules/*flickity/**/*',
    './node_modules/*fullcalendar/**/*',
    './node_modules/*glightbox/**/*',
    './node_modules/*jsvectormap/**/*',
    './node_modules/*prismjs/**/*',
    './node_modules/*pristinejs/**/*',
    './node_modules/*simple-datatables/**/*',
    './node_modules/*simplemde/**/*',
    './node_modules/*sweetalert2/**/*'
  ])
  .pipe( dest('./vendors/'))
}

exports.updateplugins = series(cleanvendor, copyvendors);

exports.default = series( devClean, devStyles, livePreview, watchFiles);

exports.prod = series(
  devClean,
  parallel(prodStyles, prodScripts), //Run All tasks in parallel
  buildFinish
);