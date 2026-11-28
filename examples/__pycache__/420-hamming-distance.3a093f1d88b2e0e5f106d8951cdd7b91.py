
# apl-source:1
# مثال 420 — مسافة هامنج ورمز التصحيح
# apl-source:2
# Hamming distance
# apl-source:3
# Demonstrates: مقارنة تسلسلات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/420-hamming-distance.apl
# apl-source:6

# apl-source:7
def هامنج(أ, ب):
    # apl-source:8
    if len(أ) != len(ب):
        # apl-source:9
        return -1
    # apl-source:10
    مسافة = 0
    # apl-source:11
    for ي in range(len(أ)):
        # apl-source:12
        if أ[ي] != ب[ي]:
            # apl-source:13
            مسافة = مسافة + 1
    # apl-source:14
    return مسافة
# apl-source:15

# apl-source:16
print(هامنج("karolin", "kathrin"))
# apl-source:17
print(هامنج("1011101", "1001001"))
# apl-source:18
print(هامنج("ABC", "AB"))
# apl-source:19
