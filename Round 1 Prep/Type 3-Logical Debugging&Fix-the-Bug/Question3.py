a = [1, 2, 3]
b = a
b.append(4)
print(a)

# A) [1, 2, 3]
# B) [1, 2, 3, 4]   ✅
# C) [4]
# D) Error

# ✅ Correct Answer: B) [1, 2, 3, 4]

# 📘 Explanation:
# - `b = a` means both refer to the **same list in memory**
# 🔧 Fix: use `b = a.copy()` to make a real copy
