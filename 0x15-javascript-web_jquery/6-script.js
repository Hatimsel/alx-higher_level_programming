const updateHeader = $('DIV#update_header')

updateHeader.on('click', changeText);

function changeText() {
    $('header').text('New header!!!')
}
