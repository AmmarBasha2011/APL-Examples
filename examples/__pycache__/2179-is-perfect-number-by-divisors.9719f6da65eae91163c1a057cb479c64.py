
# apl-source:1
# مثال 2179 — هل العدد تام
# apl-source:2
# Is number perfect
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2179-is-perfect-number-by-divisors.apl
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
  for ي in range(1, ن):
    # apl-source:21
    if ن % ي == 0:
      # apl-source:22
      م = م + ي
  # apl-source:23
  return م == ن and ن > 1
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(6), True, "حالة 6")
# apl-source:26
تأكد_يساوي(ف(28), True, "حالة 28")
# apl-source:27
تأكد_يساوي(ف(12), False, "حالة 12")
# apl-source:28
تأكد_يساوي(ف(496), True, "حالة 496")
# apl-source:29
تأكد_يساوي(ف(1), False, "حالة 1")
# apl-source:30
