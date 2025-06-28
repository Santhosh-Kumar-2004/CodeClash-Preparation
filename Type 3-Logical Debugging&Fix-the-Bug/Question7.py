nums = ['1', '2', '3']
total = sum(map(int, nums))
print(total)

# A) 123
# B) 6   ✅
# C) Error
# D) ['1', '2', '3']

# ✅ Correct Answer: B) 6

# 📘 Explanation:
# - `map(int, nums)` converts each string to int → [1, 2, 3]
# - sum([1, 2, 3]) = 6
# 🔧 No bug here — just testing understanding
