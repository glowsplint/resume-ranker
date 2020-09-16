const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  // on Windows you want to set publicPath: "http://127.0.0.1:8080/"
  // on Mac/Linux you want to set publicPath: "http://0.0.0.0:8080/"

  // publicPath: "http://127.0.0.1:8080/", // Comment out before deployment
  publicPath: "", // Use this in deployment
  assetsDir: "static",
  transpileDependencies: ["vuetify"],

  chainWebpack: config => {
    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: "./webpack-stats.json" }]);

    config.output.filename("static/bundle.js");
    config.optimization.splitChunks(false);
    config.resolve.alias.set("__STATIC__", "static");

    config.devServer
      // .public("http://127.0.0.1:8080") // Comment out before deployment
      .host("127.0.0.1")
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .disableHostCheck(true);
    // .headers({ "Access-Control-Allow-Origin": ["*"] }); // Comment out before deployment
  },

  css: {
    extract: {
      filename: "static/bundle.css",
      chunkFilename: "static/bundle.css"
    }
  }
};
