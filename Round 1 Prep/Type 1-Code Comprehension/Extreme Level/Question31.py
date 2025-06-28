x = 10

def change():
    x = x + 1
    print(x)

change()

# A) 11
# B) 10
# C) Error   ✅
# D) 1

# ✅ Explanation: Local variable x referenced before assignment — UnboundLocalError
