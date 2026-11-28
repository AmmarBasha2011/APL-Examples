
# apl-source:1
# مثال 225 — ضغط طول التكرار
# apl-source:2
# Run-length encoding
# apl-source:3
# Demonstrates: عد متتاليات، ضغط وفك
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/225-run-length.apl
# apl-source:6

# apl-source:7
def اضغط(نص_الدخل):
    # apl-source:8
    if len(نص_الدخل) == 0:
        # apl-source:9
        return ""
    # apl-source:10
    نتيجة = ""
    # apl-source:11
    عدد = 1
    # apl-source:12
    for ي in range(1, len(نص_الدخل)):
        # apl-source:13
        if نص_الدخل[ي] == نص_الدخل[ي - 1]:
            # apl-source:14
            عدد = عدد + 1
        # apl-source:15
        else:
            # apl-source:16
            نتيجة = نتيجة + نص_الدخل[ي - 1] + str(عدد)
            # apl-source:17
            عدد = 1
    # apl-source:18
    نتيجة = نتيجة + نص_الدخل[-1] + str(عدد)
    # apl-source:19
    return نتيجة
# apl-source:20

# apl-source:21
print("aaabbc ->", اضغط("aaabbc"))
# apl-source:22
print("xxxxxy ->", اضغط("xxxxxy"))
# apl-source:23
print("a ->", اضغط("a"))
# apl-source:24
