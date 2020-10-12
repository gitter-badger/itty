const webpack = require('webpack');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const BundleTracker = require('webpack-bundle-tracker');
const Dotenv = require('dotenv-webpack');
const path = require("path");

const ROOT_DIR = path.join(__dirname, '..');

const config = {
    entry: {
        main: [
            'react-hot-loader/patch',
            'webpack-dev-server/client?http://0.0.0.0:3000',
            'webpack/hot/only-dev-server',
            path.join(__dirname, '../js/src/main/index')
        ],
        index: [
            'babel-polyfill',
            ROOT_DIR + '/itty/frontend/src/index.jsx',
        ],
    },
    output: {
        path: ROOT_DIR + '/itty/frontend/assets/webpack_bundles/',
        filename: 'index.js',
    },
    module: {
        rules: [
            {
                test: /\.jsx?/,
                exclude: /node_modules/,
                use: ['babel-loader']
            },
            {
                test: /\.ts(x?)$/,
                use: [
                    {
                        loader: "babel-loader"
                    },
                    {
                        loader: "ts-loader"
                    }
                ]
            },
            {
                test: /\.css$/i,
                use: [MiniCssExtractPlugin.loader, 'css-loader'],
            },
            {
                test: /\.(svg|gif|eot|woff|ttf|woff2)$/,
                use: 'file-loader?name=[name].[ext]'
            },
            {
                test: /\.(png|jpg|jpeg)$/,
                loader: 'url-loader',
            }
        ]
    },
    performance: {
        hints: false
    },
    plugins: [
        new MiniCssExtractPlugin(),
        new BundleTracker({filename: '/itty/frontend/assets/webpack_bundles/webpack-stats.json'}),
        new webpack.EvalSourceMapDevToolPlugin({
            exclude: /node_modules/
        }),
        //Defaults to the .env file
        new Dotenv({
            safe: false,
            allowEmptyValue: true, // allows ENV_VAR= to become empty string
            silent: false,
            defaults: false
        })
    ],
    resolve: {
        extensions: [".js", ".jsx", ".css", ".ts", ".tsx"],
    },
};

module.exports = config;
