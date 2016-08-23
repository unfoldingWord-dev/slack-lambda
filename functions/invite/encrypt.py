from __future__ import print_function, unicode_literals
import base64
import sys
import pyaes.aes

if sys.version_info < (3, 0):
    prompt = raw_input
else:
    prompt = input

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


if __name__ == '__main__':

    # initialization
    plain_text = prompt('Enter the string to encrypt: ')

    # encrypt the string and display
    b64 = encrypt_slack_token(plain_text)
    print()
    print('Encrypted text: {0}'.format(b64))

    # test decrypting and display the result
    plain_text = decrypt_slack_token(b64)
    print()
    print('Decrypted text: {0}'.format(plain_text))
