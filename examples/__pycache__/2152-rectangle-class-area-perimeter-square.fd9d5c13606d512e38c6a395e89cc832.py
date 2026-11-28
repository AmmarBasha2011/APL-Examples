
# apl-source:1
# مثال 2152 — صنف مستطيل
# apl-source:2
# Rectangle class
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2152-rectangle-class-area-perimeter-square.apl
# apl-source:6

# apl-source:7
# # الأبعاد صفتان
# apl-source:8
# # وثلاث دوال
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
    def __init__(ذات, عرض, ارتفاع):
        # apl-source:20
        ذات.عرض = عرض
        # apl-source:21
        ذات.ارتفاع = ارتفاع
# apl-source:22

    # apl-source:23
    def مساحة(ذات):
        # apl-source:24
        return ذات.عرض * ذات.ارتفاع
# apl-source:25

    # apl-source:26
    def محيط(ذات):
        # apl-source:27
        return 2 * (ذات.عرض + ذات.ارتفاع)
# apl-source:28

    # apl-source:29
    def مربع(ذات):
        # apl-source:30
        return ذات.عرض == ذات.ارتفاع
# apl-source:31

# apl-source:32
م = مستطيل(3, 4)
# apl-source:33
تأكد_يساوي(م.مساحة(), 12, "المساحة")
# apl-source:34
تأكد_يساوي(م.محيط(), 14, "المحيط")
# apl-source:35
تأكد_يساوي(م.مربع(), False, "ليس مربعا")
# apl-source:36
تأكد_يساوي(مستطيل(5, 5).مربع(), True, "مربع")
# apl-source:37
