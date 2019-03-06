import collections
import string

def rotate(text, key):
    rotate_lower = string.ascii_lowercase[key::1] + string.ascii_lowercase[:key]
    rotate_upper = string.ascii_uppercase[key::1] + string.ascii_uppercase[:key]
    cipher = dict(zip(string.ascii_lowercase + string.ascii_uppercase ,rotate_lower+rotate_upper))
    return  "".join([cipher.get(ch,ch) for ch in text])
