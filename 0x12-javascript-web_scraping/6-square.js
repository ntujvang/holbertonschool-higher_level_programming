#!/usr/bin/node
// class that defines square and inherits 5-square.js
const Squar = require('./5-square.js').Square;
exports.Square = function Square (size) {
  Squar.call(this, size);
  this.size = size;
  Square.prototype.charPrint = function (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    };
  };
};
