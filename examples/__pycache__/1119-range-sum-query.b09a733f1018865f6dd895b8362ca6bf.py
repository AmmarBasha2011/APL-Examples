
# apl-source:1
# مثال 1119 — استعلام مجموع مدى
# apl-source:2
# Range sum query immutable
# apl-source:3
# Demonstrates: مجاميع تراكمية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1119-range-sum-query.apl
# apl-source:6

# apl-source:7
# نبني قائمة المجاميع التراكمية مرة واحدة
# apl-source:8
# مجموع المدى فرق تراكميين
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
class مجموع_مدى:
    # apl-source:19
    def __init__(ذات, ق):
        # apl-source:20
        ذات.تراكم = [0]
        # apl-source:21
        for س in ق:
            # apl-source:22
            ذات.تراكم = ذات.تراكم + [ذات.تراكم[-1] + س]
# apl-source:23

    # apl-source:24
    def مجموع_من(ذات, ي, ل):
        # apl-source:25
        return ذات.تراكم[ل + 1] - ذات.تراكم[ي]
# apl-source:26

# apl-source:27
م = مجموع_مدى([-2, 0, 3, -5, 2, -1])
# apl-source:28
تأكد_يساوي(م.مجموع_من(0, 2), 1, "من 0 إلى 2")
# apl-source:29
تأكد_يساوي(م.مجموع_من(2, 5), -1, "من 2 إلى 5")
# apl-source:30
تأكد_يساوي(م.مجموع_من(0, 5), -3, "الكل")
# apl-source:31
تأكد_يساوي(م.مجموع_من(3, 3), -5, "عنصر واحد")
# apl-source:32
