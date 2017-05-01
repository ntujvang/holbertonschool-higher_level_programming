#!/usr/bin/node
// script that gets the content of a webpage > file
const url = process.argv[2];
const request = require('request');
const opt = require('fs');
const file = process.argv[3];

request(url, function (err, body) {
  if (err) {
    console.log(err);
  }
  opt.writeFile(file, body.body, function (err, body) {
    if (err) {
      console.log(err);
    }
  });
});
