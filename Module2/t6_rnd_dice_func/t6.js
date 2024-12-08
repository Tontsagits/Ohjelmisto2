'use strict';

function rndDice() {
  const result = Math.floor(Math.random() * 6) + 1;
  return result;
}

let outputStr = ``;

while (true) {
  let number = rndDice();
  outputStr += `<li>${number}</li>`;
  if (number === 6) {
    break;
  }
}

document.querySelector('#tag1').innerHTML = `${outputStr}`;
