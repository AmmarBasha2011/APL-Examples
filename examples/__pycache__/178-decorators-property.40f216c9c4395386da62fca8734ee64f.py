
# apl-source:1
# مثال 178 — الخواص المحسوبة والمحددات
# apl-source:2
# Properties and setters
# apl-source:3
# Demonstrates: خاصية، محدد، صنف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/178-decorators-property.apl
# apl-source:6

# apl-source:7
class حرارة:
    # apl-source:8
    def __init__(ذات, مئوي):
        # apl-source:9
        ذات._مئوي = مئوي
# apl-source:10

    # apl-source:11
    @property
    def مئوي(ذات):
        # apl-source:12
        return ذات._مئوي
# apl-source:13

    # apl-source:14
    @مئوي.setter
    def مئوي(ذات, قيمة):
        # apl-source:15
        ذات._مئوي = قيمة
# apl-source:16

    # apl-source:17
    @property
    def فهرنهايت(ذات):
        # apl-source:18
        return ذات._مئوي * 9 / 5 + 32
# apl-source:19

    # apl-source:20
    @property
    def كلفن(ذات):
        # apl-source:21
        return ذات._مئوي + 273.15
# apl-source:22

# apl-source:23
ح = حرارة(25)
# apl-source:24
print("مئوي:", ح.مئوي)
# apl-source:25
print("فهرنهايت:", ح.فهرنهايت)
# apl-source:26
print("كلفن:", ح.كلفن)
# apl-source:27

# apl-source:28
ح.مئوي = 100
# apl-source:29
print("بعد التعديل فهرنهايت:", ح.فهرنهايت)
# apl-source:30
