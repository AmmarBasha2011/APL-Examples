
# apl-source:1
# مثال 1680 — مجموع مربعات أضلاع مضلع
# apl-source:2
# Sum of squared polygon sides
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1680-integer-polygon-perimeter-squares.apl
# apl-source:6

# apl-source:7
# الضلع الأخير يصل الأخيرة بالأولى
# apl-source:8
# نجمع مربعات الأطوال
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
def مجموع_مربعات_الأضلاع(نقاط):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  ن = len(نقاط)
  # apl-source:21
  for ك in range(ن):
    # apl-source:22
    أ = نقاط[ك]
    # apl-source:23
    ب = نقاط[(ك + 1) % ن]
    # apl-source:24
    مجموع = مجموع + (أ[0] - ب[0]) ** 2 + (أ[1] - ب[1]) ** 2
  # apl-source:25
  return مجموع
# apl-source:26

# apl-source:27
تأكد_يساوي(مجموع_مربعات_الأضلاع([[0, 0], [2, 0], [2, 2], [0, 2]]), 16, "مربع")
# apl-source:28
تأكد_يساوي(مجموع_مربعات_الأضلاع([[0, 0], [3, 0], [0, 4]]), 50, "مثلث")
# apl-source:29
