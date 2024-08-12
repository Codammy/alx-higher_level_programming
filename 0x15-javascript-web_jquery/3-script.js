$("DIV#red_header").on("click", (colorHandler(e.target.previousElementSibling))

function colorHandler(element) {
	element.classList.toggle("red");
	element.classList.toggle("green");
}
