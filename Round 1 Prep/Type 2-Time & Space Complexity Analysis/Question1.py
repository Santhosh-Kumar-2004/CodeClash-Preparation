def example1(n):
    for i in range(n):
        print(i)

# A) O(1)
# B) O(n)   ✅
# C) O(n²)
# D) O(log n)

# ✅ Correct Answer: B) O(n)

# 📘 Explanation:
# - The loop runs exactly n times (from 0 to n-1)
# - Each loop takes a fixed time (just printing)
# - So total time is directly proportional to n
# => This is called **linear time complexity**
