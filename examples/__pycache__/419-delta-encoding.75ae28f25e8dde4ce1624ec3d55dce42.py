
# apl-source:1
# مثال 419 — ترميز الفروقات
# apl-source:2
# Delta encoding
# apl-source:3
# Demonstrates: ضغط وفك تسلسل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/419-delta-encoding.apl
# apl-source:6

# apl-source:7
def فرق_ترميز(قائمة):
    # apl-source:8
    ناتج = [قائمة[0]]
    # apl-source:9
    for ي in range(1, len(قائمة)):
        # apl-source:10
        ناتج.append(قائمة[ي] - قائمة[ي - 1])
    # apl-source:11
    return ناتج
# apl-source:12

# apl-source:13
def فرق_فك(مشفر):
    # apl-source:14
    ناتج = [مشفر[0]]
    # apl-source:15
    for ي in range(1, len(مشفر)):
        # apl-source:16
        ناتج.append(ناتج[ي - 1] + مشفر[ي])
    # apl-source:17
    return ناتج
# apl-source:18

# apl-source:19
أسعار = [100, 105, 103, 110, 108, 115]
# apl-source:20
مشفر = فرق_ترميز(أسعار)
# apl-source:21
print("مشفر:", مشفر)
# apl-source:22
print("مفكوك:", فرق_فك(مشفر))
# apl-source:23
