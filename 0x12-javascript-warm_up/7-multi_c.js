#!/usr/bin/node

const argv = require('process').argv
let number = parseInt(argv[2])
if (!number)
	console.log('Missing number of occurrences');
else {
	while (number > 0)
	{
		console.log('C is fun');
		number--;
	}

}
