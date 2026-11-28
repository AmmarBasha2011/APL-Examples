
# apl-source:1
# مثال 2600 — عدد إلى الأساس 11
# apl-source:2
# Number to base 11
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2600-number-to-base-11-string-v2.apl
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
  if ن == 0:
    # apl-source:20
    return "0"
  # apl-source:21
  خ = ""
  # apl-source:22
  while ن > 0:
    # apl-source:23
    خ = str(ن % 11) + خ
    # apl-source:24
    ن = ن // 11
  # apl-source:25
  return خ
# apl-source:26

# apl-source:27
تأكد_يساوي(ف(0), "0", "حالة 1")
# apl-source:28
تأكد_يساوي(ف(1), "1", "حالة 2")
# apl-source:29
تأكد_يساوي(ف(11), "10", "حالة 3")
# apl-source:30
تأكد_يساوي(ف(50), "46", "حالة 4")
# apl-source:31
تأكد_يساوي(ف(255), "212", "حالة 5")
# apl-source:32
