n1 = int(input("Enter a number 1:"))
n2 = int(input("Enter a number 2:"))
s1 = str(n1)
s2 = str(n2)
if len(s1) < len(s2):
    print(f"{n1} is the Smallest Digit")
else:
    print(f"{n2} is the Smallest Digit")