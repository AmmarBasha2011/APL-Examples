
# apl-source:1
# مثال 278 — أطول متتالية مشتركة
# apl-source:2
# Longest common subsequence
# apl-source:3
# Demonstrates: جدول ديناميكي ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/278-lcs.apl
# apl-source:6

# apl-source:7
def أطول_مشتركة(أ, ب):
    # apl-source:8
    ن = len(أ)
    # apl-source:9
    م = len(ب)
    # apl-source:10
    جدول = []
    # apl-source:11
    for _ in range(ن + 1):
        # apl-source:12
        جدول.append([0 for _ in range(م + 1)])
    # apl-source:13
    for ي in range(1, ن + 1):
        # apl-source:14
        for ز in range(1, م + 1):
            # apl-source:15
            if أ[ي - 1] == ب[ز - 1]:
                # apl-source:16
                جدول[ي][ز] = جدول[ي - 1][ز - 1] + 1
            # apl-source:17
            elif جدول[ي - 1][ز] >= جدول[ي][ز - 1]:
                # apl-source:18
                جدول[ي][ز] = جدول[ي - 1][ز]
            # apl-source:19
            else:
                # apl-source:20
                جدول[ي][ز] = جدول[ي][ز - 1]
    # apl-source:21
    return جدول[ن][م]
# apl-source:22

# apl-source:23
print(أطول_مشتركة("abcde", "ace"))
# apl-source:24
print(أطول_مشتركة("abc", "abc"))
# apl-source:25
print(أطول_مشتركة("abc", "def"))
# apl-source:26
