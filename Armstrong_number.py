n = int(input("Enter a number:"))
s = str(n)
sum = 0
for i in s:
    i = int(i)
    sum += i**len(s)
if sum == n:    
    print("It is Armstrong Number")
else:
    print("It is not Armstrong Number")