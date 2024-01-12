#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

fs.readFile(argv[2], (err, txt1) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.readFile(argv[3], (err, txt2) => {
    if (err) {
      console.log(err);
      return;
    }
    const text = txt1.toString() + txt2.toString();
    fs.writeFile(argv[4], text, (err) => {
      if (err) { console.log(err); }
    });
  });
});
