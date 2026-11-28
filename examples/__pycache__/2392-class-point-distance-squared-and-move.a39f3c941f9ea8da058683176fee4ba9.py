
# apl-source:1
# مثال 2392 — صنف نقطة بمربع المسافة
# apl-source:2
# Point class with squared distance
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2392-class-point-distance-squared-and-move.apl
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
class نقطة:
    # apl-source:19
    def __init__(ذات, س, ص):
        # apl-source:20
        ذات.س = س
        # apl-source:21
        ذات.ص = ص
# apl-source:22

    # apl-source:23
    def حرك(ذات, ا, ب):
        # apl-source:24
        ذات.س = ذات.س + ا
        # apl-source:25
        ذات.ص = ذات.ص + ب
# apl-source:26

    # apl-source:27
    def مربع_البعد(ذات, ق):
        # apl-source:28
        return (ذات.س - ق.س) ** 2 + (ذات.ص - ق.ص) ** 2
# apl-source:29

# apl-source:30
أ = نقطة(0, 0)
# apl-source:31
ب = نقطة(3, 4)
# apl-source:32
تأكد_يساوي(أ.مربع_البعد(ب), 25, "٣-٤-٥")
# apl-source:33
أ.حرك(3, 4)
# apl-source:34
تأكد_يساوي(أ.مربع_البعد(ب), 0, "نفس المكان")
# apl-source:35
