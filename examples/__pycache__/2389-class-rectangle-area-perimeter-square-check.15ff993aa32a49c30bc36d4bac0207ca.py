
# apl-source:1
# مثال 2389 — صنف مستطيل
# apl-source:2
# Rectangle class
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2389-class-rectangle-area-perimeter-square-check.apl
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
class مستطيل:
    # apl-source:19
    def __init__(ذات, ط, ع):
        # apl-source:20
        ذات.ط = ط
        # apl-source:21
        ذات.ع = ع
# apl-source:22

    # apl-source:23
    def مساحة(ذات):
        # apl-source:24
        return ذات.ط * ذات.ع
# apl-source:25

    # apl-source:26
    def محيط(ذات):
        # apl-source:27
        return 2 * (ذات.ط + ذات.ع)
# apl-source:28

    # apl-source:29
    def مربع(ذات):
        # apl-source:30
        return ذات.ط == ذات.ع
# apl-source:31

# apl-source:32
م = مستطيل(3, 4)
# apl-source:33
تأكد_يساوي(م.مساحة(), 12, "مساحة")
# apl-source:34
تأكد_يساوي(م.محيط(), 14, "محيط")
# apl-source:35
تأكد_يساوي(م.مربع(), False, "ليس مربعا")
# apl-source:36
تأكد_يساوي(مستطيل(5, 5).مربع(), True, "مربع")
# apl-source:37
