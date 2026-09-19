n = int(input("Enter a number:"))
a = n**2
s = str(a)
if int(s[-1]) == n:
    print("It is Automorphic number")
else:
    print("It is not Automorphic number")
