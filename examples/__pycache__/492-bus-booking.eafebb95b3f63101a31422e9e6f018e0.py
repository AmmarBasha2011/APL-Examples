
# apl-source:1
# مثال 492 — حجز مقاعد حافلة
# apl-source:2
# Bus seat booking
# apl-source:3
# Demonstrates: خريطة مقاعد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/492-bus-booking.apl
# apl-source:6

# apl-source:7
مقاعد = []
# apl-source:8
for ي in range(10):
    # apl-source:9
    مقاعد.append("فارغ")
# apl-source:10

# apl-source:11
def اعرض():
    # apl-source:12
    رسم = ""
    # apl-source:13
    for م in مقاعد:
        # apl-source:14
        if م == "فارغ":
            # apl-source:15
            رسم = رسم + "[_]"
        # apl-source:16
        else:
            # apl-source:17
            رسم = رسم + "[X]"
    # apl-source:18
    print(رسم)
# apl-source:19

# apl-source:20
def احجز_مقعد(رقم):
    # apl-source:21
    if مقاعد[رقم] == "فارغ":
        # apl-source:22
        مقاعد[رقم] = "محجوز"
        # apl-source:23
        print("تم حجز المقعد", رقم)
    # apl-source:24
    else:
        # apl-source:25
        print("المقعد", رقم, "محجوز مسبقا")
# apl-source:26

# apl-source:27
اعرض()
# apl-source:28
احجز_مقعد(3)
# apl-source:29
احجز_مقعد(3)
# apl-source:30
احجز_مقعد(7)
# apl-source:31
اعرض()
# apl-source:32
