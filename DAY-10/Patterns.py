

'''

n= int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print(col,end=' ')
    print()
    
'''

'''

n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print(row,end=' ')
    print()
    
'''

'''
n=int(input("Enter the size: "))
num=1
for row in range(n):
    for col in range(n):
        print(num,end=' ')
        num+=1
    print()
'''
'''
n=int(input("Enter the size: "))
num=1
for row in range(n):
    for col in range(n):
        print(row+col,end=' ')
        num+=1
    print()
'''

'''
n=int(input("Enter the size: "))
for row in range(n):
    for col in range (n):
        if (row+col)%2==0:
            print(0,end=' ')
        else:
            print('X',end=' ')
    print()
'''

n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n-row):
        print("*",end=' ')
    print()
        
























