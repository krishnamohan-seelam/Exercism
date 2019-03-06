def hey(phrase):

    if not phrase.strip():
        return 'Fine. Be that way!'
    if not phrase.isupper() and phrase.strip()[-1] == '?':
        response = "Sure."
    elif phrase.isupper() and phrase.strip()[-1] == '?':
        response = "Calm down, I know what I'm doing!"
    elif phrase.isupper():
        response = 'Whoa, chill out!'
    else:
        response = 'Whatever.'
    return response
