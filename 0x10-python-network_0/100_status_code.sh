#!/bin/bash
# sends a request to a url passed as argument
curl -I $1 | grep OK - | cut -c10-12
