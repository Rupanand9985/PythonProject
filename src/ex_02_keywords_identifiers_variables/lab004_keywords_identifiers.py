# ============================================
# Lab 002 - Keywords and Identifiers
# ============================================

# --- KEYWORDS ---
# Keywords are Python's own "special words".
# We cannot use them as names for our boxes (variables).

import keyword

print("Total keywords in Python:", len(keyword.kwlist))
print(keyword.kwlist)

# Check if a word is a keyword
print("Is 'if' a keyword?", keyword.iskeyword("if"))       # True
print("Is 'name' a keyword?", keyword.iskeyword("name"))   # False


# --- IDENTIFIERS ---
# Identifiers are names WE create.

# ✅ Valid identifiers
user_name = "Rupanand"
testCase1 = "Login Test"
_private = "hidden value"
TOTAL_TESTS = 50

print(user_name)
print(testCase1)
print(_private)
print(TOTAL_TESTS)

# ❌ Invalid identifiers (uncomment one at a time to see the error!)
# 1test = "fail"        # cannot start with a number
# test-case = "fail"    # hyphen not allowed
# user name = "fail"    # spaces not allowed
# class = "fail"        # 'class' is a keyword

# --- CASE SENSITIVE ---
# Python treats capital and small letters as DIFFERENT names
status = "pass"
Status = "fail"
print(status)   # pass
print(Status)   # fail