#!/usr/bin/node
/*
a script that prints the number of movies where the character “Wedge Antilles” is present.

The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
*/
const request = require('request');

const url = process.argv[2];
const characterId = '18';
let count = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const val1 = (data.results);
    const val1len = val1.length;

    for (let i = 0; i < val1len; i++) {
      const valCharlen = val1[i].characters.length;
      for (let j = 0; j < valCharlen; j++) {
        if (val1[i].characters[j].includes(characterId)) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
