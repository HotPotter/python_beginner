    # find integers from a list, and move all the integers into a newList

newList = []

def search(aList):
    for node in aList:
        if type(node) is not list:
            if type(node) is int:
                aList.remove(node)
                newList.append(node)
            else:
                continue
        else:
            return search(aList)
            #return search(node)
aList = [0,
    [1,"a","b"],
    ["c","d",[2,"e","f"],"g"],
    [3,4],
    [5,[6,[7,"h","i"],"j"],"k"]
]

search(aList)
print(newList)
