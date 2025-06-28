def fun(n):
    if n == 1:
        return 1
    # print(n - fun(n - 1))
    # print(n * fun(n - 1))
    # print(n / fun(n - 1))
    # print(n + fun(n - 1))
    return n + fun(n - 1)

print(fun(3))

# A) 3
# B) 5
# C) 6   ✅
# D) 7

# ✅ Explanation: 3 + 2 + 1 = 6 (classic sum recursion)
