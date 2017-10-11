from collections import deque

def inp():
    d_len = input()
    deck_inp = input()
    return deck_inp

def deck_create(deck_inp):
    deck = deque(map(int, deck_inp.split()))
    return deck

def pile(deck):
    i = 0
    while i < len(deck) - 1 and deck[i] >= deck[i+1]:
        i += 1
    while i < len(deck) - 1 and deck[i] <= deck[i+1]:
        i += 1

    if i == len(deck)-1:
        print("Yes")
    else:
        print("No")

def go():
    deck_inp = inp()
    deck = deck_create(deck_inp)
    pile(deck)

for _ in range(int(input())):
    go()