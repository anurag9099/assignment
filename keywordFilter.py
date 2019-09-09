import re
import sys
import pprint

path = sys.argv[1]

with open(path, 'r') as file:
    corpus = file.read().replace('\n', '')
    
    
def filter_key(key, corpus):
    pattern = "[^.]*"+key+"[^.]*\."
    r = re.findall(pattern, corpus, re.IGNORECASE)
    return r

key = str(input("Enter Filter Keyword:\n")

pprint.pprint(filter_key(key,corpus), width=200)
