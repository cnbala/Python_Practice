def prime(n):
    if n<=2:
        num=2 
    else:
        num=int(n**(0.5))
    flag='false'
    for i in range(num,1,-1):
        if (n%i==0):
            flag='true'
            break
    if flag == 'true':
        print (n,' is not a prime number')
    else:
        print (n,' is a prime number')
    return flag    
    
n=int(input("Enter the number:"))   

prime(n)   
    
