# Order summary - contains 5 bugs!
product = "Wireless Mouse"
price = "799"
quantity = 3
discount_percent = 5

total = int(price) * quantity
discount_amount = total * discount_percent / 100
final_total = total - discount_amount

print(f"Product: {product}")
print(f"Quantity: {quantity}")
print(f"Final total: {final_total}")

assert final_total == 2277.15
print("Order placed successfully")
