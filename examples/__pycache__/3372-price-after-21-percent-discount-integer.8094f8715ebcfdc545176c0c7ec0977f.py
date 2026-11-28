
# apl-source:1
# مثال 3372 — السعر بعد خصم 21 بالمئة
# apl-source:2
# Price after 21 percent discount
# apl-source:3
# Demonstrates: حسابات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/3372-price-after-21-percent-discount-integer.apl
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
  return ن - ن * 21 // 100
# apl-source:20

# apl-source:21
تأكد_يساوي(ف(100), 79, "حالة 1")
# apl-source:22
تأكد_يساوي(ف(250), 198, "حالة 2")
# apl-source:23
تأكد_يساوي(ف(999), 790, "حالة 3")
# apl-source:24
تأكد_يساوي(ف(0), 0, "حالة 4")
# apl-source:25
