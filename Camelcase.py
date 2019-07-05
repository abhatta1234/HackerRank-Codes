# Given a camelcase string, find the total words in the string.

import re

string = input()

a = re.findall(r'[A-Z]+', string)

print(len(a)+1)
