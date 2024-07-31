#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const [URL, path] = [...require('process').argv.slice(2, 4)];

request(URL).pipe(fs.createWriteStream(path));
