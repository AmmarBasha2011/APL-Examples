
# apl-source:1
# مثال 5244 — آخر رقم للعدد 11 أس ن
# apl-source:2
# Last digit of 11^n
# apl-source:3
# Demonstrates: تمارين متنوعة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5244-last-digit-power-11.apl
# apl-source:6

# apl-source:7
# نستخدم الباقي على 10 في كل ضرب
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
  ر = 1
  # apl-source:19
  for ي in range(ن):
    # apl-source:20
    ر = ر * 11 % 10
  # apl-source:21
  return ر
# apl-source:22

# apl-source:23
تأكد_يساوي(ف(0), 1, "حالة 1")
# apl-source:24
تأكد_يساوي(ف(1), 1, "حالة 2")
# apl-source:25
تأكد_يساوي(ف(5), 1, "حالة 3")
# apl-source:26
تأكد_يساوي(ف(13), 1, "حالة 4")
# apl-source:27
تأكد_يساوي(ف(100), 1, "حالة 5")
# apl-source:28
