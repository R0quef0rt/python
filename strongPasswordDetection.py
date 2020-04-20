import re

def strongPasswordDetection(password):
    lengthRegex = re.compile(r'.{8,}')
    if lengthRegex.search(password):
        print('Password is 8 or more characters in length.')

    uppercaseRegex = re.compile(r'[A-Z]{1,}')
    if uppercaseRegex.search(password):
        print('Password contains at least 1 uppercase character.')

    lowercaseRegex = re.compile(r'[a-z]{1,}')
    if lowercaseRegex.search(password):
        print('Password contains at least 1 lowercase character.')

    numberRegex = re.compile(r'[0-9]{1,}')
    if numberRegex.search(password):
        print('Password contains at least 1 number.')

strongPasswordDetection('H7iL54Ntpc;')