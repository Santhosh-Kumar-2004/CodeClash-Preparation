def sum_list(lst):
    total = 0
    for i in range(len(lst) + 1):
        total += lst[i]
    return total

print(sum_list([1, 2, 3]))

# A) 6
# B) 7
# C) IndexError   ✅
# D) 0

# ✅ Correct Answer: C) IndexError

# 📘 Explanation:
# - range(len(lst) + 1) → tries to access index 3, which doesn't exist
# 🔧 Fix: Change to `range(len(lst))` or simply `for i in lst:`
