def palindrome(input_str):
    pal_str=input_str[::-1]
    if input_str == pal_str :
        print (input_str," is a palindrome")
        return True
    else:
        print (input_str," is not a palindrome")
        return False  
    
input_str=input("Enter the String:")  

palindrome(input_str)    
         