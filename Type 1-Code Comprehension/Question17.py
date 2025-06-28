d = {'a': 1, 'b': 2}
print(d.get('c', 3))
print(d)

# A) 1
# B) 2
# C) 3   ✅
# D) Error

# ✅ Explanation: .get('c', 3) returns default if key not found
