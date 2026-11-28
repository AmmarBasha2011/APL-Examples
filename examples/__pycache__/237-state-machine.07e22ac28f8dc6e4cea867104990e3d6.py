
# apl-source:1
# مثال 237 — آلة الحالات (إشارة مرور)
# apl-source:2
# State machine (traffic light)
# apl-source:3
# Demonstrates: انتقالات الحالات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/237-state-machine.apl
# apl-source:6

# apl-source:7
class إشارة:
    # apl-source:8
    def __init__(ذات):
        # apl-source:9
        ذات.حالة = "أحمر"
# apl-source:10

    # apl-source:11
    def التالي(ذات):
        # apl-source:12
        match ذات.حالة:
            # apl-source:13
            case "أحمر":
                # apl-source:14
                ذات.حالة = "أخضر"
            # apl-source:15
            case "أخضر":
                # apl-source:16
                ذات.حالة = "أصفر"
            # apl-source:17
            case _:
                # apl-source:18
                ذات.حالة = "أحمر"
        # apl-source:19
        return ذات.حالة
# apl-source:20

# apl-source:21
إ = إشارة()
# apl-source:22
print("البداية:", إ.حالة)
# apl-source:23
for _ in range(4):
    # apl-source:24
    print("->", إ.التالي())
# apl-source:25
