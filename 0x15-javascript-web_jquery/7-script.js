fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error('An Error Occured');
        }
        return response.json();
    })
    .then(data => {
        const character = data.name;
        const divCharacter = $('DIV#character');
        divCharacter.text(`${character}`);
    })
    .catch(error => {
        console.error('Error Occured')
    });
