
# apl-source:1
# مثال 1560 — رقم اليوم في السنة
# apl-source:2
# Day of the year number
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1560-day-of-year-number.apl
# apl-source:6

# apl-source:7
# نجمع أيام الشهور السابقة
# apl-source:8
# ونضيف اليوم ويوماً لفبراير الكبيس
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
def رقم_اليوم_في_السنة(س, ش, ي):
  # apl-source:19
  مدد_الشهور = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # apl-source:20
  كبيسة = (س % 4 == 0 and س % 100 != 0) or س % 400 == 0
  # apl-source:21
  مجموع = ي
  # apl-source:22
  for م in range(ش - 1):
    # apl-source:23
    مجموع = مجموع + مدد_الشهور[م]
  # apl-source:24
  if كبيسة and ش > 2:
    # apl-source:25
    مجموع = مجموع + 1
  # apl-source:26
  return مجموع
# apl-source:27

# apl-source:28
تأكد_يساوي(رقم_اليوم_في_السنة(2023, 1, 1), 1, "أول يناير")
# apl-source:29
تأكد_يساوي(رقم_اليوم_في_السنة(2023, 3, 1), 60, "أول مارس")
# apl-source:30
تأكد_يساوي(رقم_اليوم_في_السنة(2024, 3, 1), 61, "كبيسة")
# apl-source:31
تأكد_يساوي(رقم_اليوم_في_السنة(2024, 12, 31), 366, "آخر كبيسة")
# apl-source:32
