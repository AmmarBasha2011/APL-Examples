
# apl-source:1
# مثال 2162 — حاصل ضرب الأرقام غير الصفرية
# apl-source:2
# Product of nonzero digits
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2162-product-of-digits-nonzero-only.apl
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
  ح = 1
  # apl-source:20
  for ر in str(ن):
    # apl-source:21
    if ر != "0":
      # apl-source:22
      ح = ح * int(ر)
  # apl-source:23
  return ح
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(7), 7, "حالة 7")
# apl-source:26
تأكد_يساوي(ف(100), 1, "حالة 100")
# apl-source:27
تأكد_يساوي(ف(2030), 6, "حالة 2030")
# apl-source:28
تأكد_يساوي(ف(999), 729, "حالة 999")
# apl-source:29
