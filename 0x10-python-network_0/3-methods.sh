#!/bin/bash
# takes in a URL, sends a request to that URL.
curl -sIX ALLOW $1 | grep Allow | cut -c 8-
