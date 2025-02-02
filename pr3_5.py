num = int(input("Enter number: "))
rev = 0

while num!=0:
    a = num%10
    rev = rev*10+a
    num//=10
    
print("Reverse number is: ",rev)


# Enter number: 2715
# Reverse number is:  5172