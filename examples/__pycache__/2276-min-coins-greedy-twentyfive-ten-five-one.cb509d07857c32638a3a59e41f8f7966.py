
# apl-source:1
# مثال 2276 — أقل عدد عملات جشع
# apl-source:2
# Greedy coins 25 10 5 1
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2276-min-coins-greedy-twentyfive-ten-five-one.apl
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
  ع = 0
  # apl-source:20
  for ق in [25, 10, 5, 1]:
    # apl-source:21
    ع = ع + ن // ق
    # apl-source:22
    ن = ن % ق
  # apl-source:23
  return ع
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(0), 0, "حالة 1")
# apl-source:26
تأكد_يساوي(ف(1), 1, "حالة 2")
# apl-source:27
تأكد_يساوي(ف(30), 2, "حالة 3")
# apl-source:28
تأكد_يساوي(ف(99), 9, "حالة 4")
# apl-source:29
تأكد_يساوي(ف(100), 4, "حالة 5")
# apl-source:30
