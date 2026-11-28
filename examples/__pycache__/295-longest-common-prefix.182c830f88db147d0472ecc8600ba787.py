
# apl-source:1
# مثال 295 — أطول مقدمة مشتركة
# apl-source:2
# Longest common prefix
# apl-source:3
# Demonstrates: مقارنة عمودية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/295-longest-common-prefix.apl
# apl-source:6

# apl-source:7
def مقدمة_مشتركة(نصوص):
    # apl-source:8
    مقدمة = نصوص[0]
    # apl-source:9
    for كلمة in نصوص:
        # apl-source:10
        while كلمة[0:len(مقدمة)] != مقدمة:
            # apl-source:11
            مقدمة = مقدمة[0:len(مقدمة) - 1]
            # apl-source:12
            if مقدمة == "":
                # apl-source:13
                return ""
    # apl-source:14
    return مقدمة
# apl-source:15

# apl-source:16
print(مقدمة_مشتركة(["flower", "flow", "flight"]))
# apl-source:17
print(مقدمة_مشتركة(["dog", "racecar", "car"]))
# apl-source:18
print(مقدمة_مشتركة(["برمجة", "برنامج", "برمائي"]))
# apl-source:19
