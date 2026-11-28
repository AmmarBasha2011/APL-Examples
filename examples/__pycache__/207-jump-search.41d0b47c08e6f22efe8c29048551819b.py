
# apl-source:1
# مثال 207 — البحث بالقفز
# apl-source:2
# Jump search
# apl-source:3
# Demonstrates: قفزات بحجم الجذر التربيعي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/207-jump-search.apl
# apl-source:6

# apl-source:7
def بحث_قفز(قائمة, هدف):
    # apl-source:8
    ن = len(قائمة)
    # apl-source:9
    خطوة = int(ن ** 0.5)
    # apl-source:10
    if خطوة < 1:
        # apl-source:11
        خطوة = 1
    # apl-source:12
    سابق = 0
    # apl-source:13
    while سابق < ن:
        # apl-source:14
        نهاية = سابق + خطوة
        # apl-source:15
        if نهاية > ن:
            # apl-source:16
            نهاية = ن
        # apl-source:17
        if قائمة[نهاية - 1] >= هدف:
            # apl-source:18
            break
        # apl-source:19
        سابق = نهاية
    # apl-source:20
    for ي in range(سابق, ن):
        # apl-source:21
        if قائمة[ي] == هدف:
            # apl-source:22
            return ي
        # apl-source:23
        if قائمة[ي] > هدف:
            # apl-source:24
            break
    # apl-source:25
    return -1
# apl-source:26

# apl-source:27
أرقام = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# apl-source:28
print("موضع 55:", بحث_قفز(أرقام, 55))
# apl-source:29
print("موضع 100:", بحث_قفز(أرقام, 100))
# apl-source:30
