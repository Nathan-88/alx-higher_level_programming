#!/usr/bin/node
/* a script that prints the title of a Star Wars movie where the episode number matches a given integer
You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
*/

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
