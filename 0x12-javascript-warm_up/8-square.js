#!/usr/bin/node
let row = '';
const size = process.argv[2];
for (i = 0; i < size; i++) {
  for (j = 0; j < size; j++) {
    row += 'X';
  }
  console.log(row);
  row = '';
}
