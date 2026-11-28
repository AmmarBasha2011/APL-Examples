
# apl-source:1
# مثال 1270 — مجموع بادئات ثنائي
# apl-source:2
# 2D prefix sums
# apl-source:3
# Demonstrates: مجاميع تراكمية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1270-prefix-sum-2d.apl
# apl-source:6

# apl-source:7
# نبني جدول مجاميع من الزاوية
# apl-source:8
# ومجموع أي مستطيل أربع قراءات
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
class منطقة:
  # apl-source:19
  def __init__(ذات, م):
    # apl-source:20
    ذات.ص = len(م)
    # apl-source:21
    ذات.ج = len(م[0])
    # apl-source:22
    ذات.ت = []
    # apl-source:23
    for ع in range(ذات.ص + 1):
      # apl-source:24
      ذات.ت = ذات.ت + [[0] * (ذات.ج + 1)]
    # apl-source:25
    for ع in range(ذات.ص):
      # apl-source:26
      for ك in range(ذات.ج):
        # apl-source:27
        ذات.ت[ع + 1][ك + 1] = م[ع][ك] + ذات.ت[ع][ك + 1] + ذات.ت[ع + 1][ك] - ذات.ت[ع][ك]
# apl-source:28

  # apl-source:29
  def مجموع_منطقة(ذات, ر1, ك1, ر2, ك2):
    # apl-source:30
    return ذات.ت[ر2 + 1][ك2 + 1] - ذات.ت[ر1][ك2 + 1] - ذات.ت[ر2 + 1][ك1] + ذات.ت[ر1][ك1]
# apl-source:31

# apl-source:32
م = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
# apl-source:33
ن = منطقة(م)
# apl-source:34
تأكد_يساوي(ن.مجموع_منطقة(2, 1, 4, 3), 8, "منطقة أولى")
# apl-source:35
تأكد_يساوي(ن.مجموع_منطقة(1, 1, 2, 2), 11, "منطقة ثانية")
# apl-source:36
تأكد_يساوي(ن.مجموع_منطقة(1, 2, 2, 4), 12, "منطقة ثالثة")
# apl-source:37
تأكد_يساوي(ن.مجموع_منطقة(0, 0, 0, 0), 3, "خلية")
# apl-source:38
