
# apl-source:1
# مثال 5084 — عدد مرات الحرف m
# apl-source:2
# Count occurrences of letter m
# apl-source:3
# Demonstrates: منطق وتمارين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5084-count-char-m.apl
# apl-source:6

# apl-source:7
# نمر على النص ونعد
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(ن):
  # apl-source:18
  ع = 0
  # apl-source:19
  for ح in ن:
    # apl-source:20
    if ح == "m":
      # apl-source:21
      ع = ع + 1
  # apl-source:22
  return ع
# apl-source:23

# apl-source:24
تأكد_يساوي(ف("banana"), 0, "حالة 1")
# apl-source:25
تأكد_يساوي(ف("education"), 0, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(""), 0, "حالة 3")
# apl-source:27
تأكد_يساوي(ف("rhythm"), 1, "حالة 4")
# apl-source:28
تأكد_يساوي(ف("mississippi cat"), 1, "حالة 5")
# apl-source:29
