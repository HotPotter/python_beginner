from collections import deque

#num_case = input()
#for _ in range(num_case)
def inp():
    d_len = input()
    d_inp = input()
    return d_inp


def d_create(d_inp):
    d_deque = deque(map(int,d_inp.split()))
    return d_deque

def pile(d_deque):
    while max(d_deque) in (d_deque[0] or d_deque[-1]):
        d_deque.remove(max(d_deque))
    if len(d_deque)==0:
        print("Yes")
    else:
        print("No")


def go():
    d_inp=inp()
    d_deque = d_create(d_inp)
    pile(d_deque)

go()

