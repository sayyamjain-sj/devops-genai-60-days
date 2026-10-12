#!/bin/bash

URLS=(
    "https://google.com"
    "https://github.com"
    "http://127.0.0.1:8000/health"
)

for URL in "${URLS[@]}"
do
    STATUS=$(curl -L -o /dev/null -s -w "%{http_code}" "$URL")

    if [ "$STATUS" -ge 200 ] && [ "$STATUS" -lt 400 ]; then
        echo "PASS | $URL | HTTP $STATUS"
    else
        echo "FAIL | $URL | HTTP $STATUS"
    fi
done