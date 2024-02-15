#!/usr/bin/node
const argv = require('process').argv;
const { readFile, writeFile } = require('fs');
function rFile (path) {
  return new Promise((resolve, reject) => {
    readFile(path, (err, data) => {
      if (data) {
        resolve(data.toString());
      } else {
        reject(err);
      }
    });
  });
}
async function main () {
  const data = (await rFile(argv[2])) + (await rFile(argv[3]));
  writeFile(argv[4], data, (err) => {
    if (err) {
      console.log(err);
    }
  });
}
main();
