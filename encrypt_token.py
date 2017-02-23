from __future__ import print_function, unicode_literals
import sys
from functions.invite.encrypt import encrypt_slack_token, decrypt_slack_token

if sys.version_info < (3, 0):
    prompt = raw_input
else:
    prompt = input


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
