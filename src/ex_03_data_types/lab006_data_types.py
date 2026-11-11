# Meet type(), The Detective


print(type(2.5))
print(type("Chrome"))
print(type(True))
print(type(None))
print(type("20"))

# Each type behaves differently

print(10 + 5)
print("10" + "5")
print(2.5 + 2.5)
print("Test" * 3)

# Converting between types (type casting)


# True, False and None

is_passed = True
is_blocked = False
bug_id = None
print(type(is_passed))
print(type(bug_id))

print(499 == "499")

# Challenges

# 1
test_count = "21"
execution_time = 3.0
browser = "safari"
is_passed = False
bug_id = None
print (f"test_count : {test_count}, type: {type(test_count)}")
print (f"execution_time : {execution_time}, type: {type(execution_time)}")
print (f"browser : {browser}, type: {type(browser)}")
print (f"is_passed : {is_passed}, type: {type(is_passed)}")
print (f"bug_id : {bug_id}, type: {type(bug_id)}")

# 2

price = "499"
quantity = 2
print(f"Total price: {int(price) * quantity}")

# 3

print( "Passed tests: " + str(34))
