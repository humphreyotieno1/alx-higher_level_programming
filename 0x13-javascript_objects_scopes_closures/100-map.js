#!/usr/bin/node
const list = require('./100-data').list;

const myList = list.map((a, index) => a * index);
console.log(list);
console.log(myList);
