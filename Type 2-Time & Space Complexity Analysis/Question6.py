def example(n):
    i = 1
    while i < n:
        print(i)
        i *= 2

# A) O(n)
# B) O(n²)
# C) O(log n)   ✅
# D) O(1)

# ✅ Correct Answer: C) O(log n)

# 📘 Explanation:
# - i goes: 1 → 2 → 4 → 8 → ... → up to < n
# - So loop runs ~log₂(n) times
# => This is **logarithmic time**
