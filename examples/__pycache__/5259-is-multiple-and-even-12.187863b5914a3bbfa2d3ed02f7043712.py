
# apl-source:1
# مثال 5259 — قابل للقسمة على 12 وزوجي؟
# apl-source:2
# Divisible by 12 and even
# apl-source:3
# Demonstrates: تمارين متنوعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5259-is-multiple-and-even-12.apl
# apl-source:6

# apl-source:7
# شرطان معاً بـ و
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
  return ن % 12 == 0 and ن % 2 == 0
# apl-source:19

# apl-source:20
تأكد_يساوي(ف(0), True, "حالة 1")
# apl-source:21
تأكد_يساوي(ف(12), True, "حالة 2")
# apl-source:22
تأكد_يساوي(ف(24), True, "حالة 3")
# apl-source:23
تأكد_يساوي(ف(7), False, "حالة 4")
# apl-source:24
تأكد_يساوي(ف(48), True, "حالة 5")
# apl-source:25
