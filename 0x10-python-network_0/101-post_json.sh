#!/bin/bash
# Sends a JSON POST request and Displays the body of the response
curl -s -X POST "$1" -d @"$2" -H "Content-Type: application/json"
