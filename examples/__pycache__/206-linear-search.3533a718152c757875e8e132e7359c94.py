
# apl-source:1
# مثال 206 — البحث الخطي وكل المواضع
# apl-source:2
# Linear search, all positions
# apl-source:3
# Demonstrates: المرور مع الفهرس، تجميع النتائج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/206-linear-search.apl
# apl-source:6

# apl-source:7
def ابحث_كل(قائمة, هدف):
    # apl-source:8
    مواضع = []
    # apl-source:9
    for ي in range(len(قائمة)):
        # apl-source:10
        if قائمة[ي] == هدف:
            # apl-source:11
            مواضع.append(ي)
    # apl-source:12
    return مواضع
# apl-source:13

# apl-source:14
أرقام = [5, 3, 7, 3, 9, 3, 1]
# apl-source:15
print("مواضع 3:", ابحث_كل(أرقام, 3))
# apl-source:16
print("مواضع 9:", ابحث_كل(أرقام, 9))
# apl-source:17
print("مواضع 100:", ابحث_كل(أرقام, 100))
# apl-source:18
