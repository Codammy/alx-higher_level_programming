#!/usr/bin/node

const argv = require('process').argv;
if (argv[3]) { console.log('Arguments found'); } else if (argv[2] && (!argv[3])) { console.log('Argument found'); } else { console.log('No argument'); }
