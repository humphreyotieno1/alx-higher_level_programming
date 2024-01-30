#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];

const myUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request({ myUrl, json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    console.log(body.title);
  }
});
