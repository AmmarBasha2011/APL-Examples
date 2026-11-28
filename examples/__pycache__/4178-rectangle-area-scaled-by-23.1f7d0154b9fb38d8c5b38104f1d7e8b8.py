
# apl-source:1
# مثال 4178 — مساحة مستطيل مكبر 23 مرات
# apl-source:2
# Rectangle area scaled by 23
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4178-rectangle-area-scaled-by-23.apl
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
def ف(ق):
  # apl-source:19
  return (ق[0] * 23) * (ق[1] * 23)
# apl-source:20

# apl-source:21
تأكد_يساوي(ف([1, 2]), 1058, "حالة 1")
# apl-source:22
تأكد_يساوي(ف([3, 4]), 6348, "حالة 2")
# apl-source:23
تأكد_يساوي(ف([5, 5]), 13225, "حالة 3")
# apl-source:24
تأكد_يساوي(ف([10, 1]), 5290, "حالة 4")
# apl-source:25
