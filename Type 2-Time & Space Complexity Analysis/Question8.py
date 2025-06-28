def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# What is the **space complexity**?

# A) O(1)
# B) O(n)   ✅
# C) O(log n)
# D) O(n²)

# ✅ Correct Answer: B) O(n)

# 📘 Explanation:
# - Each recursive call is kept in the call stack until done
# - n calls before returning → O(n) extra memory
