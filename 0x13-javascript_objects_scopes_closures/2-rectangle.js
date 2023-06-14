#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (isNaN(w) || isNaN(h) || w === 0 || h === 0 || Math.sign(w) === -1 || Math.sign(h) === -1) {
      this.width;
      this.height;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
