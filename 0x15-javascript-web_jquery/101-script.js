document.addEventListener('DOMContentLoaded', () => {
    const addItem = $('DIV#add_item');
    addItem.on('click', addLi);

    function addLi() {
        $('UL.my_list').append('<li>Item</li>');
    }
    const removeItem = $('DIV#remove_item');
    removeItem.on('click', removeLi);
    function removeLi() {
        $('UL.my_list li:last').remove();
    }
    const clear = $('DIV#clear_list');
    clear.on('click', clearAll);

    function clearAll() {
        $('UL.my_list li').remove();
    }
})
