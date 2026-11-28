
# apl-source:1
# مثال 360 — صنف درجة حرارة
# apl-source:2
# Temperature class
# apl-source:3
# Demonstrates: تحويلات بين الوحدات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/360-temperature-class.apl
# apl-source:6

# apl-source:7
class حرارة_ج:
    # apl-source:8
    def __init__(ذات, مئوي):
        # apl-source:9
        ذات.مئوي = مئوي
# apl-source:10

    # apl-source:11
    def إلى_فهرنهايت(ذات):
        # apl-source:12
        return ذات.مئوي * 9 / 5 + 32
# apl-source:13

    # apl-source:14
    def إلى_كلفن(ذات):
        # apl-source:15
        return ذات.مئوي + 273.15
# apl-source:16

    # apl-source:17
    def صف(ذات):
        # apl-source:18
        print(ذات.مئوي, "°C =", ذات.إلى_فهرنهايت(), "°F =", ذات.إلى_كلفن(), "K")
# apl-source:19

# apl-source:20
حرارة_ج(0).صف()
# apl-source:21
حرارة_ج(100).صف()
# apl-source:22
غليان = حرارة_ج((180) * 5 / 9)
# apl-source:23
print("212°F =", غليان.مئوي, "°C")
# apl-source:24
