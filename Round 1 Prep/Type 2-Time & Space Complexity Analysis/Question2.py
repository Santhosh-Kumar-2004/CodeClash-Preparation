def example2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# A) O(n)
# B) O(n log n)
# C) O(n²)   ✅
# D) O(1)

# ✅ Correct Answer: C) O(n²)

# 📘 Explanation:
# - Outer loop runs n times
# - For each `i`, the inner loop runs n times
# → Total: n × n = n² steps
# => This is called **quadratic time**
