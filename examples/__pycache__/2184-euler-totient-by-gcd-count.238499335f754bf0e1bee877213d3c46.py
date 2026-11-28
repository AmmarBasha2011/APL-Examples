
# apl-source:1
# مثال 2184 — دالة أويلر بالعد
# apl-source:2
# Euler totient by counting
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2184-euler-totient-by-gcd-count.apl
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
def قسم(أ, ب):
  # apl-source:19
  while ب != 0:
    # apl-source:20
    أ, ب = ب, أ % ب
  # apl-source:21
  return أ
# apl-source:22

# apl-source:23
def ف(ن):
  # apl-source:24
  ع = 0
  # apl-source:25
  for ي in range(1, ن + 1):
    # apl-source:26
    if قسم(ي, ن) == 1:
      # apl-source:27
      ع = ع + 1
  # apl-source:28
  return ع
# apl-source:29

# apl-source:30
تأكد_يساوي(ف(1), 1, "حالة 1")
# apl-source:31
تأكد_يساوي(ف(9), 6, "حالة 9")
# apl-source:32
تأكد_يساوي(ف(10), 4, "حالة 10")
# apl-source:33
تأكد_يساوي(ف(36), 12, "حالة 36")
# apl-source:34
تأكد_يساوي(ف(97), 96, "حالة 97")
# apl-source:35
