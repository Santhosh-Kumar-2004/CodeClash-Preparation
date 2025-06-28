def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        # merge step...

# A) O(n²)
# B) O(n log n)   ✅
# C) O(log n)
# D) O(n)

# ✅ Correct Answer: B) O(n log n)

# 📘 Explanation:
# - Array is divided into 2 parts log n times (divide step)
# - Each level merges all n elements (combine step)
# → n × log n = **O(n log n)** time
