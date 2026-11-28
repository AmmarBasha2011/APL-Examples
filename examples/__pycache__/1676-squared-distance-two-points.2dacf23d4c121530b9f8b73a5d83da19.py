
# apl-source:1
# مثال 1676 — مربع المسافة بين نقطتين
# apl-source:2
# Squared distance between points
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1676-squared-distance-two-points.apl
# apl-source:6

# apl-source:7
# الفرق في كل بعد
# apl-source:8
# نجمع مربعيهما
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
def مربع_مسافة(أ, ب):
  # apl-source:19
  س = أ[0] - ب[0]
  # apl-source:20
  ص = أ[1] - ب[1]
  # apl-source:21
  return س * س + ص * ص
# apl-source:22

# apl-source:23
تأكد_يساوي(مربع_مسافة([0, 0], [3, 4]), 25, "ثلاثة وأربعة")
# apl-source:24
تأكد_يساوي(مربع_مسافة([1, 1], [1, 1]), 0, "نقطة")
# apl-source:25
تأكد_يساوي(مربع_مسافة([-1, -1], [2, 3]), 25, "سالبة")
# apl-source:26
