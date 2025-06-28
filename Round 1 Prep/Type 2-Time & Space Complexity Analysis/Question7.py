def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Worst-case time complexity?

# A) O(n)
# B) O(n log n)
# C) O(n²)   ✅
# D) O(1)

# ✅ Correct Answer: C) O(n²)

# 📘 Explanation:
# - Worst case = array is in descending order (e.g., [5,4,3,2,1])
# - Every new element has to shift all previous elements
# - For n elements: 1 + 2 + 3 + ... + (n-1) = O(n²)
