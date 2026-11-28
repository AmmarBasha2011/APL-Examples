
# apl-source:1
# مثال 306 — الجذر الرقمي
# apl-source:2
# Digital root
# apl-source:3
# Demonstrates: جمع الأرقام حتى خانة واحدة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/306-digital-root.apl
# apl-source:6

# apl-source:7
def جذر_رقمي(عدد):
    # apl-source:8
    while عدد >= 10:
        # apl-source:9
        مجموع = 0
        # apl-source:10
        for رقم in str(عدد):
            # apl-source:11
            مجموع = مجموع + int(رقم)
        # apl-source:12
        عدد = مجموع
    # apl-source:13
    return عدد
# apl-source:14

# apl-source:15
print("38:", جذر_رقمي(38))
# apl-source:16
print("999:", جذر_رقمي(999))
# apl-source:17
print("12345:", جذر_رقمي(12345))
# apl-source:18
