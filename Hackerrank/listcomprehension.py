''' regular way
x = int (input())
y = int (input())
z = int (input())
n = int (input())
ar = []
p = 0
for i in range ( x + 1 ) :
    for j in range( y + 1):
        for t in range (z+1):
            if i+j+t != n:
                ar.append([])
                ar[p] = [ i , j, t ]
                p+=1
print(ar)
'''

#list comprehension
x = int (input())
y = int (input())
z = int (input())
n = int (input())
ar = [[i,j,t]for i in range(x+1) for j in range(y+1) for t in range(z+1) if (i+j+t !=n)]
print(ar)