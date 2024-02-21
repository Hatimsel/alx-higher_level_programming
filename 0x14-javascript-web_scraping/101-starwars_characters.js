#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

async function getCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (err, resp, body) => {
      if (err) {
        reject(err);
      } else {
        const name = JSON.parse(body).name;
        resolve(name);
      }
    });
  });
}

async function getFilmCharacters (filmUrl) {
  return new Promise((resolve, reject) => {
    request(filmUrl, (err, resp, body) => {
      if (err) {
        reject(err);
      } else {
        const characters = JSON.parse(body).characters;
        resolve(characters);
      }
    });
  });
}

async function main () {
  try {
    const filmCharacters = await getFilmCharacters(url.concat(process.argv[2]));
    for (const character of filmCharacters) {
      const characterName = await getCharacterName(character);
      console.log(characterName);
    }
  } catch (error) {
    console.error(error);
  }
}

main();
