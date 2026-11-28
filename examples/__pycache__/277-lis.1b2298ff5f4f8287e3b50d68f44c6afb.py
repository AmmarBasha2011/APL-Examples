
# apl-source:1
# مثال 277 — أطول متتالية متزايدة
# apl-source:2
# Longest increasing subsequence
# apl-source:3
# Demonstrates: برمجة ديناميكية على المتتاليات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/277-lis.apl
# apl-source:6

# apl-source:7
def أطول_متزايدة(قائمة):
    # apl-source:8
    ن = len(قائمة)
    # apl-source:9
    أطوال = [1 for _ in range(ن)]
    # apl-source:10
    for ي in range(1, ن):
        # apl-source:11
        for ز in range(ي):
            # apl-source:12
            if قائمة[ز] < قائمة[ي] and أطوال[ز] + 1 > أطوال[ي]:
                # apl-source:13
                أطوال[ي] = أطوال[ز] + 1
    # apl-source:14
    أطول = أطوال[0]
    # apl-source:15
    for ط in أطوال:
        # apl-source:16
        if ط > أطول:
            # apl-source:17
            أطول = ط
    # apl-source:18
    return أطول
# apl-source:19

# apl-source:20
print(أطول_متزايدة([10, 9, 2, 5, 3, 7, 101, 18]))
# apl-source:21
print(أطول_متزايدة([0, 1, 0, 3, 2, 3]))
# apl-source:22
