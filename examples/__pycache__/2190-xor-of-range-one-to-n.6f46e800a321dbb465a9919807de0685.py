
# apl-source:1
# مثال 2190 — XOR الأعداد من 1 إلى ن
# apl-source:2
# XOR of 1..n
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2190-xor-of-range-one-to-n.apl
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
  ن2 = 0
  # apl-source:20
  for ي in range(1, ن + 1):
    # apl-source:21
    ن2 = ن2 ^ ي
  # apl-source:22
  return ن2
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(1), 1, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(2), 3, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(3), 0, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(4), 4, "حالة 4")
# apl-source:28
تأكد_يساوي(ف(10), 11, "حالة 10")
# apl-source:29
