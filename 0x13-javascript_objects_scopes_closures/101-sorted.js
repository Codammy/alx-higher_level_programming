#!/usr/bin/node
const { dict } = require("./101-data");
const newDict = {}
for (let id in dict) {
	let occ = dict[id]
	if (newDict[occ])
	{
		let arr = newDict[occ];
		arr.push(id);
		continue;
	}
	newDict[occ] = Array(id);
}
console.log(newDict);
