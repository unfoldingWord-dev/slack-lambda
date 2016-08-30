from __future__ import print_function, unicode_literals
import base64
import pyaes.aes

key = 'unfoldingWord.org_door43.org_ufw'
iv = 'unfoldingWord_43'


def encrypt_slack_token(token):
    global key, iv

    aes = pyaes.AESModeOfOperationOFB(key, iv=iv)
    encrypted_text = aes.encrypt(token)
    return base64.b64encode(encrypted_text)


def decrypt_slack_token(encrypted_token):
    global key, iv

    aes = pyaes.AESModeOfOperationOFB(key, iv=iv)
    return aes.decrypt(base64.b64decode(encrypted_token))
