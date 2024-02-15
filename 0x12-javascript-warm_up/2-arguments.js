#!/usr/bin/node
const proc = require('process').argv;
if (proc[3]) {
  console.log('Arguments found');
} else if (proc[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
