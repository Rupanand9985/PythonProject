# comparison operators

print(10 == 10)  # my guess: True
print(10 == 20)  # my guess: False
print(10 != 20)  # my guess: True
print(18 >= 18)  # my guess: True
print(17 > 18)  # my guess: False

print(type(10 == 10))

# print (5 = 5)

# Comparing text 🔤

print("Chrome" == "Chrome")  # my guess : True
print("Chrome" == "chrome")  # my guess : True
print("Login" != "Logout")  # my guess : True
print(499 == "499")  # my guess : False

# Storing the answer in a box

expected_title = "Amazon.in"
actual_title = "Amazon.com"

is_title_correct = actual_title == expected_title
print(f"Title correct: {is_title_correct}")

# Logical operators, combining questions 🔗
print(True and True)  # guess: True
print(True and False)  # guess: False
print(True or False)  # guess: True
print(False or False)  # guess: False
print(not True)  # guess: False
print(not False)  # guess: True

# Real example, a login check 🔐
username = "admin"
password = "1234"

is_login_ok = username == "admin1" or password == "1234"
print(f"Login successful: {is_login_ok}")

# Sneak peek, assert 🧪
assert 5 == 5
print("First check passed")

assert "Chrome" == "Chrome"
print("Second check passed")

# Challenges

# 1 Title check:
expected_title = "Google"
actual_title = "google"
is_match = actual_title == expected_title
print(f"Title_matches = {is_match}")

# 2 Age check:
age = 17
can_signup = age >= 18
print(f"Age_matches = {can_signup}")

# 3 API test
status_code = 200
response_time = 3.5
print(status_code == 200)
print(response_time <= 2.0)    # 🤔 you fill in the operator
is_test_passed = status_code == 200 and response_time <= 2.0
print (f" Test_passed: {is_test_passed}")

# 4 Payment check:
has_card = False
has_upi = True
can_pay = has_card or has_upi
print(f"Payment_possible: {can_pay}")

# 5 Assert
product_cost = 499
quantity = 3
discount = 10
total_price = product_cost * quantity
discount_applied = total_price * discount / 100
final_price = total_price - discount_applied

assert final_price == 1347.3
print("Cart total check passed ✅")