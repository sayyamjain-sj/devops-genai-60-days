#!/bin/bash

echo "================================"
echo " NETWORK HEALTH MONITOR"
echo "================================"

echo ""
echo "Time:"
date

echo ""
echo "Hostname:"
hostname

echo ""
echo "Local IP:"

LOCAL_IP=$(ipconfig getifaddr en0 2>/dev/null)

if [ -n "$LOCAL_IP" ]; then
    echo "$LOCAL_IP"
else
    echo "Unable to detect Wi-Fi IP"
fi

echo ""
echo "Internet Connectivity:"

if ping -c 1 google.com > /dev/null 2>&1; then
    echo "PASS: Internet reachable"
else
    echo "FAIL: Internet unreachable"
fi

echo ""
echo "DNS Test:"

if nslookup google.com > /dev/null 2>&1; then
    echo "PASS: DNS working"
else
    echo "FAIL: DNS problem"
fi

echo ""
echo "FastAPI Health Check:"

STATUS=$(curl \
    --connect-timeout 3 \
    --max-time 5 \
    -o /dev/null \
    -s \
    -w "%{http_code}" \
    http://127.0.0.1:8000/health)

if [ "$STATUS" -eq 200 ]; then
    echo "PASS: API healthy"
else
    echo "FAIL: API returned HTTP $STATUS"
fi

echo ""
echo "Port 8000:"
lsof -i :8000

echo ""
echo "================================"
echo " CHECK COMPLETE"
echo "================================"