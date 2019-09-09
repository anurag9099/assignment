import re
import sys

path = sys.argv[1]

with open(path, 'r') as file:
    corpus = file.read().replace('\n', '')
    
    
def filter_key(key, corpus):
    pattern = "[^.]*"+key+"[^.]*\."
    r = re.findall(pattern, corpus, re.IGNORECASE)
    return r

key = str(input("Enter Filter Keyword:\n"))
print(filter_key(key, corpus))