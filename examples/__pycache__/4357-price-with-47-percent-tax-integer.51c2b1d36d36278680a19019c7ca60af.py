
# apl-source:1
# مثال 4357 — السعر مع ضريبة 47 بالمئة
# apl-source:2
# Price with 47 percent tax
# apl-source:3
# Demonstrates: حسابات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4357-price-with-47-percent-tax-integer.apl
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
  return ن + ن * 47 // 100
# apl-source:20

# apl-source:21
تأكد_يساوي(ف(100), 147, "حالة 1")
# apl-source:22
تأكد_يساوي(ف(250), 367, "حالة 2")
# apl-source:23
تأكد_يساوي(ف(999), 1468, "حالة 3")
# apl-source:24
تأكد_يساوي(ف(0), 0, "حالة 4")
# apl-source:25
