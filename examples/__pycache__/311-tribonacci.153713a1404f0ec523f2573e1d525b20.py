
# apl-source:1
# مثال 311 — متتالية تريبوناتشي
# apl-source:2
# Tribonacci sequence
# apl-source:3
# Demonstrates: مجموع ثلاثة حدود سابقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/311-tribonacci.apl
# apl-source:6

# apl-source:7
def تريبوناتشي(ن):
    # apl-source:8
    if ن == 0:
        # apl-source:9
        return 0
    # apl-source:10
    if ن <= 2:
        # apl-source:11
        return 1
    # apl-source:12
    أ = 0
    # apl-source:13
    ب = 1
    # apl-source:14
    ج = 1
    # apl-source:15
    for _ in range(3, ن + 1):
        # apl-source:16
        تالي = أ + ب + ج
        # apl-source:17
        أ = ب
        # apl-source:18
        ب = ج
        # apl-source:19
        ج = تالي
    # apl-source:20
    return ج
# apl-source:21

# apl-source:22
for ن in range(10):
    # apl-source:23
    print(ن, ":", تريبوناتشي(ن))
# apl-source:24
