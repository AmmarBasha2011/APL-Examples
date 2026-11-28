
# apl-source:1
# مثال 2014 — الأس بالباقي بالتربيع والضرب
# apl-source:2
# Modular exponentiation
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2014-modular-power-square-and-multiply.apl
# apl-source:6

# apl-source:7
# # نقسم الأس على 2 في كل خطوة
# apl-source:8
# # ونأخذ الباقي دائما لنبقي الأعداد صغيرة
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
def قوة(ا, ن, م):
  # apl-source:19
  ناتج = 1
  # apl-source:20
  ا = ا % م
  # apl-source:21
  while ن > 0:
    # apl-source:22
    if ن % 2 == 1:
      # apl-source:23
      ناتج = ناتج * ا % م
    # apl-source:24
    ا = ا * ا % م
    # apl-source:25
    ن = ن // 2
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(قوة(2, 10, 1000), 24, "٢^١٠")
# apl-source:29
تأكد_يساوي(قوة(3, 200, 13), 9, "٣^٢٠٠")
# apl-source:30
تأكد_يساوي(قوة(5, 0, 7), 1, "أس صفر")
# apl-source:31
