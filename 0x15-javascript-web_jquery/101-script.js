#!/usr/bin/node
/**
 * a JavaScript script that adds, removes and clears LI elements from a
 * list when the user clicks:
 */
$(document).ready(function() {
  $('#add_item').click(function() {
    var newItem = $('<li>Item</li>');
    $('.my_list').append(newItem);
  });

  $('#remove_item').click(function() {
    $('.my_list li:last-child').remove();
  });

  $('#clear_list').click(function() {
    $('.my_list').empty();
  });
});
