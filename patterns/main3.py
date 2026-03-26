n=int(input("enter the number of size: "))
for row in range(n):
    for col in range(row +1):
        print('*',end=' ')
    print()