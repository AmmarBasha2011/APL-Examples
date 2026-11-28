
# apl-source:1
# مثال 209 — طرق صعود السلم (برمجة ديناميكية)
# apl-source:2
# Climbing stairs (DP)
# apl-source:3
# Demonstrates: جدول ديناميكي من الأسفل للأعلى
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/209-climbing-stairs.apl
# apl-source:6

# apl-source:7
def طرق_الصعود(ن):
    # apl-source:8
    if ن <= 2:
        # apl-source:9
        return ن
    # apl-source:10
    طرق = [0 for _ in range(ن + 1)]
    # apl-source:11
    طرق[1] = 1
    # apl-source:12
    طرق[2] = 2
    # apl-source:13
    for ي in range(3, ن + 1):
        # apl-source:14
        طرق[ي] = طرق[ي - 1] + طرق[ي - 2]
    # apl-source:15
    return طرق[ن]
# apl-source:16

# apl-source:17
for درجات in [3, 5, 10, 20]:
    # apl-source:18
    print("سلم من", درجات, "درجات:", طرق_الصعود(درجات), "طريقة")
# apl-source:19
