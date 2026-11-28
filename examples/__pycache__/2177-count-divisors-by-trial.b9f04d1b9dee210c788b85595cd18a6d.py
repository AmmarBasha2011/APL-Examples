
# apl-source:1
# مثال 2177 — عدد القواسم بالتجربة
# apl-source:2
# Count divisors by trial
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2177-count-divisors-by-trial.apl
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
  for ي in range(1, ن + 1):
    # apl-source:21
    if ن % ي == 0:
      # apl-source:22
      ع = ع + 1
  # apl-source:23
  return ع
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(1), 1, "حالة 1")
# apl-source:26
تأكد_يساوي(ف(12), 6, "حالة 12")
# apl-source:27
تأكد_يساوي(ف(36), 9, "حالة 36")
# apl-source:28
تأكد_يساوي(ف(97), 2, "حالة 97")
# apl-source:29
