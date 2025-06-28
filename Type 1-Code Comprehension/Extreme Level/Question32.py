def gen():
    yield 1
    yield 2

g = gen()
print(next(g))
print(next(g))

# A) 1 2   ✅
# B) 2 1
# C) 0 1
# D) Error

# ✅ Explanation: Generators yield one item at a time on each call to `next()`
