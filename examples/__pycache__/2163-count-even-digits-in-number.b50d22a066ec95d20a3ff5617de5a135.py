
# apl-source:1
# مثال 2163 — عدد الأرقام الزوجية في العدد
# apl-source:2
# Count even digits in number
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2163-count-even-digits-in-number.apl
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
  for ر in str(ن):
    # apl-source:21
    if int(ر) % 2 == 0:
      # apl-source:22
      ع = ع + 1
  # apl-source:23
  return ع
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(0), 1, "حالة 0")
# apl-source:26
تأكد_يساوي(ف(13579), 0, "حالة 13579")
# apl-source:27
تأكد_يساوي(ف(2468), 4, "حالة 2468")
# apl-source:28
تأكد_يساوي(ف(1002), 3, "حالة 1002")
# apl-source:29
