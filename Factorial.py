# loop
def factorial(n):
    fact=1
    for i in range(n,1,-1):
        fact=fact*(i)
        
    return fact

n=int(input("Enter number:"))
print(factorial(n))

#Recursion
def factorial(n):
    fact=1
    if (n ==0 or n==1):
        print("loop")
        return fact
         
    else:
        fact=n*factorial(n-1)
        return fact

n=int(input("Enter number:"))
print(factorial(n))
