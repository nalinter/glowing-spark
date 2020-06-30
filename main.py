import sys
import json
import requests


if __name__ == '__main__':

    webhook_url = 'https://hooks.slack.com/services/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'

    pr_number = sys.argv[1]
    pr_package_name = "module_" + pr_number + "_modules_1.zip"
    console_output = sys.argv[2] + "console"
    job_url = "http://ddywdcdevin01.sl.bluecloud.ibm.com:8080/job/pipeline-testing-CI/PRE-SBX_Report"
    data = {
        "channel": "#random",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "sample message please ignore"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Environment: PRE-SBX"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*PR Number*: " + pr_number + "\n"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*PR Package Name*: " + pr_package_name + "\n"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Deployment To PRE-SBX: *Successful*\n "
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Smoke Test: *Successful*\n "
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Smoke Tests Report: " + job_url
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Click the below Button to go ahead and deploy package to SBX Environment"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "URL:" + console_output
                }
            }
            # {
            #     "type": "section",
            #     "text": {
            #         "type": "mrkdwn",
            #         "text": approval_url
            #     }
            # },
            # {
            #     "type": "actions",
            #     "elements": [
            #         {
            #             "type": "button",
            #             "text": {
            #                 "type": "plain_text",
            #                 "text": "Approve"
            #             },
            #             "value": "click_approve"
            #         },
            #         {
            #             "type": "button",
            #             "text": {
            #                 "type": "plain_text",
            #                 "text": "Reject"
            #             },
            #             "value": "click_reject"
            #         }
            #     ]
            # }
        ],
        'username': 'APPROVAL',
        'icon_emoji': ':robot_face:'
    }

    response = requests.post(
        webhook_url,
        data=json.dumps(data),
        headers={
            'Content-Type': 'application/json'
        }
    )

    print('Response: ' + str(response.text))
    print('Response code: ' + str(response.status_code))
