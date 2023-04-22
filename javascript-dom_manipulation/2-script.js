#!/usr/bin/node
// if @red_header is clicked, his class is set to 'red'
const redClass = document.getElementById('toggle_header');

const clases = redClass.classList;

redClass.addEventListener('mousedown', function (clases) {
  if (!red in clases) {
    clases[0] = 'red';
  } else {
    clases[0] = 'green';
  }
});
