
# apl-source:1
# مثال 303 — الأعداد السعيدة
# apl-source:2
# Happy numbers
# apl-source:3
# Demonstrates: مجموع مربعات الأرقام حتى التقارب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/303-happy-number.apl
# apl-source:6

# apl-source:7
def سعيد(عدد):
    # apl-source:8
    مرئية = {}
    # apl-source:9
    while عدد != 1:
        # apl-source:10
        if عدد in مرئية:
            # apl-source:11
            return False
        # apl-source:12
        مرئية[عدد] = True
        # apl-source:13
        مجموع = 0
        # apl-source:14
        for رقم in str(عدد):
            # apl-source:15
            مجموع = مجموع + int(رقم) ** 2
        # apl-source:16
        عدد = مجموع
    # apl-source:17
    return True
# apl-source:18

# apl-source:19
print("19:", سعيد(19))
# apl-source:20
print("2:", سعيد(2))
# apl-source:21

# apl-source:22
قائمة = [ن for ن in range(1, 50) if سعيد(ن)]
# apl-source:23
print("السعيدة حتى 50:", قائمة)
# apl-source:24
