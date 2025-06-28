def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(3))

# A) 6   ✅
# B) 3
# C) 9
# D) Error

# ✅ Explanation: 3! = 3 × 2 × 1 = 6
