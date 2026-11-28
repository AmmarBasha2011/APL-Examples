
# apl-source:1
# مثال 2137 — إزاحة قيصر بين كلمتين
# apl-source:2
# Caesar shift between words
# apl-source:3
# Demonstrates: تشفير
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2137-caesar-shift-between-two-words.apl
# apl-source:6

# apl-source:7
# # نقيس الإزاحة من الحرف الأول
# apl-source:8
# # ونتأكد أنها نفسها لكل الحروف
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
def ازاحة(ا, ب):
  # apl-source:19
  if len(ا) != len(ب) or len(ا) == 0:
    # apl-source:20
    return -1
  # apl-source:21
  ز = (ord(ب[0]) - ord(ا[0])) % 26
  # apl-source:22
  for ك in range(len(ا)):
    # apl-source:23
    if (ord(ب[ك]) - ord(ا[ك])) % 26 != ز:
      # apl-source:24
      return -1
  # apl-source:25
  return ز
# apl-source:26

# apl-source:27
تأكد_يساوي(ازاحة("abc", "def"), 3, "ثلاثة")
# apl-source:28
تأكد_يساوي(ازاحة("abc", "abd"), -1, "ليست إزاحة")
# apl-source:29
تأكد_يساوي(ازاحة("xyz", "abc"), 3, "التفاف")
# apl-source:30
