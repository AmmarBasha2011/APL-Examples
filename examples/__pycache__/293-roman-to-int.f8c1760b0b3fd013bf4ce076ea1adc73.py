
# apl-source:1
# مثال 293 — من أرقام رومانية إلى عشرية
# apl-source:2
# Roman to integer
# apl-source:3
# Demonstrates: قاموس قيم وقاعدة الطرح
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/293-roman-to-int.apl
# apl-source:6

# apl-source:7
قيم = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
# apl-source:8

# apl-source:9
def من_روماني(نص_الدخل):
    # apl-source:10
    مجموع = 0
    # apl-source:11
    for ي in range(len(نص_الدخل)):
        # apl-source:12
        حالي = قيم[نص_الدخل[ي]]
        # apl-source:13
        if ي + 1 < len(نص_الدخل) and قيم[نص_الدخل[ي + 1]] > حالي:
            # apl-source:14
            مجموع = مجموع - حالي
        # apl-source:15
        else:
            # apl-source:16
            مجموع = مجموع + حالي
    # apl-source:17
    return مجموع
# apl-source:18

# apl-source:19
print("III =", من_روماني("III"))
# apl-source:20
print("IV =", من_روماني("IV"))
# apl-source:21
print("IX =", من_روماني("IX"))
# apl-source:22
print("MCMXCIV =", من_روماني("MCMXCIV"))
# apl-source:23
