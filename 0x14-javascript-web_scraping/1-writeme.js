#!/usr/bin/node

const fs = require('fs');
const [filepath, text] = [...require('process').argv.slice(2, 4)];

fs.writeFile(filepath, text, 'utf-8', (err) => {
  if (err) { console.log(err); }
});
