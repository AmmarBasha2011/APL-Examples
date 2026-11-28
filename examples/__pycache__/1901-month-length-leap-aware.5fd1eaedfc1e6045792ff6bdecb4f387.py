
# apl-source:1
# مثال 1901 — عدد أيام الشهر مع الكبيسة
# apl-source:2
# Days in month with leap years
# apl-source:3
# Demonstrates: تاريخ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1901-month-length-leap-aware.apl
# apl-source:6

# apl-source:7
# السنة كبيسة إن قبلت القسمة على ٤
# apl-source:8
# ما عدا القرون إلا إن قبلت ٤٠٠
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
def ايام_الشهر(س, ش):
  # apl-source:26
  if ش == 2:
    # apl-source:27
    if كبيسة(س):
      # apl-source:28
      return 29
    # apl-source:29
    return 28
  # apl-source:30
  if ش in [4, 6, 9, 11]:
    # apl-source:31
    return 30
  # apl-source:32
  return 31
# apl-source:33

# apl-source:34
تأكد_يساوي(ايام_الشهر(2024, 2), 29, "فبراير ٢٠٢٤")
# apl-source:35
تأكد_يساوي(ايام_الشهر(2100, 2), 28, "فبراير ٢١٠٠")
# apl-source:36
تأكد_يساوي(ايام_الشهر(2000, 2), 29, "فبراير ٢٠٠٠")
# apl-source:37
تأكد_يساوي(ايام_الشهر(2023, 4), 30, "أبريل")
# apl-source:38
تأكد_يساوي(ايام_الشهر(2023, 12), 31, "ديسمبر")
# apl-source:39
