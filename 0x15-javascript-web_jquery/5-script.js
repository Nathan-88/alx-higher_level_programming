#!/usr/bin/node
/**
 * a JavaScript script that adds a <li> element to a list when the user clicks on the tag
 * DIV#add_item
 */
$(document).ready(function() {
  $('#add_item').click(function() {
    var newItem = $('<li>Item</li>');
    $('.my_list').append(newItem);
  });
});
