#!/bin/bash
# sends json post request from a file to a passed url(argument).
curl -sX POST -d @$2 -H "Content-Type: application/json" $1
