#!/bin/bash
#Accept URL, add header variable
curl -s -H "X-School-User-Id":98 "$1"
