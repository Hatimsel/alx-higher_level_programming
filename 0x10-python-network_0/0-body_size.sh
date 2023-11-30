#!/bin/bash
# Displays the size of the body of the message
curl -s $1 -i | grep -i Content-Length | cut -d ' ' -f2
