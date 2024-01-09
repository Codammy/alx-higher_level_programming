#!/usr/bin/node
const { argv } = require("process");
let size = Number(argv[2]);
if (size)
	for (let i = 0; i < size; i++)
		for (let j = 0; j < size; j++)
			console.log("X", end="");
else
	console.log("Missing size")
