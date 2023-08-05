#!/usr/bin/node
/**
 * a JavaScript script that fetches and prints how to say “Hello” depending on the language
 */
$(document).ready(function () {
	$("input#btn_translate").click(fetchTranslation);
	$("input#language_code").keyup(function (event) {
		if (event.keyCode === 13) {
			fetchTranslation();
		}
	});

	function fetchTranslation() {
		const languageCode = $("input#language_code").val();
		$.getJSON(`https://hellosalut.stefanbohacek.dev/hello/?lang=${languageCode}`, function (data) {
				$("#hello").text(data.hello);
			}
		)
		.fail(function () {
			$("#hello").text('Translation failed. Please try again later.');
		});
	}
});
