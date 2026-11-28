
# apl-source:1
# مثال 1502 — أطول سلسلة متتالية في رمي العملة
# apl-source:2
# Longest coin flip streak
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1502-longest-coin-streak.apl
# apl-source:6

# apl-source:7
# نعد التكرار المتصل
# apl-source:8
# نحتفظ بأكبر عدد
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
def أطول_سلسلة(رميات):
  # apl-source:19
  if رميات == "":
    # apl-source:20
    return 0
  # apl-source:21
  أقصى = 1
  # apl-source:22
  حالي = 1
  # apl-source:23
  for ع in range(1, len(رميات)):
    # apl-source:24
    if رميات[ع] == رميات[ع - 1]:
      # apl-source:25
      حالي = حالي + 1
    # apl-source:26
    else:
      # apl-source:27
      حالي = 1
    # apl-source:28
    if حالي > أقصى:
      # apl-source:29
      أقصى = حالي
  # apl-source:30
  return أقصى
# apl-source:31

# apl-source:32
تأكد_يساوي(أطول_سلسلة("HHTTTH"), 3, "ثلاثة")
# apl-source:33
تأكد_يساوي(أطول_سلسلة("HTHT"), 1, "متناوبة")
# apl-source:34
تأكد_يساوي(أطول_سلسلة(""), 0, "فارغة")
# apl-source:35
