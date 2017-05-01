#!/usr/bin/node
// finding the right star wars title
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  var movie = JSON.parse(body);
  console.log(movie.title);
});
