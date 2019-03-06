import re 
import collections
def word_count(phrase):
    pattern = re.compile(r"[^a-zA-Z0-9']")
    keywords=[ word[1:-1].lower() if word.startswith("'") and  word.endswith("'") else 
               word.lower()
               for word in pattern.split(phrase) if word
             ]

    return collections.Counter(keywords)

