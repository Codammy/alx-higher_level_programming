#!/bin/bash
# sends json post request from a file to a passed url(argument).
curl -sH "Content-Type: application/json" -X GET -d @$1 $2
