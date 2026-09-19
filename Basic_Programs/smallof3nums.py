n1 = int(input("Enter a number 1: "))
n2 = int(input("Enter a number 2: "))
n3 = int(input("Enter a number 3: "))
if(n1<n2 and n1<n3):
    smallest = n1
elif(n2<n1 and n2<n3):
    smallest = n2
else:
    smallest = n3
print("Smallest Number is =",smallest)           
    
