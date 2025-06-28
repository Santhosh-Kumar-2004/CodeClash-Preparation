def fun(n):
    if n == 0:
        return
    fun(n - 1)
    print(n, end=" ")

fun(3)

# A) 3 2 1
# B) 1 2 3   ✅
# C) 0 1 2 3
# D) Error

# ✅ Explanation: prints after recursion, so ascending output
