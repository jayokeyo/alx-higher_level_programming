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
  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }
  rotate () {
    let tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
