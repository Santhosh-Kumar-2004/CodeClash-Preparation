def is_palindrome(s):
    return s == s.reverse()

print(is_palindrome("madam"))

# A) True
# B) False
# C) Error
# D) None   ✅

# ✅ Correct Answer: D) None

# 📘 Explanation:
# - `s.reverse()` modifies list in-place and returns `None`
# 🔧 Fix: use `s[::-1]` or `reversed(s)` with `join`
