from __future__ import unicode_literals

import json
from unittest import TestCase
from functions.invite import requests
from functions.invite.slack_invite import SlackInvite


class TestSlackInvite(TestCase):

    class MockSlackInvite(SlackInvite):
        """
        Subclass SlackInvite so we can override the actual web request
        """

        def do_request(self, slack_data):
            """
            Overridden so we can test various scenarios without hitting the actual Slack API
            :param dict slack_data:
            """
            if slack_data['last_name'] == 'good_request_response':
                resp = requests.Response()
                resp.status_code = 200
                resp._content = bytes('{"ok": 1, "error": ""}')
                self.response = resp
                return

            if slack_data['last_name'] == 'error_request_response':
                resp = requests.Response()
                resp.status_code = 200
                resp._content = bytes('{"ok": 0, "error": "Some_error_message"}')
                self.response = resp
                return

            if slack_data['last_name'] == 'fail_request_response':
                resp = requests.Response()
                resp.status_code = 500
                resp.reason = bytes('Server error')
                self.response = resp
                return

    def test_good_request_response(self):
        """
        This tests the normal flow
        """
        querystring = {'token': 'OQC2issg+AT7',
                       'email': 'test@test.com',
                       'first_name': 'Bob',
                       'last_name': 'good_request_response',
                       'callback': 'CallBack'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        callback, data, validJsonp = self.parseJsonp(response)
        self.assertEqual(querystring['callback'],callback)
        self.assertEqual(True, validJsonp)
        self.assertEqual('success', data['result'])
        self.assertEqual('Invitation sent', data['message'])

    def test_error_missing_callback(self):
        """
        This tests the normal flow
        """
        querystring = {'token': 'OQC2issg+AT7',
                       'email': 'test@test.com',
                       'first_name': 'Bob',
                       'last_name': 'good_request_response'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        callback, data, validJsonp = self.parseJsonp(response)
        self.assertEqual('failed', data['result'])
        self.assertEqual(msi.PARAMETER_PARSE_EXCEPTION, data['message'])

    def test_error_request_response(self):
        """
        This tests when the Slack API returns a not-OK response
        """
        querystring = {'token': 'OQC2issg+AT7',
                       'email': 'test@test.com',
                       'first_name': 'Bob',
                       'last_name': 'error_request_response',
                       'callback': 'CallBack'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        callback, data, validJsonp = self.parseJsonp(response)
        self.assertEqual(querystring['callback'],callback)
        self.assertEqual(True, validJsonp)
        self.assertEqual('error', data['result'])
        self.assertEqual('Some error message', data['message'])

    def test_fail_request_response(self):
        """
        This tests when the Slack API returns a not-OK response
        """
        querystring = {'token': 'OQC2issg+AT7',
                       'email': 'test@test.com',
                       'first_name': 'Bob',
                       'last_name': 'fail_request_response',
                       'callback': 'CallBack'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        callback, data, validJsonp = self.parseJsonp(response)
        self.assertEqual(querystring['callback'],callback)
        self.assertEqual(True, validJsonp)
        self.assertEqual('failed', data['result'])
        self.assertEqual('500: Server error', data['message'])

    def test_fail_invalid_token(self):
        """
        This tests when the Slack API returns a not-OK response
        """
        querystring = {'token': 'OQC2issg+AT7X',
                       'email': 'test@test.com',
                       'first_name': 'Bob',
                       'last_name': 'fail_request_response',
                       'callback': 'CallBack'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        callback, data, validJsonp = self.parseJsonp(response)
        self.assertEqual(querystring['callback'],callback)
        self.assertEqual(True, validJsonp)
        self.assertEqual('failed', data['result'])
        self.assertEqual(msi.PARAMETER_PARSE_EXCEPTION, data['message'])

    def test_missing_token(self):
        """
        This tests when the Slack API returns a not-OK response
        """
        querystring = {'email': 'test@test.com',
                       'first_name': 'Bob',
                       'last_name': 'fail_request_response',
                       'callback': 'CallBack'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        callback, data, validJsonp = self.parseJsonp(response)
        self.assertEqual(querystring['callback'],callback)
        self.assertEqual(True, validJsonp)
        self.assertEqual('failed', data['result'])
        self.assertEqual(msi.PARAMETER_PARSE_EXCEPTION, data['message'])

    def test_missing_email(self):
        """
        This tests when the Slack API returns a not-OK response
        """
        querystring = {'token': 'OQC2issg+AT7',
                       'first_name': 'Bob',
                       'last_name': 'fail_request_response',
                       'callback': 'CallBack'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        callback, data, validJsonp = self.parseJsonp(response)
        self.assertEqual(querystring['callback'],callback)
        self.assertEqual(True, validJsonp)
        self.assertEqual('failed', data['result'])
        self.assertEqual(msi.PARAMETER_PARSE_EXCEPTION, data['message'])

    def test_missing_first_name(self):
        """
        This tests when the Slack API returns a not-OK response
        """
        querystring = {'token': 'OQC2issg+AT7',
                       'email': 'test@test.com',
                       'last_name': 'fail_request_response',
                       'callback': 'CallBack'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        callback, data, validJsonp = self.parseJsonp(response)
        self.assertEqual(querystring['callback'],callback)
        self.assertEqual(True, validJsonp)
        self.assertEqual('failed', data['result'])
        self.assertEqual(msi.PARAMETER_PARSE_EXCEPTION, data['message'])

    def test_missing_last_name(self):
        """
        This tests when the Slack API returns a not-OK response
        """
        querystring = {'token': 'OQC2issg+AT7',
                       'email': 'test@test.com',
                       'first_name': 'Bob',
                       'callback': 'CallBack'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        callback, data, validJsonp = self.parseJsonp(response)
        self.assertEqual(querystring['callback'],callback)
        self.assertEqual(True, validJsonp)
        self.assertEqual('failed', data['result'])
        self.assertEqual(msi.PARAMETER_PARSE_EXCEPTION, data['message'])

    # helper methods

    def parseJsonp(self, text):
        valid = False
        callback = None
        data = None
        try:
            prefix = text.split('(')
            DUMMY_TEST = '__'
            payload = (prefix[1] + DUMMY_TEST).split(')')
            callback = prefix[0]
            data = json.loads(payload[0])
            valid = (payload[1] == DUMMY_TEST) and (len(data) > 0)
        except:
            pass

        return  callback, data, valid

