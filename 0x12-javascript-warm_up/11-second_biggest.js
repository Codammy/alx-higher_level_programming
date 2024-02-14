#!/usr/bin/node
const { argv } = require('process');
let biggest = 0;
for (let i = 2; i < argv.length; i++) {
  biggest = biggest < Number(argv[i]) ? Number(argv[i]) : biggest;
}
console.log(biggest);
