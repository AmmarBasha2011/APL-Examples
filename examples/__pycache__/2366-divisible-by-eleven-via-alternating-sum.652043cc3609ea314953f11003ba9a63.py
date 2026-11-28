
# apl-source:1
# مثال 2366 — القسمة على 11 بالمتناوب
# apl-source:2
# Divisible by eleven rule
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2366-divisible-by-eleven-via-alternating-sum.apl
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
  ش = 1
  # apl-source:21
  while ن > 0:
    # apl-source:22
    م = م + ش * (ن % 10)
    # apl-source:23
    ش = -ش
    # apl-source:24
    ن = ن // 10
  # apl-source:25
  return م % 11 == 0
# apl-source:26

# apl-source:27
تأكد_يساوي(ف(11), True, "حالة 1")
# apl-source:28
تأكد_يساوي(ف(121), True, "حالة 2")
# apl-source:29
تأكد_يساوي(ف(123), False, "حالة 3")
# apl-source:30
تأكد_يساوي(ف(1331), True, "حالة 4")
# apl-source:31
تأكد_يساوي(ف(2728), True, "حالة 5")
# apl-source:32
تأكد_يساوي(ف(100), False, "حالة 6")
# apl-source:33
