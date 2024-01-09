#!/usr/bin/node
const { argv } = require("process");
let n = Number(argv[2]);
if (n == NaN)
	n = 1;
function factorial(n)
{
	if (n == 1)
		return (1);
	return (n * factorial(n - 1));
}
console.log(factorial(n));
