n = int(input("Enter a number:"))
s = str(n)
sum_digit = 0
for i in s:
    i = int(i)
    sum_digit += i
print("Sum of Digits:",sum_digit)