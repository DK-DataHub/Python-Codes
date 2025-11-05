purchase_history = {
"Alice": ["Laptop", "Mouse", "Keyboard"],
"Bob": ["Mouse", "Monitor", "Laptop"],
"Carol": ["Keyboard", "Mouse", "Webcam"],
"David": ["Monitor", "Laptop", "Headphones"],
}
unique_products = set()
for products in purchase_history.values():
    unique_products.update(products)
print("Unique Products are:",unique_products)
product_counts = {}
for products in purchase_history.values():
    for product in products:
        product_counts.setdefault(product, 0)
        product_counts[product] += 1
print("The total number of each product bought was:",product_counts)
from collections import Counter

# Flatten all products
all_products = [product for products in purchase_history.values() for product in products]

# Count and get top 3
product_counts = Counter(all_products)
top_3 = product_counts.most_common(3)
print("Top 3 popular products:", top_3)
