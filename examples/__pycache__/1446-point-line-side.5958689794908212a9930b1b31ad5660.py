
# apl-source:1
# مثال 1446 — جانب النقطة من الخط
# apl-source:2
# Which side of a directed line
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1446-point-line-side.apl
# apl-source:6

# apl-source:7
# نحسب الجداء التقاطعي لاتجاه الخط والنقطة
# apl-source:8
# الإشارة تحدد الجانب
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
def جانب(أ, ب, ن):
  # apl-source:19
  ض = (ب[0] - أ[0]) * (ن[1] - أ[1]) - (ب[1] - أ[1]) * (ن[0] - أ[0])
  # apl-source:20
  if ض > 0:
    # apl-source:21
    return "left"
  # apl-source:22
  if ض < 0:
    # apl-source:23
    return "right"
  # apl-source:24
  return "on"
# apl-source:25

# apl-source:26
تأكد_يساوي(جانب([0,0], [1,0], [0,1]), "left", "يسار")
# apl-source:27
تأكد_يساوي(جانب([0,0], [1,0], [0,-1]), "right", "يمين")
# apl-source:28
تأكد_يساوي(جانب([0,0], [1,0], [2,0]), "on", "على الخط")
# apl-source:29
