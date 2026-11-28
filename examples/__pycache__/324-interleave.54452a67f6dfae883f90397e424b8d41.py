
# apl-source:1
# مثال 324 — تداخل قائمتين
# apl-source:2
# Interleave two lists
# apl-source:3
# Demonstrates: دمج بالتناوب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/324-interleave.apl
# apl-source:6

# apl-source:7
def داخل(أ, ب):
    # apl-source:8
    نتيجة = []
    # apl-source:9
    أطول = len(أ)
    # apl-source:10
    if len(ب) > أطول:
        # apl-source:11
        أطول = len(ب)
    # apl-source:12
    for ي in range(أطول):
        # apl-source:13
        if ي < len(أ):
            # apl-source:14
            نتيجة.append(أ[ي])
        # apl-source:15
        if ي < len(ب):
            # apl-source:16
            نتيجة.append(ب[ي])
    # apl-source:17
    return نتيجة
# apl-source:18

# apl-source:19
print(داخل([1, 2, 3], ["أ", "ب", "ج"]))
# apl-source:20
print(داخل([1, 2], ["أ", "ب", "ج", "د"]))
# apl-source:21
