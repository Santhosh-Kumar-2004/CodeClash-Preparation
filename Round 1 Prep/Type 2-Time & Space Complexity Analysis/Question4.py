def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# A) O(n)
# B) O(n²)
# C) O(log n)
# D) O(2ⁿ)   ✅

# ✅ Correct Answer: D) O(2ⁿ)

# 📘 Explanation:
# - Every call makes 2 more calls → exponential tree
# - The number of calls doubles each time
# => This gives **exponential time complexity**
