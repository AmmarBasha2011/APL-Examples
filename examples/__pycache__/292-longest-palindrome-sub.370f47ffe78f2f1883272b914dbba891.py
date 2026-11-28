
# apl-source:1
# مثال 292 — أطول مقطع متناظر
# apl-source:2
# Longest palindromic substring
# apl-source:3
# Demonstrates: التوسع من المركز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/292-longest-palindrome-sub.apl
# apl-source:6

# apl-source:7
def وسع(نص_الدخل, أيسر, أيمن):
    # apl-source:8
    while أيسر >= 0 and أيمن < len(نص_الدخل) and نص_الدخل[أيسر] == نص_الدخل[أيمن]:
        # apl-source:9
        أيسر = أيسر - 1
        # apl-source:10
        أيمن = أيمن + 1
    # apl-source:11
    return نص_الدخل[أيسر + 1:أيمن]
# apl-source:12

# apl-source:13
def أطول_متناظر(نص_الدخل):
    # apl-source:14
    أفضل = ""
    # apl-source:15
    for ي in range(len(نص_الدخل)):
        # apl-source:16
        فردي = وسع(نص_الدخل, ي, ي)
        # apl-source:17
        زوجي = وسع(نص_الدخل, ي, ي + 1)
        # apl-source:18
        if len(فردي) > len(أفضل):
            # apl-source:19
            أفضل = فردي
        # apl-source:20
        if len(زوجي) > len(أفضل):
            # apl-source:21
            أفضل = زوجي
    # apl-source:22
    return أفضل
# apl-source:23

# apl-source:24
print(أطول_متناظر("babad"))
# apl-source:25
print(أطول_متناظر("cbbd"))
# apl-source:26
print(أطول_متناظر("racecar"))
# apl-source:27
