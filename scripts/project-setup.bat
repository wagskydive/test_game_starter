#!/bin/bash
set -e

for dir in src scripts docs config tests logs; do
    mkdir -p "$dir"
    echo "Created $dir" 1>&2
done

if [ ! -f requirements.txt ]; then
    echo "pytest" > requirements.txt
fi

pip install -r requirements.txt
