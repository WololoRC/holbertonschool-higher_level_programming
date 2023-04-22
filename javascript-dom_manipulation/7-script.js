#!/usr/bin/node

const listMovies = document.getElementById('list_movies');

async function fetchJSONData () {
  const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
  const jsonData = await response.json();

  for (const movie of jsonData.results) {
    const itemList = document.createElement('li');
    itemList.textContent = movie.title;
    listMovies.appendChild(itemList);
  }
}

fetchJSONData();
