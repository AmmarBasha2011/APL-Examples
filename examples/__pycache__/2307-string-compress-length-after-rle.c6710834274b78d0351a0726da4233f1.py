
# apl-source:1
# مثال 2307 — طول النص بعد الضغط
# apl-source:2
# Length after RLE
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2307-string-compress-length-after-rle.apl
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
  ط = 0
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
      ط = ط + 1 + len(str(ع))
      # apl-source:28
      ع = 1
  # apl-source:29
  return ط + 1 + len(str(ع))
# apl-source:30

# apl-source:31
تأكد_يساوي(ف("aaabb"), 4, "حالة 1")
# apl-source:32
تأكد_يساوي(ف("abc"), 6, "حالة 2")
# apl-source:33
تأكد_يساوي(ف("zzzzzzzzzzzz"), 3, "حالة 3")
# apl-source:34
تأكد_يساوي(ف("a"), 2, "حالة 4")
# apl-source:35
