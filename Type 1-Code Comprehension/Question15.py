def append_item(val, lst=[]):
    lst.append(val)
    return lst

print(append_item(1))
print(append_item(2))

# A) [1] [2]
# B) [1] [1, 2]   ✅
# C) [1, 2] [1, 2]
# D) Error

# ✅ Explanation: Default list persists across calls
