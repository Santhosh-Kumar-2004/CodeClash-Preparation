s = "abcdefgh"
print(s[::-2])

# A) h f d b   (with spaces)
# B) "hfdb"   ✅
# C) "hgfedcba"
# D) "abcdefgh"

# ✅ Explanation: [::-2] = reverse string skipping every second → h f d b → "hfdb"
