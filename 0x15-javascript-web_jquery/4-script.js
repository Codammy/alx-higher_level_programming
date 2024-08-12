const elem = $('DIV#toggle_header');
elem.on('click', colorHandler);
function colorHandler () {
  elem.prev().toggleClass('red green');
}
