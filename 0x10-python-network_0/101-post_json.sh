#!/bin/bash
#Accept URL and filename, post file contents
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
