
# apl-source:1
# مثال 202 — ترتيب الاختيار
# apl-source:2
# Selection sort
# apl-source:3
# Demonstrates: إيجاد الأصغر في كل جولة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/202-selection-sort.apl
# apl-source:6

# apl-source:7
def اختيار(قائمة):
    # apl-source:8
    for ي in range(len(قائمة)):
        # apl-source:9
        أصغر = ي
        # apl-source:10
        for ز in range(ي + 1, len(قائمة)):
            # apl-source:11
            if قائمة[ز] < قائمة[أصغر]:
                # apl-source:12
                أصغر = ز
        # apl-source:13
        مؤقت = قائمة[ي]
        # apl-source:14
        قائمة[ي] = قائمة[أصغر]
        # apl-source:15
        قائمة[أصغر] = مؤقت
    # apl-source:16
    return قائمة
# apl-source:17

# apl-source:18
أرقام = [64, 25, 12, 22, 11]
# apl-source:19
print("قبل:", أرقام)
# apl-source:20
print("بعد:", اختيار(أرقام))
# apl-source:21
