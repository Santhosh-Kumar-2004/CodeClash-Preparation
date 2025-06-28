def is_even(n):
    if n % 2 = 0:
        return True
    return False

# A) True
# B) False
# C) SyntaxError   ✅
# D) None   

# ✅ Correct Answer: C) SyntaxError

# 📘 Explanation:
# - `=` is assignment, not comparison
# 🔧 Fix: use `==` → `if n % 2 == 0`
