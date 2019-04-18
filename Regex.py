import re

def RegexExact(pat,query):
    found = re.search(pat,query,flags=re.IGNORECASE)
    if (found!=None):
        return True
    else:
        return False

def RegexNotExact(pat,query):
    for words in pat.split(' '):
        found = re.search(words,query,flags=re.IGNORECASE)
        if (found==None):
            return False
    return True

def Regex(query,dictionary):
    output = []
    for keys in dictionary:
        if (RegexExact(keys,query)):
            output.append((keys))
        else:
            if (RegexNotExact(keys,query)):
                output.append((keys))
    return output