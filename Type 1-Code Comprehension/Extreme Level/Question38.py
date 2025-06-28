a = [[0] * 3] * 3
a[0][0] = 1
print(a)

# A) [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
# B) [[1, 0, 0], [1, 0, 0], [1, 0, 0]]   ✅
# C) [[1], [0], [0]]
# D) Error

# ✅ Explanation: All 3 rows refer to the same inner list object
