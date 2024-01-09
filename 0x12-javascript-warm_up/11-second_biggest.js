#!/usr/bin/node
const { argv } = require("process");
let len = argv.length;
let big;

if (len < 4)
	console.log(0);
else
{
	big = Number(argv[2]);
	for (let i = 2; i < len; i++)
	{
		if (big < Number(argv[i]))
			big = Number(argv[i]);
	}
	console.log(big);
}
