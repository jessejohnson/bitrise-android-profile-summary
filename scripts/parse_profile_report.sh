#!/usr/bin/env bash

apt-get install -y python-bs4
python $BITRISE_STEP_SOURCE_DIR/scripts/parse_report.py ./build/reports/profile/ | envman add --key REPORT_SUMMARY
