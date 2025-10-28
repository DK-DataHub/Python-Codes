a = 250
b = 500
c = 1000
if(a>b) and (a>c):
    print("The first largest number is",a)
    if(b>c):
        print("The second largest number is",b)
    else:
        print("The second largest number is",c)
elif(b>a) and (b>c):
    print("The first largest number is",b)
    if(a>c):
        print("The second largest number is",a)
    else:
        print("The second largest number is",c)
else:
    print("The first largest number is",c)
    if(a>b):
        print("The second largest number is",a)
    else:
        print("The second largest number is",b)
if(a<b) and (a<c):
    print("The first smallest number is",a)
    if(b<c):
        print("The second smallest number is",b)
    else:
        print("The second smallest number is",c)
elif(b<a) and (b<c):
    print("The first smallest number is",b)
    if(a<c):
        print("The second smallest number is",a)
    else:
        print("The second smallest number is",c)
else:
    print("The first smallest number is",c)
    if(a<b):
        print("The second smallest number is",a)
    else:
        print("The second smallest number is",b)
