const elem = $('DIV#add_item');
elem.on('click', add_item);

function add_item () {
  $('UL.my_list').append('<li>my_list</li>');
}
