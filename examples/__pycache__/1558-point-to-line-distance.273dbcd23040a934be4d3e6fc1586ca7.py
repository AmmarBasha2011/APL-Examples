
# apl-source:1
# مثال 1558 — بعد نقطة عن مستقيم
# apl-source:2
# Distance from a point to a line
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1558-point-to-line-distance.apl
# apl-source:6

# apl-source:7
# نستخدم مساحة المتوازي
# apl-source:8
# نقسمها على طول القطعة
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
def بعد_عن_مستقيم(ن, أ, ب):
  # apl-source:19
  بسط = (ب[0] - أ[0]) * (أ[1] - ن[1]) - (أ[0] - ن[0]) * (ب[1] - أ[1])
  # apl-source:20
  if بسط < 0:
    # apl-source:21
    بسط = -بسط
  # apl-source:22
  طول_ = ((ب[0] - أ[0]) ** 2 + (ب[1] - أ[1]) ** 2) ** 0.5
  # apl-source:23
  return بسط / طول_
# apl-source:24

# apl-source:25
تأكد_يساوي(بعد_عن_مستقيم([2, 3], [0, 0], [4, 0]), 3.0, "فوق المحور")
# apl-source:26
تأكد_يساوي(بعد_عن_مستقيم([0, 5], [0, 0], [0, 4]), 0.0, "على المستقيم")
# apl-source:27
تأكد_يساوي(بعد_عن_مستقيم([3, 0], [0, 0], [0, 4]), 3.0, "بجانب الرأسي")
# apl-source:28
