
# apl-source:1
# مثال 399 — الانحدار الخطي
# apl-source:2
# Linear regression
# apl-source:3
# Demonstrates: الميل والمقطع يدويا
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/399-linear-regression.apl
# apl-source:6

# apl-source:7
def انحدار(س, ص):
    # apl-source:8
    ن = len(س)
    # apl-source:9
    مجموع_س = 0
    # apl-source:10
    مجموع_ص = 0
    # apl-source:11
    مجموع_سص = 0
    # apl-source:12
    مجموع_سس = 0
    # apl-source:13
    for ي in range(ن):
        # apl-source:14
        مجموع_س = مجموع_س + س[ي]
        # apl-source:15
        مجموع_ص = مجموع_ص + ص[ي]
        # apl-source:16
        مجموع_سص = مجموع_سص + س[ي] * ص[ي]
        # apl-source:17
        مجموع_سس = مجموع_سس + س[ي] * س[ي]
    # apl-source:18
    ميل = (ن * مجموع_سص - مجموع_س * مجموع_ص) / (ن * مجموع_سس - مجموع_س * مجموع_س)
    # apl-source:19
    مقطع = (مجموع_ص - ميل * مجموع_س) / ن
    # apl-source:20
    return [ميل, مقطع]
# apl-source:21

# apl-source:22
نتيجة = انحدار([1, 2, 3, 4, 5], [2, 4, 5, 4, 5])
# apl-source:23
print("الميل:", نتيجة[0])
# apl-source:24
print("المقطع:", نتيجة[1])
# apl-source:25
print("التوقع عند 6:", نتيجة[0] * 6 + نتيجة[1])
# apl-source:26
