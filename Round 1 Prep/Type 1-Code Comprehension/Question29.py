a = "hello"
b = "he" + "llo"
print(a is b)

# A) True   ✅
# B) False
# C) Error
# D) Depends

# ✅ Explanation: String interning makes `a is b` True for literals
