def bubblesort(list):
    for i in range(len(a)-1):
        flag='unswapped'
        for j in range((len(a)-1-i)):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                flag='swapped'
        if flag=='unswapped':
            break
        
        
a=[int(x) for x in input().split()]
print("Before Sorting:")
print(a)
bubblesort(a)            
print("After Sorting:")
print(a)
            