#Given a string remove all adjacent same string. Example: aaabccddd changes to abd

import re
inp = input()

diff = len(inp)- len(set(inp))

for i in range(diff):
    a = re.sub(r'(.)\1',"",inp)
    inp = a
    if a != inp: # Adding this statement makes the program more efficient as it will break loop when there are no
        inp = a  # adjacent repeating characters.
    else:
        break
if a:
    print(a)
else:
    print("Empty String")