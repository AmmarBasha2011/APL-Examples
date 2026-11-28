
# apl-source:1
# مثال 318 — المضاعف المشترك الأصغر لقائمة
# apl-source:2
# LCM of a list
# apl-source:3
# Demonstrates: تطبيق متكرر للم.م.أ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/318-lcm-list.apl
# apl-source:6

# apl-source:7
def قاسم_مشترك(أ, ب):
    # apl-source:8
    while ب != 0:
        # apl-source:9
        مؤقت = ب
        # apl-source:10
        ب = أ % ب
        # apl-source:11
        أ = مؤقت
    # apl-source:12
    return أ
# apl-source:13

# apl-source:14
def مضاعف_مشترك(أ, ب):
    # apl-source:15
    return أ * ب // قاسم_مشترك(أ, ب)
# apl-source:16

# apl-source:17
def مضاعف_قائمة(أرقام):
    # apl-source:18
    نتيجة = 1
    # apl-source:19
    for ع in أرقام:
        # apl-source:20
        نتيجة = مضاعف_مشترك(نتيجة, ع)
    # apl-source:21
    return نتيجة
# apl-source:22

# apl-source:23
print("م.م.أ [4, 6]:", مضاعف_قائمة([4, 6]))
# apl-source:24
print("م.م.أ [2, 3, 4, 5]:", مضاعف_قائمة([2, 3, 4, 5]))
# apl-source:25
print("م.م.أ [1..10]:", مضاعف_قائمة([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# apl-source:26
