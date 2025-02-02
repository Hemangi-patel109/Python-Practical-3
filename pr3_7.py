#Palindrome

num = int(input("Enter number: "))
rev = 0
x = num
while num!=0:
    a = num%10
    rev = rev*10+a
    num//=10
    
print("Reverse number is: ",rev)

if rev==x:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
    

# Enter number: 121
# Reverse number is:  121
# Number is Palindrome