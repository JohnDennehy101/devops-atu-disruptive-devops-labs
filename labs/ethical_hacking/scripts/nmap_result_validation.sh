# Configuration of what is expected and what should not be observed
ALLOWED_PORTS="80|443"
FORBIDDEN_PROD_SERVICES="Werkzeug|DEBUG"

# Grep the results file to filter to only open ports
grep "/open/" scan_results.txt | sed 's/, /\n/g' > open_ports_list.txt

echo "--- Current Open Ports ---"
cat open_only.txt
echo "------------------------------"

# Check that services blacklisted are not present - fail if so
if grep -qiE "$FORBIDDEN_PROD_SERVICES" open_only.txt; then
    echo "CRITICAL: Forbidden service detected (Match: $FORBIDDEN_PROD_SERVICES)"
    exit 1
fi

# Check that only expected ports are exposed and open
UNAUTHORISED=$(grep -vE "($ALLOWED)/open" open_only.txt)

if [ ! -z "$UNAUTHORISED" ]; then
    echo "SECURITY ALERT: Unauthorised open ports found"
    echo "$UNAUTHORISED"
    exit 1
fi

echo "Security Checks Passed: All services compliant with defined configuration."