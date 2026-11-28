
# apl-source:1
# مثال 443 — حسابات الدائرة والخط
# apl-source:2
# Circle and line math
# apl-source:3
# Demonstrates: محيط ومساحة وميل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/443-circle-line.apl
# apl-source:6

# apl-source:7
باي = 3.14159265358979
# apl-source:8

# apl-source:9
def دائرة(نصف_قطر):
    # apl-source:10
    return [باي * نصف_قطر * نصف_قطر, 2 * باي * نصف_قطر]
# apl-source:11

# apl-source:12
def ميل_خط(س1, ص1, س2, ص2):
    # apl-source:13
    if س2 == س1:
        # apl-source:14
        return "رأسي"
    # apl-source:15
    return (ص2 - ص1) / (س2 - س1)
# apl-source:16

# apl-source:17
نتيجة = دائرة(5)
# apl-source:18
print("المساحة:", نتيجة[0])
# apl-source:19
print("المحيط:", نتيجة[1])
# apl-source:20
print("الميل:", ميل_خط(0, 0, 2, 6))
# apl-source:21
print("الميل:", ميل_خط(3, 1, 3, 5))
# apl-source:22
