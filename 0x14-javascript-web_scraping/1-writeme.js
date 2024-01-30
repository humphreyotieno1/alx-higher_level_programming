#!/usr/bin/node

let myFile = process.argv[2];
let text = process.argv[3];
const fs = require('fs');
fs.writeFile(myFile, text, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
