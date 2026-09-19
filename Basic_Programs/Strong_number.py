n = int(input("Enter a number:"))
s = str(n)
sum = 0
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
for i in s:
    i = int(i)
    sum += fact(i)
if sum == n:
    print("It is Strong Number")   
else:
    print("It is not a Strong number")