a = [1, 2, 3]
b = a
b.append(4)
print(a)

# A) [1, 2, 3]
# B) [1, 2, 3, 4]   ✅
# C) Error
# D) [4]

# ✅ Explanation: b is reference to a. So append affects a too.
