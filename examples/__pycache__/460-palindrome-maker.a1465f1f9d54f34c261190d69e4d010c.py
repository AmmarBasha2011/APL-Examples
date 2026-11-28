
# apl-source:1
# مثال 460 — مولد متناقضات لفظية
# apl-source:2
# Palindrome maker
# apl-source:3
# Demonstrates: بناء أطول متناقض من حروف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/460-palindrome-maker.apl
# apl-source:6

# apl-source:7
def اصنع_متناقض(حروف):
    # apl-source:8
    تكرار = {}
    # apl-source:9
    for حرف in حروف:
        # apl-source:10
        قديم = تكرار.get(حرف, 0)
        # apl-source:11
        تكرار[حرف] = قديم + 1
    # apl-source:12
    يسار = ""
    # apl-source:13
    منتصف = ""
    # apl-source:14
    حروف_مرتبة = sorted(تكرار.keys())
    # apl-source:15
    for مفتاح in حروف_مرتبة:
        # apl-source:16
        أزواج = تكرار[مفتاح] // 2
        # apl-source:17
        for _ in range(أزواج):
            # apl-source:18
            يسار = يسار + مفتاح
        # apl-source:19
        if تكرار[مفتاح] % 2 == 1 and منتصف == "":
            # apl-source:20
            منتصف = مفتاح
    # apl-source:21
    يمين = ""
    # apl-source:22
    for ي in range(1, len(يسار) + 1):
        # apl-source:23
        يمين = يمين + يسار[len(يسار) - ي]
    # apl-source:24
    return يسار + منتصف + يمين
# apl-source:25

# apl-source:26
print(اصنع_متناقض("aabbc"))
# apl-source:27
print(اصنع_متناقض("aabbbcc"))
# apl-source:28
