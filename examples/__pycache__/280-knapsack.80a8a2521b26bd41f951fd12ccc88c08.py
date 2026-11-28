
# apl-source:1
# مثال 280 — حقيبة الظهر 0/1
# apl-source:2
# 0/1 Knapsack
# apl-source:3
# Demonstrates: برمجة ديناميكية للاختيار الأمثل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/280-knapsack.apl
# apl-source:6

# apl-source:7
def حقيبة(أوزان, قيم, سعة):
    # apl-source:8
    ن = len(أوزان)
    # apl-source:9
    جدول = []
    # apl-source:10
    for _ in range(ن + 1):
        # apl-source:11
        جدول.append([0 for _ in range(سعة + 1)])
    # apl-source:12
    for ي in range(1, ن + 1):
        # apl-source:13
        for س in range(سعة + 1):
            # apl-source:14
            جدول[ي][س] = جدول[ي - 1][س]
            # apl-source:15
            if أوزان[ي - 1] <= س:
                # apl-source:16
                أخذ = جدول[ي - 1][س - أوزان[ي - 1]] + قيم[ي - 1]
                # apl-source:17
                if أخذ > جدول[ي][س]:
                    # apl-source:18
                    جدول[ي][س] = أخذ
    # apl-source:19
    return جدول[ن][سعة]
# apl-source:20

# apl-source:21
print(حقيبة([1, 3, 4, 5], [1, 4, 5, 7], 7))
# apl-source:22
print(حقيبة([10, 20, 30], [60, 100, 120], 50))
# apl-source:23
