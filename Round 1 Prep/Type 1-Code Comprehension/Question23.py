def greet():
    return "Hi"

hello = greet
print(hello())

# A) greet
# B) Hi   ✅
# C) Error
# D) None

# ✅ Explanation: Functions are first-class → hello = greet
