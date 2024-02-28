const red_header = $('DIV#red_header');

red_header.on("click", changeColor);

function changeColor() {
    red_header.css('color', '#FF0000');
}
