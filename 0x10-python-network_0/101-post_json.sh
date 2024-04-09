#!/bin/bash
# sends json post request from a file to a passed url(argument).
curl -sH "Content-Type: application/json" -X POST -d @$1 $2
