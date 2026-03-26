n=int(input("Enter the number of sizes: "))
for row in range(n):
    for spc in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()