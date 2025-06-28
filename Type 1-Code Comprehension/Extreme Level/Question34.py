def foo(val, lst=[]):
    lst.append(val)
    return lst

print(foo(1))
print(foo(2))
print(foo(3))

# A) [1] [2] [3]
# B) [1] [1, 2] [1, 2, 3]   ✅
# C) [1] [2] [1, 2, 3]
# D) Error

# ✅ Explanation: Default list persists → keeps growing across calls
