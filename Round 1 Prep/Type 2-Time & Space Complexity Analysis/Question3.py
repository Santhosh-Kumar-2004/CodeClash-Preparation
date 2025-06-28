def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

# A) O(n)
# B) O(log n)   ✅
# C) O(n log n)
# D) O(1)

# ✅ Correct Answer: B) O(log n)

# 📘 Explanation:
# - Each step cuts the search space in half (divide and conquer)
# - First n → then n/2 → n/4 → ... → 1
# - This takes log₂(n) steps
# => Binary search has **logarithmic time**
