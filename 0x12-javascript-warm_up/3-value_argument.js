#!/usr/bin/node

const argv = require('process').argv;
argv[2] ? console.log(argv[2]) : console.log('No argument');
