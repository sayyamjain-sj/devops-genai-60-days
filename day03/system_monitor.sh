REPORT_DIR="reports"
REPORT_FILE="$REPORT_DIR/system_$(date +%Y-%m-%d_%H-%M-%S).txt"

mkdir -p "$REPORT_DIR"
{
    echo "=============================="
    echo " SYSTEM HEALTH REPORT"
    echo "=============================="

    echo ""
    echo "Timestamp:"
    date

    echo ""
    echo "Hostname:"
    hostname

    echo ""
    echo "Current User:"
    whoami

    echo ""
    echo "Disk Usage:"
    df -h

    echo ""
    echo "Project Directory Size:"
    du -sh ~/devops-genai

    echo ""
    echo "Top CPU Processes:"
    ps aux | sort -nrk 3 | head -5

    echo ""
    echo "Top Memory Processes:"
    ps aux | sort -nrk 4 | head -5

} > "$REPORT_FILE"

echo "Report created:"
echo "$REPORT_FILE"

DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')

if [ "$DISK_USAGE" -gt 80 ]; then
    echo "WARNING: Disk usage is above 80%!"
else
    echo "Disk usage is healthy."
fi