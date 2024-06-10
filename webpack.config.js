const path = require('path');

module.exports = {
  entry: './front-end/query.js',  // path to our input file
  output: {
    filename: 'index-bundle.js',  // output bundle file name
    path: path.resolve(__dirname, './front-end/static'),  // path to our Django static directory
  },
  module: {
    rules: [
      {
        test: /.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options:{
            presets: ["@babel/preset-env", ["@babel/preset-react", {"runtime": "automatic"}]],
          }
        },
      },
    ],
  }
};
