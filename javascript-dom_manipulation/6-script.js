const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then(response => response.json())
  .then(data => {
    const characterName = data.name;
    document.getElementById('character').textContent = characterName;
  })
  .catch(error => console.error('Error fetching character:', error));