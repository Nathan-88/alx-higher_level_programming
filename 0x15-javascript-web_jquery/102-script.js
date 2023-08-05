#!/usr/bin/node
/**
 * a JavaScript script that fetches and prints how to say “Hello”
 * depending on the language
 */
$(document).ready(function() {
  $('#btn_translate').click(function() {
    var languageCode = $('#language_code').val();
    var apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

    $.getJSON(apiUrl, function(data) {
      $('#hello').text(data.hello);
    })
    .fail(function() {
      $('#hello').text('Translation failed. Please try again later.');
    });
  });
});
