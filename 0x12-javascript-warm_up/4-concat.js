#!/usr/bin/node
let arg1 = process.argv[2];
let arg2 = process.argv[3];
if (arg1 && arg2) {
  console.log([arg1 , 'is' , arg2].join(' '));
} else if (arg1) {
  console.log([arg1, 'is', 'undefined'].join(' '));
} else {
  console.log('undefined is undefined');
}
