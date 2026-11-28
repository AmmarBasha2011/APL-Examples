
# apl-source:1
# مثال 2187 — طول التمثيل الثنائي
# apl-source:2
# Binary length of a number
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2187-binary-length-of-number.apl
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
  ط = 0
  # apl-source:20
  while ن > 0:
    # apl-source:21
    ن = ن // 2
    # apl-source:22
    ط = ط + 1
  # apl-source:23
  return ط
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(0), 0, "حالة 0")
# apl-source:26
تأكد_يساوي(ف(1), 1, "حالة 1")
# apl-source:27
تأكد_يساوي(ف(8), 4, "حالة 8")
# apl-source:28
تأكد_يساوي(ف(255), 8, "حالة 255")
# apl-source:29
تأكد_يساوي(ف(256), 9, "حالة 256")
# apl-source:30
