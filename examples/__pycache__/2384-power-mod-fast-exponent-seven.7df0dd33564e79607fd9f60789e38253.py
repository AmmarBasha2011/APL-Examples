
# apl-source:1
# مثال 2384 — قوة بالباقي ٧
# apl-source:2
# Fast modular power base 7
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2384-power-mod-fast-exponent-seven.apl
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
  ن2 = ن
  # apl-source:20
  ب = 7
  # apl-source:21
  ح = 1
  # apl-source:22
  while ن2 > 0:
    # apl-source:23
    if ن2 % 2 == 1:
      # apl-source:24
      ح = ح * ب % 13
    # apl-source:25
    ب = ب * ب % 13
    # apl-source:26
    ن2 = ن2 // 2
  # apl-source:27
  return ح
# apl-source:28

# apl-source:29
تأكد_يساوي(ف(0), 1, "حالة 1")
# apl-source:30
تأكد_يساوي(ف(1), 7, "حالة 2")
# apl-source:31
تأكد_يساوي(ف(5), 11, "حالة 3")
# apl-source:32
تأكد_يساوي(ف(12), 1, "حالة 4")
# apl-source:33
تأكد_يساوي(ف(100), 9, "حالة 5")
# apl-source:34
تأكد_يساوي(ف(1000), 9, "حالة 6")
# apl-source:35
