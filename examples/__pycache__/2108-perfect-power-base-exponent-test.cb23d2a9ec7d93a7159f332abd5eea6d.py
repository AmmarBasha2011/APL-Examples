
# apl-source:1
# مثال 2108 — هل العدد قوة كاملة
# apl-source:2
# Perfect power test v2
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2108-perfect-power-base-exponent-test.apl
# apl-source:6

# apl-source:7
# # الأساس يبدأ من 2
# apl-source:8
# # 1 قوة كاملة
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
def قوة_كاملة(ن):
  # apl-source:19
  if ن == 1:
    # apl-source:20
    return True
  # apl-source:21
  ب = 2
  # apl-source:22
  while ب * ب <= ن:
    # apl-source:23
    ق = ب * ب
    # apl-source:24
    while ق < ن:
      # apl-source:25
      ق = ق * ب
    # apl-source:26
    if ق == ن:
      # apl-source:27
      return True
    # apl-source:28
    ب = ب + 1
  # apl-source:29
  return False
# apl-source:30

# apl-source:31
تأكد_يساوي(قوة_كاملة(8), True, "٨")
# apl-source:32
تأكد_يساوي(قوة_كاملة(9), True, "٩")
# apl-source:33
تأكد_يساوي(قوة_كاملة(10), False, "١٠")
# apl-source:34
تأكد_يساوي(قوة_كاملة(81), True, "٨١")
# apl-source:35
تأكد_يساوي(قوة_كاملة(72), False, "٧٢")
# apl-source:36
