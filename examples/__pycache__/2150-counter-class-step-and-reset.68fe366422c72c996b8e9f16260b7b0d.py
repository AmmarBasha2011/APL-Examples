
# apl-source:1
# مثال 2150 — صنف عداد بخطوة وإعادة ضبط
# apl-source:2
# Counter class
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2150-counter-class-step-and-reset.apl
# apl-source:6

# apl-source:7
# # يمكن إعادة العداد للصفر
# apl-source:8
# # ويسجل عدد مرات الزيادة
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
class عداد:
    # apl-source:19
    def __init__(ذات, خطوة):
        # apl-source:20
        ذات.قيمة = 0
        # apl-source:21
        ذات.خطوة = خطوة
        # apl-source:22
        ذات.مرات = 0
# apl-source:23

    # apl-source:24
    def زد(ذات):
        # apl-source:25
        ذات.قيمة = ذات.قيمة + ذات.خطوة
        # apl-source:26
        ذات.مرات = ذات.مرات + 1
# apl-source:27

    # apl-source:28
    def صفر(ذات):
        # apl-source:29
        ذات.قيمة = 0
# apl-source:30

# apl-source:31
ع = عداد(5)
# apl-source:32
ع.زد()
# apl-source:33
ع.زد()
# apl-source:34
ع.زد()
# apl-source:35
تأكد_يساوي(ع.قيمة, 15, "ثلاث مرات")
# apl-source:36
ع.صفر()
# apl-source:37
تأكد_يساوي(ع.قيمة, 0, "بعد الصفر")
# apl-source:38
تأكد_يساوي(ع.مرات, 3, "عدد المرات")
# apl-source:39
