from __future__ import unicode_literals
import json
import urllib
import requests
import time
import logging
from encrypt import decrypt_slack_token

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class SlackInvite(object):
    """
    Process a request to send someone a Slack invitation
    """

    PARAMETER_PARSE_EXCEPTION = 'Invalid token'

    def __init__(self):
        self.slack_url = 'https://team43.slack.com/api/users.admin.invite?t={0}'.format(int(time.time()))
        self.response = None

    def send_invite(self, querystring):
        """
        Build the request and interpret the response from the Slack API
        :param dist querystring:
        :return: dict
        """
        callback = ""
        try:
            # decrypt the passed token
            callback = querystring['callback']
            token = decrypt_slack_token(urllib.unquote(querystring['token']))
            email = urllib.unquote(querystring['email'])
            f_name = urllib.unquote(querystring['first_name'])
            l_name = urllib.unquote(querystring['last_name'])
            # noinspection SpellCheckingInspection
            channels = 'C04PNHLCE'

            slack_data = {'email': email, 'channels': channels,
                          'first_name': f_name, 'last_name': l_name,
                          'token': token, 'set_active': 'true', '_attempts': '1'}
            self.do_request(slack_data)

            if self.response.status_code == 200:
                resp_obj = json.loads(self.response.text)
                if resp_obj['ok']:
                    logger.info("slack invite success to: " + email)
                    data = {'result': 'success', 'message': 'Invitation sent'}
                else:
                    reason = resp_obj['error'].replace('_', ' ')
                    logger.error("invite to '" + email + "' returned error: " + reason)
                    data = {'result': 'error', 'message': reason}
            else:
                reason = str(self.response.status_code) + ': ' + self.response.reason
                logger.error("invite call failed: " + reason)
                data = {'result': 'failed', 'message': reason}
        except:
            logger.exception("crash parsing parameters")
            data = {'result': 'failed', 'message': self.PARAMETER_PARSE_EXCEPTION}

        return callback + '(' + json.dumps(data) + ')'

    def do_request(self, slack_data):
        """
        This is separate so we can override it for unit testing
        :param dict slack_data:
        """
        self.response = requests.post(self.slack_url, data=slack_data)
