n = int(input("Enter a number:"))
divisor = 0
for i in range(1,n-1):
    if n%i == 0:
        divisor += i
if n == divisor:
    print("It is a Perfect Number")       
else:
    print("It is not a Perfect Number")          
