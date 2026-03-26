n=int(input("Enter the number of sizes: "))
for row in range(n):
    for spc in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
            print('*',end=' ')
    print()