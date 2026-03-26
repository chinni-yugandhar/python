n=int(input("enter the number of size: "))
for row in range(n):
    for col in range(n-row):
        print('*',end=' ')
    print()