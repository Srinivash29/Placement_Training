n = int(input("Enter a number:"))
a = n**2
s = str(a)
sum = 0
for i in s:
    i = int(i)
    sum += i
if n == sum:
    print("It is Neon Number")
else:
    print("It is not Neon Number")

