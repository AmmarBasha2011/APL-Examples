
# apl-source:1
# مثال 3575 — مساحة دائرة بتقريب 43
# apl-source:2
# Circle area with pi approx 43/7
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/3575-square-of-radius-times-43-area-approx.apl
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
  return ن * ن * 43 // 7
# apl-source:20

# apl-source:21
تأكد_يساوي(ف(0), 0, "حالة 1")
# apl-source:22
تأكد_يساوي(ف(1), 6, "حالة 2")
# apl-source:23
تأكد_يساوي(ف(7), 301, "حالة 3")
# apl-source:24
تأكد_يساوي(ف(14), 1204, "حالة 4")
# apl-source:25
تأكد_يساوي(ف(21), 2709, "حالة 5")
# apl-source:26
