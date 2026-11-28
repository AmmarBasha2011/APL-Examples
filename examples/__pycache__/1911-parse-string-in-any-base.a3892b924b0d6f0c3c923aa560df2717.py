
# apl-source:1
# مثال 1911 — قراءة نص في أي أساس
# apl-source:2
# Parse a string in any base
# apl-source:3
# Demonstrates: تحويل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1911-parse-string-in-any-base.apl
# apl-source:6

# apl-source:7
# نبحث عن الخانة في جدول الرموز
# apl-source:8
# الناتج = الناتج × الأساس + الخانة
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
def اقرأ(س, ب):
  # apl-source:19
  رموز = "0123456789abcdef"
  # apl-source:20
  ن = 0
  # apl-source:21
  for ح in س:
    # apl-source:22
    ن = ن * ب + رموز.find(ح)
  # apl-source:23
  return ن
# apl-source:24

# apl-source:25
تأكد_يساوي(اقرأ("1010", 2), 10, "ثنائي")
# apl-source:26
تأكد_يساوي(اقرأ("ff", 16), 255, "ست عشري")
# apl-source:27
تأكد_يساوي(اقرأ("777", 8), 511, "ثماني")
# apl-source:28
