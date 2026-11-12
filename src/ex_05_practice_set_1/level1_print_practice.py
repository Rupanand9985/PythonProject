# Challenge 1: Smoke test report banner 📋

print("=" * 30)
print("\t SMOKE TEST REPORT")
print("=" * 30)
print("Project:\t Amazon Clone")
print("Build:\t v2.4.1")
print("Tester:\t Anand")

# Challenge 2: Screenshot file path 📸

folder = "C:\\Users\\Anand\\screenshots"
file_name = "login_fail.png"
print(folder)
print(f"Screenshot saved at: {folder}\\{file_name}")

# Challenge 3: Test case ID generator 🏷️
module = "LOGIN"
test_number = 7
test_id = "TC_" + module + "_" + str(test_number)
print(test_id)

print(f"TC_{module}_{test_number}")
test_number += 1
print(f"TC_{module}_{test_number}")
test_number += 1
print(f"TC_{module}_{test_number}")
