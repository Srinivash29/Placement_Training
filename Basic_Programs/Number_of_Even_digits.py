n = int(input("Enter a number:"))
s = str(n)
count = 0
for i in s:
    i = int(i)
    if i%2 == 0:
        count += 1
print("Number of Even Digits:",count)        