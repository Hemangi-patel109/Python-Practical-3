#print all even numbers between 1 to n except the numbers divisible by 6

n = int(input("Enter number: "))
for i in range(n+1):
    if i%2==0:
        if i%6==0:
            continue
        print("Even numbers are: ",i)
    

# Enter number: 20
# Even numbers are:  2
# Even numbers are:  4
# Even numbers are:  8
# Even numbers are:  10
# Even numbers are:  14
# Even numbers are:  16
# Even numbers are:  20