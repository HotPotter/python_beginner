import xml.etree.ElementTree as ET
import sqlite3

fname = input("enter file: ")
if len(fname)<1:
    fname = "library01.xml"

def lookup(d, key):
    found = False
    for child in d:
        print('Child Tag:', child.tag, "    Child Text: ", child.text)
        if found : return child.text
        print('return value: ', child.text)
        if child.tag == 'key' and child.text == key :
            found = True

    return None

data = ET.parse(fname)
all = data.findall('dict/dict/dict')
print(len(all))



for entry in all:
    if ( lookup(entry, 'Track ID') is None ): continue

    title = lookup(entry, 'Name')
    #artist = lookup(entry,'Artist')
    #album = lookup(entry,'Album')
    #genre = lookup(entry, 'Genre')
    #count = lookup(entry,'Play Count')
    ##len = lookup(entry,'Total Time')

#    if title is None or artist is None or album is None or genre is None :continue
    print(title)
