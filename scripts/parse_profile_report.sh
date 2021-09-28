#!/usr/bin/env bash

echo "Parsing Android build report"
apt get install beautifulsoup4
python3 ./scripts/buildreport/parse_report.py ./build/reports/profile/ | envman add --key REPORT_SUMMARY
