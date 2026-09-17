n = int(input("Enter a number:"))
s = str(n)
if s[::1] == s[::-1]:
    print("It is Palindrome")
else:
    print("It is not a Palindrome")