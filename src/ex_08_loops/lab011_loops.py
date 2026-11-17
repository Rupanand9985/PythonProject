# Lesson 10: Loops 🔁
# from unittest import result

# for number in range(5):
#     print(number)

# for number in range(1,4):
#     print(number)
#
# for number in range(7,10):
#     print(f"TC_login_{number}")

# for number in range(1, 101):
#     print(f"TC_LOGIN_{number}")

# total_time = 0

# for test in range(1, 6):
#     print(f"Running test {test}... took 8 seconds")
#     total_time += test
#
# print(f"All tests done! Total time: {total_time} seconds")

# for age in [17, 18, 60, 61]:
#     if 18 <= age <= 60:
#         print(f"Age {age} -> Eligible ✅")
#     else:
#         print(f"Age {age} -> Not eligible ❌")

# attempts = 5
#
# while attempts <= 3:
#     print(f"Login attempt {attempts}")
#     attempts += 1
#
# print("No more attempts")

# attempts = 1
#
# while attempts <= 3:
#     password = input(f"Attempt {attempts} - Password: ")
#     if password == "Test@123":
#         print("Login successful ✅")
#         break
#     print("Wrong password ❌")
#     attempts += 1

# 🟢 Challenge 1: Test ID Generator
#
# Part A
#
# for test_number in range(1, 11):
#     print(f"TC_LOGIN_{test_number}")
#
# Part B
#
# for test_number in range(101, 111):
#     print(f"TC_CART_{test_number}")

# ➡️ Challenge 2: Data-driven Coupon Test 🎟️

# expected_coupon = "SAVE10"
#
# for coupon in ["SAVE10", "save10", "SAVE10 ", "SAVE20", "FREE50"]:
#
#     if coupon == expected_coupon:
#         print(f"'{coupon}' -Valid Coupon")
#
#     else:
#         print(f"'{coupon}' -Invalid coupon")

# ➡️ Next: Challenge 3, Test Results Counter 🐷
# passed = 0
# failed = 0
# for test_result in ["pass", "fail", "pass", "pass", "fail", "pass"]:
#     if test_result == "pass":
#         passed += 1
#     else:
#         failed += 1
#
# print(f"Passed: {passed}")
# print(f"Failed: {failed}")
#
# total = passed + failed
#
# print(f"Pass % = {passed * 100 / total:.2f}%")

# ➡️ Next: Challenge 4, Login with Lockout 🔒

# attempts = 1
#
# while attempts <= 3:
#     password = input(f"Attempt {attempts} - Password: ")
#     if password == "Test@123":
#         print("Login successful ✅")
#         break
#     print("Wrong password ❌")
#     attempts += 1
#
# if attempts > 3:
#     print("Account Locked")

# ✅ Leap Year Checker:

# leap_year = int(input("Enter the year: "))
#
# if leap_year % 400 == 0:
#     print("Leap year")
# elif leap_year % 100 == 0:
#     print("Not a leap year")
# elif leap_year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")
