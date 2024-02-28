fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
        if (!response.ok) {
            throw new Error('An Error Occured');
        }
        return response.json();
    })
    .then(data => {
        const translateHello = data.hello;
        const hello = $('DIV#hello');
        hello.text(`${translateHello}`);
    })
    .catch(error => {
        console.error('Error Occured')
    });
