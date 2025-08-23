# List of items in the cart with their prices
shopping_cart = [
    {"item": "Protein Powder", "price": 1200},
    {"item": "Yoga Mat", "price": 850},
    {"item": "Running Shoes", "price": 2999},
    {"item": "Smart Scale", "price": 1750}
]

# Initialize total cost
total_cost = 0

# Loop through each item and add its price to the total
for product in shopping_cart:
    print(f"Adding {product['item']} - ₹{product['price']}")
    total_cost += product["price"]

# Final output
print(f"\n🧾 Total cost of your cart: ₹{total_cost}")
