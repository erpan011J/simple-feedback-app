const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  devServer: {
    host: "0.0.0.0",
    port: 8080,
    hot: true,
  },

  configureWebpack: {
    watchOptions: {
      poll: true,
      ignored: /node_modules/,
    },
  },

  transpileDependencies: ["vuetify"],
});
