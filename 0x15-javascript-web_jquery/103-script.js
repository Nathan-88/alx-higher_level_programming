#!/usr/bin/node
/**
 * a JavaScript script that fetches and prints how to say “Hello” depending on the language
 */
$(document).ready(function () {
	$("INPUT#btn_translate").click(fetchTranslation);
	$("INPUT#language_code").keyup(function (event) {
		if (event.keyCode === 13) {
			fetchTranslation();
		}
	});

	function fetchTranslation() {
		const language_code = $("INPUT#language_code").val();
		$.getJSON(
			`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`,
			function (data) {
				$("#hello").text(data.hello);
			}
		);
	}
});