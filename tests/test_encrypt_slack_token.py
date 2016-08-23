from __future__ import unicode_literals
from unittest import TestCase
from functions.invite.encrypt import encrypt_slack_token, decrypt_slack_token


class TestEncryptSlackToken(TestCase):
    # noinspection SpellCheckingInspection
    def test_encrypt_slack_token(self):

        test_token = 'asdfghjkl'
        expected_value = 'OQC2issg+AT7'

        # test the encryption
        encrypted_token = encrypt_slack_token(test_token)
        self.assertEqual(expected_value, encrypted_token)

        # test the decryption
        decrypted_token = decrypt_slack_token(encrypted_token)
        self.assertEqual(test_token, decrypted_token)
