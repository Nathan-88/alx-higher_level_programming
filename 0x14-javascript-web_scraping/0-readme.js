#!/usr/bin/node
// a script that reads and prints the content of a file
const fs = require('fs');

// Replace 'your_file_path.txt' with the path to your file
const filePath = process.argv[2];

// Read the file using utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, content) => {
  if (err) {
    console.error(err);
  } else {
    console.log(content);
  }
});
