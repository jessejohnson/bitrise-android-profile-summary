#!/usr/bin/env bash

$BITRISE_STEP_SOURCE_DIR/scripts/buildreport/print_out_artifact_urls.sh | envman add --key ARTIFACT_URL