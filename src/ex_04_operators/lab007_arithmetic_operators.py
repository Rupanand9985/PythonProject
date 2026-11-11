# Warm-up

print("5" * 3)  # my guess is 555
print(5 * 3)  # my guess is 15

# The 7 maths operators

print(10 + 3)  # my guess is 13
print(10 - 3)  # my guess is 7
print(10 * 3)  # my guess is 30
print(10 / 3)  # my guess is 3.3
print(10 // 3)  # my guess is 10/3
print(10 % 3)  # my guess is 0.3
print(10 ** 3)

# The two surprising ones, // and % 🍬
print(17 // 5)  # my guess is 3
print(17 % 5)  # my guess is 2
print(20 % 2)  # my guess is 0
print(21 % 2)  # my guess is 1

# Order of operations (BODMAS) 🧮

print(2 + 3 * 4)
print((2 + 3) * 4)

# Break it on purpose

print(10 / 0)

# Assignment shortcuts

score = 10
score = score + 5

print(score)  # my guess is score5

score = 10
score += 5  # same as: score = score + 5
print(score)

tests_run = 0
tests_run += 1
tests_run += 1
tests_run += 1
print(tests_run)

# Challenges

# 1
total = 45
passed = 38

print(f"Failed : {total - passed}")
print(f"Pass percentage : {passed / total * 100}%")

# 2
test_cases = 50
testers = 4

print(f" Each tester gets : {test_cases // testers}")
print(f" Left over : {test_cases % testers}")

# 3
bugs_found = 0
bugs_found += 2
bugs_found += 5
bugs_found += 1

print(f" Total bugs : {bugs_found}")

# 4

product_cost = 499
quantity = 3
discount = 10
total_price = product_cost * quantity
discount_applied = total_price * discount / 100
final_price = total_price - discount_applied

print(f"Final price: {final_price}")
