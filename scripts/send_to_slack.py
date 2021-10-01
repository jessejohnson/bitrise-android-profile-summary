import os
import requests
import json

def send_to_slack():

    SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']
    REPORT_SUMMARY = os.environ['REPORT_SUMMARY']
    ARTIFACT_URL = os.environ['ARTIFACT_URL']
    BITRISE_BUILD_URL = os.environ['BITRISE_BUILD_URL']
    APP_TITLE = os.environ['BITRISE_APP_TITLE']
    BRANCH = os.environ['BITRISE_GIT_BRANCH']
    WORKFLOW = os.environ['BITRISE_TRIGGERED_WORKFLOW_ID']

    data = {
        "attachments": [
            {
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": REPORT_SUMMARY
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "View Build",
                                },
                                "value": "view_build",
                                "url": BITRISE_BUILD_URL
                            },
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "Download Report",
                                },
                                "value": "download_report",
                                "url": ARTIFACT_URL
                            }
                        ]
                    },
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "plain_text",
                                "text": "{} | {} | {}".format(APP_TITLE, BRANCH, WORKFLOW)
                            }
                        ]
                    }
                ]
            }
        ]
    }

    headers = {"Content-Type": "application/json"}

    result = requests.post(SLACK_WEBHOOK_URL, headers=headers, data=json.dumps(data))
    print(result.status_code)
    print(result.text)

send_to_slack()