# Challenge 4: Sprint test summary 📊
total_tests = 120
passed = 95
failed = 18
skipped = 7
print(f"Skipped : {skipped}")
print(f"Pass%: {passed / total_tests * 100}")
print(f"Fail%: {failed * 100 / total_tests}")
assert passed + failed + skipped == total_tests
print("Report check passed ✅")

# Challenge 5: Cart Total with GST 🛒
item1_price = "1250"
item1_qty = 2
item2_price = "500"
item2_qty = 1
coupon_discount = 200
gst_percent = 18
website_total = "3304"
subtotal = (int(item1_price) * item1_qty + int(item2_price) * item2_qty)
print(f"Subtotal: {subtotal}")
after_coupon = (subtotal - coupon_discount)
print(f"After coupon: {after_coupon}")
gst_amount = (after_coupon * gst_percent) / 100
print(f"GST Amount: {gst_amount:.2f}")
final_total = (after_coupon + gst_amount)
print(f"Final Total: {final_total:.2f}")
assert float(website_total) == final_total, "Website total is wrong!"
print("cart total verified")

# Challenge 6: Test Execution Time

total_test_cases = 47
seconds_per_test = 8
total_seconds = total_test_cases * seconds_per_test
print(f"Total time: {total_seconds} seconds")
minutes = total_seconds // 60
remaining_seconds = total_seconds % 60
print(f"That is {minutes} minutes and {remaining_seconds} seconds")

assert minutes * 60 + remaining_seconds == total_seconds, "execution time is wrong!"
print("Test Execution time verified")

# Challenge 7, Defect Density 🐞
bugs_found = 36
lines_of_code = 12500
thousand_lines = lines_of_code / 1000
print(f"Defect density: {bugs_found / thousand_lines} bugs per KLOC")
