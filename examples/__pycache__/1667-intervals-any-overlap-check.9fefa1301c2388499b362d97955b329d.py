
# apl-source:1
# مثال 1667 — هل تتداخل فترتان
# apl-source:2
# Any pair of intervals overlaps
# apl-source:3
# Demonstrates: فترات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1667-intervals-any-overlap-check.apl
# apl-source:6

# apl-source:7
# بعد الترتيب يكفي فحص الجار
# apl-source:8
# التداخل إذا بدأت فترة قبل نهاية سابقتها
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
def يوجد_تداخل(فترات):
  # apl-source:19
  ف = []
  # apl-source:20
  for ع in فترات:
    # apl-source:21
    ف.append([ع[0], ع[1]])
  # apl-source:22
  ف.sort()
  # apl-source:23
  for ك in range(1, len(ف)):
    # apl-source:24
    if ف[ك][0] < ف[ك - 1][1]:
      # apl-source:25
      return True
  # apl-source:26
  return False
# apl-source:27

# apl-source:28
تأكد_يساوي(يوجد_تداخل([[1, 3], [2, 4]]), True, "تداخل")
# apl-source:29
تأكد_يساوي(يوجد_تداخل([[1, 2], [2, 3]]), False, "تلامس فقط")
# apl-source:30
تأكد_يساوي(يوجد_تداخل([[5, 6], [1, 2], [3, 4]]), False, "غير مرتبة")
# apl-source:31
