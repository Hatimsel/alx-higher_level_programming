#!/bin/bash
# Display the body of a 200 status code response
if [ "$(curl -s "$1" | head -n 1 | grep -E "[0-9]{3}" -o)" == "200"]; then curl -sI "$1"; fi
