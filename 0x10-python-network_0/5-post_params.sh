#!/bin/bash
# Sends a POST request to the passed URL, and displays the body of the response
curl -sF "email=test@gmail.com" -F "subject=I will always be here for PLD" "$1"
