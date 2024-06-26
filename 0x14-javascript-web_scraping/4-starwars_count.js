#!/usr/bin/node

const request = require('request');
const URL = require('process').argv[2];

let count = 0;
request(URL, (err, res, dt) => {
  if (err) { console.log(err); } else {
    dt = JSON.parse(dt);
    for (const movie of dt.results) {
      for (const characters of movie.characters) {
        if (characters.slice(-3, -1) === '18') { count++; }
      }
    }
    console.log(count);
  }
});
