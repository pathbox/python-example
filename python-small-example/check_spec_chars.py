import re


def has_spec_chars(mystr):
    pat = re.compile(r'\W+')
    return pat.search(mystr) != None


r = has_spec_chars('learnpython110*7%%99hello')
print(r)
