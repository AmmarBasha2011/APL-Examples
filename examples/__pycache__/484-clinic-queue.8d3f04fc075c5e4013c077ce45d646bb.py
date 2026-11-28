import queue
# apl-source:1
# مثال 484 — طابور عيادة
# apl-source:2
# Clinic queue
# apl-source:3
# Demonstrates: حجز ونداء بالترتيب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/484-clinic-queue.apl
# apl-source:6

# apl-source:7
طابور = []
# apl-source:8

# apl-source:9
def احجز(اسم):
    # apl-source:10
    طابور.append(اسم)
    # apl-source:11
    print("حجز:", اسم, "- رقمك", len(طابور))
# apl-source:12

# apl-source:13
def ناد_التالي():
    # apl-source:14
    if len(طابور) == 0:
        # apl-source:15
        print("لا أحد في الانتظار")
        # apl-source:16
        return
    # apl-source:17
    تالي = طابور.pop(0)
    # apl-source:18
    print("ادخل:", تالي, "- متبقي", len(طابور))
# apl-source:19

# apl-source:20
احجز("أحمد")
# apl-source:21
احجز("منى")
# apl-source:22
احجز("سامي")
# apl-source:23
ناد_التالي()
# apl-source:24
ناد_التالي()
# apl-source:25
ناد_التالي()
# apl-source:26
ناد_التالي()
# apl-source:27
