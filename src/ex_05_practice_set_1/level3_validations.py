
expected_username = "anand_qa"
expected_password = "Test@123"
entered_username = "anand_qa"
entered_password = "Test@123"
is_account_locked = False
username_ok = entered_username == expected_username
print(f"Username OK: {username_ok}")
password_ok = entered_password == expected_password
print(f"Password OK: {password_ok}")

account_ok = not is_account_locked
print(f"Account OK: {account_ok}")

can_login = username_ok and password_ok and account_ok
print(f"Can login: {can_login}")

# Challenge 9: Coupon Code Check

expected_coupon = "SAVE10"

# Test 1 = exact match
entered_coupon = "SAVE10"
is_coupon_valid = entered_coupon == expected_coupon
print(f"Entered coupon: {entered_coupon} -> Valid: {is_coupon_valid}")

# Test 2 = Enter small letters
entered_coupon = "save10"
is_coupon_valid = entered_coupon == expected_coupon
print(f"Entered coupon: {entered_coupon} -> Valid: {is_coupon_valid}")

# Test 3 = Add space after coupon
entered_coupon = "SAVE10 "
is_coupon_valid = entered_coupon == expected_coupon
print(f"Entered coupon: '{entered_coupon}' -> Valid: {is_coupon_valid}")

# Challenge 10, Page Load Performance ⚡
home_load_time = 2.8
status_code = 200
search_load_time = 1.2

home_page_ok = home_load_time <= 3.0
status_code_ok = status_code == 200
search_load_ok = search_load_time <= 1.5

print(f"Home page OK: {home_page_ok}")
print(f"Status OK: {status_code_ok}")
print(f"Search Load OK: {search_load_ok}")
test_passed = home_page_ok and status_code_ok and search_load_ok
print(f"Overall test passed: {test_passed}")
assert test_passed, "performance test failed"
print("Page load performance passed")

# Challenge 11: Insurance Form Age (Boundary Testing)

# Test 1
age = 17
is_valid_age = 18 <= age <= 60
print(f"Age {age} -> Valid age: {is_valid_age}")

# Test 2
age = 18
is_valid_age = 18 <= age <= 60
print(f"Age {age} -> Valid age: {is_valid_age}")

# Test 3
age = 61
is_valid_age = 18 <= age <= 60
print(f"Age {age} -> Valid age: {is_valid_age}")

# Test 4
age = 60
is_valid_age = 18 <= age <= 60
print(f"Age {age} -> Valid age: {is_valid_age}")

# Challenge 12: Free Delivery Rule

# Test 1 small cart, not prime
# cart_total = 450
# is_prime_member = False
# free_delivery = cart_total >= 499 or is_prime_member == True
# print(f"Free delivery: {free_delivery}")

# Test 2 small cart , prime member
# cart_total = 450
# is_prime_member = True
# free_delivery = cart_total >= 499 or is_prime_member == True
# print(f"Free delivery: {free_delivery}")

# Test 2 small cart , prime member
cart_total = 499
is_prime_member = False
free_delivery = cart_total >= 499 or is_prime_member == True
print(f"Free delivery: {free_delivery}")