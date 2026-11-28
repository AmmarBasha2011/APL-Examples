
# apl-source:1
# مثال 5172 — مجموع تراكمي مع زيادة 3
# apl-source:2
# Running total plus 3 per step
# apl-source:3
# Demonstrates: تمارين متنوعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5172-cumulative-3.apl
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
    م = م + خ + 3
    # apl-source:22
    ر = ر + [م]
  # apl-source:23
  return ر
# apl-source:24

# apl-source:25
تأكد_يساوي(ف([1, 2, 3]), [4, 9, 15], "حالة 1")
# apl-source:26
تأكد_يساوي(ف([]), [], "حالة 2")
# apl-source:27
تأكد_يساوي(ف([5, 5, 5, 5]), [8, 16, 24, 32], "حالة 3")
# apl-source:28
