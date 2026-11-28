
# apl-source:1
# مثال 2372 — مجموع مضروبات الأرقام
# apl-source:2
# Sum of digit factorials
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2372-digit-factorial-sum-of-number.apl
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
  ق = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
  # apl-source:20
  م = 0
  # apl-source:21
  for ر in str(ن):
    # apl-source:22
    م = م + ق[int(ر)]
  # apl-source:23
  return م
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(0), 1, "حالة 1")
# apl-source:26
تأكد_يساوي(ف(145), 145, "حالة 2")
# apl-source:27
تأكد_يساوي(ف(40585), 40585, "حالة 3")
# apl-source:28
تأكد_يساوي(ف(123), 9, "حالة 4")
# apl-source:29
تأكد_يساوي(ف(999), 1088640, "حالة 5")
# apl-source:30
