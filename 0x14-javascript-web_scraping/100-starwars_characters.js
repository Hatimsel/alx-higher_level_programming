#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url.concat(process.argv[2]), (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    try {
      const characters = JSON.parse(body).characters;
      for (const character of characters) {
        request(character, (err, bd) => {
          if (err) {
            console.error(err);
          } else {
            const name = JSON.parse(bd.body);
            console.log(name.name);
          }
        });
      }
    } catch (parseError) {
      console.log(parseError);
    }
  }
});
