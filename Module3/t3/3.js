'use strict';

const names = ['John', 'Paul', 'Jones'];

const u = document.querySelector('#target');

let outputStr = ``;

for (let name of names) {
  outputStr += `<li>${name}</li>`;
}

u.innerHTML = `${outputStr}`;
