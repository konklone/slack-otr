#!/usr/bin/env python

import os
from slackclient import SlackClient



def init(token):
    slack = SlackClient(token)

    # Find test channel ID.
    channels = slack.api_call("channels.list")['channels']
    test_name = "bot-testing"
    test_channel = None
    for channel in channels:
        if channel['name'] == test_name:
            test_channel = channel['id']

    slack.api_call(
      "chat.postMessage",
      channel=test_channel,
      text="Hello again, as the bot"
    )

    slack.api_call(
      "chat.postMessage",
      channel=test_channel,
      as_user=True,
      text="Hello again, as me"
    )


if __name__ == '__main__':
    admin_token = os.environ["SLACK_ADMIN_USER_TOKEN"]
    init(admin_token)
