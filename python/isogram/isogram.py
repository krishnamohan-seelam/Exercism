def is_isogram(string):
    if string is None:
        raise ValueError("Not valid string")
    if string =="":
        return True
    all_chars =[a.lower() for a in string if a.isalpha()]

    return len(all_chars) == len(set(all_chars))