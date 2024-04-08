#!/bin/bash
# Bash script that takes in a URL, send request and displays response size
curl -sI $1 | grep "Content-Length" | cut -c17- -;
