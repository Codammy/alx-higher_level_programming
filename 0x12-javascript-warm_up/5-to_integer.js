#!/usr/bin/node
const proc = require('process').argv;
const num = parseInt(proc[2]);
num ? console.log(`My number: ${num}`) : console.log('Not a number');
