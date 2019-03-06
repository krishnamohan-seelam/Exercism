import re
import string
def is_pangram(sentence):
    sentence = re.sub('[^A-Za-z]+','',sentence).lower()
    return set(sentence) == set(string.ascii_lowercase)

