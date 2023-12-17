#!/usr/bin/node
const numberArray = process.argv.slice(2);
function second (array) {
  if (array.length < 2) {
    return (0);
  } else {
    array.sort((a, b) => a - b);
    array.pop();
    return (array.pop());
  }
}
console.log(second(numberArray));
