
# apl-source:1
# مثال 3305 — مجموع أرقام 39 أس ن
# apl-source:2
# Digit sum of 39 power n
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/3305-digit-sum-of-39-to-the-power-n.apl
# apl-source:6

# apl-source:7
# # ندخل القيم
# apl-source:8
# # ونقارن النتيجة
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
def ف(ن):
  # apl-source:19
  ق = 39 ** ن
  # apl-source:20
  م = 0
  # apl-source:21
  for ر in str(ق):
    # apl-source:22
    م = م + int(ر)
  # apl-source:23
  return م
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(0), 1, "حالة 1")
# apl-source:26
تأكد_يساوي(ف(1), 12, "حالة 2")
# apl-source:27
تأكد_يساوي(ف(5), 36, "حالة 3")
# apl-source:28
تأكد_يساوي(ف(10), 54, "حالة 4")
# apl-source:29
تأكد_يساوي(ف(20), 117, "حالة 5")
# apl-source:30
