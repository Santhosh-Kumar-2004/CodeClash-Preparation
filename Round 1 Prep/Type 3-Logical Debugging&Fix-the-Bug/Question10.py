d = {(1, 2): 'a', [3, 4]: 'b'}
print(d)

# A) Error   ✅
# B) {(1, 2): 'a', (3, 4): 'b'}
# C) {'a', 'b'}
# D) {'[3, 4]': 'b'}

# ✅ Correct Answer: A) Error

# 📘 Explanation:
# - Lists are **unhashable** → can't be used as dict keys
# 🔧 Fix: convert `[3, 4]` to `(3, 4)`
