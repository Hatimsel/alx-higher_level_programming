#!/bin/bash

read -p "Commit message: " COMMIT
git add .
git commit -m "$COMMIT"
git push
