#!/usr/bin/node
exports.converter = function (base) {
	return ((n)=>parseInt(n, base))
}
