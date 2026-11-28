
# apl-source:1
# مثال 1120 — مجموع منطقة في مصفوفة
# apl-source:2
# Range sum query 2D
# apl-source:3
# Demonstrates: مجاميع تراكمية ثنائية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1120-matrix-region-sum.apl
# apl-source:6

# apl-source:7
# جدول المجاميع التراكمية للمستطيل من الزاوية العليا
# apl-source:8
# ومجموع أي منطقة بالتضمين والاستبعاد
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
class مجموع_منطقة:
    # apl-source:19
    def __init__(ذات, م):
        # apl-source:20
        ص = len(م)
        # apl-source:21
        ع = len(م[0])
        # apl-source:22
        ذات.ت = []
        # apl-source:23
        for ر in range(ص + 1):
            # apl-source:24
            ذات.ت = ذات.ت + [[0] * (ع + 1)]
        # apl-source:25
        for ر in range(ص):
            # apl-source:26
            for ك in range(ع):
                # apl-source:27
                ذات.ت[ر + 1][ك + 1] = م[ر][ك] + ذات.ت[ر][ك + 1] + ذات.ت[ر + 1][ك] - ذات.ت[ر][ك]
# apl-source:28

    # apl-source:29
    def منطقة(ذات, ر1, ك1, ر2, ك2):
        # apl-source:30
        return ذات.ت[ر2 + 1][ك2 + 1] - ذات.ت[ر1][ك2 + 1] - ذات.ت[ر2 + 1][ك1] + ذات.ت[ر1][ك1]
# apl-source:31

# apl-source:32
م = مجموع_منطقة([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
# apl-source:33
تأكد_يساوي(م.منطقة(2, 1, 4, 3), 8, "المنطقة الأولى")
# apl-source:34
تأكد_يساوي(م.منطقة(1, 1, 2, 2), 11, "المنطقة الثانية")
# apl-source:35
تأكد_يساوي(م.منطقة(1, 2, 2, 4), 12, "المنطقة الثالثة")
# apl-source:36
تأكد_يساوي(م.منطقة(0, 0, 0, 0), 3, "خلية واحدة")
# apl-source:37
