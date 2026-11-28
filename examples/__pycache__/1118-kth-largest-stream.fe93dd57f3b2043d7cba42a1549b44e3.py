
# apl-source:1
# مثال 1118 — الأكبر ك في تدفق
# apl-source:2
# Kth largest element in a stream
# apl-source:3
# Demonstrates: قائمة مرتبة بحجم ثابت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1118-kth-largest-stream.apl
# apl-source:6

# apl-source:7
# نحتفظ بأكبر ك أعداد فقط مرتبة تصاعدياً
# apl-source:8
# وأولها هو الأكبر ك
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
class اكبر_ك:
    # apl-source:19
    def __init__(ذات, ك, بداية):
        # apl-source:20
        ذات.ك = ك
        # apl-source:21
        ذات.اكبر = []
        # apl-source:22
        for س in بداية:
            # apl-source:23
            ذات.اضف_رقم(س)
# apl-source:24

    # apl-source:25
    def اضف_رقم(ذات, س):
        # apl-source:26
        ذات.اكبر = ذات.اكبر + [س]
        # apl-source:27
        ذات.اكبر = sorted(ذات.اكبر)
        # apl-source:28
        if len(ذات.اكبر) > ذات.ك:
            # apl-source:29
            ذات.اكبر = ذات.اكبر[1:]
        # apl-source:30
        return ذات.اكبر[0]
# apl-source:31

# apl-source:32
م = اكبر_ك(3, [4, 5, 8, 2])
# apl-source:33
تأكد_يساوي(م.اضف_رقم(3), 4, "بعد 3")
# apl-source:34
تأكد_يساوي(م.اضف_رقم(5), 5, "بعد 5")
# apl-source:35
تأكد_يساوي(م.اضف_رقم(10), 5, "بعد 10")
# apl-source:36
تأكد_يساوي(م.اضف_رقم(9), 8, "بعد 9")
# apl-source:37
تأكد_يساوي(م.اضف_رقم(4), 8, "بعد 4")
# apl-source:38
