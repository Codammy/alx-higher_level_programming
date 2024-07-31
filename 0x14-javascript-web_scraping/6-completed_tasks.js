#!/usr/bin/node

const request = require('request');
const URL = require('process').argv[2];

request(URL, (err, res, data) => {
  if (err) {
    console.log(err);
    return;
  }
  const users = JSON.parse(data).filter(d => d.completed === true);
  const usersWithTasks = {};
  for (const user of users) {
    const userId = user.userId;
    usersWithTasks[userId] = users.filter(u => u.userId === userId).length;
  }
  console.log(usersWithTasks);
});
