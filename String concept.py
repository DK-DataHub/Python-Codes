normalstring = "Hi Good afternoon everyone, Myself Deepak."
numstring = "Cyclone Montha LIVE: Landfall expected in Andhra, 32 trains cancelled in Odisha as storm intensifies."
print(normalstring.upper())
print(normalstring.lower())
print(numstring.capitalize())
print(numstring.split(" "))
x = numstring.find("LIVE",0)
print(x)
y = numstring.replace("Andhra","TamilNadu").replace("Odisha","Chennai")
print(y)
print(f"The length of array is: {len(normalstring)}")
print(f"The length of string is: {len(numstring)}")
print(numstring[2])
for i in range(len(normalstring)):
    print(normalstring[i])

