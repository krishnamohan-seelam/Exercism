import re
def abbreviate(words):
    #words =[re.sub("[^a-zA-Z' ]+",'',token.replace("'", ""))[0]  for token in re.findall("[a-zA-Z']+",words)]
    words =[token[0]  for token in re.findall("[a-zA-Z']+",words)]
    return "".join(words).upper()
