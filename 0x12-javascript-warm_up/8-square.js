#!/usr/bin/node

const argv = require('process').argv
let number = parseInt(argv[2])
let c = number * number;
let str='';
if (!number)
	console.log('Missing size');
else {
	r = 0;
	while (c > 0)
	{
		str += 'X'
		c--;
		if ((c % number === 0) && c !=0)
		{
			str += '\n';
		}
	}
	console.log(str)
}
