
# apl-source:1
# مثال 2534 — قيصر بإزاحة 2
# apl-source:2
# Caesar shift 2
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2534-caesar-shift-by-2-lowercase.apl
# apl-source:6

# apl-source:7
# # ندخل النص
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
  ر = ""
  # apl-source:20
  for ح in ن:
    # apl-source:21
    if ح.islower():
      # apl-source:22
      ر = ر + chr((ord(ح) - 97 + 2) % 26 + 97)
    # apl-source:23
    else:
      # apl-source:24
      ر = ر + ح
  # apl-source:25
  return ر
# apl-source:26

# apl-source:27
تأكد_يساوي(ف("abc"), "cde", "حالة 1")
# apl-source:28
تأكد_يساوي(ف("xyz"), "zab", "حالة 2")
# apl-source:29
تأكد_يساوي(ف("hello world"), "jgnnq yqtnf", "حالة 3")
# apl-source:30
تأكد_يساوي(ف("a1"), "c1", "حالة 4")
# apl-source:31
