
# apl-source:1
# مثال 326 — إزالة التكرار المتتالي
# apl-source:2
# Remove consecutive duplicates
# apl-source:3
# Demonstrates: ضغط المتتاليات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/326-dedupe-consecutive.apl
# apl-source:6

# apl-source:7
def بدون_تكرار_متتالي(قائمة):
    # apl-source:8
    if len(قائمة) == 0:
        # apl-source:9
        return []
    # apl-source:10
    نتيجة = [قائمة[0]]
    # apl-source:11
    for ي in range(1, len(قائمة)):
        # apl-source:12
        if قائمة[ي] != نتيجة[-1]:
            # apl-source:13
            نتيجة.append(قائمة[ي])
    # apl-source:14
    return نتيجة
# apl-source:15

# apl-source:16
print(بدون_تكرار_متتالي([1, 1, 2, 2, 2, 3, 1, 1]))
# apl-source:17
print(بدون_تكرار_متتالي(["أ", "أ", "ب"]))
# apl-source:18
