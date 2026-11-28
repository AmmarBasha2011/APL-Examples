
# apl-source:1
# مثال 2189 — أقرب قوة اثنين لا تقل
# apl-source:2
# Next power of two at least n
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2189-next-power-of-two-at-least.apl
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
  while ق < ن:
    # apl-source:21
    ق = ق * 2
  # apl-source:22
  return ق
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(1), 1, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(2), 2, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(3), 4, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(17), 32, "حالة 17")
# apl-source:28
تأكد_يساوي(ف(64), 64, "حالة 64")
# apl-source:29
تأكد_يساوي(ف(65), 128, "حالة 65")
# apl-source:30
