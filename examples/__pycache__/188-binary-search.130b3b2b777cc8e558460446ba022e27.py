
# apl-source:1
# مثال 188 — البحث الثنائي بالعودية
# apl-source:2
# Recursive binary search
# apl-source:3
# Demonstrates: العودية، التقسيم النصفي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/188-binary-search.apl
# apl-source:6

# apl-source:7
def بحث_ثنائي(قائمة, هدف, منخفض, مرتفع):
    # apl-source:8
    if منخفض > مرتفع:
        # apl-source:9
        return -1
    # apl-source:10
    منتصف = (منخفض + مرتفع) // 2
    # apl-source:11
    if قائمة[منتصف] == هدف:
        # apl-source:12
        return منتصف
    # apl-source:13
    elif قائمة[منتصف] < هدف:
        # apl-source:14
        return بحث_ثنائي(قائمة, هدف, منتصف + 1, مرتفع)
    # apl-source:15
    else:
        # apl-source:16
        return بحث_ثنائي(قائمة, هدف, منخفض, منتصف - 1)
# apl-source:17

# apl-source:18
أرقام = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# apl-source:19
print("موضع 23:", بحث_ثنائي(أرقام, 23, 0, len(أرقام) - 1))
# apl-source:20
print("موضع 100:", بحث_ثنائي(أرقام, 100, 0, len(أرقام) - 1))
# apl-source:21
