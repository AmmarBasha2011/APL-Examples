
# apl-source:1
# مثال 1227 — أس بباقٍ
# apl-source:2
# Modular exponent by squaring
# apl-source:3
# Demonstrates: تربيع متكرر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1227-pow-mod-recursive.apl
# apl-source:6

# apl-source:7
# نربع الأساس ونقسم الأس على اثنين
# apl-source:8
# ونضرب الناتج عندما يكون الأس فردياً
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
def اس_باقي(أ, ب, م):
  # apl-source:19
  ناتج = 1
  # apl-source:20
  أ = أ % م
  # apl-source:21
  while ب > 0:
    # apl-source:22
    if ب % 2 == 1:
      # apl-source:23
      ناتج = (ناتج * أ) % م
    # apl-source:24
    أ = (أ * أ) % م
    # apl-source:25
    ب = ب // 2
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(اس_باقي(2, 10, 1000), 24, "ألف")
# apl-source:29
تأكد_يساوي(اس_باقي(3, 200, 13), 9, "ثلاثة عشر")
# apl-source:30
تأكد_يساوي(اس_باقي(5, 0, 7), 1, "أس صفر")
# apl-source:31
تأكد_يساوي(اس_باقي(7, 128, 13), pow(7, 128, 13), "مقارنة بالمدمج")
# apl-source:32
