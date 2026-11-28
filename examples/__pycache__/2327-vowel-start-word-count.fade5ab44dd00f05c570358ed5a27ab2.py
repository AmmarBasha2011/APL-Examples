
# apl-source:1
# مثال 2327 — كلمات تبدأ بحرف صوتي
# apl-source:2
# Words starting with vowel
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2327-vowel-start-word-count.apl
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
  for و2 in ن.lower().split():
    # apl-source:21
    if "aeiou".find(و2[0]) != -1:
      # apl-source:22
      ع = ع + 1
  # apl-source:23
  return ع
# apl-source:24

# apl-source:25
تأكد_يساوي(ف("an apple a day"), 3, "حالة 1")
# apl-source:26
تأكد_يساوي(ف("xyz"), 0, "حالة 2")
# apl-source:27
تأكد_يساوي(ف("Open Up Every Inbox"), 4, "حالة 3")
# apl-source:28
تأكد_يساوي(ف("b c d"), 0, "حالة 4")
# apl-source:29
