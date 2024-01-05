#!/bin/bash
#Accept URL, displyay status codes
curl -o /dev/null -w '%{http_code}' -sLI "$1"
