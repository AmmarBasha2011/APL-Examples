
# apl-source:1
# مثال 2209 — هل الجملة تحوي كل الحروف
# apl-source:2
# Is pangram
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2209-is-pangram-all-letters-present.apl
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
  for ك in range(26):
    # apl-source:20
    if ن.lower().find(chr(97 + ك)) == -1:
      # apl-source:21
      return False
  # apl-source:22
  return True
# apl-source:23

# apl-source:24
تأكد_يساوي(ف("The quick brown fox jumps over the lazy dog"), True, "حالة 1")
# apl-source:25
تأكد_يساوي(ف("hello"), False, "حالة 2")
# apl-source:26
تأكد_يساوي(ف("abcdefghijklmnopqrstuvwxyz"), True, "حالة 3")
# apl-source:27
تأكد_يساوي(ف("abc"), False, "حالة 4")
# apl-source:28
