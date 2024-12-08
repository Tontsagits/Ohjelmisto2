'use strict';

const sides = parseInt(
    prompt('How many sides to a dice?', 'Number of sides here.'));
const dices = parseInt(
    prompt('How many dices will be thrown?', 'Number of dices here.'));

function rndDice(dSides) {
  const result = Math.floor(Math.random() * dSides) + 1;
  return result;
}

let outputStr = ``;
let rolled = 0;

while (true) {
  let number = rndDice(sides);
  outputStr += `<li>Rolled: ${number}</li>`;
  rolled++;
  if (rolled === dices) {
    break;
  }
}

document.querySelector('#tag1').innerHTML = `${outputStr}`;
