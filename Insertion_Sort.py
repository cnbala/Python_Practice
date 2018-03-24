def insertionSort(a):
 
    for i in range(1, len(a)):
        key = a[i]
        print("Key:",key)
        j = i-1
        while j >=0 and key < a[j] :
                a[j+1] = a[j]
                print(a[j+1])
                j -= 1
        a[j+1] = key
        print("arr[j+1] = key:",a[j+1])
        
a = [12, 11, 13, 5, 6]
insertionSort(a)
print (a)