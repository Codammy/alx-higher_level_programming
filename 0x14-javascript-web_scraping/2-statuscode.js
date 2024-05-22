#!/usr/bin/node

const request = require('request')
const URL = require('process').argv[2]

request.get(URL, function (err, res, data){
	console.log(res.statusCode)
})
