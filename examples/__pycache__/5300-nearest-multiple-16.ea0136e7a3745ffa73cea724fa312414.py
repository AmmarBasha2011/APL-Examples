
# apl-source:1
# مثال 5300 — أقرب مضاعف للعدد 16
# apl-source:2
# Nearest multiple of 16
# apl-source:3
# Demonstrates: تمارين متنوعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5300-nearest-multiple-16.apl
# apl-source:6

# apl-source:7
# نقرب للأدنى أو الأعلى حسب الباقي
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(ن):
  # apl-source:18
  ب = ن % 16
  # apl-source:19
  if ب * 2 < 16:
    # apl-source:20
    return ن - ب
  # apl-source:21
  return ن - ب + 16
# apl-source:22

# apl-source:23
تأكد_يساوي(ف(0), 0, "حالة 1")
# apl-source:24
تأكد_يساوي(ف(7), 0, "حالة 2")
# apl-source:25
تأكد_يساوي(ف(13), 16, "حالة 3")
# apl-source:26
تأكد_يساوي(ف(100), 96, "حالة 4")
# apl-source:27
تأكد_يساوي(ف(17), 16, "حالة 5")
# apl-source:28
