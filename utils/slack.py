####
# Helper functions to make using the Slack Python SDK easier.

# Official Slack Python SDK:
# https://slackapi.github.io/python-slackclient/
from slackclient import SlackClient

# TODO: Set up logger from env vars or something.
logger = None
log_channel = "#otr-bot-logging"
log_channel_id = None


# Create a Slack client for a user token.
def client_for(token):
    return SlackClient(token)


# Map a channel name to a channel ID.
def get_channel(client, channel_name):
    channels = client.api_call("conversations.list")['channels']
    for channel in channels:
        if channel['name'] == channel_name.replace("#", ""):
            return channel
    return None


# Post to a channel with a given name.
# When posting as a workspace app, cannot use as_user.
def post_to(client, message, channel_id=None, channel_name=None):
    if (channel_id is None) and (channel_name is not None):
        channel_id = get_channel(client, channel_name)['id']
    if channel_id is None:
        return None

    return client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message
    )


# Returns a list of public channel objects right from the API.
# TODO: Pagination in case channels > 100.
def all_public_channels(client):
    return client.api_call("conversations.list")['channels']


# Returns a list of message objects right from the API.
# Can filter to messages older_than a given datetime.
# TODO: Pagination in case messages > 100.
def public_messages(client, channel_id=None, channel_name=None, older_than=None):
    if (channel_id is None) and (channel_name is not None):
        channel_id = get_channel(client, channel_name)['id']
    if channel_id is None:
        return None

    if older_than is not None:
        messages = client.api_call(
            "conversations.history",
            channel=channel_id,
            latest=older_than.timestamp(),
            inclusive=True
        )
    else:
        messages = client.api_call(
            "conversations.history",
            channel=channel_id
        )

    return messages['messages']


# Given a message's channel and timestamp, delete it.
def delete_message(client, channel_id, timestamp):
    return client.api_call(
        "chat.delete",
        channel=channel_id,
        ts=timestamp
    )


# Logging, via a given Slack channel
def log(message):
    global log_channel, log_channel_id, log_client

    if log_channel_id is None:
        log_channel_id = get_channel(logger, log_channel)['id']
        # print("Debug: Cached log channel ID: %s" % log_channel_id)

    print("Logging: %s" % message)
    response = logger.api_call(
        "chat.postMessage",
        channel=log_channel_id,
        text=message
    )
    # print("Debug: %s" % response)

    return response

