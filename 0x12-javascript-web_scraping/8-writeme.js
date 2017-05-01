#!/usr/bin/node
// script that write a string to a file
const opt = require('fs');
const file = process.argv[2];
const data = process.argv[3];
opt.writeFile(file, data, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
