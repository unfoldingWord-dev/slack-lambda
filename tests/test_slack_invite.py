from __future__ import unicode_literals
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
                       'last_name': 'good_request_response'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        self.assertEqual('success', response['result'])
        self.assertEqual('Invitation sent', response['message'])

    def test_error_request_response(self):
        """
        This tests when the Slack API returns a not-OK response
        """
        querystring = {'token': 'OQC2issg+AT7',
                       'email': 'test@test.com',
                       'first_name': 'Bob',
                       'last_name': 'error_request_response'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        self.assertEqual('error', response['result'])
        self.assertEqual('Some error message', response['message'])

    def test_fail_request_response(self):
        """
        This tests when the Slack API returns a not-OK response
        """
        querystring = {'token': 'OQC2issg+AT7',
                       'email': 'test@test.com',
                       'first_name': 'Bob',
                       'last_name': 'fail_request_response'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        self.assertEqual('failed', response['result'])
        self.assertEqual('500: Server error', response['message'])

    def test_fail_invalid_token(self):
        """
        This tests when the Slack API returns a not-OK response
        """
        querystring = {'token': 'OQC2issg+AT7X',
                       'email': 'test@test.com',
                       'first_name': 'Bob',
                       'last_name': 'fail_request_response'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        self.assertEqual('failed', response['result'])
        self.assertEqual(msi.PARAMETER_PARSE_EXCEPTION, response['message'])

    def test_missing_token(self):
        """
        This tests when the Slack API returns a not-OK response
        """
        querystring = {'email': 'test@test.com',
                       'first_name': 'Bob',
                       'last_name': 'fail_request_response'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        self.assertEqual('failed', response['result'])
        self.assertEqual(msi.PARAMETER_PARSE_EXCEPTION, response['message'])

    def test_missing_email(self):
        """
        This tests when the Slack API returns a not-OK response
        """
        querystring = {'token': 'OQC2issg+AT7',
                       'first_name': 'Bob',
                       'last_name': 'fail_request_response'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        self.assertEqual('failed', response['result'])
        self.assertEqual(msi.PARAMETER_PARSE_EXCEPTION, response['message'])

    def test_missing_first_name(self):
        """
        This tests when the Slack API returns a not-OK response
        """
        querystring = {'token': 'OQC2issg+AT7',
                       'email': 'test@test.com',
                       'last_name': 'fail_request_response'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        self.assertEqual('failed', response['result'])
        self.assertEqual(msi.PARAMETER_PARSE_EXCEPTION, response['message'])

    def test_missing_last_name(self):
        """
        This tests when the Slack API returns a not-OK response
        """
        querystring = {'token': 'OQC2issg+AT7',
                       'email': 'test@test.com',
                       'first_name': 'Bob'}

        msi = TestSlackInvite.MockSlackInvite()
        response = msi.send_invite(querystring)

        self.assertEqual('failed', response['result'])
        self.assertEqual(msi.PARAMETER_PARSE_EXCEPTION, response['message'])
