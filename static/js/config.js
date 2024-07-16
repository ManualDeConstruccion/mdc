module.exports = {
	config: {
		tailwindjs: "./tailwind.config.js",
		port: 3100
	},
	paths: {
		root: "./",
		src: {
			base: "./src",
			css: "./src/css",
			tailwindcss: "./src/tailwindcss",
			js: "./src/js",
			img: "./src/img"
		},
		dist: {
			base: "./dist",
			css: "./dist/css",
			js: "./dist/js"
		},
		vendors: "./vendors",
	}
}