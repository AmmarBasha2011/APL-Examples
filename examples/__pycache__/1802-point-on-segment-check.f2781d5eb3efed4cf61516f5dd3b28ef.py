
# apl-source:1
# مثال 1802 — هل النقطة على القطعة
# apl-source:2
# Point on line segment
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1802-point-on-segment-check.apl
# apl-source:6

# apl-source:7
# الجداء الاتجاهي صفر
# apl-source:8
# الإحداثيات داخل المستطيل المحيط
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
def على_القطعة(أ, ب, ن):
  # apl-source:19
  ق = (ب[0] - أ[0]) * (ن[1] - أ[1]) - (ب[1] - أ[1]) * (ن[0] - أ[0])
  # apl-source:20
  if ق != 0:
    # apl-source:21
    return False
  # apl-source:22
  return ن[0] >= min(أ[0], ب[0]) and ن[0] <= max(أ[0], ب[0]) and ن[1] >= min(أ[1], ب[1]) and ن[1] <= max(أ[1], ب[1])
# apl-source:23

# apl-source:24
تأكد_يساوي(على_القطعة([0, 0], [4, 4], [2, 2]), True, "منتصف")
# apl-source:25
تأكد_يساوي(على_القطعة([0, 0], [4, 4], [5, 5]), False, "خارج")
# apl-source:26
تأكد_يساوي(على_القطعة([0, 0], [4, 4], [2, 3]), False, "بعيدة")
# apl-source:27
