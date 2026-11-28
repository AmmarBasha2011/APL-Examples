
# apl-source:1
# مثال 2160 — عد الأعداد التي تحوي الرقم ثلاثة
# apl-source:2
# Count numbers containing digit three
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2160-count-digits-equal-to-three-in-range.apl
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
  for ي in range(1, ن + 1):
    # apl-source:21
    if str(ي).count("3") > 0:
      # apl-source:22
      ع = ع + 1
  # apl-source:23
  return ع
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(2), 0, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(3), 1, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(30), 4, "حالة 30")
# apl-source:28
تأكد_يساوي(ف(100), 19, "حالة 100")
# apl-source:29
