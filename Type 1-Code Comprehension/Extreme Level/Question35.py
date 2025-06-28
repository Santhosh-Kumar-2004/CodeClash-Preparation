d = {}
d[[]] = "test"
print(d)

# A) {'[]': 'test'}
# B) {'test'}
# C) Error   ✅
# D) {}

# ✅ Explanation: Lists are unhashable → cannot be used as dictionary keys
