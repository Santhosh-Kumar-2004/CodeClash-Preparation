def find_even(nums):
    result = []
    for n in nums:
        if n % 2:
            result.append(n)
    return result

print(find_even([2, 4, 6]))

# A) [2, 4, 6]
# B) []   ✅
# C) [4]
# D) [2, 6]

# ✅ Correct Answer: B) []

# 📘 Explanation:
# - `if n % 2:` means **true for odd numbers**
# 🔧 Fix: use `if n % 2 == 0:` to catch even numbers
