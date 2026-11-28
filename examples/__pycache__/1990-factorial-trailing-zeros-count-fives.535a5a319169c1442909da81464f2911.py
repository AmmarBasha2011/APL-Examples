
# apl-source:1
# مثال 1990 — أصفار نهاية المضروب
# apl-source:2
# Factorial trailing zeros
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1990-factorial-trailing-zeros-count-fives.apl
# apl-source:6

# apl-source:7
# # نقسم على 5 ثم 25 ثم 125
# apl-source:8
# # ونجمع النواتج
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
def اصفار(ن):
  # apl-source:19
  عدد = 0
  # apl-source:20
  ق = 5
  # apl-source:21
  while ق <= ن:
    # apl-source:22
    عدد = عدد + ن // ق
    # apl-source:23
    ق = ق * 5
  # apl-source:24
  return عدد
# apl-source:25

# apl-source:26
تأكد_يساوي(اصفار(0), 0, "صفر")
# apl-source:27
تأكد_يساوي(اصفار(5), 1, "٥")
# apl-source:28
تأكد_يساوي(اصفار(25), 6, "٢٥")
# apl-source:29
تأكد_يساوي(اصفار(100), 24, "١٠٠")
# apl-source:30
تأكد_يساوي(اصفار(1000), 249, "١٠٠٠")
# apl-source:31
