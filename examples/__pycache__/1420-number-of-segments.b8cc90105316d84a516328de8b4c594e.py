
# apl-source:1
# مثال 1420 — عدد المقاطع
# apl-source:2
# Number of segments in a string
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1420-number-of-segments.apl
# apl-source:6

# apl-source:7
# المقطع هو تسلسل حروف غير فارغة
# apl-source:8
# نعد بداية كل مقطع
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
def عد_المقاطع(نص_):
  # apl-source:19
  عدد = 0
  # apl-source:20
  for ع in range(len(نص_)):
    # apl-source:21
    if (نص_[ع] != " ") and ((ع == 0) or (نص_[ع - 1] == " ")):
      # apl-source:22
      عدد = عدد + 1
  # apl-source:23
  return عدد
# apl-source:24

# apl-source:25
تأكد_يساوي(عد_المقاطع("Hello, my name is John"), 5, "خمسة")
# apl-source:26
تأكد_يساوي(عد_المقاطع(""), 0, "فارغ")
# apl-source:27
تأكد_يساوي(عد_المقاطع("   a  b "), 2, "مسافات زائدة")
# apl-source:28
