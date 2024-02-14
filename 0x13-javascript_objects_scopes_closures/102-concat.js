#!/usr/bin/node
const argv = require("process").argv;
const { readFile, writeFile } = require("fs");

function rFile(path) {
	return new Promise((resolve, reject)=> {
	 readFile(path, (err, data)=>{
		 if (data)
			 resolve(data.toString());
		 else
			 reject(err);
	 })
	}
)}
async function main() {
let data1 = await rFile(argv[2]);
let data2 = await rFile(argv[2]);
}
main()
