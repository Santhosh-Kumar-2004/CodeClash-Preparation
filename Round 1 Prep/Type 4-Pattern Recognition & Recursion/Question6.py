def fun(n):
    if n == 0:
        return
    print(n)
    fun(n - 1)

fun(3)

# What is output?

# A) 3 2 1   ✅
# B) 1 2 3
# C) 0 1 2
# D) 3 2 1 0

# ✅ Answer: A) 3 2 1

# 📘 Recursive countdown → prints before the call
