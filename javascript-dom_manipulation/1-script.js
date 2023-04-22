#!/usr/bin/node
// if @red_header is clicked color = red
const redHeader = document.getElementById('red_header');

redHeader.addEventListener('mousedown', function () {
  this.style.color = 'red';
});
