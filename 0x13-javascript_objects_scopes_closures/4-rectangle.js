#!/usr/bin/node
const process = require('process');
class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0)
		{
			this.width = w;
			this.height = h;
		}
	}
	print() {
		for (let h = 0; h < this.height; h++)
		{
			for (let w = 0; w < this.width; w++)
				process.stdout.write('X');
			console.log();
		}
	}
	rotate() {
		let temp = this.width;
		this.width = this.height;
		this.height = temp;
	}
	double() {
		this.width += this.width;
		this.height += this.height;
	}
}
module.exports = Rectangle;
