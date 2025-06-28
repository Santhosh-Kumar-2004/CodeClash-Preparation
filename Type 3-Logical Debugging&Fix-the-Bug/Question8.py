def factorial(n):
    if n == 0:
        print(1)
    else:
        return n * factorial(n - 1)

print(factorial(3))

# A) 6
# B) 3
# C) None   ✅
# D) Error

# ✅ Correct Answer: C) None

# 📘 Explanation:
# - Base case doesn’t return anything → breaks the chain
# 🔧 Fix: change `print(1)` to `return 1`
