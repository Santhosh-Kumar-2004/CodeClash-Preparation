def countdown(n):
    print(n)
    countdown(n - 1)

countdown(5)

# A) 5 4 3 2 1 0
# B) 5 4 3 2 1
# C) RecursionError   ✅
# D) Nothing

# ✅ Correct Answer: C) RecursionError

# 📘 Explanation:
# - No base case → infinite recursion
# 🔧 Fix: Add `if n == 0: return` before the recursive call
