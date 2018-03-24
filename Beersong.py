# beer song using For loop

for qty in range(99,0,-1):
    if(qty>1):
        print(qty,"Bottles of beer on the wall,",qty,"bottles of beer")
        suffix= str(qty-1) + " bottle"+('s' if (qty!=2) else '')+" of beer on the wall"
    else :
        print("1 bottle of beer on the wall,1 bottle of beer")
        suffix="No more beer on the wall"
        
    print ("Take one down and pass it around,",suffix)
    print ("----------------------")
    
