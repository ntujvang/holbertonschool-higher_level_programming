#!/usr/bin/node
// script that prints content of a file
const opt = require('fs');
const file = process.argv[2];
opt.readFile(file, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
  console.log(String(data).replace('\n', ''));
});
