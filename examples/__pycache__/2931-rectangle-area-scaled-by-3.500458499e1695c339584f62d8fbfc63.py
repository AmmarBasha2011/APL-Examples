
# apl-source:1
# مثال 2931 — مساحة مستطيل مكبر 3 مرات
# apl-source:2
# Rectangle area scaled by 3
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2931-rectangle-area-scaled-by-3.apl
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
  return (ق[0] * 3) * (ق[1] * 3)
# apl-source:20

# apl-source:21
تأكد_يساوي(ف([1, 2]), 18, "حالة 1")
# apl-source:22
تأكد_يساوي(ف([3, 4]), 108, "حالة 2")
# apl-source:23
تأكد_يساوي(ف([5, 5]), 225, "حالة 3")
# apl-source:24
تأكد_يساوي(ف([10, 1]), 90, "حالة 4")
# apl-source:25
