# # age = 17
# #
# # if age >= 18:
# #     print("you can apply")
# # else:
# #     print("you can not apply")
# #
# # print("Program successfully finished")
#
# # light = "red"
# #
# # if light == "green":
# #     print("GO")
# # elif light == "red":
# #     print("STOP")
# # elif light == "yellow":
# #     print("BE READY")
# # else:
# #     print("INVALID LIGHT COLOUR")
#
#
# # username = input("Username: ")
# # password = input("Password: ")
# #
# # if username == "anand_qa" and password == "Test@123":
# #     print("Login successful")
# # else:
# #     print("Invalid username or password")
#
# # Challenge: 1 Age validator 2.0
#
# age = int(input("What is your age? "))
#
# if 18 <= age <= 60:
#     print("Eligible for insurance")
# else:
#     print("Not eligible: Age must be older than 18")

# Challenge 2: Free Delivery
#
# price = float(input("Cart Price? "))
# prime_member = input("Prime Member (yes/no): ")
# if price >= 499 or prime_member == "yes":
#     print("Free delivery")
#
# else:
#     print("Delivery cost: 40/-")

# Challenge 3: Test Result Grader 🚀 💪

# pass_percentage = float(input("Enter a percentage: "))

# if pass_percentage < 0 or pass_percentage > 100:
#     print("Invalid percentage")
#
# elif pass_percentage >= 90:
#     print("Release ready")
#
# elif 75 >= pass_percentage >= 89.99:
#     print("Needs Review")
#
# elif pass_percentage <= 75:
#     print("Release blocked")
#
# else:
#     print("Release blocked ⛔")

# Challenge 4: HTTP Status Checker
# status_code = int(input("Enter Status code: "))
#
# if status_code == 200:
#     print("OK")
# elif status_code == 404:
#     print("Page Not Found")
# elif status_code == 500:
#     print("Server Error")
#
# else:
#     print("Unknown Status Code")

# Challenge 5: Bug Hunt, the Wrong Discount

cart_total = 2000

if cart_total >= 5000:
    print("Discount: 10%")
elif cart_total >= 1000:
    print("Discount: 5%")
else:
    print("No discount")

# BUG REPORT
# Title: <one short line describing the bug>
# Steps: <how to reproduce it>
# Expected: <what should happen>
# Actual: <what happened>
# Cause: <why it happened>
# Fix: <what you changed>