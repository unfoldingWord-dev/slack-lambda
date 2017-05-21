from __future__ import unicode_literals
import json
import logging
from slack_invite import SlackInvite

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# noinspection PyUnusedLocal
def handle(event, context):
    """
    Receives a JSONP request and returns an appropriate response
    :param dict event:
    :param context:
    :return: str
    """
    querystring = event['params']['querystring']
    response = SlackInvite().send_invite(querystring)
    return querystring['callback'] + '(' + json.dumps(response) + ')'
