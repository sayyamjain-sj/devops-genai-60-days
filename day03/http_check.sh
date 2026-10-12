#!/bin/bash

URL="http://127.0.0.1:8000/health"

echo "Checking $URL..."

STATUS_CODE=$(curl \
    --connect-timeout 5 \
    --max-time 10 \
    -o /dev/null \
    -s \
    -w "%{http_code}" \
    "$URL")

if [ "$STATUS_CODE" -eq 200 ]; then
    echo "PASS: Service is healthy."
else
    echo "FAIL: Service returned status $STATUS_CODE."
fi