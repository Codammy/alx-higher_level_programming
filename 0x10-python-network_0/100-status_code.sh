#!/bin/bash
# sends a request to a url passed as argument
curl -sI -o /dev/null -w "%{http_code}" $1 
