#Loop
def sum(n):
    sum1=0
    for i in range(1,n+1):
        sum1+=i
    return sum1

n=int(input("Enter the number"))   

print(sum(n))


#Recursion
def sum(n):
    if n <= 0:
        return n
    else:
        n+=sum(n-1)
        return n

n=int(input("Enter the number"))   

print(sum(n))

