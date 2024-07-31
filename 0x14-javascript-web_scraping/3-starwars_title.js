#!/usr/bin/node

const request = require('request');
const rp = require('process').argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${rp}`, function (err, res, data) {
  if (err) {
    console.log(err);
    return;
  }
  data = JSON.parse(data);
  console.log(data.title);
});
