
# apl-source:1
# مثال 2168 — الأصفار في نهاية العدد
# apl-source:2
# Trailing zeros of a number
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2168-count-trailing-zeros-of-number.apl
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
  while ن > 0 and ن % 10 == 0:
    # apl-source:21
    ن = ن // 10
    # apl-source:22
    ع = ع + 1
  # apl-source:23
  return ع
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(5), 0, "حالة 5")
# apl-source:26
تأكد_يساوي(ف(10), 1, "حالة 10")
# apl-source:27
تأكد_يساوي(ف(1200), 2, "حالة 1200")
# apl-source:28
تأكد_يساوي(ف(70000), 4, "حالة 70000")
# apl-source:29
