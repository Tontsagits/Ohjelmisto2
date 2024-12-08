'use strict';

// set number of candidates
const nCandis = parseInt(
    prompt('Enter number of candidates:', 'Number of candidates here.'));

// set array for candidates
const candidates = [];

// create each candidates as object literal and store into array
for (let i = 1; i <= nCandis; i++) {
  let candidate = {};
  const candidateName = prompt(`Name for candidate ${i}:`, 'Name here.');
  candidate.name = candidateName;
  candidate.votes = 0;
  candidates.push(candidate);
}

// set number of voters
const nVoters = parseInt(
    prompt('Enter number of voters:', 'Number of voters here.'));

// each voter gets to vote for a name
// if mispelled or empty then not counted
for (let j = 1; j <= nVoters; j++) {
  const whoToVote = prompt(`Voter ${j}. Who do you vote for?`,
      'Enter your candidates name here:');
  for (let k = 0; k < candidates.length; k++) {
    if (candidates[k].name === whoToVote) {
      candidates[k].votes++;
      console.log(`Voter ${j} voted for ${candidates[k].name}.`);
    }
  }
}

// check who wins
// sort by votes
candidates.sort((a, b) => b.votes - a.votes);
// print winner info as lists first item
console.log(
    `The winner is ${candidates[0].name} with ${candidates[0].votes} votes.`);
console.log('results:');
for (const candidate of candidates) {
  console.log(`Name: ${candidate.name} | Votes: ${candidate.votes}`);
}
