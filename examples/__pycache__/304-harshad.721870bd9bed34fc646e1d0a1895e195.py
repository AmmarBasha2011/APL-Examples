
# apl-source:1
# مثال 304 — أعداد هارشاد
# apl-source:2
# Harshad numbers
# apl-source:3
# Demonstrates: قابلية القسمة على مجموع الأرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/304-harshad.apl
# apl-source:6

# apl-source:7
def هارشاد(عدد):
    # apl-source:8
    مجموع = 0
    # apl-source:9
    for رقم in str(عدد):
        # apl-source:10
        مجموع = مجموع + int(رقم)
    # apl-source:11
    return عدد % مجموع == 0
# apl-source:12

# apl-source:13
print("18:", هارشاد(18))
# apl-source:14
print("19:", هارشاد(19))
# apl-source:15

# apl-source:16
قائمة = [ن for ن in range(1, 60) if هارشاد(ن)]
# apl-source:17
print("هارشاد حتى 60:", قائمة)
# apl-source:18
