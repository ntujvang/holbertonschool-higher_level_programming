#!/usr/bin/node
// class that defines square and inherits rectangle_v4
const Rectangle = require('./4-rectangle.js').Rectangle;
module.exports.Square = function Square (size) {
  Rectangle.call(this, size, size);
};
