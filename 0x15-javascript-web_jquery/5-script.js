const addItem = $('DIV#add_item')
addItem.on('click', addLi)

function addLi() {
    $('UL.my_list').append('<li>Item</li>')
}
