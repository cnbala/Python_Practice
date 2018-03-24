#Loop
n=int(input("Enter the number")) 
a,b=0,1
for i in range(0,n):
    print(b)
    a,b=b,a+b
    
    
#Recursion
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print (fibonacci(i))
        
    
