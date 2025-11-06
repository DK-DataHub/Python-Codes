budget1 = (110000, 325000)
budget2 = (240000, 410000)
Yamaha = [
    ("R15", (180000, 250000)),
    ("FZ", (80000, 110000)),
    ("MT15", (125000, 190000, 340000)),
    ("RX100", (80000, 95000, 150000))
]
RoyalEnfield = [
    ("Classic", (180000, 250000)),
    ("Thunderbird", (80000, 110000)),
    ("ContinentalGT", (125000, 190000, 340000, 480000)),
    ("Bullet", (80000, 95000, 150000))
]   
print(f"My total budget for Yamaha bike is : {sum(budget1)}")
for name, price in Yamaha:
    print(f"{name} variants:")
    variant = 1
    for prices in price:
        print(f"Variant {variant} costs {prices}")
        variant += 1
    print()
# alternative way
#    for i, p in enumerate(price):
#        print(f"Variant {i+1} costs {p}")
#    print()

print(f"My total budget for Royal Enfield bike is : {sum(budget2)}")
for name,price in RoyalEnfield:
    print(f"{name} variants:")
    for i, p in enumerate(price):
        print(f"Variant {i+1} costs {p}")
    print()

