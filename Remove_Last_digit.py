n = int(input("Enter a number:"))
s = str(n)
a = ""
for i in range(len(s)):
    if s[i] == s[-1]:
        continue
    a += s[i]
print(a)    
