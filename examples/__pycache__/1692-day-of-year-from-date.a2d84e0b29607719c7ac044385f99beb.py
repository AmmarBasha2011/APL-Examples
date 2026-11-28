
# apl-source:1
# مثال 1692 — رقم اليوم في السنة
# apl-source:2
# Day of year from a date
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1692-day-of-year-from-date.apl
# apl-source:6

# apl-source:7
# نعالج السنة الكبيسة
# apl-source:8
# نجمع الأشهر قبل الحالي
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
def كبيسة(س):
  # apl-source:19
  if س % 400 == 0:
    # apl-source:20
    return True
  # apl-source:21
  if س % 100 == 0:
    # apl-source:22
    return False
  # apl-source:23
  return س % 4 == 0
# apl-source:24

# apl-source:25
def رقم_اليوم(س, ش, ي):
  # apl-source:26
  أطوال = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # apl-source:27
  if كبيسة(س):
    # apl-source:28
    أطوال[1] = 29
  # apl-source:29
  مجموع = ي
  # apl-source:30
  for ك in range(ش - 1):
    # apl-source:31
    مجموع = مجموع + أطوال[ك]
  # apl-source:32
  return مجموع
# apl-source:33

# apl-source:34
تأكد_يساوي(رقم_اليوم(2023, 1, 1), 1, "أول يوم")
# apl-source:35
تأكد_يساوي(رقم_اليوم(2023, 3, 1), 60, "مارس")
# apl-source:36
تأكد_يساوي(رقم_اليوم(2024, 3, 1), 61, "كبيسة")
# apl-source:37
تأكد_يساوي(رقم_اليوم(2023, 12, 31), 365, "آخر يوم")
# apl-source:38
