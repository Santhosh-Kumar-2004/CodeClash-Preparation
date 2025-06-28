def mystery(n):
    if n <= 1:
        return n
    return mystery(n - 1) + mystery(n - 2)

print(mystery(4))

# A) 4
# B) 3
# C) 5   ✅
# D) 6

# ✅ Explanation: Fibonacci → mystery(4) = 3 + 2 = 5
