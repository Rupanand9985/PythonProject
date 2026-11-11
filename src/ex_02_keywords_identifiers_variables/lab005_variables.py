#reading = right away
name = "Anand"
print("name")

#Changing what's Inside
score = 80
print(score)
score = 100
print(score)

# math with boxes
passed = 5
failed = 2
total = passed + failed
print(f" total: {total}")

# Shortcuts

#many boxes in one line
browser, os, version = "chrome", "windows", "11 Pro"
print (browser, os, version)

#same value in many boxes
x=y=z= "pending"
print(x,y,z)

#Swapping two boxes (a Python special trick)

first = "login"
second = "logout"
first, second = second, first
print(first, second)

# CHALLENGE

# 1
test_id = "TC_2126"
test_name = "Verify with valid user"
browser = "chrome"
is_passed = True

print(f"Test {test_id} - {test_name} - ran on {browser} - passed = {is_passed}")

# 2
total_tests = 40
failed_tests = 6
passed_tests = total_tests - failed_tests
print (f"passed_tests : {passed_tests}")

print (f"Passed: {passed_tests} out of {total_tests}")

# 3
env1 = "QA"
env2 = "PRD"
print (f"Before swap: env1 = {env1}, env2 = {env2}")
env1,env2 = env2, env1
print (f"After swap: env1 = {env1}, env2 = {env2}")

# 4

a = 21
b = a
a = 22
print(b)




