from pprint import pprint
all_list = [['Harry', 37.21], ['Berry', 37.21], ['Cat', 378], ['Akriti', 41], ['Harsh', 39], ['Berry', 37.2]]

all_list.sort()

pprint(all_list)

def get_element_2(L):
    return L[1]

def sort_by_name_length(L):
    return len(L[0])

def ___(x):
    return len(x)
#students.sort(key=sort_by_name_length)
#students.sort(key=lambda x: len(x[0]))
all_list.sort(key=lambda x: x[1])
pprint(all_list)

print('what is name???', __name__)

if __name__ == '__main__':
    min_score = all_list[0][1]
    second_min = None
    names = []

    for s in all_list:
        if s[1] == min_score:
            continue
        else:
            if second_min is None:
                second_min = s[1]
                names.append(s[0])
            elif s[1] == second_min:
                names.append(s[0])
            else:
                break

    names.sort()
    print(*names, sep='\n')

print('5')
print('3 3')
print('-1 0 1')
print('4 2')
print('-1 0 1 2')
print('5 4')
print('-1 0 1 2 3')
print('6 3')
print('-2 -1 0 1 2 3')
print('7 5')
print('-2 -1 0 1 2 3 4')
print('8 3')
print('-3 -2 -1 0 1 2 3 4')