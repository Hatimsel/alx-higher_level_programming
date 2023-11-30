#!/bin/bash
# Sends a POST request, and Displays the body of the response
curl -s "{$1}" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
