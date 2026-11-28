
# apl-source:1
# مثال 4026 — قوة 24 بالحلقة
# apl-source:2
# Power of 24 by loop
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4026-nth-power-of-24-by-loop.apl
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
  ق = 1
  # apl-source:20
  for ي in range(ن):
    # apl-source:21
    ق = ق * 24
  # apl-source:22
  return ق
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(0), 1, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(1), 24, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(3), 13824, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(6), 191102976, "حالة 4")
# apl-source:28
تأكد_يساوي(ف(10), 63403380965376, "حالة 5")
# apl-source:29
