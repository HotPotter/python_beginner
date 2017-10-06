import sys,re
N = int(input().strip())
listName = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if  re.match('.*(@gmail.com)', str(emailID)):
        listName.append(firstName)

print(*sorted(listName),sep='\n')


