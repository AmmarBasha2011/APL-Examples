
# apl-source:1
# مثال 2387 — صنف مكدس مع الحجم
# apl-source:2
# Stack class with size
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2387-class-stack-push-pop-size.apl
# apl-source:6

# apl-source:7
# # نعرف صنفا
# apl-source:8
# # ونختبر سلوكه
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
class مكدس:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.ع = []
# apl-source:21

    # apl-source:22
    def ادفع(ذات, ق):
        # apl-source:23
        ذات.ع = ذات.ع + [ق]
# apl-source:24

    # apl-source:25
    def اسحب(ذات):
        # apl-source:26
        ق = ذات.ع[-1]
        # apl-source:27
        ذات.ع = ذات.ع[:-1]
        # apl-source:28
        return ق
# apl-source:29

    # apl-source:30
    def حجم(ذات):
        # apl-source:31
        return len(ذات.ع)
# apl-source:32

# apl-source:33
م = مكدس()
# apl-source:34
م.ادفع(1)
# apl-source:35
م.ادفع(2)
# apl-source:36
م.ادفع(3)
# apl-source:37
تأكد_يساوي(م.حجم(), 3, "ثلاثة")
# apl-source:38
تأكد_يساوي(م.اسحب(), 3, "الأخير")
# apl-source:39
تأكد_يساوي(م.حجم(), 2, "اثنان")
# apl-source:40
