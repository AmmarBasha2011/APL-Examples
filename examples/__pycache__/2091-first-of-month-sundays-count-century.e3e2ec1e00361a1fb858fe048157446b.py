
# apl-source:1
# مثال 2091 — الأحاد التي وافقت أول الشهر
# apl-source:2
# Sundays on first of month
# apl-source:3
# Demonstrates: تواريخ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2091-first-of-month-sundays-count-century.apl
# apl-source:6

# apl-source:7
# # نستخدم طريقة ساكاموتو
# apl-source:8
# # الناتج المعروف 171
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
def يوم(س, ش, ي):
  # apl-source:19
  ج = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
  # apl-source:20
  if ش < 3:
    # apl-source:21
    س = س - 1
  # apl-source:22
  return (س + س // 4 - س // 100 + س // 400 + ج[ش - 1] + ي) % 7
# apl-source:23

# apl-source:24
عدد = 0
# apl-source:25
for س in range(1901, 2001):
  # apl-source:26
  for ش in range(1, 13):
    # apl-source:27
    if يوم(س, ش, 1) == 0:
      # apl-source:28
      عدد = عدد + 1
# apl-source:29
تأكد_يساوي(عدد, 171, "قرن كامل")
# apl-source:30
