def selectionsort(list):
    num=len(a)
    for i in range(0,num-1,1):
        #finding min element in unsorted list
        minindex=i
        for j in range (i+1,num):
            if (a[minindex]> a[j]):
                minindex=j
        if minindex!=i:
            a[i],a[minindex]=a[minindex],a[i]
        
            
        
        
a=[int(x) for x in input().split()]
print("Before Sorting:")
print(a)
selectionsort(a)            
print("After Sorting:")
print(a)
            