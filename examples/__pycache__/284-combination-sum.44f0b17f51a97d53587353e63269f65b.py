
# apl-source:1
# مثال 284 — مجموعات بمبلغ مستهدف
# apl-source:2
# Combination sum
# apl-source:3
# Demonstrates: تراجع مع إعادة الاستخدام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/284-combination-sum.apl
# apl-source:6

# apl-source:7
def ابحث(مرشحون, هدف, بداية, حالية, نتيجة):
    # apl-source:8
    if هدف == 0:
        # apl-source:9
        نتيجة.append(حالية)
        # apl-source:10
        return
    # apl-source:11
    for ي in range(بداية, len(مرشحون)):
        # apl-source:12
        if مرشحون[ي] <= هدف:
            # apl-source:13
            ابحث(مرشحون, هدف - مرشحون[ي], ي, حالية + [مرشحون[ي]], نتيجة)
# apl-source:14

# apl-source:15
def مجموعات_مبلغ(مرشحون, هدف):
    # apl-source:16
    نتيجة = []
    # apl-source:17
    ابحث(مرشحون, هدف, 0, [], نتيجة)
    # apl-source:18
    return نتيجة
# apl-source:19

# apl-source:20
print(مجموعات_مبلغ([2, 3, 6, 7], 7))
# apl-source:21
print(مجموعات_مبلغ([2, 3, 5], 8))
# apl-source:22
