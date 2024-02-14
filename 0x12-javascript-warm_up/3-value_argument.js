#!/usr/bin/node
const proc = require('process').argv;
proc[2] ? console.log(proc[2]) : console.log('No argument');
