a = 250
b = 500
c = 1000
if(a>b):
    if(a>c):
        print("The largest number is:a")
        if (b>c):
            print("The second largest number is:b")
        else:
            print("The second largest number is:c")
    else:
        print("The largest number is:c")        
        print("The second largest number is:a")
else:
    if (b>c):
        print("The largest number is:b")
        if (b>a):
            print("The second largest number is:b")
        else:
            print("The second largest number is:a")
    else:
        print("The largest number is:",c)        
        print("The second largest number is:",b)
    
    
