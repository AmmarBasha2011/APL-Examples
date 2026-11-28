
# apl-source:1
# مثال 2371 — عدد قواسم العدد المثلثي
# apl-source:2
# Divisors of nth triangular
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2371-nth-triangular-number-with-most-divisors-small.apl
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
  ت = ن * (ن + 1) // 2
  # apl-source:20
  ع = 0
  # apl-source:21
  for ي in range(1, ت + 1):
    # apl-source:22
    if ت % ي == 0:
      # apl-source:23
      ع = ع + 1
  # apl-source:24
  return ع
# apl-source:25

# apl-source:26
تأكد_يساوي(ف(1), 1, "حالة 1")
# apl-source:27
تأكد_يساوي(ف(3), 4, "حالة 2")
# apl-source:28
تأكد_يساوي(ف(7), 6, "حالة 3")
# apl-source:29
تأكد_يساوي(ف(12), 8, "حالة 4")
# apl-source:30
تأكد_يساوي(ف(20), 16, "حالة 5")
# apl-source:31
