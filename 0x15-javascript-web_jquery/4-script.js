const toggle = $('DIV#toggle_header');

toggle.on("click", toggleHeader)

function toggleHeader() {
    const clas = $('header').attr('class');
    if (clas === 'red') {
        $('header').toggleClass(`${clas} green`);
    }
    if (clas === 'green') {
        $('header').toggleClass(`${clas} red`);
    }
}
