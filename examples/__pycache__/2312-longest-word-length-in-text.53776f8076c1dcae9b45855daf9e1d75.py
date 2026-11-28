
# apl-source:1
# مثال 2312 — طول أطول كلمة
# apl-source:2
# Longest word length
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2312-longest-word-length-in-text.apl
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
  ك = 0
  # apl-source:20
  for و2 in ن.split():
    # apl-source:21
    if len(و2) > ك:
      # apl-source:22
      ك = len(و2)
  # apl-source:23
  return ك
# apl-source:24

# apl-source:25
تأكد_يساوي(ف("a bb ccc"), 3, "حالة 1")
# apl-source:26
تأكد_يساوي(ف("hello"), 5, "حالة 2")
# apl-source:27
تأكد_يساوي(ف(""), 0, "حالة 3")
# apl-source:28
تأكد_يساوي(ف("the quick brown"), 5, "حالة 4")
# apl-source:29
