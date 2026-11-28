
# apl-source:1
# مثال 476 — دالة تجزية يدوية
# apl-source:2
# Manual FNV hash
# apl-source:3
# Demonstrates: خوارزمية FNV-1a
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/476-fnv-hash.apl
# apl-source:6

# apl-source:7
def تجزئة(نص_الدخل):
    # apl-source:8
    ناتج = 2166136261
    # apl-source:9
    for حرف in نص_الدخل:
        # apl-source:10
        ناتج = ناتج ^ ord(حرف)
        # apl-source:11
        ناتج = (ناتج * 16777619) % 4294967296
    # apl-source:12
    return ناتج
# apl-source:13

# apl-source:14
print(تجزئة("hello"))
# apl-source:15
print(تجزئة("hello"))
# apl-source:16
print(تجزئة("world"))
# apl-source:17
