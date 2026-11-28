
# apl-source:1
# مثال 2169 — أصفار المضروب
# apl-source:2
# Trailing zeros of factorial
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2169-factorial-trailing-zeros-count.apl
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
  ق = 5
  # apl-source:21
  while ق <= ن:
    # apl-source:22
    ع = ع + ن // ق
    # apl-source:23
    ق = ق * 5
  # apl-source:24
  return ع
# apl-source:25

# apl-source:26
تأكد_يساوي(ف(4), 0, "حالة 4")
# apl-source:27
تأكد_يساوي(ف(5), 1, "حالة 5")
# apl-source:28
تأكد_يساوي(ف(25), 6, "حالة 25")
# apl-source:29
تأكد_يساوي(ف(100), 24, "حالة 100")
# apl-source:30
تأكد_يساوي(ف(125), 31, "حالة 125")
# apl-source:31
