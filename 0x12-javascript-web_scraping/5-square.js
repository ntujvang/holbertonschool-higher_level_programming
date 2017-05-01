#!/usr/bin/node
// class that defines square and inherits rectangle_v4
const Rectangle = require('./4-rectangle.js').Rectangle;
function Square (size) {
  Rectangle.call(this, size, size);
}
exports.Square = Square;
