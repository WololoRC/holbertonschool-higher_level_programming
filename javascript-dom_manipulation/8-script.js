#!/usr/bin/node

window.onload = function () {
  const sayHello = document.getElementById('hello');

  async function helloFetch () {
    const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
    const jsonData = await response.json();

    sayHello.textContent = jsonData.hello;
  }
  helloFetch();
};
