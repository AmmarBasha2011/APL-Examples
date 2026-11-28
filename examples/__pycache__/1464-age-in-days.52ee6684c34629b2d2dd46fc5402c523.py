
# apl-source:1
# مثال 1464 — العمر بالأيام
# apl-source:2
# Age in days between dates
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1464-age-in-days.apl
# apl-source:6

# apl-source:7
# نحول كل تاريخ إلى رقم يوم
# apl-source:8
# الفرق بين الرقمين هو الجواب
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
  return (س % 4 == 0 and س % 100 != 0) or س % 400 == 0
# apl-source:20

# apl-source:21
def رقم_اليوم(س, ش, ي):
  # apl-source:22
  مدد = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # apl-source:23
  مجموع = 0
  # apl-source:24
  for سنة in range(1970, س):
    # apl-source:25
    مجموع = مجموع + 365
    # apl-source:26
    if كبيسة(سنة):
      # apl-source:27
      مجموع = مجموع + 1
  # apl-source:28
  for م in range(1, ش):
    # apl-source:29
    مجموع = مجموع + مدد[م - 1]
    # apl-source:30
    if م == 2 and كبيسة(س):
      # apl-source:31
      مجموع = مجموع + 1
  # apl-source:32
  return مجموع + ي
# apl-source:33

# apl-source:34
def فرق_الأيام(أ, ب):
  # apl-source:35
  return رقم_اليوم(ب[0], ب[1], ب[2]) - رقم_اليوم(أ[0], أ[1], أ[2])
# apl-source:36

# apl-source:37
تأكد_يساوي(فرق_الأيام([2024, 1, 1], [2024, 1, 31]), 30, "شهر")
# apl-source:38
تأكد_يساوي(فرق_الأيام([2023, 12, 31], [2024, 1, 1]), 1, "رأس السنة")
# apl-source:39
تأكد_يساوي(فرق_الأيام([2024, 2, 28], [2024, 3, 1]), 2, "فبراير كبيس")
# apl-source:40
تأكد_يساوي(فرق_الأيام([2000, 1, 1], [2001, 1, 1]), 366, "سنة كبيسة")
# apl-source:41
