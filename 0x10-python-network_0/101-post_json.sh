#!/bin/bash
# sends json post request from a file to a passed url(argument).
curl -s-H "Content-Type: application/json" -X POST -d @$1 $2
