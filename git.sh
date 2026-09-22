#!/bin/bash

# Stop execution if any command fails
set -e

echo "--- Checking Git Status ---"
git status

echo "--- Staging assignment1_part2.py ---"
git add assignment1_part2.py

echo "--- Committing Changes ---"
git commit -m "Add assignment1_part2.py with Book class implementation"

echo "--- Pushing to GitHub ---"
git push origin master

echo "--- Git operations complete! ---"
