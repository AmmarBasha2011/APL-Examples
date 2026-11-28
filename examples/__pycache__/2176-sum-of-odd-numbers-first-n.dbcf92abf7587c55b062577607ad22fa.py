
# apl-source:1
# مثال 2176 — مجموع أول ن عدد فردي
# apl-source:2
# Sum of first n odd numbers
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2176-sum-of-odd-numbers-first-n.apl
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
  م = 0
  # apl-source:20
  for ي in range(ن):
    # apl-source:21
    م = م + 2 * ي + 1
  # apl-source:22
  return م
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(1), 1, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(4), 16, "حالة 4")
# apl-source:26
تأكد_يساوي(ف(9), 81, "حالة 9")
# apl-source:27
تأكد_يساوي(ف(25), 625, "حالة 25")
# apl-source:28
