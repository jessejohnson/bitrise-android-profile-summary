#!/bin/bash
set -ex

pip3 install beautifulsoup4
python3 $BITRISE_STEP_SOURCE_DIR/scripts/script.py ./build/reports/profile/
