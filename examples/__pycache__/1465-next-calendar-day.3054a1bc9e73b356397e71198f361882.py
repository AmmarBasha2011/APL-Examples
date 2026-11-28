
# apl-source:1
# مثال 1465 — اليوم التالي في التقويم
# apl-source:2
# Next calendar day
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1465-next-calendar-day.apl
# apl-source:6

# apl-source:7
# نتحقق من آخر أيام الشهر
# apl-source:8
# فبراير يتغير في السنة الكبيسة
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
def أيام_الشهر(س, ش):
  # apl-source:19
  if ش == 2:
    # apl-source:20
    if (س % 4 == 0 and س % 100 != 0) or س % 400 == 0:
      # apl-source:21
      return 29
    # apl-source:22
    return 28
  # apl-source:23
  if ش == 4 or ش == 6 or ش == 9 or ش == 11:
    # apl-source:24
    return 30
  # apl-source:25
  return 31
# apl-source:26

# apl-source:27
def اليوم_التالي(س, ش, ي):
  # apl-source:28
  if ي < أيام_الشهر(س, ش):
    # apl-source:29
    return [س, ش, ي + 1]
  # apl-source:30
  if ش < 12:
    # apl-source:31
    return [س, ش + 1, 1]
  # apl-source:32
  return [س + 1, 1, 1]
# apl-source:33

# apl-source:34
تأكد_يساوي(اليوم_التالي(2024, 5, 10), [2024, 5, 11], "عادي")
# apl-source:35
تأكد_يساوي(اليوم_التالي(2024, 2, 28), [2024, 2, 29], "كبيسة")
# apl-source:36
تأكد_يساوي(اليوم_التالي(2023, 2, 28), [2023, 3, 1], "غير كبيسة")
# apl-source:37
تأكد_يساوي(اليوم_التالي(2023, 12, 31), [2024, 1, 1], "نهاية السنة")
# apl-source:38
