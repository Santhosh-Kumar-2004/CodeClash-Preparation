def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Best-case time complexity?

# A) O(n)   ✅
# B) O(n log n)
# C) O(n²)
# D) O(1)

# ✅ Correct Answer: A) O(n)

# 📘 Explanation:
# - Best case = array already sorted (e.g., [1, 2, 3, 4])
# - `swapped` remains False → loop breaks early
# → Only one full pass needed → O(n)
