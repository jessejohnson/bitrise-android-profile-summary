#!/bin/bash
set -ex

# echo "This is the value specified for the input 'example_step_input': ${example_step_input}"

# Set up environment
pip3 install beautifulsoup4
# sh $BITRISE_STEP_SOURCE_DIR/scripts/parse_profile_report.sh
# sh $BITRISE_STEP_SOURCE_DIR/scripts/get_profile_report_url.sh

python3 $BITRISE_STEP_SOURCE_DIR/scripts/parse_report.py ./build/reports/profile/ | envman add --key REPORT_SUMMARY
python3 $BITRISE_STEP_SOURCE_DIR/scripts/get_report_url.py $BITRISE_API_ACCESS_TOKEN $BITRISE_APP_SLUG $BITRISE_BUILD_SLUG | envman add --key ARTIFACT_URL
#
# --- Export Environment Variables for other Steps:
# You can export Environment Variables for other Steps with
#  envman, which is automatically installed by `bitrise setup`.
# A very simple example:
# envman add --key EXAMPLE_STEP_OUTPUT --value 'the value you want to share'
# Envman can handle piped inputs, which is useful if the text you want to
# share is complex and you don't want to deal with proper bash escaping:
#  cat file_with_complex_input | envman add --KEY EXAMPLE_STEP_OUTPUT
# You can find more usage examples on envman's GitHub page
#  at: https://github.com/bitrise-io/envman

#
# --- Exit codes:
# The exit code of your Step is very important. If you return
#  with a 0 exit code `bitrise` will register your Step as "successful".
# Any non zero exit code will be registered as "failed" by `bitrise`.
