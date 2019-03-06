import collections
def find_anagrams(word, candidates):
    anagrams =[candidate for candidate in candidates 
                         if word.lower() != candidate.lower() 
                         and (collections.Counter(candidate.lower())==collections.Counter(word.lower()))]
    return anagrams
