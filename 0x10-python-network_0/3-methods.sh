#!/bin/bash
#Accept URL, display all methods
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '
