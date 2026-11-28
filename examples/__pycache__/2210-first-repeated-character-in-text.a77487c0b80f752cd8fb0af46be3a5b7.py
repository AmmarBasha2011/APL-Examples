
# apl-source:1
# مثال 2210 — أول حرف مكرر
# apl-source:2
# First repeated character
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2210-first-repeated-character-in-text.apl
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
  شوهد = ""
  # apl-source:20
  for ح in ن:
    # apl-source:21
    if شوهد.find(ح) != -1:
      # apl-source:22
      return ح
    # apl-source:23
    شوهد = شوهد + ح
  # apl-source:24
  return "-"
# apl-source:25

# apl-source:26
تأكد_يساوي(ف("abcdb"), "b", "حالة 1")
# apl-source:27
تأكد_يساوي(ف("abc"), "-", "حالة 2")
# apl-source:28
تأكد_يساوي(ف("hello"), "l", "حالة 3")
# apl-source:29
تأكد_يساوي(ف("aabb"), "a", "حالة 4")
# apl-source:30
