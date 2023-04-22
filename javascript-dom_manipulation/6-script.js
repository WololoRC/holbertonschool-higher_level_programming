#!/usr/bin/node

// fetch @name for @response.json() and set DOM

const aCharacter = document.getElementById('character');

async function logJSONData () {
  const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  const jsonData = await response.json();

  console.log(jsonData);
  aCharacter.textContent = jsonData.name;
}

logJSONData();
