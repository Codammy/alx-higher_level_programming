#!/usr/bin/node
const dict = require("./101-data.js").dict
let newObj = {}
let arr = Object.entries(dict);
for (let i = 0; i < arr.length; i++) {
	let k = arr[i][1];
	let v = arr[i][0];
	if (newObj[k] === undefined)
		newObj[k] = [ v ];
	else
		newObj[k].push(v)
}
console.log(newObj)
