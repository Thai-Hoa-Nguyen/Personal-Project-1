inventory = {"Shoes": 1000, "Shirt": 500}
customer_cart = ["Shoes", "Shirt"]

total_bill = 0

for i in customer_cart:
    total_bill += inventory[i]

print(f"Your cart: {customer_cart}")
print(f"Total Bill: {total_bill}")