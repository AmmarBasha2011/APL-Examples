
# apl-source:1
# مثال 5252 — مجموع تراكمي مع زيادة 11
# apl-source:2
# Running total plus 11 per step
# apl-source:3
# Demonstrates: تمارين متنوعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5252-cumulative-11.apl
# apl-source:6

# apl-source:7
# كل خطوة نضيف العنصر والزيادة
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
def ف(ق):
  # apl-source:18
  ر = []
  # apl-source:19
  م = 0
  # apl-source:20
  for خ in ق:
    # apl-source:21
    م = م + خ + 11
    # apl-source:22
    ر = ر + [م]
  # apl-source:23
  return ر
# apl-source:24

# apl-source:25
تأكد_يساوي(ف([1, 2, 3]), [12, 25, 39], "حالة 1")
# apl-source:26
تأكد_يساوي(ف([]), [], "حالة 2")
# apl-source:27
تأكد_يساوي(ف([5, 5, 5, 5]), [16, 32, 48, 64], "حالة 3")
# apl-source:28
