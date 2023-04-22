#!/usr/bin/node

const addItem = document.getElementById('add_item');
const myList = document.getElementsByClassName('my_list')[0];

addItem.addEventListener('mousedown', function () {
  const newElement = document.createElement('li');
  newElement.textContent = 'Item';
  myList.appendChild(newElement);
});
