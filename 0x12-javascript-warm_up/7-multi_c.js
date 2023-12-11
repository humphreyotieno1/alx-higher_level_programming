#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
	for (let i = number; i > 0; i -= 1) {
	  console.log('C is fun');
	}
}
