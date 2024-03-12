#!/usr/bin/node

const dict = require('./101-data').dict;
const newObj = {};
for (let k in dict) {
	let v = dict[k];
	if (newObj.hasOwnProperty(v)) {
		newObj[v].push(k);
	}
	else {
		newObj[v] = [ k ];
	}
}
console.log(newObj);

