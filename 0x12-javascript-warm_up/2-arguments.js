#!/usr/bin/node
const proc = require('process');
const argLen = proc.argv.length;
if (argLen === 3) { console.log('Argument found'); } else if (argLen > 3) { console.log('Arguments found'); } else { console.log('No argument'); }
