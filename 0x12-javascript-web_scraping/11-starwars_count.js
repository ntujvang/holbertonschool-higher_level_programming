#!/usr/bin/node
// script that prints num of movies with Wdge Antilles
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  var count = 0;
  var movie = JSON.parse(body);
  for (let i = 0; i < movie.length; i++) {
    if (movie[i].characters === 18) {
      count++;
    }
  }
  console.log(count);
});
