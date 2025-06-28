def func(x):
    x[0] = 99

lst = [1, 2, 3]
func(lst)
print(lst)

# A) [1, 2, 3]
# B) [99, 2, 3]   ✅
# C) [1, 99, 3]
# D) Error

# ✅ Explanation: Lists are mutable; function modifies the original
