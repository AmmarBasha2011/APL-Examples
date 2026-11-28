
# apl-source:1
# مثال 1803 — مساحة تقاطع مستطيلين
# apl-source:2
# Intersection area of two rectangles
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1803-rectangles-intersect-area.apl
# apl-source:6

# apl-source:7
# التداخل أفقياً ورأسياً
# apl-source:8
# سالب يعني لا تقاطع
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
def مساحة_التقاطع(أ, ب):
  # apl-source:19
  عرض = min(أ[2], ب[2]) - max(أ[0], ب[0])
  # apl-source:20
  ارتفاع = min(أ[3], ب[3]) - max(أ[1], ب[1])
  # apl-source:21
  if عرض <= 0 or ارتفاع <= 0:
    # apl-source:22
    return 0
  # apl-source:23
  return عرض * ارتفاع
# apl-source:24

# apl-source:25
تأكد_يساوي(مساحة_التقاطع([0, 0, 4, 4], [2, 2, 6, 6]), 4, "تداخل")
# apl-source:26
تأكد_يساوي(مساحة_التقاطع([0, 0, 1, 1], [2, 2, 3, 3]), 0, "منفصلان")
# apl-source:27
تأكد_يساوي(مساحة_التقاطع([0, 0, 4, 4], [1, 1, 2, 2]), 1, "داخل")
# apl-source:28
