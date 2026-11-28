
# apl-source:1
# مثال 2218 — فرق الصوتية والصامتة
# apl-source:2
# Vowel minus consonant count
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2218-vowel-consonant-difference-text.apl
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
  ص = 0
  # apl-source:20
  ق = 0
  # apl-source:21
  for ح in ن.lower():
    # apl-source:22
    if "aeiou".find(ح) != -1:
      # apl-source:23
      ص = ص + 1
    # apl-source:24
    elif ح.isdigit() == False and ح != " ":
      # apl-source:25
      ق = ق + 1
  # apl-source:26
  return ص - ق
# apl-source:27

# apl-source:28
تأكد_يساوي(ف("hello"), -1, "حالة 1")
# apl-source:29
تأكد_يساوي(ف("aeiou"), 5, "حالة 2")
# apl-source:30
تأكد_يساوي(ف("rhythm"), -6, "حالة 3")
# apl-source:31
تأكد_يساوي(ف("hi there 12"), -1, "حالة 4")
# apl-source:32
