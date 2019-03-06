twelve_days = {1: 'first',
               2: 'second',
               3: 'third',
               4: 'fourth',
               5: 'fifth',
               6: 'sixth',
               7: 'seventh',
               8: 'eighth',
               9: 'ninth',
               10: 'tenth',
               11: 'eleventh',
               12: 'twelfth',
               }

verses='twelve Drummers Drumming,eleven Pipers Piping,ten Lords-a-Leaping,\
nine Ladies Dancing,eight Maids-a-Milking,seven Swans-a-Swimming,\
six Geese-a-Laying,five Gold Rings,four Calling Birds,three French Hens,\
two Turtle Doves,a Partridge in a Pear Tree.'

verses = verses.split(',')

def recite(start_verse, end_verse):
    poem = []
    for key in range(start_verse, end_verse+1):
        dayname = twelve_days[key]
        daymessage = ", ".join(verses[-1 * key:-1]) 
        daymessage  =  daymessage + ', and ' + verses[-1] if daymessage else verses[-1]
        verse = "On the {} day of Christmas my true love gave to me: {}".format(dayname, daymessage)
        poem.append(verse)
    return poem
