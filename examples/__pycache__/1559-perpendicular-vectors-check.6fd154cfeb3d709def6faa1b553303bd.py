
# apl-source:1
# مثال 1559 — هل المتجهان متعامدان
# apl-source:2
# Perpendicular vectors check
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1559-perpendicular-vectors-check.apl
# apl-source:6

# apl-source:7
# نحسب الجداء النقطي
# apl-source:8
# إن كان صفراً فالزاوية قائمة
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
def متعامدان(أ, ب):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  for ع in range(len(أ)):
    # apl-source:21
    مجموع = مجموع + أ[ع] * ب[ع]
  # apl-source:22
  return مجموع == 0
# apl-source:23

# apl-source:24
تأكد_يساوي(متعامدان([1, 0], [0, 5]), True, "محوران")
# apl-source:25
تأكد_يساوي(متعامدان([1, 2], [2, -1]), True, "قطري")
# apl-source:26
تأكد_يساوي(متعامدان([1, 1], [1, 2]), False, "غير متعامدين")
# apl-source:27
تأكد_يساوي(متعامدان([1, 2, 3], [3, 0, -1]), True, "ثلاثة أبعاد")
# apl-source:28
