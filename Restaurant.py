menu = {
    "Pizza": 12,
    "Burger": 8,
    "Pasta": 10,
    "Salad": 6,
    "Soda": 3,
}
orders = {
    "John": ["Pizza", "Soda"],
    "Maria": ["Salad", "Pasta", "Soda"],
    "Liam": ["Burger", "Pizza"],
    "Sophia": ["Pasta", "Salad"],
    "Ethan": ["Pizza", "Burger", "Soda"],
}
bills = {}
for customer, items in orders.items():
    total = sum(menu[item] for item in items)
    bills[customer] = total
print("Customer Bills:")
for customer, total in bills.items():
    print(f"{customer}: ${total}")
unique_dishes = set()
for items in orders.values():
    unique_dishes.update(items)
print("Unique dishes are:",unique_dishes)