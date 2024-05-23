#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const movie_id = require('process').argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + movie_id, (err, res, dt) => {
	if (err) {
	console.log(err);
	} else {
	const films = JSON.parse(dt);
	for (const c_url of films.characters) {
		request(c_url, (err, res, data) => {
			if (!err) {
				const c = JSON.parse(data);
				console.log(c.name);
			}
		});
	}
	}
});
