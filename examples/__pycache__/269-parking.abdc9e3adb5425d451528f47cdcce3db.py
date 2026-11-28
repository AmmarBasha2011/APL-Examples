
# apl-source:1
# مثال 269 — موقف سيارات
# apl-source:2
# Parking lot
# apl-source:3
# Demonstrates: أماكن وشاغل/فارغ، حساب رسوم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/269-parking.apl
# apl-source:6

# apl-source:7
class موقف:
    # apl-source:8
    def __init__(ذات, سعة):
        # apl-source:9
        ذات.أماكن = ["فارغ" for _ in range(سعة)]
# apl-source:10

    # apl-source:11
    def أوقف(ذات, لوحة):
        # apl-source:12
        for ي in range(len(ذات.أماكن)):
            # apl-source:13
            if ذات.أماكن[ي] == "فارغ":
                # apl-source:14
                ذات.أماكن[ي] = لوحة
                # apl-source:15
                return ي
        # apl-source:16
        return -1
# apl-source:17

    # apl-source:18
    def غادر(ذات, لوحة, ساعات):
        # apl-source:19
        for ي in range(len(ذات.أماكن)):
            # apl-source:20
            if ذات.أماكن[ي] == لوحة:
                # apl-source:21
                ذات.أماكن[ي] = "فارغ"
                # apl-source:22
                return ساعات * 10
        # apl-source:23
        return 0
# apl-source:24

    # apl-source:25
    def متاح(ذات):
        # apl-source:26
        عدد = 0
        # apl-source:27
        for مكان in ذات.أماكن:
            # apl-source:28
            if مكان == "فارغ":
                # apl-source:29
                عدد = عدد + 1
        # apl-source:30
        return عدد
# apl-source:31

# apl-source:32
م = موقف(5)
# apl-source:33
print("ركن في مكان:", م.أوقف("أ ب ج 123"))
# apl-source:34
print("ركن في مكان:", م.أوقف("س ص ع 456"))
# apl-source:35
print("متاح:", م.متاح())
# apl-source:36
print("رسوم 3 ساعات:", م.غادر("أ ب ج 123", 3))
# apl-source:37
print("متاح:", م.متاح())
# apl-source:38
