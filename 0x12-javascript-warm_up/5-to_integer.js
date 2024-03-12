#!/usr/bin/node

const argv = require('process').argv;
const number = parseInt(argv[2]);
console.log(`${number ? `My number: ${number}` : 'Not a number'}`);
