#!/usr/bin/node
// class that defines a rectangle_v2
exports.Rectangle = function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
};
