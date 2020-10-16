const merge = require('webpack-merge');
const common = require('./webpack.common.js');
const path = require("path");


const ROOT_DIR = path.join(__dirname, '..');

module.exports = merge(common, {
    mode: 'development',
    devtool: 'inline-source-map',
    output: {
        filename: 'index.js',
        path: path.join(ROOT_DIR, "/itty/frontend/assets/webpack_bundles"),
        publicPath: '/staticfiles/webpack_bundles/',
    },
    devServer: {
        contentBase: path.join(ROOT_DIR, "/itty/frontend/assets/webpack_bundles"),
        hot: true,
        proxy: {
            '!/static/webpackbundles/**': {
                target: 'http://localhost:8000', // points to django dev server
                changeOrigin: true,
            },
        },
    },
});
