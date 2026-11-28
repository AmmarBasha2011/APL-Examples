
# apl-source:1
# مثال 445 — تحويل الزوايا
# apl-source:2
# Angle conversions
# apl-source:3
# Demonstrates: درجات وراديان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/445-angles.apl
# apl-source:6

# apl-source:7
باي = 3.14159265358979
# apl-source:8

# apl-source:9
def إلى_راديان(درجة):
    # apl-source:10
    return درجة * باي / 180
# apl-source:11

# apl-source:12
def إلى_درجة(راديان):
    # apl-source:13
    return راديان * 180 / باي
# apl-source:14

# apl-source:15
print("90 درجة =", إلى_راديان(90), "راديان")
# apl-source:16
print("1 راديان =", إلى_درجة(1), "درجة")
# apl-source:17
print("360 درجة =", إلى_راديان(360), "راديان")
# apl-source:18
