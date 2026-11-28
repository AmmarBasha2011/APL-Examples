
# apl-source:1
# مثال 2202 — عدد الحروف الصوتية الإنجليزية
# apl-source:2
# Count Latin vowels
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2202-count-vowels-latin-letters.apl
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
  ع = 0
  # apl-source:20
  for ح in ن.lower():
    # apl-source:21
    if "aeiou".find(ح) != -1:
      # apl-source:22
      ع = ع + 1
  # apl-source:23
  return ع
# apl-source:24

# apl-source:25
تأكد_يساوي(ف("hello"), 2, "حالة 1")
# apl-source:26
تأكد_يساوي(ف("AEIOU"), 5, "حالة 2")
# apl-source:27
تأكد_يساوي(ف("rhythm"), 0, "حالة 3")
# apl-source:28
تأكد_يساوي(ف("Programming"), 3, "حالة 4")
# apl-source:29
