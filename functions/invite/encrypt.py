from __future__ import print_function, unicode_literals
import base64
import sys
import pyaes.aes

if sys.version_info < (3, 0):
    prompt = raw_input
else:
    prompt = input


if __name__ == '__main__':

    # initialization
    plain_text = prompt('Enter the string to encrypt: ')
    key = 'unfoldingWord.org_door43.org_ufw'
    iv = 'unfoldingWord_43'

    # encrypt the string and display
    aes = pyaes.AESModeOfOperationOFB(key, iv=iv)
    encrypted_text = aes.encrypt(plain_text)
    b64 = base64.b64encode(encrypted_text)
    print()
    print('Encrypted text: {0}'.format(b64))

    # test decrypting and display the result
    aes = pyaes.AESModeOfOperationOFB(key, iv=iv)
    plain_text = aes.decrypt(base64.b64decode(b64))
    print()
    print('Decrypted text: {0}'.format(plain_text))
