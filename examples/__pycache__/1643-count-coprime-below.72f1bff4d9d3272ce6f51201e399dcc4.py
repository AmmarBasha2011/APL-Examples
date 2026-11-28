
# apl-source:1
# مثال 1643 — الأعداد الأولية نسبياً مع عدد
# apl-source:2
# Count integers coprime with n
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1643-count-coprime-below.apl
# apl-source:6

# apl-source:7
# نعد من 1 إلى ن ناقص واحد
# apl-source:8
# نختبر القاسم المشترك
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
def قاسم(أ, ب):
  # apl-source:19
  while ب != 0:
    # apl-source:20
    ت = ب
    # apl-source:21
    ب = أ % ب
    # apl-source:22
    أ = ت
  # apl-source:23
  return أ
# apl-source:24

# apl-source:25
def عدد_المتباينة(ن):
  # apl-source:26
  عد = 0
  # apl-source:27
  for ك in range(1, ن):
    # apl-source:28
    if قاسم(ك, ن) == 1:
      # apl-source:29
      عد = عد + 1
  # apl-source:30
  return عد
# apl-source:31

# apl-source:32
تأكد_يساوي(عدد_المتباينة(9), 6, "تسعة")
# apl-source:33
تأكد_يساوي(عدد_المتباينة(10), 4, "عشرة")
# apl-source:34
تأكد_يساوي(عدد_المتباينة(7), 6, "أولي")
# apl-source:35
