#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, resp, body) => {
  if (error) {
    console.error(error);
  }
  const tasks = {};
  const jsonData = JSON.parse(body);
  jsonData.forEach(task => {
    const userId = task.userId;
    if (task.completed) {
      if (tasks[userId]) {
        tasks[userId]++;
      } else {
        tasks[userId] = 1;
      }
    }
  });
  console.log(tasks);
});
