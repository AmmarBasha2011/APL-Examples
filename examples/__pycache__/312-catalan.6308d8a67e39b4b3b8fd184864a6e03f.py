
# apl-source:1
# مثال 312 — أعداد كاتالان
# apl-source:2
# Catalan numbers
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/312-catalan.apl
# apl-source:6

# apl-source:7
def كاتالان(ن):
    # apl-source:8
    جدول = [0 for _ in range(ن + 1)]
    # apl-source:9
    جدول[0] = 1
    # apl-source:10
    if ن >= 1:
        # apl-source:11
        جدول[1] = 1
    # apl-source:12
    for ي in range(2, ن + 1):
        # apl-source:13
        for ز in range(ي):
            # apl-source:14
            جدول[ي] = جدول[ي] + جدول[ز] * جدول[ي - 1 - ز]
    # apl-source:15
    return جدول[ن]
# apl-source:16

# apl-source:17
print([كاتالان(ن) for ن in range(10)])
# apl-source:18
