
# apl-source:1
# مثال 434 — تنسيق الأرقام الكبيرة
# apl-source:2
# Number formatting
# apl-source:3
# Demonstrates: فواصل الآلاف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/434-number-format.apl
# apl-source:6

# apl-source:7
def بفواصل(عدد):
    # apl-source:8
    نص_عدد = str(عدد)
    # apl-source:9
    ناتج = ""
    # apl-source:10
    عد = 0
    # apl-source:11
    for ي in range(1, len(نص_عدد) + 1):
        # apl-source:12
        حرف = نص_عدد[len(نص_عدد) - ي]
        # apl-source:13
        if عد == 3:
            # apl-source:14
            ناتج = "," + ناتج
            # apl-source:15
            عد = 0
        # apl-source:16
        ناتج = حرف + ناتج
        # apl-source:17
        عد = عد + 1
    # apl-source:18
    return ناتج
# apl-source:19

# apl-source:20
print(بفواصل(1234567))
# apl-source:21
print(بفواصل(950))
# apl-source:22
print(بفواصل(1000000))
# apl-source:23
