#!/usr/bin/env bash

echo "Parsing Android build"
# pip install beautifulsoup4
apt-get install python-bs4
python3 $BITRISE_STEP_SOURCE_DIR/scripts/parse_report.py ./build/reports/profile/ | envman add --key REPORT_SUMMARY
