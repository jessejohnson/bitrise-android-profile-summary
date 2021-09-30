#!/bin/bash
set -ex

pip3 install beautifulsoup4

echo $BITRISE_PERMANENT_DOWNLOAD_URL_MAP
python3 $BITRISE_STEP_SOURCE_DIR/scripts/parse_report.py ./build/reports/profile/ | envman add --key REPORT_SUMMARY
python3 $BITRISE_STEP_SOURCE_DIR/scripts/get_report_url.py \
$BITRISE_API_ACCESS_TOKEN $BITRISE_APP_SLUG $BITRISE_BUILD_SLUG | envman add --key ARTIFACT_URL
