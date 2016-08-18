from __future__ import print_function, unicode_literals
from base64 import b64decode
import json
import logging
import time
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# noinspection PyUnusedLocal
def handle(event, context):
    """
    Receives a JSONP request and
    :param event:
    :param context:
    :return: str
    """
    querystring = event['params']['querystring']
    callback = querystring['callback']

    # noinspection PyBroadException
    token = b64decode('slack key goes here')
    email = querystring['email']
    f_name = querystring['first_name']
    l_name = querystring['last_name']
    channels = 'C04PNHLCE'

    slack_url = 'https://team43.slack.com/api/users.admin.invite?t={0}'.format(int(time.time()))
    slack_data = {'email': email, 'channels': channels,
                  'first_name': f_name, 'last_name': l_name,
                  'token': token, 'set_active': 'true', '_attempts': '1'}
    response = requests.post(slack_url, data=slack_data)

    if response.status_code == 200:
        resp_obj = json.loads(response.text)
        if resp_obj['ok']:
            return callback + '({"result": "success", "message": "{0}"})'.format(response.text)
    else:
        return callback + '({"result": "failed", "message": "{0}: {1}"})'.format(response.status_code,
                                                                                 response.reason)
