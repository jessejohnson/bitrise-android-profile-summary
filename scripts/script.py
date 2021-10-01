from parse_report import find_report, parse
from get_report_url import get_permanent_download_url, get_expiring_download_url
from send_to_slack import send_slack_message

import sys

REPORT_DIR = sys.argv[1]

# First, find and parse report
report_file = find_report(REPORT_DIR)
summary = parse_report(report_file)

# Then, get report artifact url
download_url = get_permanent_download_url()
if download_url is None:
    download_url = get_expiring_download_url()

# Finally, send to Slack!
send_slack_message(summary, download_url)