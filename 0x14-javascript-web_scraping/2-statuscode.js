#!/usr/bin/node

let myUrl = process.argv[2];
const request = require('request');

request(myUrl, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
