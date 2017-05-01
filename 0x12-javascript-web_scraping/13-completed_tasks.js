#!/usr/bin/node
// script that computers number of completed task by UID
const url = process.argv[2];
const request = require('request');
var completed = {};
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  var data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    var user = data[i].userId;
    if (data[i].completed) {
      completed[user] += 1;
    }
  }
  console.log(completed);
});
