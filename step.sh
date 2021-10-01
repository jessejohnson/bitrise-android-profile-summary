#!/bin/bash
set -ex

pip3 install beautifulsoup4

# python3 $BITRISE_STEP_SOURCE_DIR/scripts/parse_report.py ./build/reports/profile/ | envman add --key REPORT_SUMMARY
# python3 $BITRISE_STEP_SOURCE_DIR/scripts/get_report_url.py | envman add --key ARTIFACT_URL
# python3 $BITRISE_STEP_SOURCE_DIR/scripts/send_to_slack.py
python3 $BITRISE_STEP_SOURCE_DIR/scripts/script.py ./build/reports/profile/
