
# apl-source:1
# مثال 2271 — هل العدد مربع كامل
# apl-source:2
# Is perfect square
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2271-is-perfect-square-via-root-loop.apl
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
  ي = 0
  # apl-source:20
  while ي * ي < ن:
    # apl-source:21
    ي = ي + 1
  # apl-source:22
  return ي * ي == ن
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(0), True, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(1), True, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(2), False, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(16), True, "حالة 4")
# apl-source:28
تأكد_يساوي(ف(24), False, "حالة 5")
# apl-source:29
تأكد_يساوي(ف(49), True, "حالة 6")
# apl-source:30
