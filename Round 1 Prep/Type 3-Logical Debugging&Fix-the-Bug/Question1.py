def add(a, b):
    c = a + b

print(add(2, 3))

# A) 5
# B) None   ✅
# C) Error
# D) 23

# ✅ Correct Answer: B) None

# 📘 Explanation:
# - The function doesn't `return` anything → Python defaults to returning `None`
# 🔧 Fix: Add `return c`
