fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error('An Error Occured');
        }
        return response.json();
    })
    .then(data => {
        const titles = data.results;
        const listMovies = $('UL#list_movies');
        for (const t of titles) {
            const title = (t['title'])
            listMovies.append('<li>' + `${title}` + '</li>');
        }
    })
    .catch(error => {
        console.error('Error Occured')
    });
