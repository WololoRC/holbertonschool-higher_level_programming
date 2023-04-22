#!/usr/bin/node

const getAction = document.getElementById('update_header');
const upHeader = document.querySelector('header');

getAction.addEventListener('mousedown', function () {
  upHeader.textContent = 'New Header!!!';
});
