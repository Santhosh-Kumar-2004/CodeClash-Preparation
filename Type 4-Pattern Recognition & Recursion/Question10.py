def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(12, 8))

# A) 4   ✅
# B) 2
# C) 6
# D) 8

# ✅ Answer: A) 4

# 📘 Euclidean algorithm: gcd(12,8) → gcd(8,4) → gcd(4,0) = 4
