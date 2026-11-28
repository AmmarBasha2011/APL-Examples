
# apl-source:1
# مثال 190 — مجموع العددين
# apl-source:2
# Two sum
# apl-source:3
# Demonstrates: قاموس للبحث السريع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/190-two-sum.apl
# apl-source:6

# apl-source:7
def مجموع_العددين(أرقام, هدف):
    # apl-source:8
    مرئية = {}
    # apl-source:9
    for ي in range(len(أرقام)):
        # apl-source:10
        مكمل = هدف - أرقام[ي]
        # apl-source:11
        if مكمل in مرئية:
            # apl-source:12
            return [مرئية[مكمل], ي]
        # apl-source:13
        مرئية[أرقام[ي]] = ي
    # apl-source:14
    return []
# apl-source:15

# apl-source:16
print(مجموع_العددين([2, 7, 11, 15], 9))
# apl-source:17
print(مجموع_العددين([3, 2, 4], 6))
# apl-source:18
print(مجموع_العددين([3, 3], 6))
# apl-source:19
