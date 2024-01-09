#!/usr/bin/node
const { argv } = require('process');
const len = argv.length;
let big;

if (len < 4) { console.log(0); } else {
  big = Number(argv[2]);
  for (let i = 2; i < len; i++) {
    if (big < Number(argv[i])) { big = Number(argv[i]); }
  }
}
let newBig = big;
for (let i = 2; i < len; i++) {
	if (newBig >= Number(argv[i]) && newBig !== big)
	{
		console.log(newBig);
		break;
	}
	newBig = Number(argv[i])
  }
