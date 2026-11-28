
# apl-source:1
# مثال 1902 — رقم اليوم في السنة
# apl-source:2
# Day number within the year
# apl-source:3
# Demonstrates: تاريخ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1902-ordinal-day-of-year-calc.apl
# apl-source:6

# apl-source:7
# نجمع أيام كل شهر قبل الشهر الحالي
# apl-source:8
# ثم نضيف رقم اليوم
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
def يوم_السنة(س, ش, ي):
  # apl-source:26
  ايام = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # apl-source:27
  if كبيسة(س):
    # apl-source:28
    ايام[1] = 29
  # apl-source:29
  كلي = ي
  # apl-source:30
  for ك in range(ش - 1):
    # apl-source:31
    كلي = كلي + ايام[ك]
  # apl-source:32
  return كلي
# apl-source:33

# apl-source:34
تأكد_يساوي(يوم_السنة(2024, 3, 1), 61, "١ مارس ٢٠٢٤")
# apl-source:35
تأكد_يساوي(يوم_السنة(2023, 12, 31), 365, "آخر ٢٠٢٣")
# apl-source:36
تأكد_يساوي(يوم_السنة(2024, 12, 31), 366, "آخر ٢٠٢٤")
# apl-source:37
تأكد_يساوي(يوم_السنة(2023, 1, 1), 1, "أول يناير")
# apl-source:38
