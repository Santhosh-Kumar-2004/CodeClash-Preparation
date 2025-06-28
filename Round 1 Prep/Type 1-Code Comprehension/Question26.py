def f(x):
    return x * 2

print(f(f(2)))

# A) 4
# B) 8   ✅
# C) 2
# D) Error

# ✅ Explanation: f(2) = 4 → f(4) = 8
