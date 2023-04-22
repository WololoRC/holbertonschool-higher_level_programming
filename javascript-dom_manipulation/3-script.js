#!/usr/bin/node
// if @toggle_header is clicked, his class is set to 'red' or 'green'
const redClass = document.getElementById('toggle_header');

redClass.addEventListener('mousedown', function () {
  if (!redClass.classList.contains('red')) {
    if (redClass.classList.contains('green')) {
      redClass.classList.replace('green', 'red');
    } else {
      redClass.classList.add('red');
    }
  } else {
    redClass.classList.replace('red', 'green');
  }
});
