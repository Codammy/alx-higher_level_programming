#!/usr/bin/node

const request = require('request')
const rp = require('process').argv[2]

request.get(`https://swapi-api.alx-tools.com/api/films/:${rp}`, function (err, res, data){
	const f = data.results.filter((film)=> film.episode_id === rp)
	console.log(f.title)
})
