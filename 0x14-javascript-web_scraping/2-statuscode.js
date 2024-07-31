#!/usr/bin/node

const request = require('request');
const URL = require('process').argv[2];

request.get(URL, function (err, res, data) {
  if (err) { console.log(err); } else { console.log('code: ' + res.statusCode); }
});
