#Armstrong

num = int(input("Enter number: "))
rev = 0
x = num
while num!=0:
    a = num%10
    rev = rev+(a*a*a)
    num//=10
    
print("Number is: ",rev)

if rev==x:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
    
    
# Enter number: 153
# Number is:  153
# Number is Armstrong