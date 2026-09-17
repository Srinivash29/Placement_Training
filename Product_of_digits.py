n = int(input("Enter a number:"))
s = str(n)
product_digit = 1
for i in s:
    i = int(i)
    product_digit *= i
print("Product of Digits:",product_digit)