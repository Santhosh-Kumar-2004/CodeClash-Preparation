a = [1, 2, 3]
b = a
a = [4, 5, 6]
print(b)

# A) [1, 2, 3]   ✅
# B) [4, 5, 6]
# C) Error
# D) None

# ✅ Explanation: `b` still points to original list; `a` reassigned
