
# apl-source:1
# مثال 2196 — المعامل ذو الحدين المركزي
# apl-source:2
# Central binomial coefficient
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2196-central-binomial-coefficient.apl
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
  for ي in range(1, ن + 1):
    # apl-source:21
    ح = ح * (ن + ي) // ي
  # apl-source:22
  return ح
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(0), 1, "حالة 0")
# apl-source:25
تأكد_يساوي(ف(1), 2, "حالة 1")
# apl-source:26
تأكد_يساوي(ف(3), 20, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(5), 252, "حالة 5")
# apl-source:28
تأكد_يساوي(ف(10), 184756, "حالة 10")
# apl-source:29
