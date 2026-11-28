
# apl-source:1
# مثال 1519 — عد حروف الكلمة العربية
# apl-source:2
# Count Arabic letters in a text
# apl-source:3
# Demonstrates: نصوص عربية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1519-arabic-letter-count.apl
# apl-source:6

# apl-source:7
# نعد ما يعتبره isalpha حرفاً
# apl-source:8
# الأرقام والمسافات لا تدخل
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
def عدد_الحروف(نص_):
  # apl-source:19
  عد = 0
  # apl-source:20
  for ح in نص_:
    # apl-source:21
    if ح.isalpha():
      # apl-source:22
      عد = عد + 1
  # apl-source:23
  return عد
# apl-source:24

# apl-source:25
تأكد_يساوي(عدد_الحروف("مرحبا بالعالم"), 12, "جملة")
# apl-source:26
تأكد_يساوي(عدد_الحروف("اقرأ 123!"), 4, "أرقام")
# apl-source:27
تأكد_يساوي(عدد_الحروف(""), 0, "فارغ")
# apl-source:28
