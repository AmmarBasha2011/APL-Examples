
# apl-source:1
# مثال 1936 — عدد الحروف المتحركة
# apl-source:2
# Count vowels in English text
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1936-count-vowels-in-english-text.apl
# apl-source:6

# apl-source:7
# نحول الحروف لصغيرة
# apl-source:8
# نبحث عن الحرف في قائمة المتحركات
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
def متحركة(س):
  # apl-source:19
  عد = 0
  # apl-source:20
  for ح in س.lower():
    # apl-source:21
    if "aeiou".find(ح) >= 0:
      # apl-source:22
      عد = عد + 1
  # apl-source:23
  return عد
# apl-source:24

# apl-source:25
تأكد_يساوي(متحركة("hello world"), 3, "جملة")
# apl-source:26
تأكد_يساوي(متحركة("AEIOU"), 5, "كبيرة")
# apl-source:27
تأكد_يساوي(متحركة("rhythm"), 0, "بلا متحركة")
# apl-source:28
