
# apl-source:1
# مثال 279 — مسافة التحرير
# apl-source:2
# Edit distance (Levenshtein)
# apl-source:3
# Demonstrates: جدول ديناميكي للتشابه
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/279-edit-distance.apl
# apl-source:6

# apl-source:7
def مسافة(أ, ب):
    # apl-source:8
    ن = len(أ)
    # apl-source:9
    م = len(ب)
    # apl-source:10
    جدول = []
    # apl-source:11
    for ي in range(ن + 1):
        # apl-source:12
        جدول.append([0 for _ in range(م + 1)])
        # apl-source:13
        جدول[ي][0] = ي
    # apl-source:14
    for ز in range(م + 1):
        # apl-source:15
        جدول[0][ز] = ز
    # apl-source:16
    for ي in range(1, ن + 1):
        # apl-source:17
        for ز in range(1, م + 1):
            # apl-source:18
            if أ[ي - 1] == ب[ز - 1]:
                # apl-source:19
                جدول[ي][ز] = جدول[ي - 1][ز - 1]
            # apl-source:20
            else:
                # apl-source:21
                أقل = جدول[ي - 1][ز - 1]
                # apl-source:22
                if جدول[ي - 1][ز] < أقل:
                    # apl-source:23
                    أقل = جدول[ي - 1][ز]
                # apl-source:24
                if جدول[ي][ز - 1] < أقل:
                    # apl-source:25
                    أقل = جدول[ي][ز - 1]
                # apl-source:26
                جدول[ي][ز] = أقل + 1
    # apl-source:27
    return جدول[ن][م]
# apl-source:28

# apl-source:29
print(مسافة("horse", "ros"))
# apl-source:30
print(مسافة("intention", "execution"))
# apl-source:31
