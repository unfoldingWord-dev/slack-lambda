from __future__ import print_function, unicode_literals
import json
import logging
import time
import urllib
import requests
from functions.invite.encrypt import decrypt_slack_token

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

    # decrypt the passed token
    token = decrypt_slack_token(urllib.unquote(querystring['token']))
    email = urllib.unquote(querystring['email'])
    f_name = urllib.unquote(querystring['first_name'])
    l_name = urllib.unquote(querystring['last_name'])
    channels = 'C04PNHLCE'

    slack_url = 'https://team43.slack.com/api/users.admin.invite?t={0}'.format(int(time.time()))
    slack_data = {'email': email, 'channels': channels,
                  'first_name': f_name, 'last_name': l_name,
                  'token': token, 'set_active': 'true', '_attempts': '1'}
    response = requests.post(slack_url, data=slack_data)

    if response.status_code == 200:
        resp_obj = json.loads(response.text)
        if resp_obj['ok']:
            data = {'result': 'success', 'message': 'Invitation sent'}
        else:
            data = {'result': 'error', 'message': resp_obj['error'].replace('_', ' ')}
    else:
        data = {'result': 'failed', 'message': response.status_code + ': ' + response.reason}

    return callback + '(' + json.dumps(data) + ')'
