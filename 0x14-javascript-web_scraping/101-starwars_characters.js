#!/usr/bin/node

const request = require('request');
const movieId = require('process').argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + movieId, (err, res, dt) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(dt);
    for (const cUrl of films.characters) {
      request(cUrl, (err, res, data) => {
        if (!err) {
          const c = JSON.parse(data);
          console.log(c.name);
        }
      });
    }
  }
});
