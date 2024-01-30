#!/usr/bin/node

let myFile = process.argv[2];
const fs = require('fs');
fs.readFile(myFile, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
