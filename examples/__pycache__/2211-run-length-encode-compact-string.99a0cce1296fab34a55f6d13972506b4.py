
# apl-source:1
# مثال 2211 — ترميز الأشواط
# apl-source:2
# Run length encode compact
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2211-run-length-encode-compact-string.apl
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
    return ""
  # apl-source:21
  ر = ""
  # apl-source:22
  س = ن[0]
  # apl-source:23
  ع = 1
  # apl-source:24
  for ي in range(1, len(ن)):
    # apl-source:25
    if ن[ي] == س:
      # apl-source:26
      ع = ع + 1
    # apl-source:27
    else:
      # apl-source:28
      ر = ر + س + str(ع)
      # apl-source:29
      س = ن[ي]
      # apl-source:30
      ع = 1
  # apl-source:31
  return ر + س + str(ع)
# apl-source:32

# apl-source:33
تأكد_يساوي(ف("aaabcc"), "a3b1c2", "حالة 1")
# apl-source:34
تأكد_يساوي(ف("abc"), "a1b1c1", "حالة 2")
# apl-source:35
تأكد_يساوي(ف("zzzz"), "z4", "حالة 3")
# apl-source:36
تأكد_يساوي(ف("a"), "a1", "حالة 4")
# apl-source:37
