
# apl-source:1
# مثال 275 — دمج الفترات المتداخلة
# apl-source:2
# Merge intervals
# apl-source:3
# Demonstrates: ترتيب ثم دمج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/275-merge-intervals.apl
# apl-source:6

# apl-source:7
def ادمج(فترات):
    # apl-source:8
    مرتبة = sorted(فترات, key=lambda ف: ف[0])
    # apl-source:9
    نتيجة = [مرتبة[0]]
    # apl-source:10
    for ي in range(1, len(مرتبة)):
        # apl-source:11
        أخيرة = نتيجة[-1]
        # apl-source:12
        حالية = مرتبة[ي]
        # apl-source:13
        if حالية[0] <= أخيرة[1]:
            # apl-source:14
            if حالية[1] > أخيرة[1]:
                # apl-source:15
                أخيرة[1] = حالية[1]
        # apl-source:16
        else:
            # apl-source:17
            نتيجة.append(حالية)
    # apl-source:18
    return نتيجة
# apl-source:19

# apl-source:20
print(ادمج([[1, 3], [2, 6], [8, 10], [15, 18]]))
# apl-source:21
print(ادمج([[1, 4], [4, 5]]))
# apl-source:22
