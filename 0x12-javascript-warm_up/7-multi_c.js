#!/usr/bin/node
// prints 3 lines:  by
// using an array of string and a loop

const lang = 'C is fun';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(lang);
  }
}
