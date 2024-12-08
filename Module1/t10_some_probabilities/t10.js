'use strict';

// pyydetään noppien lukumäärä ja etsitty niiden heittojen summa
const numberOfDice = parseInt(
    prompt('How many dice you want to be thrown?', 'Number of dice here.'));
const sumOfInterest = parseInt(
    prompt('What sum of dice throws do you want?', 'Sum of dice throws here.'));

// simulaatioiden lukumäärä
const rollsTotal = 10000;
// alustetaan onnistuneiden heittojen lukumäärä
let rollsSuccesfull = 0;

// heitetään noppia simulaation määrän kertaa
for (let i = 0; i < rollsTotal; i++) {
  // heitetään jokaista noppaa vuorollaan ja lasketaan summa yhteen
  let sumOfDice = 0;
  for (let j = 0; j < numberOfDice; j++) {
    // arvontaan muuttuja välillä 0-1, kerrotaan kuudella ja lisätään 1
    sumOfDice += Math.floor((Math.random() * 6) + 1);
    // console.log(`Sum of dice ${j}: ${sumOfDice}`);
  }
  console.log(`Total sum of dice throws: ${sumOfDice}`);
  // verrataan saatua noppien summaa haluttuun
  // jos sama niin merkitään onnistuneeksi heitoksi
  if (sumOfDice === sumOfInterest) {
    rollsSuccesfull++;
  }
  console.log(`Total number of dice throws: ${i}`);
}

// tsekataan montako onnistunutta heittoa tarvittiin
// simulaation heittojen määrästä eli todennäköisyys
const hitProbability = (rollsSuccesfull / rollsTotal) * 100;
document.querySelector(
    '#tag1').innerHTML = `Probability to get total sum of ${sumOfInterest} with ${numberOfDice} dices each thrown just once is about ${hitProbability.toFixed(
    2)}% (tested with total of ${rollsTotal} times ${numberOfDice} dice throws)`;
