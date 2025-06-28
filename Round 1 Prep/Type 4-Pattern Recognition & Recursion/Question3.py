def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print(fact(4))

# A) 16
# B) 24   ✅
# C) 20
# D) 120

# ✅ Answer: B) 24

# 📘 4! = 4 × 3 × 2 × 1 = 24
