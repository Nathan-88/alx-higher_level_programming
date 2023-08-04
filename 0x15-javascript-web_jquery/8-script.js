#!/usr/bin/node
/**
 * a JavaScript script that fetches and lists the title for all movies by using this URL: https:
 * swapi-api.alx-tools.com/api/films/?format=json
 */
$(document).ready(function() {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    var movies = data.results;
    var list = $('#list_movies');
    
    $.each(movies, function(index, movie) {
      list.append($('<li>').text(movie.title));
    });
  });
});

// $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
//   $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
// });