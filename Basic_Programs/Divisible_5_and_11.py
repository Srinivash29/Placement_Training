n = int(input("Enter a number:"))
for i in range(1,n+1):
    if i%5==0 and i%11==0:
        print(i,end=" ")