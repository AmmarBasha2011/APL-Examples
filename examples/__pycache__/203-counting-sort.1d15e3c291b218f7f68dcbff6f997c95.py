
# apl-source:1
# مثال 203 — الترتيب بالعد
# apl-source:2
# Counting sort
# apl-source:3
# Demonstrates: مصفوفة التكرار، إعادة البناء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/203-counting-sort.apl
# apl-source:6

# apl-source:7
def ترتيب_عد(قائمة, أكبر):
    # apl-source:8
    عد = [0 for _ in range(أكبر + 1)]
    # apl-source:9
    for ع in قائمة:
        # apl-source:10
        عد[ع] = عد[ع] + 1
    # apl-source:11
    نتيجة = []
    # apl-source:12
    for قيمة in range(أكبر + 1):
        # apl-source:13
        for _ in range(عد[قيمة]):
            # apl-source:14
            نتيجة.append(قيمة)
    # apl-source:15
    return نتيجة
# apl-source:16

# apl-source:17
أرقام = [4, 2, 2, 8, 3, 3, 1]
# apl-source:18
print("قبل:", أرقام)
# apl-source:19
print("بعد:", ترتيب_عد(أرقام, 8))
# apl-source:20
