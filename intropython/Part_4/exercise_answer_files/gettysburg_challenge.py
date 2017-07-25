from collections import Counter
import re

with open("gettysburg_address.txt") as f:
    wf= Counter(re.split(r'\W+', f.read())) # r'\W+' is a regular expression for 1+ non-word characters
del wf[''] # the . at the very end creates a single entry of ''

print("Number of words in the file:",wf)