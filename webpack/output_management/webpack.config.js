const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');


module.exports = {
  // entry: './src/index.js',
  entry: {
    index: './src/index.js',
    print: './src/print.js',
  },
  plugins: [
    new HtmlWebpackPlugin({ // npm install --save-dev html-webpack-plugin
      title: 'Output Management',
    }),
  ],
  output: {
    // filename: 'main.js',
    // filename: 'bundle.js',
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist'),
    clean: true,
  },
};
