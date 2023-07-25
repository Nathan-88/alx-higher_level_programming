#!/usr/bin/node
// a script that display the status code of a GET request

const request = require('request');
const url = process.argv[2];

request.get(url, (err, response) => {
  if (err) {
    console.log(console.err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
