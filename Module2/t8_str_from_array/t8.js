'use strict';

function concat(array) {
  let outputStr = ``;
  for (let item of array) {
    outputStr += `${item}`;
  }
  return outputStr;
}

const listOfNames = ['Johnny', 'DeeDee', 'Joey', 'Marky'];

const finalResultStr = concat(listOfNames);

document.querySelector('#tag1').innerText = `${finalResultStr}`;
