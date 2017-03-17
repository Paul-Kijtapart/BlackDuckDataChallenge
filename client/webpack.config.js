const path = require('path');
const webpack = require('webpack');

const SRC = path.resolve(__dirname, 'src');
const PUBLIC = path.resolve(__dirname, 'public');
const NODE_MODULES = path.resolve(__dirname, 'node_modules');

module.exports = {
  entry: path.join(SRC, 'index.js'),
  output: {
    filename: 'index.js',
    path: PUBLIC
  },
  module: {
    rules: [{
      test: /\.jsx?$/,
      exclude: [NODE_MODULES],
      use: [{
        loader: 'babel-loader'
      }]
    }, {
      test: /\.json$/,
      use: [{
        loader: 'json-loader'
      }]
    }]
  },
  resolve: {
    modules: [
      SRC,
      NODE_MODULES
    ]
  }
};