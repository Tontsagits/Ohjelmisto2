'use strict';

const APIKey = '8891ed0ba67dbb011bea8d0213972a42';

const lomake = document.querySelector('form');
const hakusana = document.querySelector('input');

lomake.addEventListener('submit', function(evt) {
  evt.preventDefault();
  const kaupunki = hakusana.value;
  fetchWeather(kaupunki);
});

// const kaupunki = 'Forssa';

// const request = `https://api.openweathermap.org/data/2.5/weather?units=metric&appid=${APIKey}&q=${kaupunki}`;

async function fetchWeather(kaupunki) {
  const request = `https://api.openweathermap.org/data/2.5/weather?units=metric&appid=${APIKey}&q=${kaupunki}`;
  try {
    const response = await fetch(request);
    if (!response.ok) {
      throw new Error('Server not found');
    }
    const weather = await response.json();
    const name = weather.name;
    const temp = weather.main.temp;
    // console.log(weather);
    console.log(`Name: ${name}`);
    console.log(`Temperature: ${temp}C`);
  } catch (error) {
    console.log(error.message);
  }
}

// fetchWeather();
