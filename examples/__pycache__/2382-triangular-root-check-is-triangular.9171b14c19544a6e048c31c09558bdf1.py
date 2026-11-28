
# apl-source:1
# مثال 2382 — هل العدد مثلثي
# apl-source:2
# Is triangular number
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2382-triangular-root-check-is-triangular.apl
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
  ي = 0
  # apl-source:21
  while م < ن:
    # apl-source:22
    ي = ي + 1
    # apl-source:23
    م = م + ي
  # apl-source:24
  return م == ن
# apl-source:25

# apl-source:26
تأكد_يساوي(ف(0), True, "حالة 1")
# apl-source:27
تأكد_يساوي(ف(1), True, "حالة 2")
# apl-source:28
تأكد_يساوي(ف(3), True, "حالة 3")
# apl-source:29
تأكد_يساوي(ف(6), True, "حالة 4")
# apl-source:30
تأكد_يساوي(ف(10), True, "حالة 5")
# apl-source:31
تأكد_يساوي(ف(11), False, "حالة 6")
# apl-source:32
تأكد_يساوي(ف(15), True, "حالة 7")
# apl-source:33
تأكد_يساوي(ف(28), True, "حالة 8")
# apl-source:34
تأكد_يساوي(ف(50), False, "حالة 9")
# apl-source:35
