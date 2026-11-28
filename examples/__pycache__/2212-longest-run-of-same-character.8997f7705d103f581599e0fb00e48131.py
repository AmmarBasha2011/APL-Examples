
# apl-source:1
# مثال 2212 — أطول شوط لحرف
# apl-source:2
# Longest run of same char
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2212-longest-run-of-same-character.apl
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
  if ن == "":
    # apl-source:20
    return 0
  # apl-source:21
  ك = 1
  # apl-source:22
  ع = 1
  # apl-source:23
  for ي in range(1, len(ن)):
    # apl-source:24
    if ن[ي] == ن[ي - 1]:
      # apl-source:25
      ع = ع + 1
    # apl-source:26
    else:
      # apl-source:27
      ع = 1
    # apl-source:28
    if ع > ك:
      # apl-source:29
      ك = ع
  # apl-source:30
  return ك
# apl-source:31

# apl-source:32
تأكد_يساوي(ف("aabbbc"), 3, "حالة 1")
# apl-source:33
تأكد_يساوي(ف("abc"), 1, "حالة 2")
# apl-source:34
تأكد_يساوي(ف("zzzz"), 4, "حالة 3")
# apl-source:35
تأكد_يساوي(ف("aabbaaaa"), 4, "حالة 4")
# apl-source:36
