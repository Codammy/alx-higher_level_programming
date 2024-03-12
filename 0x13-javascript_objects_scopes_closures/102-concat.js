#!/usr/bin/node

const { readFileSync, writeFileSync } = require('fs');
const argv = require('process').argv;
writeFileSync(argv[4], readFileSync(argv[2]) + readFileSync(argv[3]));
