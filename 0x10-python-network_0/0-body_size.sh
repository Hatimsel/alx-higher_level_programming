#!/bin/bash
# Displays the body's size of an HTTP response

curl -sI "$1" | grep 'Content-Length' | grep -e '[0-9]*' -o
