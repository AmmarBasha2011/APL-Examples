
# apl-source:1
# مثال 1877 — التباين بأعداد صحيحة
# apl-source:2
# Variance scaled by n squared
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1877-variance-integer-scaled.apl
# apl-source:6

# apl-source:7
# نتجنب الكسور
# apl-source:8
# القيمة تساوي ن² × التباين
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
def تباين_مضروب(ق):
  # apl-source:19
  ن = len(ق)
  # apl-source:20
  مجموع = 0
  # apl-source:21
  مربعات = 0
  # apl-source:22
  for ع in ق:
    # apl-source:23
    مجموع = مجموع + ع
    # apl-source:24
    مربعات = مربعات + ع * ع
  # apl-source:25
  return ن * مربعات - مجموع * مجموع
# apl-source:26

# apl-source:27
تأكد_يساوي(تباين_مضروب([2, 4, 4, 4, 5, 5, 7, 9]), 256, "ثمانية")
# apl-source:28
تأكد_يساوي(تباين_مضروب([5, 5, 5]), 0, "متساوية")
# apl-source:29
تأكد_يساوي(تباين_مضروب([1, 3]), 4, "اثنان")
# apl-source:30
