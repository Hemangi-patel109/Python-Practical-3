n = int(input("Enter number : "))
sum = 1
for i in range(1, n+1):
    sum = sum * i
    
print(f"factorial of {n} is {sum}")